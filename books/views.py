from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    """Serve the main IELTS books guide & index page."""
    return render(request, 'index.html')

def book_reader(request):
    """Serve the interactive online book reader page."""
    return render(request, 'book/index.html')

def robots_txt(request):
    """Serve the robots.txt file with correct content type."""
    robots_file = BASE_DIR / 'static' / 'robots.txt'
    if not robots_file.exists():
        robots_file = BASE_DIR / 'robots.txt'
    if robots_file.exists():
        content = robots_file.read_text(encoding='utf-8')
    else:
        content = "User-agent: *\nAllow: /\n"
    return HttpResponse(content, content_type="text/plain")

def sitemap_xml(request):
    """Serve sitemap.xml with xml content type."""
    sitemap_file = BASE_DIR / 'static' / 'sitemap.xml'
    if not sitemap_file.exists():
        sitemap_file = BASE_DIR / 'sitemap.xml'
    if sitemap_file.exists():
        content = sitemap_file.read_text(encoding='utf-8')
    else:
        content = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>'
    return HttpResponse(content, content_type="application/xml")

def health_check(request):
    """Health check endpoint for Railway deployment monitoring."""
    return JsonResponse({"status": "healthy", "service": "ielts-books-django"})

def custom_page_not_found_view(request, exception=None):
    """Custom 404 handler."""
    return render(request, '404.html', status=404)

def custom_error_view(request):
    """Custom 500 handler."""
    return render(request, '500.html', status=500)
