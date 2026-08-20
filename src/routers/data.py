from fastapi import APIRouter
import importlib.resources as resources

import numpy as np
from fsdc_calories import DataCal
from fsdc_security import SecurityData
import polars as pl
import pandas as pd

router = APIRouter()


@router.get("/data/calaries/")
async def get_calaries_data():
    return DataCal().gen_nuti_data().to_pandas().to_dict()


@router.get("/data/security/")
async def get_security_data():
    df = SecurityData().calc_security()
    return df[["year", "geoid"]].to_dict()


@router.get("/data/price")
async def get_price_data():
    df = DataCal().process_price(agriculture_filter=True)
    path_data = str(resources.files("fsdc_calories").joinpath("data/hts4_walk.parquet"))

    desc_df = pl.read_parquet(path_data).rename(
        {"code_4": "hs4", "Description": "hts_desc"}
    )
    df = df.join(desc_df, on="hs4", how="inner", validate="m:1")

    # Drop nulls directly in Polars
    df = df.drop_nulls()

    # Convert Polars to Pandas
    pdf = df.to_pandas()

    # Drop rows with infinite values (inf / -inf)
    pdf = pdf.replace([np.inf, -np.inf], np.nan).dropna()

    # Return as a list of dictionaries (records)
    return pdf.to_dict(orient="records")
