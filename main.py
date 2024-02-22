import os 
import shutil

file_name = input("Enter the nomenclature you want to search:\n")

folder_path = input("Enter the name of the directory/folder you want to organize:\n")  
if os.path.exists(folder_path):
    print(f"Ordering...")
else:
    print(f"The folder path'{folder_path}' does not exists.")
                
final_folder = input("Enter the path to the folder where things will be stored\n")
if os.path.exists(final_folder):
    print(f"Ordering...")
else:
    print(f"The folder path'{final_folder}' does not exists.")


def move_files(origing_folder,final_folder, name):
    files  = os.listdir(origing_folder)
    for fil in files:
        path_file = os.path.join(origing_folder, fil)
        if name in fil:
            shutil.move(path_file, final_folder)

move_files(folder_path,final_folder,file_name )

print("The folder has been organized.")
