# Import FastAPI
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from h11 import Request
from routers import posts, users, auth, votes
from settings.config import settings as set
from fastapi.middleware.cors import CORSMiddleware
# Create app instance
app = FastAPI()

origins = ["*"]

app.add_middleware(
                    CORSMiddleware,
                    allow_origins = origins,
                    allow_credentials = True,
                    allow_methods = ['*'],
                    allow_headers = ['*']
                    )

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content = {"error": exc.detail, "status_code": exc.status_code})

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error":"Internal Server Error", "details":str(exc)})

app.include_router(posts.router)

app.include_router(users.router)

app.include_router(auth.router)

app.include_router(votes.router)
