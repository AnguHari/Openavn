import re
import my_packages.logstest
import my_packages.copyfoldertestos
import my_packages.copyfoldertest
import os

def move_folder(name_dir,path_dir,zip_filename,add_item,index_of_item):


    #Desktop
    #Windows Classification
    bin_search = '[B-b]+[I-i]+[N-n]+$'
    mzothers_search = '[M-m]+[Z-z]+[O-o]+[T-t]+[H-h]+[E-e]+[R-r]+[S-s]+$'
    dll32_search = '[D-d]+[L-l]+[L-l]+32+$'
    exe32_search = '[E-e]+[X-x]+[E-e]+32+$'
    sys32_search = '[S-s]+ys32$'
    dll64_search = '[D-d]+[L-l]+[L-l]+64+$'
    exe64_search = '[E-e]+[X-x]+[E-e]+64+$'
    sys64_search = '[S-s]+ys64$'
    archives_search = '[A-a]+[R-r]+[C-c]+[H-h]+[I-i]+[V-v]+[E-e]+[S-s]+$'
    archive_search = '[A-a]+[R-r]+[C-c]+[H-h]+[I-i]+[V-v]+[E-e]+$'
    others_search = '[O-o]+thers$'
    
    #MacOs
    macdmg_search = '[M-m]+[A-a]+[C-c]+[D-d]+[M-m]+[G-g]+$'

    #Java
    java_search = '[J-j]+[A-a]+[V-v]+[A-a]+$'

    #Common
    pdf_search = '[P-p]+[D-d]+[F-f]+$'

    #Mobile
    #Android
    apk_search = '[A-a]+[P-p]+[K-k]+$'
    dex_search = '[D-d]+[E-e]+[X-x]+$'
    a_elf_search = '[E-e]+[L-l]+[F-f]+$'
    metadata_search = '[M-m]+[E-e]+[T-t]+[A-a]+[D-d]+[A-a]+[T-t]+[A-a]+$'

        
    #Bin
    try:            
        if(name_dir == 'bin'):
            save_location1 = os.getcwd() + '//ETL//Desktop//Windows//Bin'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location1,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)         
        elif(re.match(bin_search,name_dir)):
            save_location1 = os.getcwd() + '//ETL//Desktop//Windows//Bin'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location1,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e1:
        logstest.error_logs(e1)
        pass    
            
        

    #MzOthers
    try:        
        if(name_dir == 'mzothers'):
            save_location2 = os.getcwd() + '//ETL//Desktop//Windows//Mzothers'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location2,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(mzothers_search,name_dir)):
            save_location2 = os.getcwd() + '//ETL//Desktop//Windows//Mzothers'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location2,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e2:
        my_packages.logstest.error_logs(e2)
        pass
        
        


    #x32
    #DLL
    try:        
        if(name_dir == 'dll32'):
            save_location3 = os.getcwd() + '//ETL//Desktop//Windows//x32//DLL'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location3,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(dll32_search,name_dir)):
            save_location3 = os.getcwd() + '//ETL//Desktop//Windows//x32//DLL'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location3,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e3:
        my_packages.logstest.error_logs(e3)
        pass
        
        

    #EXE
    try:        
        if(name_dir =='exe32'):
            save_location4 = os.getcwd() + '//ETL//Desktop//Windows//x32//EXE'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location4,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(exe32_search,name_dir)):
            save_location4 = os.getcwd() + '//ETL//Desktop//Windows//x32//EXE'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location4,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e4:
        my_packages.logstest.error_logs(e4)
        pass    
        

    #SYS
    try:        
        if(name_dir == 'sys32'):
            save_location5 = os.getcwd() + '//ETL//Desktop//Windows//x32//SYS'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location5,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(sys32_search,name_dir)):
            save_location5 = os.getcwd() + '//ETL//Desktop//Windows//x32//SYS'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location5,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e5:
        my_packages.logstest.error_logs(e5)
        pass
                

    #x64
    #DLL
    try:        
        if(name_dir == 'dll64'):
            save_location6 = os.getcwd() + '//ETL//Desktop//Windows//x64//DLL'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location6,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(dll64_search,name_dir)):
            save_location6 = os.getcwd() + '//ETL//Desktop//Windows//x64//DLL'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location6,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e6:
        my_packages.logstest.error_logs(e6)
        pass
        
        

    #EXE
    try:        
        if(name_dir == 'exe64'):
            save_location7 =os.getcwd() + '//ETL//Desktop//Windows//x64//EXE'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location7,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(exe64_search,name_dir)):
            save_location7 =os.getcwd() + '//ETL//Desktop//Windows//x64//EXE'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location7,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e7:
        my_packages.logstest.error_logs(e7)
        pass
        
        

    #SYS
    try:        
        if(name_dir == 'sys64'):
            save_location8 =os.getcwd() + '//ETL//Desktop//Windows//x64//SYS'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location8,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(sys64_search,name_dir)):
            save_location8 =os.getcwd() + '//ETL//Desktop//Windows//x64//SYS'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location8,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e8:
        my_packages.logstest.error_logs(e8)
        pass
        
    #Archives
    try:        
        if(name_dir == 'archive'):
            save_location9 =os.getcwd() + '//ETL//Desktop//Others//Archives'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location9,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(archive_search,name_dir) or re.match(archives_search,name_dir)):
            save_location9 =os.getcwd() + '//ETL//Desktop//Others//Archives'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location9,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e9:
        my_packages.logstest.error_logs(e9)
        pass
        

    #Common
    #PDF
    try:        
        if(name_dir == 'pdf'):
            save_location10 =os.getcwd() + '//ETL//Common//PDF'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location10,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(pdf_search,name_dir)):
            save_location10 =os.getcwd() + '//ETL//Common//PDF'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location10,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e10:
        my_packages.logstest.error_logs(e10)
        pass
        
        

    #Java
    try:            
        if(name_dir == 'java'):
            save_location11 =os.getcwd() + '//ETL//Desktop//Java'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location11,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(java_search,name_dir)):
            save_location11 =os.getcwd() + '//ETL//Desktop//Java'
            my_packages.copyfoldertestos.copy_folder_desktop(save_location11,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e11:
        my_packages.logstest.error_logs(e11)
        pass
        

    #Mac
    #Macdmg
    try:        
        if(name_dir == 'macdmg'):
            if(zip_filename.split('_')[0] == "OpenAVN"):
                save_location12 =os.getcwd() + '//ETL//Desktop//Mac//MacDMG'
                my_packages.copyfoldertestos.copy_folder_desktop(save_location12,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)
            elif(zip_filename.split('_')[0] == "Android"):
                save_location13 =os.getcwd() + '//ETL//Desktop//Mac//A_MacDMG'
                my_packages.copyfoldertestos.copy_folder_mobile(save_location13,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)
        elif(re.match(macdmg_search,name_dir)):
            if(zip_filename.split('_')[0] == "OpenAVN"):
                save_location12 =os.getcwd() + '//ETL//Desktop//Mac//MacDMG'
                my_packages.copyfoldertestos.copy_folder_desktop(save_location12,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)
            elif(zip_filename.split('_')[0] == "Android"):
                save_location13 =os.getcwd() + '//ETL//Desktop//Mac//A_MacDMG'
                my_packages.copyfoldertestos.copy_folder_mobile(save_location13,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)
    except Exception as e13:
        my_packages.logstest.error_logs(e13)
        pass
        
        

    #Others
    try:        
        if(name_dir == 'others'):
            if(zip_filename.split('_')[0] == "OpenAVN"):
                save_location14 =os.getcwd() + '//ETL//Desktop//Others//Other'
                my_packages.copyfoldertestos.copy_folder_desktop(save_location14,path_dir,name_dir,zip_filename)    
                add_item.pop(index_of_item)         
            elif(zip_filename.split('_')[0] == "Android"):
                save_location15 =os.getcwd() + '//ETL//Mobile//Others//Others'
                my_packages.copyfoldertestos.copy_folder_mobile(save_location15,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)
        elif(re.match(others_search,name_dir)):
            if(zip_filename.split('_')[0] == "OpenAVN"):
                save_location14 =os.getcwd() + '//ETL//Desktop//Others//Other'
                my_packages.copyfoldertestos.copy_folder_desktop(save_location14,path_dir,name_dir,zip_filename)    
                add_item.pop(index_of_item)         
            elif(zip_filename.split('_')[0] == "Android"):
                save_location15 =os.getcwd() + '//ETL//Mobile//Others//Others'
                my_packages.copyfoldertestos.copy_folder_mobile(save_location15,path_dir,name_dir,zip_filename)
                add_item.pop(index_of_item)             
    except Exception as e15:
        my_packages.logstest.error_logs(e15)
        pass
        
        
    
    #Android
    #APK
    try:        
        if(name_dir == 'apk'):
            save_location16 =os.getcwd() + '//ETL//Mobile//Android//APK'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location16,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif(re.match(apk_search,name_dir)):
            save_location16 =os.getcwd() + '//ETL//Mobile//Android//APK'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location16,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)         
    except Exception as e16:
        my_packages.logstest.error_logs(e16)
        pass
        

    #DEX
    try:        
        if(name_dir == 'dex'):
            save_location17 =os.getcwd() + '//ETL//Mobile//Android//DEX'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location17,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(dex_search,name_dir)):
            save_location17 =os.getcwd() + '//ETL//Mobile//Android//DEX'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location17,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e17:
        my_packages.logstest.error_logs(e17)
        pass
        
        

    #ELF
    try:        
        if(name_dir == 'elf'):
            save_location18 =os.getcwd() + '//ETL//Mobile//Android//ELF'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location18,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(a_elf_search,name_dir)):
            save_location18 =os.getcwd() + '//ETL//Mobile//Android//ELF'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location18,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e18:
        my_packages.logstest.error_logs(e18)
        pass
        
        

    #MetaData
    try:        
        if(name_dir == 'metadata'):
            save_location19 =os.getcwd() + '//ETL//Mobile//Android//MetaData'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location19,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
        elif (re.match(metadata_search,name_dir)):
            save_location19 =os.getcwd() + '//ETL//Mobile//Android//MetaData'
            my_packages.copyfoldertestos.copy_folder_mobile(save_location19,path_dir,name_dir,zip_filename)
            add_item.pop(index_of_item)
    except Exception as e19:
        my_packages.logstest.error_logs(e19)
        pass

def move_unknown_folder(file_name,unknown_path_dir,add_item,index_of_item1):
    samples_search = "[S-s]+[A-a]+[M-m]+[P-p]+[L-l]+[E-e]+[S-s]+$"
    st_search = "[S-s]+[T-t]+2+[1-2]+$"
    st_not_match = re.search(st_search,file_name)
    sample_not_match = re.search(samples_search,file_name)
    try:
        if(st_not_match or sample_not_match):
            add_item.pop(index_of_item1)            
        else:
            save_location =os.getcwd() + '//ETL//Others'
            my_packages.copyfoldertest.unknown_folder(file_name,save_location,unknown_path_dir)
            add_item.pop(index_of_item1)    
                    
    except Exception as e:
        my_packages.logstest.error_logs(e)
        pass

