import requests

class Rest:

    idcount = 0
    def get_data(self, api_url, header):
        response = requests.get(api_url, headers=header)
        return response.json()

    def post(self, api_url, header, todo):
        response = requests.post(api_url, json=todo, headers=header)
        print(response.status_code)
        if response.status_code == 201:
            Rest.idcount += 1
        print(response.json())

    def get_id(self, api_url, param, header):
        response = requests.get(api_url, params=param, headers=header)
        var = response.json()
        return var[0]["id"]

    def verify_added_user(self):
        return Rest.idcount

