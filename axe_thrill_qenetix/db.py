from sqlalchemy import JSON, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Microcontainer(Base):
    __tablename__ = 'microcontainers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    entrypoint = Column(String, nullable=False)
    domains = Column(JSON, nullable=False)
    payload = Column(JSON, nullable=True)


def bootstrap_database(uri: str = 'sqlite:///microcontainers.db'):
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)
