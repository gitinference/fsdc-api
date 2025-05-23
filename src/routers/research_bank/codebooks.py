# src/research_bank/codebooks.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from src.models import Codebook, CodebookCreate
from src.core.db import get_session

router = APIRouter(prefix="/codebooks", tags=["Codebooks"])


@router.get("/", response_model=list[Codebook])
def list_codebooks(session: Session = Depends(get_session)):
    return session.exec(select(Codebook)).all()


@router.post("/", response_model=Codebook, status_code=status.HTTP_201_CREATED)
def create_codebook(data: CodebookCreate, session: Session = Depends(get_session)):
    obj = Codebook.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
