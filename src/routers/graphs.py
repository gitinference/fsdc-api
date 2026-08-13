from enum import Enum

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from fsdc_calories import DataCal
from fsdc_security import SecurityViz
from prfood_repl import FoodDeseart

router = APIRouter()


class SecurityGraphModel(str, Enum):
    total_insec = "total_insec"
    insecurity_hous = "insecurity_hous"


class FoodGraphModel(str, Enum):
    supermarkets_and_others = "supermarkets_and_others"
    supermarkets = "supermarkets"
    convenience_retailers = "convenience_retailers"
    whole_foods = "whole_foods"


class CaloriesGraphModel(str, Enum):
    local = "local"
    both = "both"
    imported = "imported"


@router.get("/graph/nutrition", response_class=HTMLResponse)
async def get_calaries_data():
    # 1. Generate the Altair chart object
    chart = DataCal().gen_graphs_nuti_data()

    # 2. Make the chart width responsive
    chart = chart.properties(width="container", height=300)

    # 3. Export to HTML string
    html_content = chart.to_html()

    # 4. Inject mobile meta tag and centering CSS into the HTML head
    mobile_meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    centering_style = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background-color: #ffffff;
        }
        .vega-embed {
            max-width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
    </style>
    """

    if "<head>" in html_content:
        html_content = html_content.replace(
            "<head>", f"<head>{mobile_meta}{centering_style}"
        )

    return HTMLResponse(content=html_content)


@router.get("/graph/security", response_class=HTMLResponse)
async def gen_security_graph(year: int):
    # 1. Generate the Altair chart object
    chart = SecurityViz().gen_graph_total(
        year=year,
    )

    # 2. Make the chart width responsive
    chart = chart.properties(width="container", height=300)

    # 3. Export to HTML string
    html_content = chart.to_html()

    # 4. Inject mobile meta tag and centering CSS into the HTML head
    mobile_meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    centering_style = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background-color: #ffffff;
        }
        .vega-embed {
            max-width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
    </style>
    """

    if "<head>" in html_content:
        html_content = html_content.replace(
            "<head>", f"<head>{mobile_meta}{centering_style}"
        )

    return HTMLResponse(content=html_content)


@router.get("/graph/food", response_class=HTMLResponse)
async def gen_food_graph(var: FoodGraphModel, year: int, qtr: int, title):
    # 1. Generate the Altair chart object
    chart = FoodDeseart().gen_food_graph(var=var.value, year=year, qtr=qtr, title=title)

    # 2. Make the chart width responsive
    chart = chart.properties(width="container", height=300)

    # 3. Export to HTML string
    html_content = chart.to_html()

    # 4. Inject mobile meta tag and centering CSS into the HTML head
    mobile_meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    centering_style = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background-color: #ffffff;
        }
        .vega-embed {
            max-width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
    </style>
    """

    if "<head>" in html_content:
        html_content = html_content.replace(
            "<head>", f"<head>{mobile_meta}{centering_style}"
        )

    return HTMLResponse(content=html_content)


@router.get("/graph/timeseries", response_class=HTMLResponse)
async def gen_graphs_nuti_data_fiscal(source: CaloriesGraphModel):
    # 1. Generate the Altair chart object
    chart = DataCal().gen_graphs_nuti_data_fiscal(source=source.value)

    # 2. Make the chart width responsive
    chart = chart.properties(width="container", height=300)

    # 3. Export to HTML string
    html_content = chart.to_html()

    # 4. Inject mobile meta tag and centering CSS into the HTML head
    mobile_meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    centering_style = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background-color: #ffffff;
        }
        .vega-embed {
            max-width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
    </style>
    """

    if "<head>" in html_content:
        html_content = html_content.replace(
            "<head>", f"<head>{mobile_meta}{centering_style}"
        )

    return HTMLResponse(content=html_content)


@router.get("/graph/price", response_class=HTMLResponse)
async def get_price_graph():
    # 1. Generate the Altair chart object
    chart = DataCal().gen_graphs_price_change()

    # 2. Make the chart width responsive
    chart = chart.properties(width="container", height=300)

    # 3. Export to HTML string
    html_content = chart.to_html()

    # 4. Inject mobile meta tag and centering CSS into the HTML head
    mobile_meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    centering_style = """
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background-color: #ffffff;
        }
        .vega-embed {
            max-width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
    </style>
    """

    if "<head>" in html_content:
        html_content = html_content.replace(
            "<head>", f"<head>{mobile_meta}{centering_style}"
        )

    return HTMLResponse(content=html_content)


@router.get("/graph/myplate", response_class=HTMLResponse)
async def get_myplate_graph():
    chart_html = DataCal().gen_graphs_plate().to_html()

    css_patch = """
    <style>
    #vis.vega-embed {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        padding: 0 !important;
    }
    #vis.vega-embed > div {
        margin: 0 auto !important;
    }
    </style>
    """

    # Inject right after the <head> tag
    chart_html = chart_html.replace("<head>", f"<head>{css_patch}")

    return chart_html
