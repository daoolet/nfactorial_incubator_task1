from django.shortcuts import render
from django.http import JsonResponse

import requests
import json

def index(request):
    return render(request, "app_sw/index.html")


def get_planets(request):
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        context = {
            "planets": data["results"],
        }   
        return render(request, "app_sw/planets.html", context)
    

def planet_detail(request, id):
    url = f"https://swapi.dev/api/planets/{id}" 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        context = {
            "data": data,
        }   
        return render(request, "app_sw/planet_detail.html", context)

def get_people(request):
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        context = {
            "people": data["results"],
        }   
        return render(request, "app_sw/people.html", context)

def people_detail(request, id):
    ...

def get_starships(request):
    url = "https://swapi.dev/api/starships/"
    url2 = "https://swapi.dev/api/starships/?page=2"

    response = requests.get(url)
    response2 = requests.get(url2)

    if response.status_code == 200:
        data = response.json()["results"]
        data2 = response2.json()["results"]
        data.extend(data2)

        context = {
            "starships": data,
        }   
        return render(request, "app_sw/starships.html", context)

def starship_detail(request, id):
    ...
