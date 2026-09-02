from langchain_core.documents import Document
from langchain_openrouter import ChatOpenRouter

from pydantic import BaseModel, Field

from app.core.config import settings
from app.rag.prompts import CHAT_PROMPT
from app.schemas.portfolio import (
    Experience,
    KnowledgeBase,
    Project,
)


def get_llm() -> ChatOpenRouter:
    return ChatOpenRouter(
        model=settings.openrouter_model,
        api_key=settings.openrouter_api_key,
        temperature=0,
    )


# ---------------------------------------------------------
# Repair schema
# ---------------------------------------------------------
# This schema is intentionally limited to the sections that
# we want to repair. We do NOT ask the LLM to regenerate the
# entire KnowledgeBase.
# ---------------------------------------------------------

class MissingSections(BaseModel):
    experiences: list[Experience] = Field(
        default_factory=list
    )
    projects: list[Project] = Field(
        default_factory=list
    )


# ---------------------------------------------------------
# Main portfolio extraction
# ---------------------------------------------------------

def extract_portfolio(
    resume_text: str,
) -> KnowledgeBase:

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        KnowledgeBase
    )

    prompt = f"""
You are a highly reliable resume information extraction system.

Your task is to extract the COMPLETE professional profile from the
resume below and return it according to the KnowledgeBase schema.

The resume contains these sections:

1. PERSONAL INFORMATION
2. CAREER PREFERENCES
3. PROFESSIONAL SUMMARY
4. CORE STRENGTHS
5. TECHNICAL SKILLS
6. EXPERIENCE
7. PROJECTS
8. EDUCATION
9. ACHIEVEMENTS & CERTIFICATIONS

==================================================
CRITICAL EXTRACTION RULES
==================================================

GENERAL:

- Process the ENTIRE resume before producing the result.
- Extract information from every section.
- Do not stop after extracting one or two sections.
- Do not invent information.
- Do not infer information that is not supported by the resume.
- Do not duplicate any entry.
- Preserve the original meaning of the resume.
- Preserve measurable results such as percentages, counts, and metrics.
- If information is not available, use an empty list or null when
  the schema allows it.

==================================================
1. PERSONAL INFORMATION
==================================================

Extract:

- name
- current_location
- contact_number
- email_address
- linkedin
- github
- leetcode

The resume contains these URLs:

LinkedIn:
https://www.linkedin.com/in/kansari1904/

GitHub:
https://github.com/kansari1904

LeetCode:
https://leetcode.com/u/Kansari1904/

Use these URLs exactly.

==================================================
2. CAREER PREFERENCES
==================================================

Extract only preferences explicitly stated in the resume.

The resume explicitly states:

"Open to Remote / Hybrid / Onsite"

"Software Development & AI Engineering roles"

"Bengaluru"

Therefore:

target_roles:

- Software Development
- AI Engineering

preferred_work_mode:

- Remote
- Hybrid
- Onsite

preferred_locations:

- Bengaluru

Do not add other preferences.

==================================================
3. PROFESSIONAL SUMMARY
==================================================

Extract the COMPLETE professional summary.

Do not return ":".

Do not return an empty placeholder.

Do not shorten the summary unnecessarily.

Preserve the candidate's AI Engineering focus and target roles.

==================================================
4. CORE STRENGTHS
==================================================

The resume contains a section called CORE STRENGTHS.

Extract these strengths into the "strengths" field.

Do not create additional personality traits.

The resume contains:

- Full-stack development across the MERN stack (React, Node.js,
  Express, MongoDB)

- AI/LLM integration and RAG pipelines with LangChain; AI agents
  built with LangGraph

- Structured, reliable AI outputs using Pydantic, tool calling,
  and AI agent workflows

- REST API design with JWT/OAuth 2.0-secured backends;
  300+ DSA problems solved

==================================================
5. TECHNICAL SKILLS
==================================================

Organize all technical skills into:

- languages
- ai_ml
- frontend
- backend
- databases
- developer_tools

Do not remove skills.

Do not invent skills.

==================================================
6. EXPERIENCE
==================================================

Extract EVERY unique work experience.

IMPORTANT:

The resume contains EXACTLY TWO experience entries.

1. AI Engineer Intern
   Company: CalQuity Technologies Pvt. Ltd.
   Work mode: Remote
   Duration: May 2026 – Aug 2026

2. Web Developer Intern
   Company: InnoByte Services
   Work mode: Remote
   Duration: Aug 2025 – Jan 2026

Create exactly TWO experience objects.

DO NOT duplicate an experience.

For every experience:

- Extract the exact role.
- Extract company name.
- Preserve dates as human-readable strings.
- Do NOT invent exact days.
- current_status must be "completed" because both positions
  have ended.
- Extract technologies explicitly associated with the role.
- Combine responsibilities and achievements into description.
- Preserve measurable results.

Use:

"May 2026"

instead of:

"2026-05-01"

Use:

"Aug 2026"

instead of:

"2026-08-31"

==================================================
7. PROJECTS
==================================================

Extract EVERY project.

IMPORTANT:

The resume contains EXACTLY THREE projects.

1. DocuMind-AI
2. AI Customer Support Agent
3. CodeGyan E-Learning Platform

Create exactly THREE project objects.

DO NOT omit any project.

DO NOT duplicate any project.

For every project:

project_title:

Extract the project name.

project_type:

Use an appropriate type such as:

- AI Full-Stack
- AI
- Full-Stack
- Web Application

description:

Describe the main purpose of the project.

tech_stack:

Extract technologies from the project description and Tools line.

features:

Extract what the project does.

contribution:

Extract what the candidate personally built or implemented.

Do not confuse features with contribution.

live_link:

Extract the actual project URL.

Project URLs:

DocuMind-AI:
https://khaliddocumindai.vercel.app/

AI Customer Support Agent:
https://github.com/kansari1904/AI-Customer-Suppport-Agent

CodeGyan:
https://code-gyan.vercel.app/

Use the exact URLs.

Preserve measurable results including:

- 60%
- 40%
- 35%
- 30+
- 50+

==================================================
8. EDUCATION
==================================================

The resume contains EXACTLY ONE education entry.

Degree:

B.E. in Computer Science and Engineering

College:

Chandigarh University, Mohali

Duration:

2021 – 2025

CGPA:

7.6 / 10.0

Coursework:

- Data Structures and Algorithms
- Computer Networks
- DBMS
- Object Oriented Programming

Create exactly ONE education object.

==================================================
9. ACHIEVEMENTS
==================================================

The resume contains this achievement:

"Solved 300+ DSA problems on LeetCode and GeeksforGeeks,
demonstrating strong problem-solving and algorithmic skills."

Store this in achievements.

Do not put it inside certifications.

==================================================
10. CERTIFICATIONS
==================================================

The resume contains:

"HackerRank JavaScript Certificate, 2024."

Store this in certifications.

Do not put it inside achievements.

==================================================
11. ADDITIONAL INFORMATION
==================================================

Only include useful professional information that does not fit
into the other fields.

Do not duplicate information.

==================================================
FINAL VALIDATION
==================================================

Before returning the result, verify:

- 1 personal information object
- 1 professional summary
- 1 technical skills object
- exactly 2 experiences
- exactly 1 education entry
- exactly 3 projects
- exactly 1 achievement
- exactly 1 certification
- 1 career preferences object
- no duplicate experiences
- no duplicate projects
- all explicit URLs preserved
- all measurable results preserved
- experience dates remain human-readable strings
- no invented information

==================================================
RESUME
==================================================

{resume_text}

==================================================
END OF RESUME
==================================================
"""

    result = structured_llm.invoke(prompt)

    # ---------------------------------------------------------
    # Repair missing experience/projects if necessary
    # ---------------------------------------------------------

    result = repair_missing_sections(
        resume_text=resume_text,
        portfolio=result,
    )

    return result


