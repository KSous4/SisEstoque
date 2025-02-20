from fastapi import HTTPException, Request
from datetime import datetime, timedelta
from http import HTTPStatus
import jwt


# temporarary thing just make config later
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Authentication():

    @staticmethod
    def create_acess_token(data: dict, expireDelta: timedelta | None = None):
        toEncode = data.copy()
        expire = datetime.now() + (expireDelta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        toEncode.update({"exp": expire})
        return jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def getCurentUsr(r: Request):
        token = r.cookies.get('accessToken')
        if not token:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='Not Authenticated'
            )

        try:
            payload: dict = jwt.decode(
                token, SECRET_KEY, algorithms=[ALGORITHM])
            usr: str = payload.get('sub')
            if not usr:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED, detail='Invalid token'
                )
            return {'username': usr}
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='Expired token'
            )
