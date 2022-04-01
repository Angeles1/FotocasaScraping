import csv
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from pathlib import Path



class datasetGeneration:


    def CreateDataSet(file_name):
        headerList = ['ID','price', 'location', 'number_of_bedrooms','number_of_bathrooms', 'dimension', 'floor']
    
        with open(file_name, 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                                fieldnames=headerList)
            dw.writeheader()
    
    
    def GenerateDataset(dict_result):
        file_name = "dataset.csv" 
        path = Path(file_name)
        if (path.is_file() == False):
            datasetGeneration.CreateDataSet(file_name)
        df = pd.DataFrame()
        df = df.append(dict_result,ignore_index=True)
        df.to_csv(file_name,mode='a',index=False,header=False)
    

file_name = "dataset.csv"
