from . import app
from .routers import posts, users ,auth



app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def index():
    return {"message": "Hello World"}

