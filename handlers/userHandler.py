from db.database import Session
from schemas.userSchema import User
from utils.encriptation import get_password_hash

def createUser(name: str, passwd: str, email: str):

    session = Session()
    hashedPasswd = get_password_hash(passwd)

    try:
        newUser = User(
            name=name,
            passwd=hashedPasswd,
            email=email
        )
        
        session.add(newUser)
        session.commit()
    except Exception as e:
        session.rollback
    finally:
        session.close()

