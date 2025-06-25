# Job Posting Database Management System

[![Django](https://img.shields.io/badge/Django-5.0.1-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)

**DSCI551 | Group 48: David Tovmasyan, Jinyang Du, Wenjing Huang**

A comprehensive Django-based Database Management System for job postings that enhances the job search and recruitment process by providing a user-friendly, efficient, and interactive job posting platform with distributed database architecture.

**[Implementation Demo](https://www.youtube.com/watch?v=qOf86i9TUbQ)**

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a distributed job posting management system using Django with MySQL database partitioning. The system features:

- **Distributed Database Architecture**: Uses hash-based partitioning across 3 MySQL databases
- **Web Scraping**: Automated LinkedIn job data collection using Selenium and BeautifulSoup
- **User Authentication**: Complete user registration, login, and profile management
- **Job Management**: CRUD operations for job postings with advanced search capabilities
- **Responsive UI**: Modern Bootstrap-based interface with interactive features

## ✨ Features

- 🔍 **Advanced Job Search**: Search by title, location, company, and filters
- 📊 **Database Partitioning**: Hash-based distribution across multiple databases
- 🤖 **Automated Data Collection**: LinkedIn scraping with Selenium WebDriver
- 👤 **User Management**: Registration, authentication, and profile management
- 💾 **Data Import/Export**: CSV-based data management with custom commands
- 📱 **Responsive Design**: Mobile-friendly Bootstrap interface
- ⭐ **Favorites System**: Save and manage favorite job postings
- 🗓️ **Date Range Operations**: Bulk delete jobs within specified time periods

## 🏗️ Architecture

The system uses a distributed database architecture with:

- **Primary Database**: SQLite for user management and session data
- **Partitioned Databases**: 3 MySQL databases for job data distribution
- **Hash Function**: Custom partitioning algorithm based on job location state codes
- **Django ORM**: Database-agnostic data access layer

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jinyangd/DSCI551_Group48_Project.git
cd DSCI551_Group48_Project
```

### 2. Install Dependencies

```bash
pip install django
pip install mysqlclient
pip install crispy-forms
pip install crispy-bootstrap4
pip install selenium
pip install beautifulsoup4
pip install requests
```

### 3. Database Setup

Create three MySQL databases for job data partitioning:

```sql
CREATE DATABASE db_one;
CREATE DATABASE db_two;
CREATE DATABASE db_three;
```

### 4. Configure Database Settings

Edit `django_project/django_project/settings.py` and update the database configurations:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jobs'
    },
    'first': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_one',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'second': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_two',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'third': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_three',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --database=first
python manage.py migrate --database=second
python manage.py migrate --database=third
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root (optional):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Static Files

Collect static files for production:

```bash
python manage.py collectstatic
```

## 📖 Usage

### 1. Data Collection

#### Option A: Use Pre-processed Data
Download the [example.csv](https://drive.google.com/file/d/1RLI85-oi-JQM9OdJEVLjCz-DFzeScRY5/view?usp=sharing) file with pre-processed job data.

#### Option B: Scrape Fresh Data from LinkedIn

```bash
python linkedin_scrape.py
```

**Note**: Scraping may take 2+ hours depending on the number of jobs and network conditions.

### 2. Import Job Data

```bash
python manage.py import_jobs "path/to/your/jobs.csv"
```

### 3. Start Development Server

```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

### 4. Additional Commands

#### Delete Jobs by Date Range

```bash
python manage.py remove_jobs "all" "2024-01-01" "2024-12-31"
```

#### Create Superuser

```bash
python manage.py createsuperuser
```

## 📁 Project Structure

```
dsci551_group48/
├── django_project/          # Main Django project
│   ├── django_project/      # Project settings and configuration
│   ├── blog/               # Job posting application
│   │   ├── management/     # Custom Django commands
│   │   ├── templates/      # HTML templates
│   │   ├── static/         # CSS, JS, and static files
│   │   └── models.py       # Job model and database logic
│   ├── users/              # User authentication app
│   └── manage.py           # Django management script
├── linkedin_scrape.py      # LinkedIn data scraper
├── jobs                    # SQLite database file
└── media/                  # User-uploaded files
```

### Key Files

- **[Hash Function Implementation](django_project/blog/management/commands/import_jobs.py)**: Database partitioning logic
- **[LinkedIn Scraper](linkedin_scrape.py)**: Automated data collection using Selenium
- **[Job Model](django_project/blog/models.py)**: Database schema and business logic
- **[Django Settings](django_project/django_project/settings.py)**: Project configuration

## 🔌 API Endpoints

### Job Management
- `GET /` - Home page with job listings
- `GET /job/<int:pk>/` - Job detail view
- `GET /job/new/` - Create new job posting
- `POST /job/<int:pk>/update/` - Update job posting
- `POST /job/<int:pk>/delete/` - Delete job posting

### User Management
- `GET /register/` - User registration
- `GET /login/` - User login
- `GET /profile/` - User profile
- `GET /logout/` - User logout

### Search and Filtering
- `GET /search/` - Job search interface
- `GET /favorites/` - User's favorite jobs
- `GET /user/<str:username>/` - User's job postings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the DSCI551 course at USC. All rights reserved.

## 👥 Team

- **David Tovmasyan** - Backend Development & Database Architecture
- **Jinyang Du** - Frontend Development & UI/UX Design
- **Wenjing Huang** - Data Scraping & System Integration

## 📞 Support

For questions or support, please contact the development team or create an issue in the repository.

---

**Built with ❤️ for DSCI551 Database Systems**
