from enum import Enum

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity
from ..submodules.pr_food.src.data.data_process import FoodDeseart

router = APIRouter()


class SecurityGraphModel(str, Enum):
    total_insec = "total_insec"
    insecurity_hous = "insecurity_hous"


class FoodGraphModel(str, Enum):
    supermarkets_and_others = "supermarkets_and_others"
    supermarkets = "supermarkets"
    convenience_retailers = "convenience_retailers"
    whole_foods = "whole_foods"


@router.get("/graph/nutrition", response_class=HTMLResponse)
async def get_calaries_data():
    return DataCal().gen_graphs_nuti_data().to_html()


@router.get("/graph/security", response_class=HTMLResponse)
# the available variables
async def gen_security_graph(year: int, var: SecurityGraphModel):
    chart = DataSecurity().gen_graph(
        year=year, var=var.value, type="linear", title="Security Map"
    )
    return chart.to_html()


@router.get("/graph/food", response_class=HTMLResponse)
async def gen_food_graph(var: FoodGraphModel, year: int, qtr: int, title):
    return (
        FoodDeseart()
        .gen_food_graph(var=var.value, year=year, qtr=qtr, title=title)
        .to_html()
    )


@router.get("/graph/price", response_class=HTMLResponse)
async def get_price_graph():
    return DataCal().gen_graphs_price_change().to_html()


@router.get("/graph/myplate", response_class=HTMLResponse)
async def get_myplate_graph():
    return DataCal().gen_graphs_plate().to_html()
