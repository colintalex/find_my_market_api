from IPython import embed
from sqlalchemy import create_engine
from app.database import Base
from app.main import app
import pytest
from fastapi.encoders import jsonable_encoder
from app.database import SessionLocal
from app import crud
from app.schemas import UserCreate
from os import getenv

engine = create_engine(getenv("DATABASE_URL"))
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture
def cleanup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_user(db, cleanup):
    email = "dan@example.com"
    password = "123456"
    username = "chunky_lover"
    image = "12674.jpg"
    user_in = UserCreate(email=email, password=password, username=username, image=image)
    user = crud.create_user(db, user=user_in)
    assert user.email == email
    assert user.username == username
    assert user.image == image

def test_user_image_has_default_value(db, cleanup):
    email = "dan@example.com"
    password = "123456"
    username = "chunky_lover"
    user_in = UserCreate(email=email, password=password, username=username)
    user = crud.create_user(db, user=user_in)
    assert user.image == ''

