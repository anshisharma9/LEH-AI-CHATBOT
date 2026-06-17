from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.teacher import Teacher
from app.models.course import Course
from app.models.class_timing import ClassTiming
from app.models.notice import Notice
from app.models.faq import FAQ

from app.schemas.chat_schema import ChatRequest
from app.ai.gemini_service import ask_gemini


router = APIRouter()


# =====================================================
# LEH AI Identity
# =====================================================

AI_IDENTITY = """
You are LEH AI Assistant.

You are a professional digital career counselor of 
Learning Education Hub (LEH), Bhopal.

Rules:

1. Answer only what the student asks.

2. Do not give unnecessary information.

3. Give short, clear and professional answers.

4. After every answer provide relevant next options.

5. If LEH information is unavailable, suggest contacting
the counselor.

6. Never say you are Gemini AI.
"""


# =====================================================
# Standard Response Creator
# =====================================================

def create_response(answer, options=None):

    if options is None:
        options = []

    return {
        "success": True,
        "source": "LEH AI Assistant",
        "answer": answer,
        "options": options
    }


# =====================================================
# LEH Contact Support
# =====================================================

def contact_details():

    return create_response(
        """
LEH Contact Information

Phone Number:
+91 7470610859


For Career Counseling:
Rashmi Mishra (Counselor)


For Admission & Reception Support:
Deepali Mundawala (Reception)
""",

[
    "Admission Process",
    "Course Details",
    "Talk to Counselor"
]

    )


# =====================================================
# LEH Address (Only if Asked)
# =====================================================

def address_details():

    return create_response(
        """
Learning Education Hub (LEH)

Kalpataru Tower,
131/16 Opp. Mahendra Coaching,
Near Pragati Petrol Pump,
Zone-II MP Nagar,
Bhopal, Madhya Pradesh.
""",

[
    "Contact Number",
    "Courses",
    "Admission Process"
]

    )


# =====================================================
# Welcome Message
# =====================================================

def welcome_message():

    return create_response(
        """
Welcome to Learning Education Hub.

I am your LEH AI Career Assistant.

I can help you with:

- Courses
- Course Roadmaps
- Fees & Duration
- Trainers
- Batch Timings
- Admission
- Placement Guidance

Please choose a topic or ask your question.
""",

[
    "Courses",
    "Python Roadmap",
    "AI/ML Course",
    "Admission Process",
    "Contact Number"
]

    )


# =====================================================
# Counselor Support
# =====================================================

def counselor_support():

    return create_response(
        """
For personal guidance, please connect with our LEH team.

Career Counselor:
Rashmi Mishra

Reception Support:
Deepali Mundawala

Contact:
+91 7470610859
""",

[
    "Contact Number",
    "Admission Process"
]

    )
    # =====================================================
# Python Development Roadmap
# =====================================================

def python_roadmap():

    return create_response(
        """
Python Development Learning Path

Module 1: Python Fundamentals

- Introduction to Python
- Variables & Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- Strings
- Lists, Tuples & Dictionaries


Module 2: Advanced Python

- Object Oriented Programming
- Exception Handling
- File Handling
- Modules & Packages


Module 3: Database

- MySQL
- MongoDB
- SQL Concepts


Module 4: Practical Training

- Real Time Projects
- API Concepts
- Problem Solving
- Interview Preparation


Career Opportunities:

- Python Developer
- Backend Developer
- Automation Engineer
- Data Analyst (with additional skills)
""",

[
    "Python Fees",
    "Python Trainer",
    "Python Batch Timing",
    "Python Career"
]

    )


# =====================================================
# Java Development Roadmap
# =====================================================

