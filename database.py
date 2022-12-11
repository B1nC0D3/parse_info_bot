from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

engine = create_engine('sqlite:///sqlite3.db', echo=True)
session = Session(engine)
Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    xpath = Column(String)

    def __str__(self) -> str:
        return self.name


Base.metadata.create_all(engine)


def add_item(name: str, url: str, xpath: str):
    new_item = Item(
        name=name,
        url=url,
        xpath=xpath,
    )
    session.add(new_item)
    session.commit()
