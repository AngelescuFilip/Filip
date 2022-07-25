from rest import Rest
from datetime import datetime
import requests


class TodosRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_todos(self, api_url, header):
        return super().get_data(api_url, header)

    def create_todo(self, todo, api_url, header):
        super().post(todo, api_url, header)

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

    def delete_object(self, api_url, title, header):
        for item in self.get_data(api_url, header):
            print(item)
            if item["name"] == title:
                api_url = api_url + '/' + str(item["id"])
                response = requests.delete(api_url, headers=header)
                print(response.status_code)
                if response.status_code == 200:
                    print("A fost sters")
