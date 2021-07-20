import os
import csv
import time

class data_sheet:
    def __init__(self):
        self.fname = ""
        self.dir = "data/"
        self.row = ""
        # make file
        self.check_dir()
        self.createCSV()

    # check directory
    def check_dir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    # daily schedule
    def createCSV(self):
        # make new file
        self.fname = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".csv"
        # file check
        fpath = self.dir + self.fname
        if not os.path.exists(fpath):
            f = open(fpath, 'w', encoding='utf-8') # create 
            f.close()
    
    # every minute schedule
    def wirteCSV(self):
        csv_path = os.path.join(self.dir, self.fname)
        if os.path.exists(csv_path):
            f = open(csv_path, 'a', encoding='utf-8', newline='')
            w = csv.writer(f)
            w.writerow(self.row)
            f.close()
        else:
            self.createCSV()
