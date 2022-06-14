from fastapi import FastAPI
import model
import routers
from database import engine
from routers import authentication,blog,user



model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(routers.blog)
app.include_router(routers.user)







