from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..schema import User, ShowUser
from ..database import get_db
from .. import model
from ..hash import hash

router = APIRouter(
    prefix= "/User",
    tags=["user"]
)


# create user
@router.post("/", response_model=ShowUser)
def create_user(req: User, db: Session = Depends(get_db)):
    nu = model.User(name=req.name, email=req.email, Tel=req.Tel, password=hash.encrypt(req.password))
    db.add(nu)
    db.commit()
    db.refresh(nu)
    return nu


# update blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED )
def update(id, request: User, db: Session = Depends(get_db)):
    blog = db.query(model.User).filter(model.User.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")
    blog.update(request.dict())
    db.commit()
    return "updated"


# get users with id
@router.get("/{id}", response_model=ShowUser)
def getuser(id: int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with {id} not found")

    return user
