import datetime
import my_packages.logstest
import my_packages.copyfoldertest

def copy_folder_mobile(save_location,path_dir,name_dir,zip_filename):

    #Timestamp for Mobile   
    try:
        q = zip_filename
        z = q.split("_")
        yyyy = int(z[1][:2] + str(20))
        mm = int(z[1][2:4])
        dd = int(z[1][4:])
        q = datetime.datetime(yyyy,mm,dd).timestamp()   
        time_stamp = int(q)
        my_packages.copyfoldertest.copy_folder(save_location,path_dir,name_dir,time_stamp,yyyy,mm)
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass        

def copy_folder_desktop(save_location,path_dir,name_dir,zip_filename):

    #Timestamp for Desktop
    try:        
        q = zip_filename
        z = q.split("_")
        yyyy = int(z[1][:4])
        mm = int(z[1][4:6])
        dd = int(z[1][6:])
        q = datetime.datetime(yyyy, mm, dd).timestamp() 
        time_stamp = int(q) 
        my_packages.copyfoldertest.copy_folder(save_location,path_dir,name_dir,time_stamp,yyyy,mm)  
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass        