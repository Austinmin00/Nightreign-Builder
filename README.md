# Nightreign Builder

A Flask web application that replicates Elden Ring: Nightreign's "Chalice" and "Relic" build system. Players can create and customize character loadouts without launching the game, accessing a complete database of characters, stats, chalices, and relic effects.

**Video Demo:** https://youtu.be/bNMc__FY-BI

---

## Features

- **10 Playable Characters** with complete stat blocks
- **Character Workshop** with 6-slot relic builder and 33 chalices
- **189+ Relic Effects** database with detailed descriptions
- **User Authentication** with secure password validation and session management
- **Responsive UI** with Bootstrap and dynamic modal editors
- **RESTful API** for chalice slots, relic effects, and build saving

---

## Quick Start

### Prerequisites
- Python 3.10+
- Docker Desktop
- Git

### Installation

1. **Clone and setup:**
```bash
git clone <your-repository-url>
cd Projects2
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

2. **Configure environment variables:**
Create `.env` file in project root:
```env
DB_USER=Mina_Nightreign
DB_PASS=your_secure_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nightreignStats
DATABASE_URL=postgresql://Mina_Nightreign:your_secure_password@localhost:5432/nightreignStats
SECRET_KEY=your-random-secret-key
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=your_pgadmin_password
```

3. **Start services:**
```bash
cd postgres-docker
docker compose up -d
cd ..
python seed_characters.py
python app.py
```

Access at **http://localhost:5000**

---

## Usage

**Homepage** - Select from 10 characters to enter the Workshop

**Workshop** - Choose chalices, build 6-slot relic loadouts, and save configurations

**Relic Database** - Browse all effects, filter by category, view stackability

**Authentication** - Register (12+ char passwords required) or browse as Guest

---

## Technology Stack

**Backend:** Flask, SQLAlchemy, PostgreSQL, Pydantic  
**Frontend:** Bootstrap 5, JavaScript, Jinja2  
**Security:** Flask-WTF (CSRF), Flask-Limiter, Werkzeug (password hashing)  
**Infrastructure:** Docker, python-dotenv

---

## Project Structure

```
app.py              # Flask routes, authentication, API endpoints
models.py           # 8 SQLAlchemy models (User, Character, Chalice, etc.)
db.py               # Database configuration
seed_characters.py  # Populates database with game data
templates/          # HTML templates (workshop, login, register, etc.)
static/             # CSS, images (characters, chalices, relics)
postgres-docker/    # Docker Compose, CSV data files
```

**Key Components:**
- **app.py (314 lines)** - User auth with rate limiting, CSRF protection, API endpoints
- **models.py (109 lines)** - 8 database tables including User, Character, Chalice, Relic
- **workshop.html (1006 lines)** - Complex build editor with modal, API integration
- **seed_characters.py (1057 lines)** - Imports 10 characters, 33 chalices, 189+ relics

---

## Security

**Protected Files (.gitignore):**  
`.env`, `venv/`, `__pycache__/`, `flask_session/`, `pgdata/`

**Features:**
- Password requirements (12+ chars, uppercase, digits, special chars)
- Rate limiting (10 login attempts/hour)
- CSRF protection on all forms
- Scrypt password hashing with 16-byte salt
- Session fixation prevention

---

## Credits

**Data Sources:**  
slayworldkiller, unlinedbetters, emerald_wolf504 (Discord)

**Game:**  
Elden Ring: Nightreign © FromSoftware/Bandai Namco Entertainment

This is a fan project for educational purposes. All game content belongs to their respective owners. 