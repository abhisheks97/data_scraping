from django.http import HttpResponse
from selectorlib import Extractor
import requests
import json

def index(request):
    return HttpResponse("Hello, Welcome to Amazon Data Scraper")

