import logging
import time

def error_logs(e_val):
    err_logger = logging.getLogger("Openavn_Error") 

    err_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    err_log_file_name = 'Openavn_Error.log'
    err_file_handler = logging.FileHandler(err_log_file_name)
    err_logger.setLevel(logging.ERROR)
    err_file_handler.setFormatter(err_formatter)

    if (err_logger.hasHandlers()):
        err_logger.handlers.clear()
    err_logger.addHandler(err_file_handler)

    err_logger.error('------------------------------------------------------------------------------------------------------------------')
    try:
        err_logger.exception(f'[-] {e_val}')
    except:
        err_logger.logging(f'[-] {e_val}')

def info_logs(zip_filename,folder_counter,file_counter,count_known_folders,count_unknown_folders):
    info_logger = logging.getLogger("Openavn_Info") 

    info_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    info_log_file_name = 'Openavn_Info.log'
    info_file_handler = logging.FileHandler(info_log_file_name)
    info_logger.setLevel(logging.INFO)
    info_file_handler.setFormatter(info_formatter)

    if (info_logger.hasHandlers()):
        info_logger.handlers.clear()
    info_logger.addHandler(info_file_handler)

    info_logger.info('[-] ' + zip_filename + ' has successfully extracted')
    info_logger.info('[-] Extracted Folders :' + str(folder_counter) + ' and Files:'+ str(file_counter))
    info_logger.info('[-] Total Number of Known Folders in ' + zip_filename + ' : ' + str(count_known_folders))
    #count_unknown_folders1 = count_known_folders - count_unknown_folders
    info_logger.info('[-] Total Number of Unknown Folders in ' + zip_filename + ' : ' + str(count_unknown_folders))

def ext_info_logs(text_val):
    info1_logger = logging.getLogger("Openavn_Info")    

    info1_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    info1_log_file_name = 'Openavn_Info.log'
    info1_file_handler = logging.FileHandler(info1_log_file_name)
    info1_logger.setLevel(logging.INFO)
    info1_file_handler.setFormatter(info1_formatter)

    if (info1_logger.hasHandlers()):
        info1_logger.handlers.clear()
    info1_logger.addHandler(info1_file_handler)

    info1_logger.info(f'[-] {text_val}')
    
def line_info_logs():
    info2_logger = logging.getLogger("Openavn_Info")    

    info2_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    info2_log_file_name = 'Openavn_Info.log'
    info2_file_handler = logging.FileHandler(info2_log_file_name)
    info2_logger.setLevel(logging.INFO)
    info2_file_handler.setFormatter(info2_formatter)

    if (info2_logger.hasHandlers()):
        info2_logger.handlers.clear()
    info2_logger.addHandler(info2_file_handler)

    info2_logger.info('------------------------------------------------------------------------------------------------------------------')