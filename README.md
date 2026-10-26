# Diti Goals

A simple productivity web application for managing daily tasks, personal goals, and tracking progress.

---

## 📌 About the Project

Diti Goals helps users organize their daily activities, set personal goals, and monitor their progress through a clean and user-friendly interface.

The project is developed with Django as part of the SoftUni Django Basics course.

## ✨ Features

- Create, view, edit, and delete tasks
- Organize tasks by category and priority
- Set personal goals and deadlines
- Track goal progress
- View productivity statistics
- Responsive design with a white, orange, and black color scheme

*Features will be implemented progressively during development.*

## 🛠️ Technologies

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap
- Git and GitHub

## 📋 Main Functionality

- Task management
- Personal goals
- Categories and priorities
- Progress tracking

## ⚙️ Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Dimitarr05/softuni_course_project
   ```

2. Open the project folder:

   ```bash
   cd softuni_course_project
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the application at `http://127.0.0.1:8000/`.

## 🗄️ Database

The project uses SQLite. Database tables are created by running Django migrations.

## 📂 Project Applications

- **Tasks:** Manage tasks and categories.
- **Goals:** Create goals and connect them with tasks.
- **Progress:** View and record task activities.
