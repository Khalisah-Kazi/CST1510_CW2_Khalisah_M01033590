# Multi-Domain Intelligence Platform

A secure, multi-page analytics dashboard built with Streamlit, integrating AI-powered insights via the OpenAI API. Designed to support three domains — Cybersecurity, Data Science, and IT Operations — with role-based access control and a structured OOP architecture.

> **Status:** Completed as a university assignment (CST1510, Middlesex University Dubai). Achieved a grade of 68 (2:1).

---

## Features

- **Secure Authentication** — User registration and login with bcrypt password hashing, duplicate username prevention, and session state management
- **Multi-Domain Analytics** — Separate dashboard pages for Cybersecurity (incident tracking), Data Science (dataset analysis), and IT Operations (ticket management)
- **AI Assistant** — OpenAI GPT-4o integration with domain-specific system prompts and streaming responses
- **OOP Architecture** — Refactored from procedural to class-based design using entity models and service layers
- **SQLite Backend** — Persistent data storage via a `DatabaseManager` service class handling all queries

---

## Tech Stack

| Layer | Tools |
|---|---|
| Frontend | Streamlit, st.session_state, st.switch_page |
| Backend | Python, SQLite, OOP (models + services) |
| AI | OpenAI API (GPT-4o), streaming |
| Security | bcrypt, .streamlit/secrets.toml, .gitignore |
| Data | Pandas, NumPy |

---

## Project Structure

```
CST1510_CW2/
├── my_app/
│   ├── Home.py               # Login / Register entry point
│   └── 1_dashboard.py        # Dashboard page (authenticated users only)
├── app/
│   ├── data/                 # Dataset files
│   └── services/
│       ├── __init__.py
│       └── user_services.py  # Authentication and user management logic
├── models/                   # Entity classes (User, SecurityIncident, etc.)
├── DATA/                     # Raw data assets
├── demo code/                # Lab demo scripts
├── docs/                     # Documentation
├── main.py                   # App entry point
├── intelligence_platform.db  # SQLite database
├── requirements.txt
└── .gitignore
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
Create `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "sk-proj-your-key-here"
```

### 4. Run the app
```bash
streamlit run Home.py
```

---

## Architecture Overview

The project follows a layered OOP design:

- **Models** (`models/`) — Entity classes representing core domain objects (`User`, `SecurityIncident`, `Dataset`, `ITTicket`), each with private attributes, constructors, and `__str__` methods
- **Services** (`services/`) — Service classes that coordinate operations: `DatabaseManager` handles all SQLite interactions, `AuthManager` manages authentication using bcrypt, and `AIAssistant` wraps OpenAI API calls
- **Pages** (`pages/`) — Streamlit pages that consume the service and model layers, keeping UI logic separate from business logic

---

## Security

- Passwords are hashed using **bcrypt** with automatic salt generation — plaintext passwords are never stored
- API keys are stored in `.streamlit/secrets.toml` and excluded from version control via `.gitignore`
- Pages are protected by a session state login guard; unauthenticated users are redirected to the login page

---

## Requirements

```
streamlit
openai
bcrypt
pandas
numpy
```

---

## Author

**Khalisah Kazi**  
BSc Information Technology, Middlesex University Dubai  
[LinkedIn](www.linkedin.com/in/khalisah-kazi-93b933325) · [GitHub]([https://github.com/](https://github.com/kazi15khalisah))
