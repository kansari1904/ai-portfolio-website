import json
from pathlib import Path

from langchain_core.documents import Document


def load_portfolio_json(json_path: str) -> dict:
    """
    Load portfolio knowledge from a JSON file.
    """
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Portfolio JSON not found: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def portfolio_to_documents(
    portfolio: dict,
) -> list[Document]:
    """
    Convert structured portfolio data into meaningful
    LangChain Documents for semantic retrieval.
    """

    documents: list[Document] = []

    # --------------------------------------------------
    # Professional Summary
    # --------------------------------------------------

    documents.append(
        Document(
            page_content=portfolio["professional_summary"],
            metadata={
                "section": "professional_summary",
            },
        )
    )

    # --------------------------------------------------
    # Technical Skills
    # --------------------------------------------------

    skills = portfolio["technical_skills"]

    skills_text = "\n".join(
        [
            (
                "Programming Languages: "
                f"{', '.join(skills['languages'])}"
            ),
            (
                "AI/ML Technologies: "
                f"{', '.join(skills['ai_ml'])}"
            ),
            (
                "Frontend Technologies: "
                f"{', '.join(skills['frontend'])}"
            ),
            (
                "Backend & APIs: "
                f"{', '.join(skills['backend'])}"
            ),
            (
                "Databases: "
                f"{', '.join(skills['databases'])}"
            ),
            (
                "Developer Tools: "
                f"{', '.join(skills['developer_tools'])}"
            ),
        ]
    )

    documents.append(
        Document(
            page_content=skills_text,
            metadata={
                "section": "technical_skills",
            },
        )
    )

    # --------------------------------------------------
    # Experience
    # --------------------------------------------------

    for experience in portfolio["experiences"]:

        experience_text = f"""
Professional Experience

Role: {experience["role"]}

Company: {experience["company_name"]}

Duration: {experience["start_date"]} - {experience["end_date"]}

Status: {experience["current_status"]}

Technologies:
{", ".join(experience["tech_stack"])}

Responsibilities and Work:
{experience["description"]}
""".strip()

        documents.append(
            Document(
                page_content=experience_text,
                metadata={
                    "section": "experience",
                    "company": experience["company_name"],
                    "role": experience["role"],
                },
            )
        )

    # --------------------------------------------------
    # Education
    # --------------------------------------------------

    for education in portfolio["education"]:

        education_text = f"""
Education

Degree: {education["course"]}

College: {education["college_name"]}

Duration: {education["duration"]}

CGPA: {education["cgpa"]}

Coursework:
{", ".join(education["coursework"] or [])}
""".strip()

        documents.append(
            Document(
                page_content=education_text,
                metadata={
                    "section": "education",
                    "college": education["college_name"],
                    "degree": education["course"],
                },
            )
        )

    # --------------------------------------------------
    # Projects
    # --------------------------------------------------

    for project in portfolio["projects"]:

        project_text = f"""
Project

Project Name: {project["project_title"]}

Project Category: Project

Project Type: {project["project_type"]}

Description:
{project["description"]}

Technologies:
{", ".join(project["tech_stack"])}

Features:
{", ".join(project["features"])}

Contribution:
{", ".join(project["contribution"])}

Project Link:
{project["live_link"]}
""".strip()

        documents.append(
            Document(
                page_content=project_text,
                metadata={
                    "section": "project",
                    "project": project["project_title"],
                    "project_type": project["project_type"],
                },
            )
        )

    # --------------------------------------------------
    # Achievements
    # --------------------------------------------------

    for achievement in portfolio["achievements"]:

        documents.append(
            Document(
                page_content=achievement,
                metadata={
                    "section": "achievement",
                },
            )
        )

    # --------------------------------------------------
    # Certifications
    # --------------------------------------------------

    for certification in portfolio["certifications"]:

        documents.append(
            Document(
                page_content=certification,
                metadata={
                    "section": "certification",
                },
            )
        )

    # --------------------------------------------------
    # Career Preferences
    # --------------------------------------------------

    preferences = portfolio["career_preferences"]

    preferences_text = f"""
Career Preferences

Target Roles:
{", ".join(preferences["target_roles"])}

Preferred Work Mode:
{", ".join(preferences["preferred_work_mode"])}

Preferred Locations:
{", ".join(preferences["preferred_locations"])}
""".strip()

    documents.append(
        Document(
            page_content=preferences_text,
            metadata={
                "section": "career_preferences",
            },
        )
    )

    # --------------------------------------------------
    # Strengths
    # --------------------------------------------------

    strengths_text = "\n".join(
        f"- {strength}"
        for strength in portfolio["strengths"]
    )

    documents.append(
        Document(
            page_content=strengths_text,
            metadata={
                "section": "strengths",
            },
        )
    )

    return documents