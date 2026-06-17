from fastapi import FastAPI

from app.database.db import engine
from app.database.base import Base

from app.models.teacher import Teacher
from app.models.course import Course
from app.models.class_timing import ClassTiming
from app.models.notice import Notice
from app.models.faq import FAQ
from app.models.user import User
from app.routes.auth import router as auth_router
from app.routes.teacher import router as teacher_router
from app.routes.course import router as course_router
from app.routes.class_timing import router as timing_router
from app.routes.notice import router as notice_router
from app.routes.faq import router as faq_router
from app.models.knowledge import Knowledge
from fastapi.middleware.cors import CORSMiddleware
from app.routes.knowledge import (
    router as knowledge_router
)
from app.routes.chat import (
    router as chat_router
)


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(
    teacher_router,
    prefix="/teachers",
    tags=["Teachers"]
)
app.include_router(
    course_router,
    prefix="/courses",
    tags=["Courses"]
)
app.include_router(
    timing_router,
    prefix="/timings",
    tags=["Timings"]
)
app.include_router(
    notice_router,
    prefix="/notices",
    tags=["Notices"]
)
app.include_router(
    faq_router,
    prefix="/faq",
    tags=["FAQ"]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    knowledge_router,
    prefix="/knowledge",
    tags=["Knowledge"]
)
app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

@app.get("/")
def home():
    return {"message": "LEH AI Chatbot Running"}

