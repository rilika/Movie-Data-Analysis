
try:
    import pymongo
    from pymongo import MongoClient
    import pandas as pd
    import json
except Exception as e:
    print("Some Modules are Missing ")


class MongoDB(object):

    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]



    def InsertData(self, path=None):
        """

        :param path: Path os csv File
        :return: None
        """

        df = pd.read_csv(path)
        data = df.to_dict('records')
        #df.drop(['keywords','overview','homepage','tagline','spoken_languages'],axis =1,inplace = True)
        self.collection.insert_many(data, ordered=False)
        print("All the Data has been Exported to Mongo DB Server .... ")

    def insert(self): 
        try: 
            conn = MongoClient() 
            print("Connected successfully!!!") 
        except:   
            print("Could not connect to MongoDB") 
  
    

    

if __name__ == "__main__":
    mongodb = MongoDB(dBName = 'Movie3', collectionName='MovieCollection3')
    mongodb.InsertData(path="tmdb_movies_data.csv")
        
    
     
  







