from pwdlib import PasswordHash

ctx = PasswordHash.recommended() 

def get_password_hash(password: str):
    return ctx.hash(password) 

def verify_password(plain_password: str, hashed_password: str):
    return ctx.verify(plain_password, hashed_password)