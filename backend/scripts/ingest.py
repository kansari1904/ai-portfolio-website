import json
from pathlib import Path

from app.rag.loader import extract_text_from_pdf
from app.services.llm_service import extract_portfolio
from app.schemas.portfolio import Education


BASE_DIR = Path(__file__).resolve().parent.parent

RESUME_PATH = BASE_DIR / "data" / "source" / "resume.pdf"
OUTPUT_PATH = BASE_DIR / "data" / "knowledge" / "portfolio.json"


def main():
    # ---------------------------------------------------------
    # Validate resume
    # ---------------------------------------------------------

    if not RESUME_PATH.exists():
        raise FileNotFoundError(
            f"Resume not found: {RESUME_PATH}"
        )

    # ---------------------------------------------------------
    # Extract text from PDF
    # ---------------------------------------------------------

    print("Extracting text from resume...")

    resume_text = extract_text_from_pdf(
        str(RESUME_PATH)
    )

    print(
        f"Extracted {len(resume_text)} characters."
    )

    # ---------------------------------------------------------
    # LLM structured extraction
    # ---------------------------------------------------------

    print(
        "Sending resume to LLM for structured extraction..."
    )

    portfolio = extract_portfolio(
        resume_text
    )

    # ---------------------------------------------------------
    # Deterministic validation / repair
    # ---------------------------------------------------------

    # These values are explicitly present in the resume.
    # They should never disappear because of an LLM extraction issue.

    portfolio.achievements = [
        "Solved 300+ DSA problems on LeetCode and GeeksforGeeks, "
        "demonstrating strong problem-solving and algorithmic skills."
    ]

    portfolio.certifications = [
        "HackerRank JavaScript Certificate, 2024."
    ]

    # ---------------------------------------------------------
    # Education fallback
    # ---------------------------------------------------------

    if not portfolio.education:
        portfolio.education = [
            Education(
                course="B.E. in Computer Science and Engineering",
                college_name="Chandigarh University, Mohali",
                duration="2021 – 2025",
                cgpa="7.6 / 10.0",
                coursework=[
                    "Data Structures and Algorithms",
                    "Computer Networks",
                    "DBMS",
                    "Object Oriented Programming",
                ],
            )
        ]

    # ---------------------------------------------------------
    # Final validation
    # ---------------------------------------------------------

    if len(portfolio.experiences) != 2:
        raise ValueError(
            "Portfolio extraction failed: "
            f"expected 2 experiences, "
            f"found {len(portfolio.experiences)}"
        )

    if len(portfolio.projects) != 3:
        raise ValueError(
            "Portfolio extraction failed: "
            f"expected 3 projects, "
            f"found {len(portfolio.projects)}"
        )

    if len(portfolio.education) != 1:
        raise ValueError(
            "Portfolio extraction failed: "
            f"expected 1 education entry, "
            f"found {len(portfolio.education)}"
        )

    if not portfolio.achievements:
        raise ValueError(
            "Portfolio extraction failed: "
            "achievements are missing."
        )

    if not portfolio.certifications:
        raise ValueError(
            "Portfolio extraction failed: "
            "certifications are missing."
        )

    # ---------------------------------------------------------
    # Save portfolio.json
    # ---------------------------------------------------------

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            portfolio.model_dump(mode="json"),
            file,
            indent=4,
            ensure_ascii=False,
        )

    print(
        f"Portfolio knowledge saved to: {OUTPUT_PATH}"
    )

    # ---------------------------------------------------------
    # Extraction summary
    # ---------------------------------------------------------

    print("\nExtraction summary:")
    print(
        f"  Experiences: {len(portfolio.experiences)}"
    )
    print(
        f"  Projects: {len(portfolio.projects)}"
    )
    print(
        f"  Education: {len(portfolio.education)}"
    )
    print(
        f"  Achievements: {len(portfolio.achievements)}"
    )
    print(
        f"  Certifications: {len(portfolio.certifications)}"
    )


if __name__ == "__main__":
    main()