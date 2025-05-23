# src/research_bank/datasets.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from src.models import Dataset, DatasetCreate
from src.core.db import get_session

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.get("/", response_model=list[Dataset])
def list_datasets(session: Session = Depends(get_session)):
    return session.exec(select(Dataset)).all()


@router.post("/", response_model=Dataset, status_code=status.HTTP_201_CREATED)
def create_dataset(data: DatasetCreate, session: Session = Depends(get_session)):
    obj = Dataset.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
