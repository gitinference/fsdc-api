# src/research_bank/datasets.py
import uuid
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import StreamingResponse
from sqlmodel import Session, select
from env import MEDIA_ROOT
from src.core.file_manager import FileManager
from src.models import Dataset, DatasetCreate
from src.core.db import get_session

router = APIRouter(prefix="/datasets", tags=["Datasets"])
file_manager = FileManager(root_directory=MEDIA_ROOT)


@router.get("/", response_model=list[Dataset])
def list_datasets(session: Session = Depends(get_session)):
    return session.exec(select(Dataset)).all()


@router.post("/", response_model=Dataset, status_code=status.HTTP_201_CREATED)
def create_dataset(
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
):
    file_uuid = str(uuid.uuid4())

    file_subpath = f"datasets/{file_uuid}"
    file_manager.write(path=file_subpath, file_to_write=file)

    dataset = Dataset(id=file_uuid, file_name=file.filename, file_path=file_subpath)
    session.add(dataset)
    session.commit()
    session.refresh(dataset)
    return dataset


@router.get("/{id}", response_model=Dataset)
async def get_dataset_by_id(id: uuid.UUID, session: Session = Depends(get_session)):
    codebook = session.exec(select(Dataset).where(Dataset.id == id)).first()
    if not codebook:
        raise HTTPException(status_code=404, detail="Codebook not found")

    file_stream = file_manager.read(codebook.file_path)

    return StreamingResponse(
        file_stream,
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={codebook.file_name}"},
    )
