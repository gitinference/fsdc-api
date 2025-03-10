from fastapi import APIRouter
from fastapi.responses import FileResponse
from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity

import os

router = APIRouter()


@router.get("/files/nutrition/")
async def get_calaries_data():
    df = DataCal(database_file="data/data.ddb").gen_nuti_data()
    file_path = os.path.join(os.getcwd(), "data", "processed", "nutrition.csv")
    df.write_csv(file_path)
    return FileResponse(file_path, media_type="text/csv", filename="nutrition.csv")


@router.get("/files/nutrition/")
async def get_security_data():
    df = DataSecurity(database_file="data/data.ddb").calc_security()
    file_path = os.path.join(os.getcwd(), "data", "processed", "security.csv")
    df.write_csv(file_path)
    return FileResponse(file_path, media_type="text/csv", filename="security.csv")
