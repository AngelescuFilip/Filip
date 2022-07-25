import requests
import datetime
from datetime import datetime

class Methods:

    idcount = 0
#    def __init__(self):
#        self.lista = []

    def get_data(self, api_url, header):
        response = requests.get(api_url, headers=header)
        return response.json()

    def post(self, api_url, todo, header):
        response = requests.post(api_url, json=todo, headers=header)
        print(response.status_code)
        if response.status_code == 201:
            Methods.idcount += 1
        print(response.json())

    def verify_added_user(self):
        return Methods.idcount

    def get_id(self, api_url, param, header):
        response = requests.get(api_url, params=param, headers=header)
        var = response.json()
        return var[0]["id"]

    def get_number_users(self, api_url, number):
        response = requests.get(api_url)
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
        for item in self.get_data(api_url, header):
            print(item)
            if item["name"] == name:
                api_url = api_url + '/' + str(item["id"])
                response = requests.patch(api_url, json=todo, headers=header)
                print(response)
                if response.status_code == 200:
                    print("A fost updatat si salvat")

    def middle_name(self, api_url, header, number):
        data = self.get_data(api_url, header)
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

    def create(self, api_url, todo, header):
        response = requests.post(api_url, json=todo, headers=header)
        response.json()

    def due(self, api_url, header):
        information = self.get_data(api_url, header)
        for item in information:
            date = item["due_on"]
            d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f+05:30")
            d.strftime('%Y-%m-%d')
            item["due_on"] = d
            print(item["due_on"])
        a = information.sort(key=lambda x:x['due_on'])
#        for item in a:
#            final = datetime.strptime(item, "%Y-%m-%d %H:%M:%S")

        return information

    def delete_object(self, api_url, name, header):
        for item in self.get_data(api_url, header):
            print(item)
            if item["name"] == name:
                api_url = api_url + '/' + str(item["id"])
                response = requests.delete(api_url, headers=header)
                print(response.status_code)
                if response.status_code == 200:
                    print("A fost sters")

api_url = ["https://gorest.co.in/public/v2/users", "https://gorest.co.in/public/v2/posts",
           "https://gorest.co.in/public/v2/comments", "https://gorest.co.in/public/v2/todos"]

## Exercitiu 1
q = Methods()
#for item in api_url:
#    a = q.get_data(item)

## Exercitiu 2
#todo1 = {"name": "Ciprian", "email": "Ciprian@yahoo.com", "gender": "male", "status": "active"}
#todo2 = {"name": "Andr", "email": "Andr@yahoo.com", "gender": "male", "status": "active"}
header = {"Authorization": "Bearer 79fd5c55ecfe7354186dc1084638b0693d9b871842d3aa1821957454878d4423"}
#q.create_user(api_url[0], todo1, header)
#q.create_user(api_url[0], todo2, header)

## Exercitiu 3
#c = q.verify_added_user()
#print(c)

## Exercitiu 4
#param = {"name": "Ciprian"}
#d = q.get_id(api_url[0], param, header)
#print(d)

## Exercitiu 5
#e = q.get_number_users(api_url[0], 4)
#print(e)

## Exercitiu 6
#g = q.middle_name(api_url[0], header, 2)
#print(g)

## Exercitiu 7


## Exercitiu 8
#email = {"email": "Andrei@yahoo.com"}
#name = "Ciprian"
#f = q.modify_email(api_url[0], email, header, name)

## Exercitiu 9
#h = q.due(api_url[3], header)
#print(h)

## Exercitiu 10
todo3 = "Felpsi"
i = q.delete_object(api_url[0], todo3, header)

## Exercitiu 11