from zipfile import ZipFile
import os
from concurrent.futures import ThreadPoolExecutor
import threading
import my_packages.logstest
import my_packages.slackalerttest
import my_packages.movefoldertest
import shutil

def last_log(count_folder_copy):
    no_of_known_copy = "Number of Known Folders Copied : " + str(count_folder_copy)
    my_packages.logstest.ext_info_logs(no_of_known_copy)    

def zip_file(zip_file_name,zip_file_path):
    try:
        path_folder = "/root/Desktop/test/done"
        zip_filename,file_extension = os.path.splitext(zip_file_name)
        add_item = list()
        zip_filename_name = path_folder +"/"+zip_filename
        count_unknown_folders = 0
        count_known_folders = 0
        count_folder_copy = 0
        if(file_extension == ".zip"):
            with ZipFile(zip_file_path, 'r') as zip:      
                zip.extractall('/root/Desktop/test/done')
                folder_counter = sum([len(d) for r, d, folder in os.walk(zip_filename_name)])
                file_counter = sum([len(files) for r, d, files in os.walk(zip_filename_name)])
                
                for dirname, dirnames, filenames in os.walk(zip_filename_name):                                         
                    for subdirname in dirnames:         
                        name_dir = subdirname
                        path_dir = os.path.join(dirname, name_dir)
                        add_item.append(name_dir)
                        count_known_folders+=1
                        index_of_item = add_item.index(name_dir)                        
                        executor1 = ThreadPoolExecutor(max_workers=8)
                        task1 = executor1.submit(my_packages.movefoldertest.move_folder(name_dir,path_dir,zip_filename,add_item,index_of_item))
                        count_folder_copy+=1
                        for i in add_item:
                            if i not in "":
                                count_unknown_folders = count_unknown_folders + 1
                                file_name = i
                                unknown_path_dir = os.path.join(dirname , name_dir)
                                index_of_item1 = add_item.index(file_name)                              
                                executor2 = ThreadPoolExecutor(max_workers=4)
                                task2 = executor2.submit(my_packages.movefoldertest.move_unknown_folder(file_name,unknown_path_dir,add_item,index_of_item1))
                                                                
                my_packages.logstest.info_logs(zip_filename , folder_counter,file_counter ,count_known_folders,count_unknown_folders)   
                shutil.rmtree(zip_filename_name)    
        

        last_log(count_folder_copy)
        my_packages.slackalerttest.com_slack_alert(zip_filename)


                
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass
