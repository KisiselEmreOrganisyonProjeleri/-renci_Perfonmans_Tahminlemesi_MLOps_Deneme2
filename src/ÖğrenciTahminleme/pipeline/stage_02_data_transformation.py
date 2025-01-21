from src.ÖğrenciTahminleme.config.configration import ConfigurationManager
from src.ÖğrenciTahminleme.components.data_transformation import DataTransfrom
from src.ÖğrenciTahminleme import logger
from src.ÖğrenciTahminleme.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data Transformation stage"  # Aşama ismi

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Veri alım konfigürasyonunu al
        data_transformation_config = config.get_data_transformation_config
        # DataIngestion sınıfını başlat
        data_transformation = DataTransfrom(config=data_transformation_config)
        obj = DataIngestionTrainingPipeline()  # Pipeline nesnesini oluştur
        train_data,test_data = obj.main()
        train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)
        return train_arr, test_arr

