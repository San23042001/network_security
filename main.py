import sys
from src.exception import NetworkSecurityException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig



if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")

        data_ignestion_artifacts = data_ingestion.initiate_data_ingestion()
        print(data_ignestion_artifacts)
    
    except Exception as e:
        logging.error("Enter the catch block")
        raise NetworkSecurityException(e,sys)