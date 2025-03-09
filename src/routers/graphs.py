from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity
from ..submodules.pr_food.src.data.data_process import FoodDeseart

router = APIRouter()


@router.get("/graph/nutrition", response_class=HTMLResponse)
async def get_calaries_data():
    return DataCal().gen_graphs_nuti_data().to_html()


@router.get("/graph/security", response_class=HTMLResponse)
# the available variables
async def gen_security_graph(year: int, var: str):
    chart = DataSecurity().gen_graph(
        year=year, var=var, type="linear", title="Security Map"
    )
    return chart.to_html()


@router.get("/graph/food", response_class=HTMLResponse)
# the available variables are supermarkets_and_others supermarkets convenience_retailers and whole_foods
async def gen_food_graph(var: str, year: int, qtr: int, title):
    return (
        FoodDeseart().gen_food_graph(var=var, year=year, qtr=qtr, title=title).to_html()
    )
