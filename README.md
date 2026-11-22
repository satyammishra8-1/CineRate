# 🎬 CineRate
### Discover. Rate. Review. Share.

**A Full-Stack Movie Discovery & Review Platform**

CineRate is a responsive web application built with **Python, Django, and PostgreSQL**, designed to bring movie discovery and community-driven reviews together in one platform.

Users can explore movies, discover ratings, share their opinions, and manage their reviews through an intuitive interface optimized for both desktop and mobile devices.

🌐 **Live Application:** [CineRate](https://cinerate-ojlp.onrender.com)

---

## 🚀 Project Overview

CineRate was developed as a practical implementation of full-stack web development concepts during an intensive Python Full-Stack Development training program.

The project evolved beyond basic Django development into a deployed application, incorporating relational database management, cloud-based image storage, responsive frontend development, and an automated CI/CD pipeline.

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 Movie Discovery | Explore movies with posters, descriptions, genres, and release dates. |
| ⭐ Rating System | View average ratings and submit personal ratings. |
| 💬 Community Reviews | Write and read movie reviews. |
| 🔐 Authentication | User registration, login, and logout. |
| ✏️ Review Management | Edit and delete your own reviews. |
| 🛠️ Movie Management | Staff-authorized movie uploads. |
| 🔎 Search & Filters | Search movies and filter by genre or rating. |
| 📱 Responsive UI | Dedicated mobile and desktop layouts. |
| 🌗 Theme Switching | Dark and light mode support. |
| 🔗 Movie Sharing | Share movie pages using native sharing or clipboard functionality. |
| ☁️ Cloud Storage | Cloudinary integration for movie poster images. |

## 🖥️ Technology Stack

**Backend**
- Python
- Django
- Django ORM

**Frontend**
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

**Database & Storage**
- PostgreSQL
- SQLite (local development)
- Cloudinary

**DevOps & Deployment**
- GitHub Actions
- CI/CD
- Render
- Gunicorn
- WhiteNoise

## 🏗️ Application Architecture

```text
                 USERS
                   |
                   v
        Responsive Web Interface
         HTML | CSS | Bootstrap
                   |
                   v
             Django Backend
          ---------------------
          | Authentication    |
          | Movie Management  |
          | Review Management |
          | Rating Logic      |
          ---------------------
             |           |
             v           v
        PostgreSQL    Cloudinary
        Database      Image Storage

                   |
                   v
             Render Hosting
```

## ⚙️ CI/CD Pipeline

CineRate uses GitHub Actions to automate important development and deployment checks.

**Workflow:**

1. Developer pushes code to GitHub.
2. GitHub Actions initializes the Python environment.
3. Project dependencies are installed.
4. Database migration checks are performed.
5. Django system checks are executed.
6. Static files are collected.
7. Automated tests are executed.
8. Successful pushes to the `main` branch trigger Render deployment through a deployment hook.

This workflow helps validate changes before deployment and reduces repetitive manual deployment steps.

## 📸 Application Preview

Screenshots of the desktop and mobile interfaces will be showcased here.

## 💻 Run Locally

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CineRate
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Configure the database and Cloudinary credentials required by your environment.

Do not commit secret credentials to GitHub.

**5. Apply database migrations**

```bash
python manage.py migrate
```

**6. Start the development server**

```bash
python manage.py runserver
```

Open:

`http://127.0.0.1:8000/`

## 🧪 Testing

Run the Django test suite:

```bash
python manage.py test
```

## 📚 Key Learning Outcomes

Through CineRate, I gained practical experience in:

- Building full-stack applications using Python and Django.
- Implementing authentication and role-based access restrictions.
- Designing relational database models and working with Django ORM.
- Integrating PostgreSQL and third-party cloud storage.
- Developing responsive desktop and mobile interfaces.
- Deploying Django applications to a cloud hosting platform.
- Implementing CI/CD automation using GitHub Actions.

## 🔮 Future Enhancements

- Movie recommendation system.
- Advanced movie discovery and filtering.
- Pagination and performance optimization.
- Expanded automated test coverage.
- Improved user profiles and review interactions.

---

## 👨‍💻 Developer

**Satyam Mishra**

Computer Science & Engineering Student | Full-Stack Developer

- **GitHub:** [satyammishra8-1](https://github.com/satyammishra8-1)
- **LinkedIn:** [satyam-mishra19](https://www.linkedin.com/in/satyam-mishra-42b806404/)
- **Live Project:** [CineRate](https://cinerate-ojlp.onrender.com)

---

*Designed, developed and deployed with Python and Django.*
