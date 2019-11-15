import pymongo 

mongo_server="mongodb://localhost:27017/"


class nosql:

    def __init__(self):
        client = pymongo.MongoClient(mongo_server) 
        database=client["dbms"]
        self.pprofile=database["personal_profile"]        

    def get_data(self,input):
        ans=self.pprofile.find(input)
        result=[]
        for row in ans:
            result.append(row)
        return result
    
    def get_list(self):
        ans=self.pprofile.find()
        result=[]
        for row in ans:
            # temp=[]
            # temp.append(row["eid"])
            # temp.append(row["contact"])
            result.append(row["eid"])
        return result


    def update_data(self,condition,new):
        new1={}
        new1["$set"]=new
        # print(condition,new1)
        self.pprofile.update_one(condition,new1)
        # self.print_data()
        return

    def delete_data(self, condition):
        self.pprofile.delete_one(condition)
        return

    def unset_field(self,condition,field):
        newf={}
        self.print_data()
        newf["$unset"]=field
        print(condition,newf)
        self.pprofile.update_one(condition,newf)
        self.print_data()

    def insert_data(self,input):
        self.pprofile.insert_one(input)
        self.print_data()
        return
        
    def clear_data(self):
        self.pprofile.delete_many({})

    def print_data(self):
        ans=self.pprofile.find()
        for x in ans:
            print(x)
        return

