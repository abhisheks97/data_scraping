import json

import requests
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from amazon.config import *
from amazon.data_scraper import *


def index(request):
    return HttpResponse("Hello, Welcome to Amazon Data Scraper")

def amazon_search(request):

    if "keyw" in request.GET:
        keyword = request.GET["keyw"]
    else:
        print("argumentis missing")
        return HttpResponse("Alert...Missing Argument -> Keyw")

    result = []
    url = AMAZON_SEARCH_URL + str(keyword)

    status, data = scrape(url)
    if status:
        for product in data['products']:
            product['search_url'] = url
            print("Saving Product: %s" % product['title'])
            result.append(product)

        with open("amazon/results.json", 'w') as f:
            json.dump(result, f, indent=4)

        data = {"product_data": result, "error": False, "msg": ""}
        data = json.dumps(data)
        return HttpResponse(data)
    else:
        data = {"product_data": result, "error": True, "msg": ""}
        data = json.dumps(data)
        return HttpResponse(data)
