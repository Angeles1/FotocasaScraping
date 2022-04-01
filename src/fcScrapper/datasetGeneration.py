import csv
import pandas as pd
from pathlib import Path



class GenerateDataset:


    def CreateDataSet(file_name):
        headerList = ['price', 'location', 'number_of_bedrooms', 'dimension', 'floor']
    
        with open(file_name, 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=headerList)
            dw.writeheader()
    
    
    def GenerateDataset(dict_result):
        file_name = "dataset.csv" 
        path = Path(file_name)
        if (path.is_file() == False):
            GenerateDataset.CreateDataSet(file_name)
        df = pd.DataFrame()
        df = df.append(dict_result,ignore_index=True)
        df.to_csv(file_name,mode='a',index=False,header=False)
    

file_name = "dataset.csv"
