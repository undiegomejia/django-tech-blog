# Django Tech Blog

A Django-powered blog application designed for technical content sharing. Built with Django 5.2.7 and Python 3.13, implementing class-based views, user authentication, and content management.

## Technical Overview

### Backend
- Django 5.2.7 with SQLite3 database
- Class-based views for content management
- Django authentication system
- Custom user profiles with image handling
- Automated image optimization for uploads

### Frontend
- Responsive HTML5/CSS3 design
- Clean UI with CSS custom properties
- Optimized template inheritance
- Static and media file handling

## Project Structure

```
djangoblog/
├── blog/              # Blog application
│   ├── models.py      # Post model and relationships
│   ├── views.py       # Class-based view controllers
│   └── templates/     # Blog templates
├── users/             # User management
│   ├── models.py      # Profile model
│   ├── forms.py       # Custom user forms
│   └── views.py       # Authentication views
├── media/             # User uploaded content
└── django_blog/       # Core configuration
    ├── settings.py    # Project settings
    └── urls.py        # URL routing
```

## Features and Implementation

### User System
- Custom user registration and authentication
- Profile management with image upload
- Automatic image resizing (300x300px max)
- Bio and personal information storage

### Content Management
- Class-based CRUD views for articles
- Rich text editing capabilities
- Archive system with date-based navigation
- Author attribution and timestamps

### Admin Interface
- Django admin customization
- User and content management
- Media file handling
- Site monitoring capabilities

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/undiegomejia/django-tech-blog.git
cd django-tech-blog
```

2. Set up Python environment (3.13 required):
```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Database setup:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000`

## Questions?

Open an issue on GitHub repository for support

---
Built with Django 5.2.7