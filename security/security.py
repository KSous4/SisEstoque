from sqlalchemy.orm import Session
from schemas.userSchema import User
from utils.encriptation import verify_password
from typing import Union
from datetime import timedelta, datetime
import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
COOKIE_NAME = "Authorization"

def AuthUser(db: Session, email: str, passwd: str):

    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(passwd, user.passwd):
        return False
    return user

def create_access_token(data: dict, expiresDelta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expiresDelta:
        expire = datetime.now(datetime.timezone.utc) + expiresDelta
    else:
        expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt