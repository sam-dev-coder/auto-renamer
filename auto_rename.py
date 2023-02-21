import os

# Set the parent directory where all the folders are located
parent_dir = 'Project\Data\LabelNo_json'

# Loop through all the folders in the parent directory
for folder_name in os.listdir(parent_dir):
    folder_path = os.path.join(parent_dir, folder_name)
    
    # Check if the item in the current iteration is a directory
    if os.path.isdir(folder_path):
        # Get the folder name without the '_json' suffix
        folder_name_without_suffix = folder_name.replace('_json', '')
        
        # Iterate over the files in the current directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if the file is named 'img' or 'label'
            if filename == 'label.png':
                # Split the filename into the base name and extension
                base_name, ext = os.path.splitext(filename)
                
                # Rename the file to the name of the parent folder, preserving the extension
                new_name = f"{folder_name_without_suffix}_l.png"
                os.rename(file_path, os.path.join(folder_path, new_name))
