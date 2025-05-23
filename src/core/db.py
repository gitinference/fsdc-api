from sqlmodel import Session, create_engine, SQLModel
from env import get_db_credentials

DATABASE_URL = get_db_credentials()[4]
engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)

    # Initalize default values for tables
