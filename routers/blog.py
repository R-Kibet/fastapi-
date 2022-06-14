
from typing import List

from fastapi import APIRouter, Depends ,status ,HTTPException, Response
from sqlalchemy.orm import Session


from ..schema import this, showthis,User
from ..database import get_db
from .. import model
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/Blog",
    tags=["blog"]
)


# geting all the data in a d
@router.get("/", response_model=List[showthis])
def all(db: Session = Depends(get_db),get_user: User = Depends(get_current_user)):
    blogs = db.query(model.bg).all()
    return blogs


# post to a db
@router.post("/", status_code=status.HTTP_201_CREATED)
def index(req: this, db: Session = Depends(get_db)):
    new = model.bg(**req.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


# getting a particular data
@router.get("/{id}", response_model=showthis)
def one(id,  db: Session = Depends(get_db)):
    blogs = db.query(model.bg).filter(model.bg.id == id).first()
    if not blogs:
        # USE EXCEPTIONS
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        #  return {"detail": f"blog with {id} not found"}
    return blogs


# delete blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(id, db: Session = Depends(get_db)):
    blog = db.query(model.bg).filter(model.bg.id == id).delete(synchronize_session=False)

    if not blog:
        # USE EXCEPTIONS
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    # always commit on a db
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
