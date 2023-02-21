import os
import shutil

# Set the parent directory where all the subfolders are located
parent_dir = 'Project\Data\LabelNo_json'
# Set the destination directory where the renamed files will be moved to
dest_dir = 'Project\Data\Label'

# Loop through all the subfolders in the parent directory
for folder_name in os.listdir(parent_dir):
    folder_path = os.path.join(parent_dir, folder_name)
    
    # Check if the item in the current iteration is a directory
    if os.path.isdir(folder_path):
        # Iterate over the files in the current directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if the file is named '*_i.png'
            if filename.endswith('_l.png'):
                # Move the file to the destination directory
                shutil.move(file_path, os.path.join(dest_dir, filename))
