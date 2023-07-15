## Feeding the data - 1st step of the pipeline 
import os
import sys
print(sys.path)
from src.logger import logging
from src.exception import CustomException 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # explore dataclass

from src.components.data_transformation import DataTransformation

## Initialize the Data Ingetion Configuration (create data for training and testing)
 ## This module provides a decorator and functions for automatically adding generated special methods such as __init__() and __repr__() to user-defined classes

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str  = os.path.join('artifacts','raw.csv')

## Create a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion starts - Creation of training and testing data')
        try:
            df = pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index =False,header=True)


            logging.info('Data ingestion is completed ')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        

'''
if __name__ == '__main__':
    obj=DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    data_transformation_obj = DataTransformation()
    train_arr,test_arr,_= data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)

'''