def java_roadmap():

    return create_response(
        """
Java Development Learning Path


Core Java:

- Java Basics
- Variables
- Data Types
- Operators
- Conditions & Loops
- Arrays
- Strings
- Methods
- Object Oriented Programming


Advanced Java:

- Exception Handling
- Collections Framework
- File Handling
- Multithreading
- JDBC


Practical Training:

- Projects
- Coding Practice
- Interview Preparation


Career Opportunities:

- Java Developer
- Software Engineer
- Backend Developer
""",

[
    "Java Fees",
    "Java Trainer",
    "Java Batch Timing",
    "Java Career"
]

    )


# =====================================================
# Java Full Stack Development
# =====================================================

def java_fullstack_roadmap():

    return create_response(
        """
Java Full Stack Development


Frontend:

- HTML
- CSS
- JavaScript
- React.js


Backend:

- Core Java
- Advanced Java
- Spring Boot
- REST API Development


Database:

- MySQL
- MongoDB


Additional Skills:

- Git & GitHub
- Deployment Concepts


Practical Training:

- Full Stack Projects
- Interview Preparation


Career Opportunities:

- Full Stack Developer
- Software Engineer
- Java Developer
""",

[
    "Java Full Stack Fees",
    "Java Full Stack Trainer",
    "Java Full Stack Timing",
    "Career Opportunities"
]

    )


# =====================================================
# AI & Machine Learning Roadmap
# =====================================================

def ai_ml_roadmap():

    return create_response(
        """
Artificial Intelligence & Machine Learning


Foundation:

- Python Programming
- Mathematics
- Statistics


Data Handling:

- NumPy
- Pandas
- Data Cleaning
- Data Visualization


Machine Learning:

- Supervised Learning
- Unsupervised Learning
- Model Building
- Model Evaluation


Advanced AI:

- Deep Learning
- Neural Networks
- NLP
- Computer Vision


Practical Training:

- AI Projects
- Real World Case Studies


Career Opportunities:

- AI Engineer
- Machine Learning Engineer
- Data Scientist
""",

[
    "AI Fees",
    "AI Trainer",
    "AI Batch Timing",
    "AI Career"
]

    )


# =====================================================
# Data Analysis Roadmap
# =====================================================

def data_analysis_roadmap():

    return create_response(
        """
Data Analysis Learning Path


Data Preparation:

- Advanced Excel
- Data Cleaning
- Formulas & Functions


Visualization:

- Power BI
- Tableau
- Dashboard Creation


Programming:

- Python Basics
- NumPy
- Pandas


Database:

- SQL
- MySQL
- Data Querying


Statistics:

- Mean
- Median
- Probability
- Data Interpretation


Practical Training:

- Business Dashboards
- Real Time Projects


Career Opportunities:

- Data Analyst
- Business Analyst
- MIS Executive
""",

[
    "Data Analysis Fees",
    "Data Analysis Trainer",
    "Data Analysis Timing",
    "Data Analysis Career"
]

    )


# =====================================================
# C & C++ Programming
# =====================================================

def c_cpp_roadmap():

    return create_response(
        """
C & C++ Programming


C Programming:

- Variables
- Data Types
- Operators
- Conditions
- Loops
- Functions


C++ Programming:

- Classes & Objects
- Inheritance
- Polymorphism
- OOP Concepts


Advanced Concepts:

- Data Structures
- Algorithms
- Problem Solving


Career Opportunities:

- Software Developer
- System Programmer
- Game Developer
""",

[
    "C/C++ Fees",
    "C/C++ Trainer",
    "C/C++ Timing"
]

    )


# =====================================================
# MS Office & Advanced Excel
# =====================================================

def office_roadmap():

    return create_response(
        """
MS Office & Advanced Excel


MS Office:

- Microsoft Word
- Excel
- PowerPoint


Advanced Excel:

- Formulas
- Data Cleaning
- Reports
- Charts
- Dashboards


Business Tools:

- Power BI
- Tableau


Career Opportunities:

- Office Executive
- MIS Executive
- Data Analyst (Beginner)
""",

[
    "Office Fees",
    "Office Trainer",
    "Office Timing"
]

    )
    # =====================================================
