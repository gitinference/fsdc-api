from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from src.models import Subdiscipline, SubdisciplineCreate
from src.core.db import get_session

router = APIRouter(prefix="/subdisciplines", tags=["Subdisciplines"])


@router.get("/", response_model=list[Subdiscipline])
def list_subdisciplines(session: Session = Depends(get_session)):
    return session.exec(select(Subdiscipline)).all()


@router.post("/", response_model=Subdiscipline, status_code=status.HTTP_201_CREATED)
def create_subdiscipline(
    data: SubdisciplineCreate, session: Session = Depends(get_session)
):
    obj = Subdiscipline.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
