# this basically is the code for data reading 
# along with reading the dataset, we'll alse divide the data into train, test and validation.

# the main aim is to read the dataset from a specific data source.

# the we split the data to train_test and perform the data preprocessing 


import os
import sys
from src.exception import CustomException        ## this has been taken from the local file t make sure we implement our custom exceptions
from src.logger import logging    ## this is a local logger imported from our local file


import pandas as pd
from sklearn.model_selection import train_test_split



# just to check if everything is working alright :

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

## one more very important class : 

from dataclasses import dataclass

## we will also declare a class that can be used to validate whether the data received is raw, processed , data type etc.

@dataclass ## this is a decorator which enables you to define the  class variables without init.

class DataIngestionConfig:
    train_data_path : str = os.path.join("artifacts", "train.csv")  ## train.csv is the training data path
    test_data_path : str = os.path.join("artifacts", "test.csv")  ## test.csv is the training data path
    raw_data_path : str = os.path.join("artifacts", "raw.csv")  ## raw.csv is the raw data


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component ")
        try:
            df = pd.read_csv(r"C:\Users\tmvis\OneDrive\Desktop\udemy jupyter\End to End\notebook\data\StudentsPerformance.csv")
            logging.info("read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True) ##  making the folders and defining the condition that if it exists, dont create
            
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header= True)
            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state= 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header= True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header= True)

            logging.info("Ingestion of the data is completed")


            ## Next you'll return the data path to the next step, which is data transformation
            return(

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ =="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)