# Career Guidance System
# =====================================================

def career_guidance(message):

    text = message.lower()


    # Software Development Career

    if (
        "software engineer" in text or
        "software developer" in text or
        "developer" in text
    ):

        return create_response(
        """
If your goal is to become a Software Developer, you can choose these learning paths:

1. Python Development
- Backend Development
- Automation
- API Development

2. Java Development
- Enterprise Applications
- Backend Systems

3. Java Full Stack Development
- Frontend + Backend + Database


Choose a path according to your interest and career goal.
""",

[
    "Python Roadmap",
    "Java Roadmap",
    "Java Full Stack",
    "Talk to Counselor"
]

        )


    # AI Career

    if (
        "ai engineer" in text or
        "machine learning engineer" in text or
        "artificial intelligence" in text
    ):

        return create_response(
        """
To become an AI Engineer, your learning journey should be:

Step 1:
Learn Python Programming

Step 2:
Learn Mathematics & Statistics

Step 3:
Learn Data Handling using NumPy and Pandas

Step 4:
Learn Machine Learning

Step 5:
Learn Deep Learning and AI Projects


After completing these skills, you can apply for AI related roles.
""",

[
    "AI/ML Roadmap",
    "AI Fees",
    "Placement Support",
    "Career Counseling"
]

        )


    # Data Analyst Career

    if (
        "data analyst" in text or
        "data analytics" in text or
        "business analyst" in text
    ):

        return create_response(
        """
For a Data Analyst career, you should learn:

- Advanced Excel
- Power BI
- Tableau
- SQL Database
- Python Basics
- Data Visualization
- Real Dashboard Projects


Career Opportunities:

- Data Analyst
- Business Analyst
- MIS Executive
""",

[
    "Data Analysis Roadmap",
    "Data Analysis Fees",
    "Placement Support",
    "Admission Process"
]

        )


    # Student confused

    if (
        "which course" in text or
        "what course" in text or
        "suggest course" in text or
        "confused" in text or
        "best course" in text
    ):

        return create_response(
        """
I can help you choose the right course.

Please tell me your career goal:

- Software Development
- Artificial Intelligence
- Data Analysis
- Web Development
- Office Skills

I will suggest the best learning path for you.
""",

[
    "Software Developer",
    "AI Engineer",
    "Data Analyst",
    "Talk to Counselor"
]

        )


    return None


# =====================================================
# Placement Support
# =====================================================

def placement_support():

    return create_response(
    """
LEH Career & Placement Support

Our placement preparation includes:

- Real Time Projects
- Practical Training
- Resume Building
- Mock Interviews
- Technical Interview Preparation
- Communication Skill Development


We guide students to become industry ready and support them in their career journey.
""",

[
    "Career Guidance",
    "Projects",
    "Talk to Counselor"
]

    )


# =====================================================
# Admission Process
# =====================================================

def admission_details():

    return create_response(
    """
LEH Admission Process

Step 1:
Choose a course based on your career goal.

Step 2:
Talk with our Career Counselor for guidance.

Career Counselor:
Rashmi Mishra

Step 3:
Complete your registration process with the reception team.

Reception Support:
Deepali Mundawala

Step 4:
Start your classes and begin your learning journey.
""",

[
    "Contact Number",
    "Courses",
    "Batch Timings"
]

    )


# =====================================================
# Career Counseling Direct Support
# =====================================================

def career_counseling():

    return create_response(
    """
For personal career guidance, please connect with:

Rashmi Mishra
Career Counselor

She will guide you regarding:

- Course Selection
- Career Planning
- Learning Path
- Admission Guidance
""",

[
    "Contact Number",
    "Admission Process"
]

    )
    # =====================================================
# Smart Course Search
# =====================================================

