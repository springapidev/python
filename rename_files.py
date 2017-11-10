import os
def rename_files():

#(1)get file names from a folder prank
    file_list=os.listdir(r"E:\python\python\prank")
    #print(file_list)
    saved_path=os.getcwd()
    print("current working directory is "+saved_path)
    os.chdir(r"E:\python\python\prank")
#(2)For each file- Rename filename
    for file_name in file_list:
        print("Old Name "+file_name)
        print("New File Name "+file_name.translate(str.maketrans('','','1234567890')))
        os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))
    os.chdir(saved_path)
        
rename_files()
