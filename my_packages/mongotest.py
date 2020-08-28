from pymongo import MongoClient
import os
import my_packages.logstest

def upload_to_mongo():
    try:        
        client = MongoClient("mongodb://hari:hari@cluster0-shard-00-00.qcxxt.mongodb.net:27017,cluster0-shard-00-01.qcxxt.mongodb.net:27017,cluster0-shard-00-02.qcxxt.mongodb.net:27017/Logs?ssl=true&replicaSet=atlas-d0fm22-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client['Logs']     
        log_file_name1 = "Openavn_Info.log"
        if(os.path.exists(log_file_name1)):
            col = db[log_file_name1]
            files = col.files
            f = open(log_file_name1,'r')
            text = f.read()
            doc = {
                "file_name": log_file_name1,
                "contents" : text }
            files.insert_one(doc)
            text1 = "File " + log_file_name1 + " uploaded to mongodb Successfully"
            my_packages.logstest.ext_info_logs(text1)

        log_file_name2 = "Openavn_Error.log"
        if(os.path.exists(log_file_name2)):
            col1 = db[log_file_name2]
            files1 = col1.files
            f1 = open(log_file_name2,'r')
            text1 = f1.read()
            doc1 = {
                "file_name": log_file_name2,
                "contents" : text1 }
            files1.insert_one(doc1)
            text2 = "File " + log_file_name2 + " uploaded to mongodb Successfully"
            my_packages.logstest.ext_info_logs(text2)
            
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass
    #print("mongodb")
