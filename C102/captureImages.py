from operator import truediv
from tkinter import Frame
from tracemalloc import start
import cv2
import dropbox
import time
import random

start_time=time.time()

def capture_Image():
    
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        
        image_name='img'+str(number)+'.png'
        cv2.iamwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print('Snapshot Taken!!')
    
    #releases the camera
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_File(image_name):
    assess_token='sl.BFRRW-i5PlgbZeOwXq2ZBizbavI3NzcmfMxa9l8KgH4-HtfiUC1xNNkiM5ngHepqkvObeGKPgJGRp7WVghVzY9I7MGx9KFlpHlANSTNU4BPCZJG7XVZEPLBA_jmea41l8ptuOxvv_7Sl'
    file=image_name
    file_from=file
    file_to='/testFolder/'+(image_name)
    dbx=dropbox.Dropbox(assess_token)
    
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded!!')
        
        
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=capture_Image()
            upload_File(name)
            
main()