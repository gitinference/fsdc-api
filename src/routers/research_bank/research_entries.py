from __future__ import annotations

import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from src.core.db import get_session
from src.models import (
    ResearchEntry,
    ResearchEntryBase,
    ResearchEntryCreate,
    ResearchEntryUpdate,
    SubdisciplinePublic,
    ResearcherPublic,
    CodebookPublic,
    DatasetPublic,
)

router = APIRouter(prefix="/research-entries", tags=["Research Entries"])


class ResearchEntryNested(ResearchEntryBase):
    id: uuid.UUID
    subdiscipline: SubdisciplinePublic
    researcher: ResearcherPublic
    codebook: CodebookPublic
    dataset: DatasetPublic

    class Config:
        orm_mode = True


@router.get("/", response_model=List[ResearchEntryNested])
def list_entries(
    session: Session = Depends(get_session),
    approved: Optional[bool] = None,  # Add query parameter for filtering
):
    stmt = select(ResearchEntry).options(
        selectinload(ResearchEntry.subdiscipline),
        selectinload(ResearchEntry.researcher),
        selectinload(ResearchEntry.codebook),
        selectinload(ResearchEntry.dataset),
    )
    if approved is not None:
        stmt = stmt.where(ResearchEntry.approved == approved)  # Filter by 'approved'
    return session.exec(stmt).all()


@router.post(
    "/", response_model=ResearchEntryNested, status_code=status.HTTP_201_CREATED
)
def create_entry(data: ResearchEntryCreate, session: Session = Depends(get_session)):
    obj = ResearchEntry.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.put(
    "/", response_model=ResearchEntryNested, status_code=status.HTTP_201_CREATED
)
def update_entry(data: ResearchEntryUpdate, session: Session = Depends(get_session)):
    if data.id is None:
        raise HTTPException(status_code=400, detail="ID is required for update")

    obj = session.get(ResearchEntry, data.id)
    if not obj:
        raise HTTPException(status_code=404, detail="ResearchEntry not found")

    data_dict = data.model_dump(exclude_unset=True)
    for key, value in data_dict.items():
        setattr(obj, key, value)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
