import csv
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from pathlib import Path
import os
from datetime import date



class datasetGeneration:


    def CreateDataSet(file_name):
        headerList = ['ID','date','price', 'location', 'number_of_bedrooms','number_of_bathrooms', 'dimension', 'floor']
    
        with open(file_name, 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=headerList)
            dw.writeheader()
    
    
    def GenerateDataset(dict_result):
        file_name = "dataset.csv" 
        path = Path(file_name)
        if (path.is_file() == False):
            datasetGeneration.CreateDataSet(file_name)
        else:
            with open(file_name, 'rb') as f:
                try:  # catch OSError in case of a one line file 
                    f.seek(-2, os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                except OSError:
                    f.seek(0)
                last_line = f.readline().decode()
                last_ID = last_line.split(',')[0]
        today = date.today()
        dict_result['ID'] = int(last_ID)+1
        dict_result['date'] = today
        df = pd.DataFrame()
        df = df.append(dict_result,ignore_index=True)
        df.to_csv(file_name,mode='a',index=False,header=False)
    

file_name = "dataset.csv"
