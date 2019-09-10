import requests
import json

if __name__ == "__main__":

    # Open a local json file
    # Alternatively you can use requests library to get an online file

    with open('apt1.json', encoding='utf-8') as json_file:
        # now our dictionary has been imported into apt1 variable
        apt1 = json.load(json_file)

    # You can print all dictionary's objects by uncommenting next lines
    # for object in apt1["objects"]:
    #     # before printing check if key name 'name' exists in object
    #     if 'name' in object:
    #         print("field name: %s" % object["name"])

    # use our api to insert stix formatted objects to db
    # This is the url which is derived from routes we created in our api
    addurl = 'http://localhost:5000/add'

    # define headers for the post request.
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # for each of the objects contained in the json file, try to import them through api in mongodb
    for object in apt1["objects"]:
        # response contains the reply for the API. In case everything went according to the plan
        # response.status_code must be 200
        response = requests.post(addurl, data=json.dumps(object), headers=headers)
        if response.status_code == 200:
            # response contains the newly added id. Just print it
            print("Inserted object id is %s" % response.json())
