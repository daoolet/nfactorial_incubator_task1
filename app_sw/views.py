from django.shortcuts import render

import requests


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
    url = "https://swapi.dev/api/starships/"
    url2 = "https://swapi.dev/api/starships/?page=2"
    url3 = "https://swapi.dev/api/starships/?page=3"
    url4 = "https://swapi.dev/api/starships/?page=4"

    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)

    if response.status_code == 200:
        data = response.json()["results"]
        data2 = response2.json()["results"]
        data3 = response3.json()["results"]
        data4 = response4.json()["results"]
        data.extend(data2 + data3 + data4)

        context = {
            "starships": data,
        }   
        return render(request, "app_sw/starships.html", context)