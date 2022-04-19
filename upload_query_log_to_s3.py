import os
import shutil
from time import gmtime, strftime

LOG_FILE_SIZE = 2  # gb
MAX_FILE_SIZE_LIMIT_IN_GB = 1024 * 1024 * 1024  # max file size 2GB
FILE_LOCATION = ''  # Add query log file location here


def get_file_size():
    return os.path.getsize(FILE_LOCATION) // MAX_FILE_SIZE_LIMIT_IN_GB


def delete_file():
    os.remove(FILE_LOCATION)


def move_file():
    filename = f'{FILE_LOCATION}.{strftime("%Y-%m-%d-%H:%M:%S", gmtime())}'
    shutil.move(FILE_LOCATION, filename)
    return filename


def upload_file_to_s3():
    try:
        filename = move_file()
        cmd = f"aws s3 cp {filename} s3://bwrap/"
        os.system(cmd)
        print('file uploaded to s3 successfully')
        return True
    except FileNotFoundError or IOError:
        return False


if __name__ == "__main__":
    # if file size exceeds 2 GB then first upload file to s3 and then delete it
    if get_file_size() >= LOG_FILE_SIZE: # comparison in GB
        if upload_file_to_s3():
            delete_file()
            print('file deleted from log folder')
    else:
        print('nothing to upload or delete')
