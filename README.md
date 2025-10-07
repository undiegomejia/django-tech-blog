# Tech Blog - Django Web Application

A modern, feature-rich blog platform built with Django, focusing on technology, programming, and digital innovation content.

## Features

- 👥 User Authentication System
  - User registration and login
  - Profile management with avatars
  - Bio and personal information
- 📝 Blog Post Management
  - Create, edit, and delete posts
  - Rich text editing
  - Author attribution
- 📚 Content Organization
  - Chronological post listing
  - Archive view by year
  - User-specific post management
- 🎨 Modern UI/UX
  - Responsive design
  - Clean, modern interface
  - Custom styling with CSS variables
  - Avatar support for user profiles

## Technology Stack

- Python 3.13
- Django 5.2
- SQLite3 (Database)
- HTML5/CSS3
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/undiegomejia/tech-blog.git
cd tech-blog
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

## Project Structure

```
djangoblog/
├── blog/                   # Blog application
│   ├── static/            # Static files (CSS, JS)
│   ├── templates/         # HTML templates
│   ├── models.py          # Blog models
│   ├── views.py           # Blog views
│   └── urls.py            # Blog URL patterns
├── users/                 # User management application
│   ├── templates/         # User-related templates
│   ├── models.py          # User profile model
│   ├── forms.py          # User forms
│   └── views.py          # User views
├── media/                 # User-uploaded content
│   └── profile_pics/     # User avatars
└── django_blog/          # Project configuration
    ├── settings.py       # Project settings
    └── urls.py           # Main URL patterns
```

## Usage

### User Management

1. Register a new account at `/register/`
2. Login at `/login/`
3. Update your profile at `/profile/`
   - Add an avatar
   - Update bio and personal information
4. Logout at `/logout/`

### Blog Management

1. View all posts at `/blog/`
2. Create a new post at `/post/new/`
3. View post details at `/post/<id>/`
4. Edit your posts at `/post/<id>/edit/`
5. Delete posts at `/post/<id>/delete/`
6. View archived posts at `/archive/`

### Admin Interface

1. Access the admin interface at `/admin/`
2. Manage users, posts, and profiles
3. Monitor site activity

## Development

### Code Style
This project follows PEP 8 style guidelines. To check your code:
```bash
pip install flake8
flake8
```

## Deployment

1. Update settings.py for production:
```python
DEBUG = False
ALLOWED_HOSTS = ['tech-blog.com']
```

2. Configure your web server (e.g., Nginx, Apache)
3. Set up a production database (e.g., PostgreSQL)
4. Configure static files serving
5. Set up HTTPS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or feedback, please open an issue on GitHub.

---
Made with ❤️ using Django