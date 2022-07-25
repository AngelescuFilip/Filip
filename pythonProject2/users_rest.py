from rest import Rest
import requests


class UsersRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_users(self, api_url, header):
        return super().get_data(api_url, header)

    def create_user(self, todo, api_url, header):
        super().post(todo, api_url, header)

    def get_number_users(self, api_url, header, number):
        response = super().get_data(api_url, header)
        tot = response.json()
        user_count = 0
        lista = []
        myorder = list(range(len(tot)))
        myorder.reverse()
        tot = [tot[i] for i in myorder]
        for item in tot:
            if item["status"] == "active":
                lista.append(item)
                user_count += 1
            if user_count == number:
                return lista

    def modify_email(self, api_url, todo, header, name):
        for item in super().get_data(api_url, header):
            print(item)
            if item["name"] == name:
                api_url = api_url + '/' + str(item["id"])
                response = requests.patch(api_url, json=todo, headers=header)
                print(response)
                if response.status_code == 200:
                    print("A fost updatat si salvat")

    def middle_name(self, api_url, header, number):
        data = super().get_data(api_url, header)
        lista = []
        count = 0
        for item in data:
            name = item["name"]
            split_name = name.split()
            print(split_name)
            if len(split_name) == 3:
                lista.append(split_name[1])
                count += 1
            if count == number:
                return lista

    def delete_object(self, api_url, title, header):
        for item in self.get_data(api_url, header):
            print(item)
            if item["title"] == title:
                api_url = api_url + '/' + str(item["id"])
                response = requests.delete(api_url, headers=header)
                print(response.status_code)
                if response.status_code == 200:
                    print("A fost sters")