def get_course_details(db, course_name=None):

    if course_name:

        courses = (
            db.query(Course)
            .filter(
                Course.course_name.ilike(
                    f"%{course_name}%"
                )
            )
            .all()
        )

    else:
        courses = db.query(Course).all()


    if not courses:

        return create_response(
            """
Sorry, course information is currently unavailable.

Please contact our counselor for details.
            """,
            [
                "Contact Number"
            ]
        )


    answer = ""


    for course in courses:

        answer += f"""
Course:
{course.course_name}

Fees:
{course.fees}

Duration:
{course.duration}

Description:
{course.description}

-------------------------
"""


    return create_response(
        answer,
        [
            "Course Roadmap",
            "Batch Timing",
            "Admission Process"
        ]
    )


# =====================================================
# Course Wise Trainer Search
# =====================================================

def get_trainers(db, course_name=None):

    if course_name:

        trainers = (
            db.query(Teacher)
            .filter(
                Teacher.course.ilike(
                    f"%{course_name}%"
                )
            )
            .all()
        )

    else:

        trainers = db.query(Teacher).all()


    if not trainers:

        return create_response(
            """
Sorry, trainer information is not available for this course.
            """,
            [
                "Talk to Counselor"
            ]
        )


    answer = "LEH Trainer Details\n"


    for trainer in trainers:

        answer += f"""

Name:
{trainer.name}

Course:
{trainer.course}

Experience:
{trainer.experience}

------------------
"""


    return create_response(
        answer,
        [
            "Course Details",
            "Batch Timing",
            "Contact Number"
        ]
    )


# =====================================================
# Course Wise Batch Timing
# =====================================================

def get_timings(db, course_name=None):

    if course_name:

        timings = (
            db.query(ClassTiming)
            .filter(
                ClassTiming.course.ilike(
                    f"%{course_name}%"
                )
            )
            .all()
        )

    else:

        timings = db.query(ClassTiming).all()


    if not timings:

        return create_response(
            """
No batch timings are available currently.
            """,
            [
                "Contact Number"
            ]
        )


    answer = "Batch Timing Details\n"


    for timing in timings:

        answer += f"""

Course:
{timing.course}

Timing:
{timing.timing}

------------------
"""


    return create_response(
        answer,
        [
            "Admission Process",
            "Contact Number"
        ]
    )


# =====================================================
# Latest Notices
# =====================================================

def get_notices(db):

    notices = db.query(Notice).all()


    if not notices:

        return create_response(
            "Currently there are no latest updates.",
            [
                "Courses",
                "Contact Number"
            ]
        )


    answer = "Latest LEH Updates\n"


    for notice in notices:

        answer += f"""
- {notice.message}
"""


    return create_response(
        answer,
        [
            "Courses",
            "Admission Process"
        ]
    )


# =====================================================
# Smart FAQ Search
# =====================================================

def find_faq(message, db):

    text = message.lower()


    faqs = db.query(FAQ).all()


    for faq in faqs:

        question = faq.question.lower()


        if (
            question in text or
            text in question
        ):

            return create_response(
                faq.answer,
                [
                    "Courses",
                    "Contact Number"
                ]
            )


    return None


# =====================================================
# Detect Course Name From Message
# =====================================================

def detect_course(message):

    text = message.lower()


    courses = {

        "python": "python",

        "java full stack": "java full stack",

        "java": "java",

        "artificial intelligence": "ai",

        "ai": "ai",

        "machine learning": "ai",

        "data analysis": "data analysis",

        "data analyst": "data analysis",

        "excel": "excel",

        "power bi": "power bi",

        "tableau": "tableau",

        "c++": "c++",

        "c language": "c"

    }


    for key, value in courses.items():

        if key in text:

            return value


    return None
# =====================================================
# Final Smart Intent Detection
# =====================================================

