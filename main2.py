#import zipfiletest
import my_packages.mongotest
#import mongotest
import my_packages.zipfiletest
#import logstest
import my_packages.logstest
import os
import shutil
import re
from zipfile import ZipFile
import datetime
import logging
from datetime import date
import multiprocessing
import time
from slack_webhook import Slack
import random
import string

def get_random_alphanumeric_string(length):

    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    job_log = "Job ID : " + result_str
    my_packages.logstest.ext_info_logs(job_log)


def pass_zip_file(zip_file_name,zip_file_path):
    print('Thread Started : ' + zip_file_name)
    my_packages.zipfiletest.zip_file(zip_file_name,zip_file_path)
    print('Thread Finishes : ' + zip_file_name)
def main_program(): 
    #Main program
    try:
        path_folder = "/root/Desktop/test/done"
        count_zip = 0
        zip_list = list()
        t1 = time.time()
        for d, di, fi in sorted(os.walk(path_folder)):
            fi.sort()   
            for f in fi:
                zip_file_name = f
                print(zip_file_name)
                zip_file_path = os.path.join(d, zip_file_name)
                zip_list.append((zip_file_name,zip_file_path))

        get_random_alphanumeric_string(20)
        today_start = date.today()
        t1 = time.time()
        start_t = "Job Started on " + str(today_start) 
        my_packages.logstest.ext_info_logs(start_t)
        new_zip_list = zip_list
        tot_count = len(new_zip_list)
        tot_count_zip = "Total Number of ZipFiles in "+ path_folder + " : " + str(tot_count)
        my_packages.logstest.ext_info_logs(tot_count_zip)

        with multiprocessing.Pool(processes=5) as pool:
            results = pool.starmap(pass_zip_file, new_zip_list)

        t2 = time.time() - t1
        com_t = "Job Completed on " + str(today_start) + " at : " + str(t2)
        my_packages.logstest.ext_info_logs(com_t)
        
        
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass
    
if __name__ == "__main__":
    main_program()
    my_packages.mongotest.upload_to_mongo()
    my_packages.logstest.line_info_logs()
