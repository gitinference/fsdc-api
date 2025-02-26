from fastapi import APIRouter
from fastapi.responses import FileResponse
from ..submodules.fsdc_calories.src.data_process import DataCal
import os

router = APIRouter()
dc = DataCal()


@router.get("/files/nutrition/")
async def get_calaries_data():
    df = dc.gen_nuti_data()
    file_path = os.path.join(os.getcwd(), "data", "nutrition.csv")
    df.write_csv(file_path)
    return FileResponse(file_path, media_type="text/csv", filename=f"nutrition.csv")
