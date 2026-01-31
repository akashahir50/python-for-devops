#  FastAPI 

## 🎯 STAR Method

**SITUATION**: 

-> Traditional log analysis was manual and time-consuming, with logs growing daily across DevOps pipelines.

-> No easy way to query errors or metrics remotely, leading to delays in troubleshooting.

---
**TASK**:

Build an automated solution to parse logs and expose error analysis via a web API.
Enable quick, remote access to log insights for DevOps teams without CLI dependency.

---
**ACTION**: 

• Created a FastAPI app to handle log uploads and parsing.

• Implemented endpoints.

• Structured with main.py (app/routes), and requirements.txt for easy setup.

• Started the server with Uvicorn.

• Created FastAPI with log analyzer (/logs), health checks (/health), AWS summary (/aws)  

---
**RESULT**: 
• Manual log hunts dropped from hours to seconds. Now anyone can hit the API, upload a log file, and get a neat breakdown of errors by level.
•  80% time saved, instant JSON insights via browser/curl/Postman  

## Quick Start
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
