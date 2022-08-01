from . import app
from .routers import posts, users ,auth, votes



app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def index():
    return {"message": "Hello World"}

