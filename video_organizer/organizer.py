#!/usr/bin/python

#####################################
# video organizer:                  #
# Gathers the video files generated #
# by the motion daemon into folders #
# organized by date and time.       #
# Note the files of interest        #
# have a consistent naming          # 
# convention                        #        
#                                   #
# 2019-07-10                        #
#####################################

import os
import time
from os import path
from datetime import datetime

# Videos folder #
video_dir = '/videos/'

# File name format #
fmt = '%Y%m%d%H%M%S'

def valid_format(fname):
   """ 
   Validate that the correct
   date format is given in
   the filename    
   """
   try:
      datetime.strptime(fname, fmt)
      return True
   except ValueError:
      return False

def name_new_file(dir_, f):
   """
   Generate full path for
   file placement 
   """
   return os.path.join(dir_, f)

def get_date_pfx(f):
   """
   Get date prefix 
   for new file   
   """
   return f.split("-")[1][:14]

def get_datedir(date_, dir_):
   """
   Generate base path for
   file placement 
   """
   base = "Videos_" + date_[:8]
   return os.path.join(dir_, base)

def scan_directory(dir_):
   """
   Disperse any new files 
   into a new directory 
   with yyyymmdd
   """
   for root, dirs, fname in os.walk(dir_):
       for f in fname:
          try:
             path_ = os.path.join(dir_, f)
             date_ = get_date_pfx(f)
             if valid_format(date_):
                new = get_datedir(date_, dir_)
                if not os.path.exists(new):
                   os.makedirs(new)
                if os.path.exists(path_):
                   os.rename(path_, name_new_file(new, f))
          except Exception as ex:
             print str(ex)
             continue

def organize_videos():
   """ 
   Main function
   """
   while True:
      home = "/home/webcam-share"
      scan_directory(home + video_dir)
      time.sleep(5)

# run #
if __name__ == '__main__':
   organize_videos()
