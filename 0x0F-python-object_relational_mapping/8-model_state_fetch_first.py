#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()
    st = session.query(State).order_by(State.id).first()
    if (State is None):
        print("Nothing")
    print(st.id, st.name, sep=(": "))
