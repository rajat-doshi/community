from sqlalchemy import engine
from my_database.model.users.main import User
from my_database.model.family.main import Family
from my_database.db import Base, engine

def test():
    print("Testing database connection...")


def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    test()
    setup_database()