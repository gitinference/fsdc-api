from pathlib import Path
from typing import Union
from fastapi import UploadFile
import shutil
from io import BufferedReader


class FileManager:
    def __init__(self, root_directory: Union[Path, str]) -> None:
        self.root_directory = Path(root_directory)
        if not self.root_directory.exists():
            self.root_directory.mkdir(exist_ok=True)

    def get_full_path(self, path: Union[Path, str]) -> Path:
        full_path = self.root_directory / path
        return full_path.resolve()

    def read(self, path: Union[Path, str]) -> BufferedReader:
        """
        Return a file opened in binary mode.
        """
        file_path = self.get_full_path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return open(file_path, "rb")

    def write(self, path: Union[Path, str], file_to_write: UploadFile) -> None:
        """
        Save a file to the given relative path.
        """
        file_path = self.get_full_path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file_to_write.file, buffer)
