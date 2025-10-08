# Django Tech Blog

A blog website for sharing tech articles.

## Project Layout

```
djangoblog/
├── blog/          # Blog features
├── users/         # User accounts
├── media/         # Uploaded files
└── django_blog/   # Settings
```

## How to Use

### Users Can
- Create accounts
- Add profile pictures
- Write and edit articles
- View other users' posts

### Admins Can
- Manage all content
- Handle user accounts
- Monitor site activity

## Setup

1. Clone the repository:
```bash
git clone https://github.com/undiegomejia/django-tech-blog.git
cd django-tech-blog
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Create environment variables file (.env):
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

6. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Questions?

Open an issue on GitHub

---
Made with Django