def detect_intent(message, db):

    text = message.lower().strip()

    course = detect_course(text)


    # ===============================
    # Welcome
    # ===============================

    greetings = [
        "hi",
        "hello",
        "hey",
        "start"
    ]

    if text in greetings:
        return welcome_message()


    # ===============================
    # Contact Details Only
    # ===============================

    contact_words = [
        "contact",
        "phone",
        "mobile",
        "number",
        "call"
    ]

    if any(word in text for word in contact_words):
        return contact_details()


    # ===============================
    # Address Only
    # ===============================

    address_words = [
        "address",
        "location",
        "where is leh"
    ]

    if any(word in text for word in address_words):
        return address_details()


    # ===============================
    # Roadmaps / Syllabus
    # ===============================

    roadmap_words = [
        "roadmap",
        "syllabus",
        "topics",
        "what will i learn",
        "course content"
    ]

    if (
        course and
        any(word in text for word in roadmap_words)
    ):

        if course == "python":
            return python_roadmap()

        elif course == "java":
            return java_roadmap()

        elif course == "java full stack":
            return java_fullstack_roadmap()

        elif course == "ai":
            return ai_ml_roadmap()

        elif course == "data analysis":
            return data_analysis_roadmap()

        else:
            return office_roadmap()


    # ===============================
    # Course Fees / Duration
    # ===============================

    fee_words = [
        "fee",
        "fees",
        "price",
        "cost",
        "duration"
    ]

    if any(word in text for word in fee_words):

        return get_course_details(
            db,
            course
        )


    # ===============================
    # Trainers
    # ===============================

    trainer_words = [
        "teacher",
        "trainer",
        "faculty",
        "mentor",
        "who teaches"
    ]

    if any(word in text for word in trainer_words):

        return get_trainers(
            db,
            course
        )


    # ===============================
    # Batch Timing
    # ===============================

    timing_words = [
        "timing",
        "batch",
        "schedule",
        "class time"
    ]

    if any(word in text for word in timing_words):

        return get_timings(
            db,
            course
        )


    # ===============================
    # Course List
    # ===============================

    if (
        "course" in text or
        "courses" in text
    ):

        return get_course_details(db)


    # ===============================
    # Placement
    # ===============================

    placement_words = [
        "placement",
        "job",
        "internship",
        "interview"
    ]

    if any(word in text for word in placement_words):
        return placement_support()


    # ===============================
    # Admission
    # ===============================

    admission_words = [
        "admission",
        "join",
        "registration",
        "enroll"
    ]

    if any(word in text for word in admission_words):
        return admission_details()


    # ===============================
    # Career Guidance
    # ===============================

    career_answer = career_guidance(text)

    if career_answer:
        return career_answer


    # ===============================
    # Notices
    # ===============================

    if (
        "notice" in text or
        "update" in text or
        "announcement" in text
    ):

        return get_notices(db)


    # ===============================
    # FAQ Search
    # ===============================

    faq_answer = find_faq(text, db)

    if faq_answer:
        return faq_answer


    # No local answer
    return None


# =====================================================
# Final Chat API
# =====================================================

@router.post("/")
def chat(
    data: ChatRequest,
    db: Session = Depends(get_db)
):

    message = data.message.strip()


    # First LEH Database & Logic
    response = detect_intent(
        message,
        db
    )


    if response:
        return response


    # Gemini Fallback
    try:

        prompt = f"""
{AI_IDENTITY}


Student Question:
{message}


Rules:

- Answer like LEH Career Counselor.
- Keep answers simple.
- Do not give unnecessary information.
- If LEH-specific information is unknown,
  ask student to contact Rashmi Mishra
  or Deepali Mundawala.

Answer:
"""

        ai_answer = ask_gemini(prompt)


        if not ai_answer:

            return counselor_support()


        return create_response(
            ai_answer,
            [
                "Courses",
                "Admission Process",
                "Contact Number",
                "Career Guidance"
            ]
        )


    except Exception as error:

        print(
            "LEH AI Error:",
            error
        )

        return counselor_support()