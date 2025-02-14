from fastapi import APIRouter

from ..submodules.fsdc_calories.src.data_process import DataCal

router = APIRouter()


@router.get("/data/")
async def get_calaries_data():
    return DataCal().gen_nuti_data().to_pandas().to_json()
