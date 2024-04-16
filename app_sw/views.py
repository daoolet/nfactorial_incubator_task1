from django.shortcuts import render
from django.core.paginator import Paginator

import requests


def index(request):
    return render(request, "app_sw/index.html")


def get_planets(request):
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)
    data = response.json()

    context = {
        "planets": data["results"],
    }   
    return render(request, "app_sw/planets.html", context)
    

def planet_detail(request, id):
    url = f"https://swapi.dev/api/planets/{id}" 
    response = requests.get(url)
    data = response.json()

    context = {
        "data": data,
    }   
    return render(request, "app_sw/planet_detail.html", context)


def get_people(request):
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["results"]
        people_count = response.json()["count"]

        context = {
           "people": data,
           "people_count": people_count,
        } 
        return render(request, "app_sw/people.html", context)


def get_starships(request):
    urls = [
        "https://swapi.dev/api/starships/",
        "https://swapi.dev/api/starships/?page=2",
        "https://swapi.dev/api/starships/?page=3",
        "https://swapi.dev/api/starships/?page=4"
    ]

    data = []
    
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data.extend(response.json()["results"])


    page_number = request.GET.get('page', 1)
    paginator = Paginator(data, 6)

    page_obj = paginator.page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, "app_sw/starships.html", context)