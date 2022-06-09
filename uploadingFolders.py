import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        #Using os.walk() get the file name and path from the given path.Using os.walk() get the file name and path from the given path.
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                #Using os.path.relpath() and os.path.join() create a path to dropbox.
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path) 

                #rb = read mode - binary mode
                with open(local_path, 'rb') as f:
                    # files upload method is used to upload the file to the cloud destination
                    dbx.files_upload(f.read(), dropbox_path)

def main():
    access_token = 'sl.BIw_UKUca0QLKddGY4UrHEzxRcuiWZL4D8xXMML557FLhxv1bUsgw-Uln_2z2D49lyAHhfIsQBsH9ABeJDXNZxCiaa4unkU-aafM_cVqZ5lgtNY1Tacti8qlY6cS8KbzNjtKJe8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to the file: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Your file/s have been moved")

main()