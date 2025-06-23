from typing import Optional
import uuid
from datetime import date, datetime
from sqlmodel import Field, SQLModel, Relationship


# ---------- Subdiscipline ----------
class SubdisciplineBase(SQLModel):
    name: str
    description: str


class SubdisciplineCreate(SubdisciplineBase):
    pass


class SubdisciplineUpdate(SQLModel):
    name: str | None = None
    description: str | None = None


class Subdiscipline(SubdisciplineBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    research_entries: list["ResearchEntry"] = Relationship(
        back_populates="subdiscipline"
    )


class SubdisciplinePublic(SubdisciplineBase):
    id: uuid.UUID


# ---------- Researcher ----------
class ResearcherBase(SQLModel):
    fname: str
    lname: str
    education: str
    phone: str
    email: str


class ResearcherCreate(ResearcherBase):
    pass


class ResearcherUpdate(SQLModel):
    fname: str | None = None
    lname: str | None = None
    education: str | None = None
    phone: str | None = None
    email: str | None = None


class Researcher(ResearcherBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    research_entries: list["ResearchEntry"] = Relationship(back_populates="researcher")


class ResearcherPublic(ResearcherBase):
    id: uuid.UUID


# ---------- Codebook ----------
class CodebookBase(SQLModel):
    file_name: str
    file_path: Optional[str]


class CodebookCreate(CodebookBase):
    pass


class CodebookUpdate(SQLModel):
    file_name: str | None = None
    file_path: str | None = None


class Codebook(CodebookBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
    file_path: Optional[str] = Field(default=None, nullable=True)
    research_entries: list["ResearchEntry"] = Relationship(back_populates="codebook")


class CodebookPublic(CodebookBase):
    id: uuid.UUID
    uploaded_at: datetime


# ---------- Dataset ----------
class DatasetBase(SQLModel):
    file_name: str
    file_path: Optional[str]


class DatasetCreate(DatasetBase):
    pass


class DatasetUpdate(SQLModel):
    file_name: str | None = None
    file_path: str | None = None


class Dataset(DatasetBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
    file_path: Optional[str] = Field(default=None, nullable=True)
    research_entries: list["ResearchEntry"] = Relationship(back_populates="dataset")


class DatasetPublic(DatasetBase):
    id: uuid.UUID
    uploaded_at: datetime


# ---------- ResearchEntry ----------
class ResearchEntryBase(SQLModel):
    date_started: date
    date_ended: date
    description: str
    bibliography: str

    # Additional fields
    title: str
    project_summary: str
    time_period: str
    thesis_advisor_name: str
    thesis_advisor_email: str
    thesis_advisor_phone: str
    postal_address: str
    department_and_faculty: str
    orcid: str


class ResearchEntryCreate(ResearchEntryBase):
    subdiscipline_id: uuid.UUID
    researcher_id: uuid.UUID
    codebook_id: uuid.UUID
    dataset_id: uuid.UUID


class ResearchEntryUpdate(SQLModel):
    date_started: date | None = None
    date_ended: date | None = None
    description: str | None = None
    bibliography: str | None = None
    title: str | None = None
    project_summary: str | None = None
    time_period: str | None = None
    thesis_advisor_name: str | None = None
    thesis_advisor_email: str | None = None
    thesis_advisor_phone: str | None = None
    postal_address: str | None = None
    department_and_faculty: str | None = None
    orcid: str | None = None
    subdiscipline_id: uuid.UUID | None = None
    researcher_id: uuid.UUID | None = None
    codebook_id: uuid.UUID | None = None
    dataset_id: uuid.UUID | None = None
    approved: bool | None = None


class ResearchEntry(ResearchEntryBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    subdiscipline_id: uuid.UUID = Field(foreign_key="subdiscipline.id")
    subdiscipline: Subdiscipline = Relationship(back_populates="research_entries")

    researcher_id: uuid.UUID = Field(foreign_key="researcher.id")
    researcher: Researcher = Relationship(back_populates="research_entries")

    codebook_id: uuid.UUID = Field(foreign_key="codebook.id")
    codebook: Codebook = Relationship(back_populates="research_entries")

    dataset_id: uuid.UUID = Field(foreign_key="dataset.id")
    dataset: Dataset = Relationship(back_populates="research_entries")

    approved: bool = Field(default=False)


class ResearchEntryPublic(ResearchEntryBase):
    id: uuid.UUID
    subdiscipline_id: uuid.UUID
    researcher_id: uuid.UUID
    codebook_id: uuid.UUID
    dataset_id: uuid.UUID
