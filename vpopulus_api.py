__author__ = 'ca1ek'

import requests


class Citizen:
    def __init__(self, search_by, citizen_id):
        if search_by == "name":
            json = requests.get("http://api.vpopulus.net/v1/feeds/citizen.json?name=" + citizen_id).json()
        elif search_by == "id":
            json = requests.get("http://api.vpopulus.net/v1/feeds/citizen.json?id=" + citizen_id).json()
        self.raw_json = json
        self.id = json["id"]
        self.avatar_url = json["avatar-link"]
        self.wellness = json["wellness"]
        self.skills = json["skills"]
        self.citizenship = json["citizenship"]["country"]
        self.location = json["location"]["country"]
        self.region = json["location"]["region"]
        self.company = json["company"]
        self.party = json["party"]
        self.army = json["army"]
        self.newspaper = json["newspaper"]
        self.date_of_birth = json["date-of-birth"]

