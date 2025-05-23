# src/research_bank/research_entries.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from src.models import ResearchEntry, ResearchEntryCreate
from src.core.db import get_session

router = APIRouter(prefix="/research-entries", tags=["ResearchEntries"])


@router.get("/", response_model=list[ResearchEntry])
def list_research_entries(session: Session = Depends(get_session)):
    return session.exec(select(ResearchEntry)).all()


@router.post("/", response_model=ResearchEntry, status_code=status.HTTP_201_CREATED)
def create_research_entry(data: ResearchEntryCreate, session: Session = Depends(get_session)):
    obj = ResearchEntry.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
