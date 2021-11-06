from flask import Flask,render_template,request,abort
import joblib
#import pickle
import numpy as np
from log_file.logger import Logs
import pymongo
import ssl

# configuring logging method
log = Logs("log_file/log_data.log")
log.addLog("INFO", "Execution started Successfully !")



#model = pickle.load(open("Random_Forest.pkl","rb"))
model = joblib.load(open("model/Random_Regrsession.pkl", "rb"))

app = Flask(__name__)
# route for main pageapp
@app.route('/')
def index():
    return render_template("index.html")

# route for prediction 
@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == "POST":
        WETBULBTEMPF1 = request.form.get("WETBULBTEMPF1")
        RelativeHumidity = request.form.get("RelativeHumidity")
        WindSpeed = request.form.get("WindSpeed")
        WindDirection = request.form.get("WindDirection")
        SeaLevelPressure = request.form.get("SeaLevelPressure")
        log.addLog("INFO", "Successfully retrieved information from the user... !")
        input1=[[WETBULBTEMPF1,RelativeHumidity,WindSpeed,WindDirection,SeaLevelPressure]]
        print(input1)
        #input1 = np.nan_to_num(input1) 
        print(model)
        prediction = model.predict(input1)
        print(prediction)
        
        #Data Ingestion
        # database connections
        try:
            default_connection_url ="mongodb+srv://mafia123:mafia123@cluster0.j7nj9.mongodb.net/visibility_prediction?retryWrites=true&w=majority"
            client = pymongo.MongoClient(default_connection_url,ssl_cert_reqs=ssl.CERT_NONE)
            print("Database connection established.")
            log.addLog("INFO", "Database connection established..! !")
        except Exception as e:
            log.addLog("ERROR", "Error while connecting to Database :{}".format(e))

        #creation of collection      
        try:
            db_name = "visibility_prediction"
            database = client[db_name]
            log.addLog("INFO", "Database Created !")
            print("Collection Created")
            collection_name = "visibility"
            collection = database[collection_name]
            log.addLog("INFO", "Collection Created!")
        except Exception as e:
            log.addLog("ERROR", "Found error in DB or Collection : {}".format(e))
        
        #insertion in collection
        try:
            info = {
                    'WETBULBTEMPF': WETBULBTEMPF1,
                    'RelativeHumidity': RelativeHumidity,
                    'WindSpeed': WindSpeed,
                    'WindDirection': WindDirection,
                    'SeaLevelPressure': SeaLevelPressure
                }
            collection.insert_one(info)
            log.addLog("INFO", "Data Inserted in the Collection Successfully !!")
            client.close()
            log.addLog("INFO", "Database connection closed Successfully !!")
        except Exception as e:
            log.addLog("ERROR", "found error in info json :{}".format(e))
            return render_template('index.html')
        log.addLog("INFO", "Prediction done Successfully !")
        return render_template('index.html',result="the visbility is: {}".format(prediction))

    else:
        log.addLog("INFO", "Return from the Predict Route!!")
        return render_template('index.html')
   

@app.route("/database")
def database():
    
    heading = ("WETBULBTEMPF", "RelativeHumidity", "WindSpeed", "WindDirection", "SeaLevelPressure")
    all_data = ""
    try:
        default_connection_url ="mongodb+srv://mafia123:mafia123@cluster0.j7nj9.mongodb.net/visibility_prediction?retryWrites=true&w=majority"
        client = pymongo.MongoClient(default_connection_url,ssl_cert_reqs=ssl.CERT_NONE)
        log.addLog("INFO", "Database connection established..! !")
        database = client["visibility_prediction"]
        collection = database["visibility"]
        all_data = collection.find()
        log.addLog("INFO", "Retriviwed all data from Collection Visibility !")
        ele=[]
        for data in collection.find():
            ele.append([data['WETBULBTEMPF'],data['RelativeHumidity'],data['WindSpeed'],data['WindDirection'],data['SeaLevelPressure']])
        client.close()
        log.addLog("INFO", "Closing the Connection !")

    except Exception as error:
        print("Error occured while fetching all data from Database !", error)
        log.addLog("ERROR", "Error occured while fetching all data from Database : {} !" .format(error))



    log.addLog("INFO", "Rendering tamplate <database.html> with all Data !")
    return render_template('database.html', heading = heading, data = ele)


if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=8080)
    app.run(debug=True)
