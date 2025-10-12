import json 
import os

class Database:

    def __init__(self, filename='Data.json'):
        self.filename = filename
        # create file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as wf:
                json.dump({}, wf)

    def add_data(self,name,email,password):

        with open('Data.json','r') as rf:
            Database = json.load(rf)

        if email in Database:
            return 0
        else:
            Database[email] = [name,password]
            with open('Data.json','w') as wf:
                json.dump(Database,wf)
            return 1
        
    def search(self,email,password):

        with open('Data.json','r') as rf:
            Database = json.load(rf)

        if email in Database:
            if Database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0