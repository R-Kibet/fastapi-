from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class hash():
    def encrypt(password:str):
        return pwd_context.hash(password)

    def verify(plain_password , hash_password):
        return pwd_context(plain_password,hash_password)