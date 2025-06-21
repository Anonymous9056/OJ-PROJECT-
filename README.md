# Online Judge System

A modern Django-based online programming judge system where users can solve coding problems, participate in contests, and track their progress.

## Features

- **User Authentication**: Secure login and registration system
- **Problem Management**: Create and manage coding problems with different difficulty levels
- **Code Submission**: Submit solutions in multiple programming languages
- **Contest System**: Participate in timed programming contests
- **User Profiles**: Track ratings, solved problems, and achievements
- **Admin Interface**: Comprehensive admin panel for managing all aspects of the system
- **Modern UI**: Beautiful, responsive design using Bootstrap 5

## Tech Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Icons**: Font Awesome 6

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd onlinejudge
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
onlinejudge/
├── base/                   # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL patterns
│   └── admin.py           # Admin interface
├── onlinejudge/           # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── templates/             # HTML templates
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── base/
│       └── home.html      # Home dashboard
├── media/                 # User uploaded files
├── manage.py              # Django management script
└── README.md              # This file
```

## Database Models

### User
- Custom user model extending Django's AbstractUser
- Additional fields: bio, profile picture, rating, date of birth
- Tracks solved problems and submissions

### Problem
- Coding problems with title, description, difficulty
- Time and memory limits
- Test cases stored as JSON
- Input/output format specifications

### Submission
- Code submissions with language, status, execution time
- Links to user and problem
- Tracks submission history

### Contest
- Programming contests with start/end times
- Multiple problems per contest
- Participant tracking and scoring

## Usage

1. **Registration**: Create a new account at `/register/`
2. **Login**: Sign in at `/login/`
3. **Dashboard**: View your stats and recent activity
4. **Problems**: Browse and solve coding problems
5. **Contests**: Participate in programming contests
6. **Profile**: Manage your account settings

## Admin Features

The admin interface provides:
- User management with custom fields
- Problem creation and editing
- Submission monitoring and judging
- Contest management
- Statistics and analytics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- Real-time code execution and judging
- Support for more programming languages
- Advanced contest features (team contests, elimination rounds)
- Code plagiarism detection
- API endpoints for external integrations
- Mobile app support 