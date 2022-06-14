from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..schema import Login
from ..database import get_db
from .. import model,token
from ..hash import hash

router = APIRouter(
    tags=["Auth"]
)


@router.post("/login")
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == req.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credential")

    if hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credential")

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
