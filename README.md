# Cambridge IELTS Books Web Application (Django & Railway)

A production-ready Django application serving the Cambridge IELTS Books portal, complete with interactive online book reader, SEO metadata, WhiteNoise static compression, and Railway deployment configuration.

---

## 🚀 Features

- **Django 5.x / 6.x Architecture**: Clean separation with `ielts_project` settings and `books` app.
- **Production-Ready**: Configured with `WhiteNoise`, `Gunicorn`, `dj-database-url`, and PostgreSQL/SQLite support.
- **Preconfigured for Railway**: Includes `Procfile`, `railway.json`, `nixpacks.toml`, and `runtime.txt`.
- **Full SEO & Static Routing**:
  - `/` - Main IELTS Books index page
  - `/book/` - Interactive online book reader
  - `/robots.txt` - Crawling directives (served as `text/plain`)
  - `/sitemap.xml` - XML Sitemap (served as `application/xml`)
  - `/health/` - Deployment health check endpoint (`application/json`)
  - Custom 404 & 500 error templates

---

## 🛠️ Local Development

### 1. Prerequisites
- Python 3.10+ installed

### 2. Setup Virtual Environment & Install Dependencies
```bash
# Optional: Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On macOS / Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Run Migrations & Collect Static Files
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 4. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

### 5. Run Tests
```bash
python manage.py test
```

---

## 🚢 Deploying to Railway

### Method 1: Deploy via GitHub (Recommended)

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Django project ready for Railway"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Connect to Railway**:
   - Go to [Railway.app](https://railway.com/) and click **"New Project"**.
   - Select **"Deploy from GitHub repo"** and choose this repository.

3. **Configure Environment Variables (in Railway Dashboard > Variables)**:
   - `SECRET_KEY`: (Generate a secure random string)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*` (or your railway domain like `*.up.railway.app`)
   - `CSRF_TRUSTED_ORIGINS`: `https://*.railway.app,https://*.up.railway.app`
   - *(Optional)* Add a **PostgreSQL** database service in your Railway project; Railway will automatically supply the `DATABASE_URL` variable.

4. **Deploy**:
   - Railway will automatically detect the `railway.json` / `Procfile`, run `collectstatic` & `migrate`, and start Gunicorn on the allocated `$PORT`.
   - Generate a public domain under **Settings > Networking > Generate Domain**.

---

## 📁 Project Structure

```
├── ielts_project/         # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Production settings with dj-database-url & whitenoise
│   ├── urls.py           # Main routing
│   └── wsgi.py           # WSGI entry point for Gunicorn
├── books/                 # Django application
│   ├── apps.py
│   ├── tests.py          # View and health check unit tests
│   ├── urls.py           # Route definitions
│   └── views.py          # View handlers (index, reader, robots, sitemap, health)
├── templates/             # HTML Templates
│   ├── index.html        # Main landing page
│   ├── book/
│   │   └── index.html    # Online reader page
│   ├── 404.html          # Custom 404 page
│   └── 500.html          # Custom 500 server error page
├── static/                # Static assets (robots.txt, sitemap.xml, etc.)
├── Procfile               # Process definition for Railway / Heroku
├── railway.json           # Railway build & deploy settings
├── nixpacks.toml          # Nixpacks build configuration
├── runtime.txt            # Python runtime version
├── requirements.txt       # Python package dependencies
├── .env.example           # Sample environment variables
└── manage.py              # Django management script
```
