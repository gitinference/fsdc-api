from fastapi import APIRouter

from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity

router = APIRouter()


@router.get("/data/calaries/")
async def get_calaries_data():
    return DataCal().gen_nuti_data().to_pandas().to_dict()


@router.get("/data/security/")
async def get_security_data():
    df = DataSecurity().calc_security()
    return df[["year", "geoid"]].to_dict()
