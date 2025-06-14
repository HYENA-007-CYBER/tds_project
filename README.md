# 🧠 TDS Virtual TA – API for Tools in Data Science Course

This project is a basic FastAPI application that acts as a **Virtual Teaching Assistant** for the Tools in Data Science (TDS) course of the **IIT Madras Online BSc Program**.

It accepts student questions via a POST API and returns relevant answers and Discourse links from a predefined database (`fake_db.json`).

---

## ✅ Features

- Built using **FastAPI**
- Accepts student questions in JSON format
- Matches known questions and returns:
  - An `answer`
  - Related `links` from Discourse
- Responds within 30 seconds
- Ready to deploy on Replit or locally

---

## 📦 Requirements

- Python 3.8+
- `fastapi`
- `uvicorn`

Install dependencies:

```bash
pip install -r requirements.txt
