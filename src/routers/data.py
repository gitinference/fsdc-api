from fastapi import APIRouter

from ..submodules.fsdc_calories.src.data_process import DataCal
from ..submodules.fsdc_security.src.data.data_viz import DataSecurity

router = APIRouter()


@router.get("/data/calaries/")
async def get_calaries_data():
    return DataCal(database_file="data/data.ddb").gen_nuti_data().to_pandas().to_dict()


@router.get("/data/security/")
async def get_security_data():
    df = DataSecurity(database_file="data/data.ddb").calc_security()
    return df[["year", "geoid"]].to_dict()


@router.get("/data/price")
async def get_price_data():
    imports, exports = DataCal(database_file="data/data.ddb").gen_price_rankings()

    # Drop nan since they are not JSON compliant for the default FastAPI serialization library
    imports = imports.dropna()
    exports = exports.dropna()

    response = {"import_data": imports.to_dict(), "export_data": exports.to_dict()}
    return response
