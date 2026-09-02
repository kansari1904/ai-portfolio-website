from typing import Any

from app.services.portfolio_service import (
    get_achievements,
    get_certifications,
    get_education,
    get_projects,
)

from app.services.retrieval_service import (
    retrieve_documents,
)

from app.services.llm_service import (
    generate_chat_response,
    stream_chat_response,
)




class ChatRoute:
    """
    Available response paths for recruiter questions.
    """

    FAQ = "faq"
    DIRECT = "direct"
    RAG = "rag"


def classify_question(query: str) -> str:
    """
    Determine which response path should handle a question.

    This classifier is intentionally deterministic.
    We do not call an LLM just to classify a question.

    Returns:
        "direct" -> answer from portfolio.json
        "rag"    -> retrieve from Chroma and use an LLM
    """

    q = query.lower().strip()

    if not q:
        return ChatRoute.RAG

    # ==================================================
    # Direct: Projects
    # ==================================================

    project_patterns = [
        "what projects",
        "which projects",
        "what project",
        "which project",
        "what has khalid built",
        "what did khalid build",
        "projects has khalid built",
        "projects khalid built",
    ]

    if any(
        pattern in q
        for pattern in project_patterns
    ):
        return ChatRoute.DIRECT

    # ==================================================
    # Direct: Education
    # ==================================================

    education_patterns = [
        "where did khalid study",
        "where has khalid studied",
        "which university",
        "which college",
        "what university",
        "what college",
        "what degree",
        "khalid's degree",
        "khalid degree",
        "what is khalid's cgpa",
        "khalid cgpa",
    ]

    if any(
        pattern in q
        for pattern in education_patterns
    ):
        return ChatRoute.DIRECT

    # ==================================================
    # Direct: Achievements / DSA
    # ==================================================

    achievement_patterns = [
        "how many dsa",
        "dsa problems",
        "leetcode problems",
        "geeksforgeeks problems",
        "how many problems has khalid solved",
        "how many problems khalid solved",
    ]

    if any(
        pattern in q
        for pattern in achievement_patterns
    ):
        return ChatRoute.DIRECT

    # ==================================================
    # Direct: Certifications
    # ==================================================

    certification_patterns = [
        "what certifications",
        "which certifications",
        "what certificates",
        "which certificates",
        "does khalid have any certifications",
    ]

    if any(
        pattern in q
        for pattern in certification_patterns
    ):
        return ChatRoute.DIRECT

    # ==================================================
    # Everything else -> RAG
    # ==================================================

    return ChatRoute.RAG


def get_direct_answer(
    query: str,
) -> dict[str, Any] | None:
    """
    Retrieve structured portfolio information for
    questions that can be answered without an LLM.

    Returns:
        A dictionary containing the answer type and
        structured portfolio data.

        None if the question is not supported by
        the direct-answer rules.
    """

    q = query.lower().strip()

    # ==================================================
    # Projects
    # ==================================================

    if (
        "projects" in q
        or "what has khalid built" in q
        or "what did khalid build" in q
    ):
        return {
            "type": "projects",
            "data": get_projects(),
        }

    # ==================================================
    # Education
    # ==================================================

    if (
        "where did khalid study" in q
        or "where has khalid studied" in q
        or "which university" in q
        or "which college" in q
        or "what university" in q
        or "what college" in q
        or "what degree" in q
        or "khalid degree" in q
        or "cgpa" in q
    ):
        return {
            "type": "education",
            "data": get_education(),
        }

    # ==================================================
    # Achievements / DSA
    # ==================================================

    if (
        "dsa" in q
        or "leetcode problems" in q
        or "geeksforgeeks problems" in q
        or "how many problems" in q
    ):
        return {
            "type": "achievements",
            "data": get_achievements(),
        }

    # ==================================================
    # Certifications
    # ==================================================

    if (
        "certification" in q
        or "certificate" in q
    ):
        return {
            "type": "certifications",
            "data": get_certifications(),
        }

    return None


def format_direct_answer(
    result: dict[str, Any],
) -> str:
    """
    Convert structured portfolio data into a concise,
    recruiter-friendly response.

    No LLM is used here.
    """

    result_type = result["type"]
    data = result["data"]

    # ==================================================
    # Projects
    # ==================================================

    if result_type == "projects":

        lines = [
            "Khalid has built the following projects:"
        ]

        for project in data:

            lines.append(
                f"- {project['project_title']}: "
                f"{project['description']}"
            )

        return "\n".join(lines)

    # ==================================================
    # Education
    # ==================================================

    if result_type == "education":

        lines = []

        for education in data:

            lines.append(
                f"Khalid completed "
                f"{education['course']} "
                f"from {education['college_name']} "
                f"({education['duration']}) "
                f"with a CGPA of "
                f"{education['cgpa']}."
            )

        return "\n".join(lines)

    # ==================================================
    # Achievements
    # ==================================================

    if result_type == "achievements":

        if not data:
            return (
                "No achievements are currently listed."
            )

        return " ".join(data)

    # ==================================================
    # Certifications
    # ==================================================

    if result_type == "certifications":

        if not data:
            return (
                "No certifications are currently listed."
            )

        return (
            "Khalid has the following certifications:\n"
            + "\n".join(
                f"- {certification}"
                for certification in data
            )
        )

    return ""


def process_question(
    query: str,
) -> dict[str, Any]:
    """
    Main chat orchestration function.

    Routing:

        FAQ
          -> faq.json

        DIRECT
          -> portfolio.json

        RAG
          -> Chroma -> OpenRouter LLM
    """

    query = query.strip()

    if not query:
        raise ValueError(
            "Question cannot be empty."
        )

    route = classify_question(query)

    # ==================================================
    # Direct portfolio route
    # ==================================================

    if route == ChatRoute.DIRECT:

        result = get_direct_answer(query)

        if result is not None:

            answer = format_direct_answer(
                result
            )

            return {
                "route": ChatRoute.DIRECT,
                "answer": answer,
                "data": result,
            }

    # ==================================================
    # RAG route
    # ==================================================

    documents = retrieve_documents(
        query=query,
        k=3,
    )

    answer = generate_chat_response(
        question=query,
        documents=documents,
    )

    return {
        "route": ChatRoute.RAG,
        "answer": answer,
        "data": {
            "documents_retrieved": len(documents),
        },
    }

def stream_question(query: str):
    query = query.strip()

    if not query:
        raise ValueError("Question cannot be empty.")

    route = classify_question(query)

    # Direct questions don't need an LLM.
    if route == ChatRoute.DIRECT:
        result = get_direct_answer(query)

        if result is not None:
            answer = format_direct_answer(result)

            yield answer
            return

    # RAG route
    documents = retrieve_documents(
        query=query,
        k=3,
    )

    yield from stream_chat_response(
        question=query,
        documents=documents,
    )