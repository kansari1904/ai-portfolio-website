from app.schemas.portfolio import (
    CareerPreferences,
    Education,
    EmploymentStatus,
    Experience,
    KnowledgeBase,
    PersonalInfo,
    Project,
    TechnicalSkills,
)


def test_portfolio_schema():
    portfolio = KnowledgeBase(
        personal_details=PersonalInfo(
            name="Khalid Ansari",
            current_location="Bengaluru, India",
            contact_number="9999999999",
            email_address="khalid@example.com",
            linkedin="https://linkedin.com/in/example",
            github="https://github.com/example",
        ),
        professional_summary="Software Engineer and AI Engineer.",
        technical_skills=TechnicalSkills(
            languages=[
                "Python",
                "Java",
            ],
            ai_ml=[
                "LangChain",
                "RAG",
            ],
            frontend=[
                "React.js",
            ],
            backend=[
                "FastAPI",
                "Node.js",
            ],
            databases=[
                "MongoDB",
                "MySQL",
            ],
            developer_tools=[
                "Git",
                "GitHub",
            ],
        ),
        experiences=[
            Experience(
                role="Software Engineer",
                company_name="Example Company",
                start_date="2025-01-01",
                current_status=EmploymentStatus.CURRENT,
                tech_stack=[
                    "Python",
                    "FastAPI",
                ],
                description="Built backend services.",
            )
        ],
        education=[
            Education(
                course="B.E. Computer Science and Engineering",
                college_name="Chandigarh University",
                duration="2021-2025",
                coursework=[
                    "Data Structures and Algorithms",
                    "DBMS",
                    "Computer Networks",
                ],
            )
        ],
        projects=[
            Project(
                project_title="DocuMind-AI",
                project_type="AI Full-Stack",
                description="AI-powered document analysis application.",
                tech_stack=[
                    "React",
                    "Node.js",
                    "Gemini",
                ],
                features=[
                    "PDF upload",
                    "Document summarization",
                    "AI chat",
                ],
                contribution=[
                    "Built the backend",
                    "Integrated Gemini API",
                ],
            )
        ],
        achievements=[
            "Solved 300+ DSA problems on LeetCode and GeeksforGeeks",
        ],
        certifications=[
            "HackerRank JavaScript Certificate, 2024",
        ],
        career_preferences=CareerPreferences(
            target_roles=[
                "Software Engineer",
                "AI Engineer",
                "AI Full-Stack Developer",
            ],
            preferred_work_mode=[
                "Full-time",
            ],
            preferred_locations=[
                "Bengaluru",
                "Remote",
            ],
        ),
        strengths=[
            "Full-stack development",
            "Backend development",
            "LLM API integration",
            "RAG systems",
            "Problem solving",
        ],
        additional_information=[
            "Interested in building scalable AI-powered applications",
        ],
    )

    assert portfolio.personal_details.name == "Khalid Ansari"

    assert "Python" in portfolio.technical_skills.languages

    assert "LangChain" in portfolio.technical_skills.ai_ml

    assert "FastAPI" in portfolio.technical_skills.backend

    assert len(portfolio.projects) == 1

    assert portfolio.projects[0].project_title == "DocuMind-AI"

    assert len(portfolio.experiences) == 1

    assert portfolio.career_preferences.target_roles[0] == "Software Engineer"