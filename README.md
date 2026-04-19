# Validation + Workflow Engine API

A backend workflow evaluation system built using FastAPI that validates event submissions, calculates delay, applies rule-based decisions, and generates workflow outcomes (PASS / REVIEW / BLOCK) along with scoring.

This project demonstrates a clean backend architecture with separated validation, scoring, and workflow logic.

---

# Project Overview

This API evaluates event submissions using a rule-based workflow engine.

The system performs:

* Input validation
* Delay calculation
* Business rule evaluation
* Workflow decision generation
* Score calculation
* Structured API response

---

# Tech Stack

* FastAPI
* Python
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* Uvicorn
* python-dotenv

---

# Project Structure

```
REPORTING-SYSTEMS/
│
├── alembic/
├── config/
├── models/
│   ├── base.py
│   └── evaluation_record.py
│
├── router/
│   └── evaluation_api.py
│
├── schemas/
│   └── evaluation_record.py
│
├── service/
│   ├── validation_service.py
│   ├── scoring_service.py
│   └── evaluation_service.py
│
├── testcase_screenshots/
│   ├── testcase1.png
│   ├── testcase2.png
│   ├── testcase3.png
│   └── testcase4.png
│
├── venv/
├── .env
├── .gitignore
├── alembic.ini
├── main.py
├── requirements.txt
└── README.md
```

---

# Environment Setup

## 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd REPORTING-SYSTEMS
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-dotenv pydantic
```

---

# Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://username:password@host:port/database
```

---

# Database Connection Setup

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

---

# Alembic Database Migration Setup

## Initialize Alembic

```bash
alembic init alembic
```

## Configure alembic.ini

```
sqlalchemy.url = postgresql://username:password@host/database
```

## Update alembic/env.py

```python
from models.base import Base
target_metadata = Base.metadata
```

## Create Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

## Apply Migration

```bash
alembic upgrade head
```

---

# Running the Application

```bash
uvicorn main:app --reload
```

Server:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs

---

# Workflow Logic

```
delay_days = submission_date - event_date
```

## Workflow Decision Rules

| Delay Days | Reason Provided | Final Status |
| ---------- | --------------- | ------------ |
| ≤ 2        | Yes / No        | PASS         |
| > 2        | Yes             | REVIEW       |
| > 2        | No              | BLOCK        |

---

# Scoring Logic

| Status | Score |
| ------ | ----- |
| PASS   | 100   |
| REVIEW | 60    |
| BLOCK  | 0     |

---

# API Endpoint

## POST /evaluate-record

### Request

```json
{
  "event_date": "2026-04-17",
  "delay_reason": "Server downtime"
}
```

### Response

```json
{
  "submission_date": "2026-04-19",
  "final_status": "PASS",
  "delay_days": 2,
  "reason_flag": "Yes",
  "score": 100
}
```

---

# Validation Rules

* Missing event date
* Invalid date format
* Future event dates
* Submission before event date
* Delay without reason
---

# Test Cases

## Test Case 1 — Valid Submission

**Description:** Event submitted on time or within allowed delay.

**Request**

```json
{
  "event_date": "2026-04-17",
  "delay_reason": "Server downtime"
}
```

**Expected Result:** PASS

![Test Case 1](./testcase_screenshots/testcase1.png)

---

## Test Case 2 — 2 Day Delay

**Description:** Event submitted within the allowed delay period.

**Request**

```json
{
  "event_date": "2026-04-17",
  "delay_reason": "Minor operational delay"
}
```

**Expected Result:** PASS

![Test Case 2](./testcase_screenshots/testcase2.png)

---

## Test Case 3 — Delay Greater Than 2 Days With Reason

**Description:** Submission is delayed but a reason is provided.

**Request**

```json
{
  "event_date": "2026-04-14",
  "delay_reason": "Server maintenance issue"
}
```

**Expected Result:** REVIEW

![Test Case 3](./testcase_screenshots/testcase3.png)

---

## Test Case 4 — Delay Greater Than 2 Days Without Reason

**Description:** Submission delayed and no reason provided.

**Request**

```json
{
  "event_date": "2026-04-14",
  "delay_reason": ""
}
```

**Expected Result:** BLOCK

![Test Case 4](./testcase_screenshots/testcase4.png)

---

## Test Case 5 — Missing Event Date

**Description:** Required field `event_date` is missing.

**Request**

```json
{
  "delay_reason": "Testing validation"
}
```

**Expected Result:** Validation Error

![Test Case 5](./testcase_screenshots/testcase5.png)

---

## Test Case 6 — Invalid Date Format

**Description:** Event date provided in incorrect format.

**Request**

```json
{
  "event_date": "19-04-2026",
  "delay_reason": "Invalid format test"
}
```

**Expected Result:** Validation Error

![Test Case 6](./testcase_screenshots/testcase6.png)

---

## Test Case 7 — Future Event Date

**Description:** Event date cannot be in the future.

**Request**

```json
{
  "event_date": "2030-01-01",
  "delay_reason": "Future date test"
}
```

**Expected Result:** Validation Error

![Test Case 7](./testcase_screenshots/testcase7.png)

---

## Test Case 8 — Submission Before Event Date

**Description:** Submission cannot happen before event date.

**Request**

```json
{
  "event_date": "2026-04-25",
  "delay_reason": "Invalid submission test"
}
```

**Expected Result:** Validation Error

![Test Case 8](./testcase_screenshots/testcase8.png)

---


# Architecture Overview

```
Client Request
      ↓
FastAPI Router
      ↓
Evaluation Service
      ↓
Validation Service
      ↓
Scoring Service
      ↓
Database Model
      ↓
API Response
```

---

# Key Features

* Clean architecture
* Validation layer separation
* Workflow engine implementation
* Rule-based decision system
* Scoring logic abstraction
* PostgreSQL integration
* Alembic migrations
* Swagger API documentation

---

# Author

Madhumitha
Backend Developer
FastAPI | Python | PostgreSQL | API Development

---

✅ Steps:

1. Copy everything
2. Paste into README.md
3. Commit & push
4. Done — images will render automatically
