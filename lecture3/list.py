import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://luuk:Jupiter@localhost:5432/lecture3')
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flights in flights:
        print(f"{flight.origin} to {flight.destination}), {flight.duration} minutes.")

if __name__ == "__main__":
    main()
