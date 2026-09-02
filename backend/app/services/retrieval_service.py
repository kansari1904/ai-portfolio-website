from langchain_core.documents import Document

from app.rag.retriever import get_vectorstore


def infer_section(query: str) -> str | None:
    """
    Infer a high-confidence knowledge section from the query.

    This is intentionally deterministic.

    We do not call an LLM just to classify a recruiter question.
    """

    q = query.lower().strip()

    # ----------------------------------------------
    # Projects
    # ----------------------------------------------

    project_patterns = [
        "what projects",
        "which projects",
        "what project",
        "which project",
        "projects has khalid built",
        "projects khalid built",
        "what has khalid built",
        "what did khalid build",
        "applications has khalid built",
        "applications did khalid build",
    ]

    if any(pattern in q for pattern in project_patterns):
        return "project"

    # ----------------------------------------------
    # Experience
    # ----------------------------------------------

    experience_patterns = [
        "where did khalid work",
        "where has khalid worked",
        "where did khalid intern",
        "khalid's experience",
        "khalid experience",
        "work experience",
        "professional experience",
        "internship",
        "internships",
        "which company",
        "what company did khalid work",
    ]

    if any(pattern in q for pattern in experience_patterns):
        return "experience"

    # ----------------------------------------------
    # Education
    # ----------------------------------------------

    education_patterns = [
        "where did khalid study",
        "where has khalid studied",
        "which university",
        "which college",
        "what university",
        "what college",
        "khalid's education",
        "khalid education",
        "degree",
        "cgpa",
        "coursework",
    ]

    if any(pattern in q for pattern in education_patterns):
        return "education"

    # ----------------------------------------------
    # Technical Skills
    # ----------------------------------------------

    skill_patterns = [
        "what technologies",
        "what technology",
        "what tech stack",
        "technologies does khalid know",
        "technologies khalid knows",
        "technical skills",
        "what skills",
        "programming languages",
        "frontend technologies",
        "backend technologies",
        "ai technologies",
        "ai/ml technologies",
    ]

    if any(pattern in q for pattern in skill_patterns):
        return "technical_skills"

    # ----------------------------------------------
    # Achievements
    # ----------------------------------------------

    achievement_patterns = [
        "how many dsa",
        "dsa problems",
        "leetcode problems",
        "geeksforgeeks problems",
        "problems has khalid solved",
        "how many problems",
        "achievements",
    ]

    if any(pattern in q for pattern in achievement_patterns):
        return "achievement"

    # ----------------------------------------------
    # Certifications
    # ----------------------------------------------

    certification_patterns = [
        "certification",
        "certifications",
        "certificate",
        "certificates",
    ]

    if any(pattern in q for pattern in certification_patterns):
        return "certification"

    return None


def retrieve_documents(
    query: str,
    k: int = 3,
) -> list[Document]:
    """
    Retrieve relevant documents from Chroma.

    When a high-confidence section can be inferred,
    retrieval is restricted to that section.

    Otherwise, normal semantic retrieval is used.
    """

    query = query.strip()

    if not query:
        return []

    if k < 1:
        raise ValueError(
            "k must be greater than or equal to 1."
        )

    vectorstore = get_vectorstore()

    section = infer_section(query)

    if section:
        return vectorstore.similarity_search(
            query,
            k=k,
            filter={
                "section": section,
            },
        )

    return vectorstore.similarity_search(
        query,
        k=k,
    )