import os
import shutil

# Get the current working directory
cwd = os.getcwd()

metafiles = []

for root, dirs, files in os.walk(cwd):
    for filename in files: 
        if filename.endswith(".meta"):
            metafiles.append((root, filename))
            
            meta_file_location = os.path.join(root, filename)
            folder_path = meta_file_location.replace(".meta", "")
            zip_path = meta_file_location.replace(".meta", ".zip")
            ootrs_path = meta_file_location.replace(".meta", ".ootrs")
            
            for thing_to_remove in [folder_path, zip_path, ootrs_path]:
                if os.path.exists(thing_to_remove):
                    if os.path.isfile(thing_to_remove):
                        os.remove(thing_to_remove)
                    else:
                        shutil.rmtree(thing_to_remove)

# Look for directories that match the pattern "data\Music"
for root, filename in metafiles:
    if filename.endswith(".meta"):
        meta_file_location = os.path.join(root, filename)
        seq_file_location = meta_file_location.replace(".meta", ".seq")
        folder_path = meta_file_location.replace(".meta", "")
            
        if not os.path.isfile(seq_file_location):
            print(f"{meta_file_location} does not have an associated .seq file - Please check spelling")
            continue
                
        os.makedirs(folder_path)
            
        shutil.move(meta_file_location, os.path.join(folder_path, filename))
        shutil.move(seq_file_location, os.path.join(folder_path, filename.replace(".meta", ".seq")))
        
        shutil.make_archive(folder_path, 'zip', folder_path)
        
        os.rename(folder_path + ".zip", folder_path + ".ootrs")
        
        shutil.rmtree(folder_path)