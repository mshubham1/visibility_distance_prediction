import pymongo
import ssl
import logging
logging.basicConfig(filename='log_file/database_log.txt', 
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M-%S')

class connector:
    def __init__(self):
        default_connection_url ="mongodb+srv://mafia123:mafia123@cluster0.j7nj9.mongodb.net/visibility_prediction?retryWrites=true&w=majority"
        client = pymongo.MongoClient(default_connection_url,ssl_cert_reqs=ssl.CERT_NONE)
        logging.info("Database connection established..!")
        try:
            db_name = "visibility_prediction"
            database = client[db_name]
            logging.info("Database Created Successfully ..!")
            collection_name = "visibility"
            self.collection = database[collection_name]
            logging.info("Collection Created Successfully ..!")
        except Exception as e:
            logging.warning("found error in DB or Collection :{}".format(e))
            print("Error")
        

    def add_data(self,input1):
        self.input1=input1
        try:
            info = {
                'WETBULBTEMPF1': input1['WETBULBTEMPF1'],
                'RelativeHumidity': input1['RelativeHumidity'],
                'WindSpeed': input1['WindSpeed'],
                'WindDirection': input1['WindDirection'],
                'SeaLevelPressure': input1['SeaLevelPressure']
            }
            
        
            self.collection.insert_one(info)
            logging.info("Data Inserted into the Cluster !!")
   
        except Exception as e:
            logging.warning("found error in info json {}".format(e))