import shutil
import my_packages.logstest
import my_packages.slackalerttest 
import os

def copy_folder(save_location,path_dir,name_dir,time_stamp,yyyy,mm):

    try:
        perfect_location = save_location+"//"+str(int(yyyy))+"//"+str(int(mm))+"//"+str(time_stamp)
        try:
            shutil.copytree(path_dir,perfect_location+"//"+str(1))
            text1 = (name_dir + " folder copied to " + perfect_location)
            #logstest.ext_info_logs(text1)
            
            
        except:
            c = 0
            for i in os.listdir(perfect_location):
                c+=1
            count = c + 1
            shutil.copytree(path_dir,perfect_location+"//"+str(count))
            text1 = (name_dir + " folder is renamed as " + str(count) + " and saved in " + perfect_location)
            #logstest.ext_info_logs(text1)
            
            
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass

def unknown_folder(file_name,save_location,unknown_path_dir):
    
    try:
        perfect_location = save_location

        try:
            shutil.copytree(unknown_path_dir,perfect_location+"//"+file_name+"_"+str(1))
            text2 = (file_name + " folder copied to " + perfect_location)
            #logstest.ext_info_logs(text2)
            #slack1 = "Unknown Folder " + str(1) + " Found : " + file_name
            my_packages.slackalerttest.slack_alert(file_name)
            
        except:
            c = 0
            for i in os.listdir(perfect_location):
                c+=1
            count = c + 1
            shutil.copytree(unknown_path_dir,perfect_location+"//"+file_name+"_"+str(count))
            text2 = (file_name + " folder is renamed as " + str(count) + " and saved in the " + perfect_location)
            #logstest.ext_info_logs(text2)
            #slack1 = "Unknown Folder " + str(count) + " Found : " + file_name
            my_packages.slackalerttest.slack_alert(file_name)
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass