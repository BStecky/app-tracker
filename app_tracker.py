import pickle
import json
import time
from datetime import datetime

# To-Do
# Format View
# Delete Application
# Update Application 

class Application:
    def __init__(self):
        self.company = None
        self.app_link = None
        self.application_date = None
        self.received_response = None
        self.received_interview = None
        self.received_offer = None

    def show(self):
        print("\n", "----------------------------------" + "\n")
        print("Company Name: ", self.company, "\n")
        print("Application Link: ", self.app_link, "\n")
        print("Application Date: ", datetime.fromtimestamp(self.application_date), "\n")
        print("Received Response: ", self.received_response, "\n")
        print("Received Interview: ", self.received_interview, "\n")
        print("Received Offer: ", self.received_offer, "\n")
        print("----------------------------------")

    def encoder(self):
        return {'company' : self.company, 'app_link' : self.app_link, 'application_date' : self.application_date,
        'received_response' : self.received_response, 'received_interview' : self.received_interview, 'received_offer' : self.received_offer}

    def write_json(self):
        encoded = self.encoder()
        with open ('applications.json', 'r+') as file:
            file_data = json.load(file)
            print(file_data)
            file_data["applications"].append(encoded)
            file.seek(0)
            json.dump(file_data, file, indent=4)

while(True):
    response = input("Add a new application(1), view application history (2), or quit (3)? ")
    if response == '1':
        new_app = Application()
        print('add app link')
        new_app.company = input("Please input the company name. ")
        new_app.app_link = input("Please input the company link. ")
        new_app.application_date = time.time()
        new_app.show()
        response = input("Does this look okay? (y) or (n)")
        if response == 'y':
            new_app.write_json()
        else:
            continue
    elif response == '2':
        with open('applications.json', 'r') as file:
            json_object = json.load(file)
            print(json_object)
    elif response == '3':
        print('quit')
        break
    else:
        print('Invalid input')
        continue


