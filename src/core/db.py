from datetime import date
from sqlmodel import Session, create_engine, SQLModel, select
from env import get_db_credentials

from src.models import (
    Subdiscipline,
    Researcher,
    Codebook,
    Dataset,
    ResearchEntry,
)

DATABASE_URL = get_db_credentials()[4]
engine = create_engine(DATABASE_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def _seed_initial_data(session: Session) -> None:

    # # if db alraeady had data, exit.
    # if session.exec(select(Subdiscipline)).first():
    #     return

    # --- Core reference tables ----------
    sub_fs = Subdiscipline(
        name="Food Security", description="Studies on food security in PR"
    )
    sub_nt = Subdiscipline(name="Nutrition", description="Human nutrition research")

    res_ana = Researcher(
        fname="Ana",
        lname="Torres",
        education="PhD",
        phone="7875550001",
        email="ana.torres@example.com",
    )
    res_luis = Researcher(
        fname="Luis",
        lname="Ramos",
        education="MSc",
        phone="7875550002",
        email="luis.ramos@example.com",
    )

    cb_fs = Codebook(file="codebook_food_security.pdf")
    cb_nt = Codebook(file="codebook_nutrition.pdf")

    ds_fs = Dataset(file="dataset_food_security.csv")
    ds_nt = Dataset(file="dataset_nutrition.csv")

    session.add_all([sub_fs, sub_nt, res_ana, res_luis, cb_fs, cb_nt, ds_fs, ds_nt])
    session.commit()

    # --- Fact table --------
    re_fs = ResearchEntry(
        date_started=date(2024, 1, 1),
        date_ended=date(2024, 6, 30),
        description="Pilot study measuring household food insecurity levels.",
        bibliography="Torres A. et al. (2025)",
        subdiscipline_id=sub_fs.id,
        researcher_id=res_ana.id,
        codebook_id=cb_fs.id,
        dataset_id=ds_fs.id,
    )

    re_nt = ResearchEntry(
        date_started=date(2023, 3, 15),
        date_ended=date(2023, 12, 20),
        description="Cross-sectional survey of college students' nutritional intake.",
        bibliography="Ramos L. et al. (2024)",
        subdiscipline_id=sub_nt.id,
        researcher_id=res_luis.id,
        codebook_id=cb_nt.id,
        dataset_id=ds_nt.id,
    )

    session.add_all([re_fs, re_nt])
    session.commit()


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        _seed_initial_data(session)
