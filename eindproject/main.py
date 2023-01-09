from fastapi import Depends, FastAPI, HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

import os

import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = "6e34034cae5a1c8acd1a27894bb2027f36e993f5a8aa57e4293d5429f7a9538f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 480

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_shopper(db: Session, username:str, password:str):
    shopper = crud.get_shopper_by_username(db, username)
    if not shopper:
        return False
    if not verify_password(password, shopper.hashed_password):
        return False
    return shopper

def get_current_shopper(db:Session, token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    shopper = crud.get_shopper_by_username(db, username)
    if shopper is None:
        raise credentials_exception
    return shopper

def get_current_active_shopper(db: Session, token: str = Depends(oauth2_schema)):
    current_shopper = get_current_shopper(db, token)
    if not current_shopper.is_active:
        raise HTTPException(status_code=400, detail="Inactive shopper")
    return current_shopper



@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    shopper = authenticate_shopper(db, form_data.username, form_data.password)
    if not shopper:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": shopper.username}
    )
    return {"access_token": access_token, "token_type": "Bearer"}

@app.get("/shoppers/", response_model=list[schemas.Shopper])
def read_shoppers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    shoppers = crud.get_shoppers(db, skip=skip, limit=limit)
    return shoppers


@app.post("/shoppers/", response_model=schemas.Shopper)
def create_shopper(shopper: schemas.ShopperCreate, db: Session = Depends(get_db)):
    db_shopper = crud.get_shopper_by_username(db, username=shopper.username)
    if db_shopper:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_shopper(db=db, shopper=shopper)


@app.get("/shoppers/{shopper_id}", response_model=schemas.Shopper)
def read_shopper(shopper_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    db_shopper = crud.get_shopper(db, shopper_id=shopper_id)
    if db_shopper is None:
        raise HTTPException(status_code=404, detail="Shopper not found")
    return db_shopper

#@app.delete("/shoppers/delete", response_model=schemas.Shopper)
#def delete_shopper(shopper_id: int, db: Session = Depends(get_db)):
#    db_shopper = crud.get_shopper(db, shopper_id=shopper_id)
#    db.delete(db_shopper)
#    db.commit()
#    db.refresh(db_shopper)
#    return "the shopper has been deleted use the shoppers get function to check"



#@app.get("/shoppers/me", response_model=schemas.Shopper)
#def read_shoppers_me(db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
#    current_shopper = auth.get_current_shopper(db, token)
#    return current_shopper


@app.post("/shoppers/{shopper_id}/items/", response_model=schemas.Item)
def create_item_for_shopper(
    shopper_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_shopper_item(db=db, item=item, shopper_id=shopper_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

#@app.delete("/shoppers/{shopper_id}/items/delete", response_model=list[schemas.Item])
#def delete_item_for_shopper(shopp er_id: int, item: schemas.ItemDelete, db: Session = Depends(get_db)):
#    return crud.delete_shopper_item(db=db, shopper_id=shopper_id)

#@app.delete("/shoppers/{shopper_id}/delete")
#def delete_shopper(shopper_id: int, db: Session = Depends(get_db)):
#    with Session(engine) as session:
#        shopper = session.get(db, shopper_id)
#        if not shopper:
#            raise HTTPException(status_code=404, detail="Shopper not found")
#        session.delete(shopper)
#        session.commit()
#        return {"ok": True}