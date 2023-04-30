import os
import shutil

# Get the current working directory
cwd = os.getcwd()

vanilla_banks_dir = ""

metafiles = []

for root, dirs, files in os.walk(cwd):
    for filename in files: 
        if filename == "0a.bankmeta":
            vanilla_banks_dir = root
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

assert vanilla_banks_dir, "Can't find vanilla banks"

# Look for directories that match the pattern "data\Music"
for root, filename in metafiles:
    if filename.endswith(".meta"):
        meta_file_location = os.path.join(root, filename)
        seq_file_location = meta_file_location.replace(".meta", ".seq")
        folder_path = meta_file_location.replace(".meta", "")
            
        if not os.path.isfile(seq_file_location):
            print(f"{meta_file_location} does not have an associated .seq file - Please check spelling")
            continue
                
        bank = ""
        with open(meta_file_location, "r") as file:
            bank = hex(int(file.readlines()[1].strip(), 16))[2:]
                
        if len(bank) == 1:
            bank = "0" + bank
            
        zbank_file = os.path.join(vanilla_banks_dir, bank + ".zbank")
        bankmeta_file = os.path.join(vanilla_banks_dir, bank + ".bankmeta")
        
        assert os.path.exists(zbank_file)
        assert os.path.exists(bankmeta_file)
            
        os.makedirs(folder_path)
            
        shutil.move(meta_file_location, os.path.join(folder_path, filename))
        shutil.move(seq_file_location, os.path.join(folder_path, filename.replace(".meta", ".seq")))
        shutil.copy(zbank_file, os.path.join(folder_path, bank + ".zbank"))
        shutil.copy(bankmeta_file, os.path.join(folder_path, bank + ".bankmeta"))
        
        shutil.make_archive(folder_path, 'zip', folder_path)
        
        os.rename(folder_path + ".zip", folder_path + ".ootrs")
        
        shutil.rmtree(folder_path)