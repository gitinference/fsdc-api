# src/research_bank/codebooks.py
import uuid
from fastapi import APIRouter, Depends, File, Form, UploadFile, status, HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session, select
from src.core.file_manager import FileManager
from src.models import Codebook
from src.core.db import get_session
from settings import MEDIA_ROOT

router = APIRouter(prefix="/codebooks", tags=["Codebooks"])
file_manager = FileManager(root_directory=MEDIA_ROOT)


@router.get("/", response_model=list[Codebook])
def list_codebooks(session: Session = Depends(get_session)):
    return session.exec(select(Codebook)).all()


@router.post("/", response_model=Codebook, status_code=status.HTTP_201_CREATED)
def create_codebook(
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
):
    file_uuid = str(uuid.uuid4())

    file_subpath = f"codebooks/{file_uuid}"
    file_manager.write(path=file_subpath, file_to_write=file)

    codebook = Codebook(id=file_uuid, file_name=file.filename, file_path=file_subpath)
    session.add(codebook)
    session.commit()
    session.refresh(codebook)
    return codebook


@router.get("/{id}")
async def get_codebook_by_id(id: uuid.UUID, session: Session = Depends(get_session)):
    codebook = session.exec(select(Codebook).where(Codebook.id == id)).first()
    if not codebook:
        raise HTTPException(status_code=404, detail="Codebook not found")

    file_stream = file_manager.read(codebook.file_path)

    return StreamingResponse(
        file_stream,
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={codebook.file_name}"},
    )
