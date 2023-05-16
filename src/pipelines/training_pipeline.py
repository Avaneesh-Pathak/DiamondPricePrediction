import os
import sys
sys.path.append('D:\Diamond Price Prediction\src')

from src.logger import logging

from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion, DataIngestionconfig
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj = DataIngestion()
    returned_value = obj.initiate_data_ingestion()
    
    if returned_value is not None:
        train_data_path, test_data_path = returned_value  # Unpack the returned value
        print("Data ingestion successful.")
        print("Train data path:", train_data_path)
        print("Test data path:", test_data_path)
    else:
        # Handle the case when returned_value is None
        print("Error: Data ingestion failed. Check the logs for more information.")
        sys.exit(1)
        
    data_transformation=DataTransformation()
    train__arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train__arr,test_arr)