from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta

import crud
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session


SECRET_KEY = "6e34034cae5a1c8acd1a27894bb2027f36e993f5a8aa57e4293d5429f7a9538f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

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
