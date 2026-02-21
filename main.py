import sys
from src.exception import NetworkSecurityException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig



if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")

        data_ignestion_artifacts = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiaton Completed")
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ignestion_artifacts,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('Data Validation Compelted')

        logging.info("Initiate the data transformation")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info('Data Transformation Compelted')
        


    
    except Exception as e:
        logging.error("Enter the catch block")
        raise NetworkSecurityException(e,sys)