from . import app
from .routers import posts, users


app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
def index():
    return {"message": "Hello World"}

