from fastapi import APIRouter
from ..submodules.fsdc_calories.src.data_process import DataCal

router = APIRouter()

dc = DataCal()


@router.get("/graph/nutrition")
async def get_calaries_data():
    return dc.gen_graphs().to_dict()
