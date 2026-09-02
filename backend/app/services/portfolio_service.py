import json
from functools import lru_cache
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]

PORTFOLIO_PATH = (
    BASE_DIR
    / "data"
    / "knowledge"
    / "portfolio.json"
)


@lru_cache(maxsize=1)
def load_portfolio() -> dict[str, Any]:
    """
    Load portfolio.json once and keep it in memory.

    The portfolio is static knowledge, so there is no reason
    to read the JSON file from disk for every request.
    """

    if not PORTFOLIO_PATH.exists():
        raise FileNotFoundError(
            f"Portfolio knowledge base not found: {PORTFOLIO_PATH}"
        )

    with PORTFOLIO_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            "Portfolio knowledge base must be a JSON object."
        )

    return data


def get_projects() -> list[dict[str, Any]]:
    """
    Return all projects from the portfolio.
    """

    portfolio = load_portfolio()

    projects = portfolio.get("projects", [])

    if not isinstance(projects, list):
        raise ValueError(
            "Portfolio 'projects' must be a list."
        )

    return projects


def get_experiences() -> list[dict[str, Any]]:
    """
    Return all professional experiences.
    """

    portfolio = load_portfolio()

    experiences = portfolio.get("experiences", [])

    if not isinstance(experiences, list):
        raise ValueError(
            "Portfolio 'experiences' must be a list."
        )

    return experiences


def get_education() -> list[dict[str, Any]]:
    """
    Return education information.
    """

    portfolio = load_portfolio()

    education = portfolio.get("education", [])

    if not isinstance(education, list):
        raise ValueError(
            "Portfolio 'education' must be a list."
        )

    return education


def get_technical_skills() -> dict[str, Any]:
    """
    Return the complete technical skills section.
    """

    portfolio = load_portfolio()

    skills = portfolio.get("technical_skills", {})

    if not isinstance(skills, dict):
        raise ValueError(
            "Portfolio 'technical_skills' must be an object."
        )

    return skills


def get_achievements() -> list[str]:
    """
    Return portfolio achievements.
    """

    portfolio = load_portfolio()

    achievements = portfolio.get("achievements", [])

    if not isinstance(achievements, list):
        raise ValueError(
            "Portfolio 'achievements' must be a list."
        )

    return achievements


def get_certifications() -> list[str]:
    """
    Return portfolio certifications.
    """

    portfolio = load_portfolio()

    certifications = portfolio.get("certifications", [])

    if not isinstance(certifications, list):
        raise ValueError(
            "Portfolio 'certifications' must be a list."
        )

    return certifications


def get_career_preferences() -> dict[str, Any]:
    """
    Return career preferences.
    """

    portfolio = load_portfolio()

    preferences = portfolio.get(
        "career_preferences",
        {},
    )

    if not isinstance(preferences, dict):
        raise ValueError(
            "Portfolio 'career_preferences' must be an object."
        )

    return preferences


def get_professional_summary() -> str:
    """
    Return the professional summary.
    """

    portfolio = load_portfolio()

    summary = portfolio.get(
        "professional_summary",
        "",
    )

    if not isinstance(summary, str):
        raise ValueError(
            "Portfolio 'professional_summary' must be a string."
        )

    return summary