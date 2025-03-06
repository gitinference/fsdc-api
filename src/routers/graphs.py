from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity

router = APIRouter()


@router.get("/graph/nutrition", response_class=HTMLResponse)
async def get_calaries_data():
    return DataCal().gen_graphs_nuti_data().to_html()


@router.get("/graph/security", response_class=HTMLResponse)
async def gen_security_graph(year: int, var: str):
    chart = DataSecurity().gen_graph(
        year=year, var=var, type="linear", title="Security Map"
    )
    return chart.to_html()
