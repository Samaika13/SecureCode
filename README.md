# 🛡️ SecureCode

A modern AI-assisted static code analysis platform that scans GitHub repositories for common security vulnerabilities and presents the results through an interactive security dashboard.

![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

SecureCode analyzes public GitHub repositories using custom-built static analysis scanners to identify potential security vulnerabilities.

Instead of simply listing findings, SecureCode provides:

- Security severity summaries
- Risk scoring
- Interactive charts
- Search and filtering
- Expandable vulnerability explanations
- Downloadable JSON reports

The goal is to make security analysis simple, visual, and developer-friendly.

---

# Live Demo

https://securecode-tau.vercel.app/

---

## ✨ Features

- 🔍 Scan any public GitHub repository
- 🔐 Detect hardcoded secrets
- 💉 Detect SQL injection patterns using Python AST analysis
- 🔑 Detect weak cryptographic algorithms
- 📊 Interactive dashboard
- 📈 Severity distribution chart
- 📉 Scanner distribution chart
- 🎯 Risk Score calculation
- 🔎 Search findings instantly
- 🚦 Filter by severity
- 🔀 Sort findings
- 📂 Expandable finding cards
- 📄 Download JSON security reports
- ⚡ Loading overlay while scanning
- 🌙 Modern dark UI

---

## 🏗️ Tech Stack

### Frontend

- React
- Vite
- Axios
- Recharts
- CSS

### Backend

- FastAPI
- Python
- GitPython
- AST (Abstract Syntax Tree)
- Pydantic

---

## 🔍 Security Scanners

### Hardcoded Secret Scanner

Detects:

- API Keys
- Passwords
- Tokens
- Secrets

Severity:
HIGH

---

### Python AST SQL Scanner

Uses Python's Abstract Syntax Tree (AST) to detect SQL queries built using string concatenation.

Example:

```python
query = "SELECT * FROM users WHERE id=" + user_input
cursor.execute(query)
```

Severity:
HIGH

---

### Weak Cryptography Scanner

Detects insecure cryptographic algorithms including:

- MD5
- SHA1
- DES
- RC4

Severity:
MEDIUM

---

## 📊 Dashboard

The dashboard includes:

- Total Findings
- Repository Name
- Risk Score
- Severity Breakdown
- Severity Pie Chart
- Scanner Distribution Chart
- Search
- Filters
- Sorting
- Expandable Findings
- JSON Report Download

---

## 🚀 Project Structure

```
SecureCode/
│
├── backend/
│   ├── app/
│   │   ├── scanners/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone

```bash
git clone https://github.com/Samaika13/SecureCode

cd SecureCode
```

### Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📸 Screenshots

### Home

![Home](assets/home.png)

---

### Dashboard

_Add screenshot here_

---

### Expanded Finding

_Add screenshot here_

---

## 🎯 Future Improvements

- Additional security scanners
- Multi-language support
- Authentication
- Repository history
- PDF reports
- GitHub App integration
- CI/CD integration

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Samaika Kanwar**

Computer Science Student

Purdue University

GitHub: https://github.com/Samaika13

LinkedIn: https://www.linkedin.com/in/samaikakanwar/