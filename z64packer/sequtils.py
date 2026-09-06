import zipfile
import hashlib
import uuid
import re
from datetime import datetime, UTC

def is_seq(path):
    return path.endswith(".zseq") or path.endswith(".seq") or path.endswith(".aseq")

def get_md5(path):
    with zipfile.ZipFile(path, 'r') as zip:
        seq_name = next((x for x in zip.namelist() if is_seq(x)), None)
        if(seq_name == None): raise Exception("SEQ NOT FOUND IN FILE " + path)
        with zip.open(seq_name) as seq:
            # Make sure to clamp the main volume to zero, to get a consistent hash
            data = bytearray(seq.read())
            for i in range(len(data) - 1):
                if data[i] == 0xDB: data[i + 1] = 0x00
            return hashlib.md5(data).hexdigest()

def get_current_date_string():
    return datetime.now(UTC).isoformat(timespec='milliseconds').replace("+00:00", "Z")

def get_uuid():
    return str(uuid.uuid4())

def get_safe_path(game, song):
    unsafe_characters = r'[\\\/:*?"<>|]'
    remove_trailing_dots = r'\.+$'
    return re.sub(remove_trailing_dots, "", re.sub(unsafe_characters, "", game)) + "/" + re.sub(unsafe_characters, "", song)
