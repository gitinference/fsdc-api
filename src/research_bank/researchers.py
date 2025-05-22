from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from ..models import Researcher, ResearcherCreate
from ..db import get_session

router = APIRouter(prefix="/researchers", tags=["Researchers"])

@router.get("/", response_model=list[Researcher])
def list_researchers(session: Session = Depends(get_session)):
    return session.exec(select(Researcher)).all()

@router.post("/", response_model=Researcher, status_code=status.HTTP_201_CREATED)
def create_researcher(data: ResearcherCreate, session: Session = Depends(get_session)):
    obj = Researcher.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
