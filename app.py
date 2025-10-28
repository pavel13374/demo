# Импортируем все библиотеки
import flask
import requests
import jinja2
from bs4 import BeautifulSoup
import django

# Простейшее использование — просто вывод версий и приветствия
if __name__ == "__main__":
    print("Hello from latest variant!")
    print(f"Flask version: {flask.__version__}")
    print(f"Requests version: {requests.__version__}")
    print(f"Jinja2 version: {jinja2.__version__}")
    print(f"BeautifulSoup version: {BeautifulSoup('').__class__.__module__}")
    print(f"Django version: {django.get_version()}")
