from django.db import models
import datetime
import os
from django.db import models

def getFileName(request,filename):
    original_filename = filename
    now_time=datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,original_filename)
    return os.path.join('uploads/',new_filename)


