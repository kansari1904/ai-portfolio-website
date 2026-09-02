from enum import Enum

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class EmploymentStatus(str, Enum):
    CURRENT = "current"
    COMPLETED = "completed"


class PersonalInfo(BaseModel):
    name: str
    current_location: str | None = None
    contact_number: str
    email_address: EmailStr
    linkedin: HttpUrl
    github: HttpUrl
    leetcode: HttpUrl | None = None


class TechnicalSkills(BaseModel):
    languages: list[str] = Field(default_factory=list)
    ai_ml: list[str] = Field(default_factory=list)
    frontend: list[str] = Field(default_factory=list)
    backend: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    developer_tools: list[str] = Field(default_factory=list)


class Experience(BaseModel):
    role: str
    company_name: str
    start_date: str
    end_date: str | None = None  
    current_status: EmploymentStatus
    tech_stack: list[str] = Field(default_factory=list)
    description: str


class Education(BaseModel):
    course: str
    college_name: str
    duration: str
    cgpa: str | None = None
    coursework: list[str] | None = None


class Project(BaseModel):
    project_title: str
    project_type: str
    description: str
    tech_stack: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)
    contribution: list[str] = Field(default_factory=list)
    live_link: HttpUrl | None = None


class CareerPreferences(BaseModel):
    target_roles: list[str] = Field(default_factory=list)
    preferred_work_mode: list[str] = Field(default_factory=list)
    preferred_locations: list[str] = Field(default_factory=list)


class KnowledgeBase(BaseModel):
    personal_details: PersonalInfo

    professional_summary: str

    technical_skills: TechnicalSkills

    experiences: list[Experience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)

    achievements: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)

    career_preferences: CareerPreferences

    strengths: list[str] = Field(default_factory=list)

    additional_information: list[str] = Field(default_factory=list)