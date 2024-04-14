from django.shortcuts import render
from django.http import JsonResponse

import requests


def index(request):
    return render(request, "app_sw/index.html")


def get_planets(request):
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        planets = {id: planet["name"] for id, planet in enumerate(data["results"], start=1)}
        context = {
            "planets": data["results"],
        }   
        return render(request, "app_sw/planets.html", context)


def get_people(request):
    return render(request, "app_sw/people.html")

def get_starships(request):
    return render(request, "app_sw/starships.html")
