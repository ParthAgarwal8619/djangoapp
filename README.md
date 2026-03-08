# 🌙 Django Dark Notes App

A modern **Notes Management Web Application** built using **Django** with authentication, search, edit functionality, and a dark UI dashboard.

🔗 **Live Demo:**
https://djangoapp-1-jzs5.onrender.com

🔐 **Admin Panel:**
https://djangoapp-1-jzs5.onrender.com/admin

---

# 🚀 Features

* 👤 User Signup & Login
* 📝 Create Notes
* ✏ Edit Notes
* ❌ Delete Notes
* 🔎 Search Notes by Title
* 🌙 Dark Theme Dashboard UI
* 🔐 User-specific Notes (each user sees their own notes)
* ⚡ REST API Support
* ☁ Cloud Deployment

---

# 🛠 Tech Stack

* **Backend:** Django
* **API:** Django REST Framework
* **Database:** SQLite (development)
* **Deployment:** Render
* **Server:** Gunicorn
* **Static Files:** WhiteNoise

---

# 📂 Project Structure

```
djangodarkproject
│
├── darknotes        # Main Django project
│
├── notes            # Notes app
│
├── static           # CSS / Static files
│
├── templates        # HTML templates
│
├── manage.py
│
├── requirements.txt
│
└── Procfile
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/django-notes-app.git
cd django-notes-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run the server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🌐 Deployment

The project is deployed on **Render**.

### Live Application

https://djangoapp-1-jzs5.onrender.com

### Admin Dashboard

https://djangoapp-1-jzs5.onrender.com/admin

---

# 📡 API Endpoint

Example API endpoint:

```
/api/notes/
```

Returns JSON list of notes.

---

# 🎯 Future Improvements

* Email verification
* Rich text notes editor
* Tagging & categories
* Mobile responsive dashboard
* Notifications

---

# 👨‍💻 Author

Developed by **Your Name**

If you like this project, give it a ⭐ on GitHub!