# ---------------------------------------------------------
# Targeted repair
# ---------------------------------------------------------

def repair_missing_sections(
    resume_text: str,
    portfolio: KnowledgeBase,
) -> KnowledgeBase:

    missing_experience = len(portfolio.experiences) != 2
    missing_projects = len(portfolio.projects) != 3

    # Nothing needs repairing.
    if not missing_experience and not missing_projects:
        return portfolio

    llm = get_llm()

    repair_llm = llm.with_structured_output(
        MissingSections
    )

    sections_to_repair = []

    if missing_experience:
        sections_to_repair.append("EXPERIENCE")

    if missing_projects:
        sections_to_repair.append("PROJECTS")

    sections = ", ".join(sections_to_repair)

    repair_prompt = f"""
You are repairing an incomplete resume extraction.

The original extraction is missing or incomplete:

{sections}

IMPORTANT:

Extract ONLY the missing sections.

Do not regenerate the rest of the resume.

Do not modify personal information.
Do not modify professional summary.
Do not modify technical skills.
Do not modify education.
Do not modify achievements.
Do not modify certifications.
Do not modify career preferences.
Do not modify strengths.

==================================================
EXPERIENCE
==================================================

The resume contains exactly TWO unique experiences:

1. AI Engineer Intern
   Company: CalQuity Technologies Pvt. Ltd.
   Duration: May 2026 – Aug 2026

2. Web Developer Intern
   Company: InnoByte Services
   Duration: Aug 2025 – Jan 2026

Return exactly two experience objects.

Do not duplicate experiences.

Keep dates as human-readable strings.

==================================================
PROJECTS
==================================================

The resume contains exactly THREE unique projects:

1. DocuMind-AI

URL:
https://khaliddocumindai.vercel.app/

2. AI Customer Support Agent

URL:
https://github.com/kansari1904/AI-Customer-Suppport-Agent

3. CodeGyan E-Learning Platform

URL:
https://code-gyan.vercel.app/

Return exactly three project objects.

Do not duplicate projects.

==================================================
GENERAL RULES
==================================================

- Extract only information supported by the resume.
- Do not invent technologies.
- Preserve measurable results.
- Preserve project URLs.
- Preserve the candidate's actual contributions.
- Do not add information that is not in the resume.

==================================================
RESUME
==================================================

{resume_text}

==================================================
END OF RESUME
==================================================
"""

    repaired = repair_llm.invoke(
        repair_prompt
    )

    # ---------------------------------------------------------
    # Merge only the repaired sections
    # ---------------------------------------------------------

    if (
        missing_experience
        and len(repaired.experiences) == 2
    ):
        portfolio.experiences = repaired.experiences

    if (
        missing_projects
        and len(repaired.projects) == 3
    ):
        portfolio.projects = repaired.projects

    return portfolio


# ---------------------------------------------------------
# Chat response generation
# ---------------------------------------------------------

def generate_chat_response(
    question: str,
    documents: list[Document],
) -> str:
    """
    Generate a recruiter-friendly answer using
    retrieved portfolio documents.
    """

    if not documents:
        return (
            "I couldn't find enough information in "
            "Khalid's portfolio to answer that question."
        )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    llm = get_llm()

    prompt = CHAT_PROMPT.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    response = llm.invoke(prompt)

    return response.content.strip()

def stream_chat_response(
    question: str,
    documents: list[Document],
):
    """
    Stream the LLM response chunk by chunk.
    """

    if not documents:
        yield (
            "I couldn't find enough information in "
            "Khalid's portfolio to answer that question."
        )
        return

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    llm = get_llm()

    prompt = CHAT_PROMPT.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    for chunk in llm.stream(prompt):
        if chunk.content:
            yield chunk.content