from fastapi import APIRouter
from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity

router = APIRouter()


@router.get("/graph/nutrition")
async def get_calaries_data():
    return DataCal().gen_graphs().to_dict()


@router.get("/graph/security")
async def gen_security_graph(year: int, var: str):
    chart = DataSecurity().gen_graph(
        year=year, var=var, type="linear", title="Security Map"
    )
    return chart.to_dict()
