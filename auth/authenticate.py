from fastapi import HTTPException, Request
from datetime import datetime, timedelta
from http import HTTPStatus
import jwt

# Temporary configuration (replace with a proper config later)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Authentication:
    @staticmethod
    def create_access_token(data: dict, expireDelta: timedelta | None = None) -> str:
        """
        Create a JWT access token.

        Args:
            data (dict): The data to encode in the token.
            expireDelta (timedelta | None): Optional expiration time delta.

        Returns:
            str: The encoded JWT token.
        """
        to_encode = data.copy()
        expire = datetime.now() + (expireDelta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def get_current_user(r: Request) -> dict:
        """
        Get the current user from the JWT token in the request cookies.

        Args:
            r (Request): The FastAPI request object.

        Returns:
            dict: The user data (e.g., username).

        Raises:
            HTTPException: If the token is missing, invalid, or expired.
        """
        token = r.cookies.get('accessToken')
        if not token:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='Not Authenticated'
            )

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get('sub')
            if not username:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED, detail='Invalid token'
                )
            return {'username': username}
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='Expired token'
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='Invalid token'
            )