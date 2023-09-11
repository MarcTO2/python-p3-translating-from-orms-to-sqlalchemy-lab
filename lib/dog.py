from sqlalchemy import create_engine
from models import Dog

# Create an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')

def create_table(base):
    # Create tables based on the models defined in 'models.py'
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    # Add a dog object to the session and commit changes to the database
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    # Retrieve a dog from the database based on its ID and return it
    query = session.query(Dog).filter_by(id=row.id).first()
    return query

def get_all(session):
    # Retrieve all dog records from the database and return them
    query = session.query(Dog).all()
    return query

def find_by_name(session, name):
    # Find a dog by name and return it
    query = session.query(Dog).filter_by(name=name).first()
    return query

def find_by_id(session, id):
    # Find a dog by ID and return it
    query = session.query(Dog).filter_by(id=id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    # Find a dog by name and breed, and return it
    query = session.query(Dog).filter_by(name=name, breed=breed).first()
    return query

def update_breed(session, dog, breed):
    # Update the breed of a dog in the database
    query = session.query(Dog).filter_by(id=dog.id).first()
    query.breed = breed
    session.commit()
    return session
