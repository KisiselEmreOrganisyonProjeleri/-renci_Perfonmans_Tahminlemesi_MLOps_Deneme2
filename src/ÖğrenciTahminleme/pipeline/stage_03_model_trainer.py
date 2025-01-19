from src.ÖğrenciTahminleme.config.configration import ConfigurationManager
from src.ÖğrenciTahminleme.components.model_trainer import ModelTrainer
from src.ÖğrenciTahminleme.components.data_transformation import DataTransfrom

from src.ÖğrenciTahminleme import logger

STAGE_NAME = "Model Trainer stage"  # Aşama ismi

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Veri alım konfigürasyonunu al
        model_trainer_config = config.get_model_trainer_config

        config = ConfigurationManager()
        # Veri alım konfigürasyonunu al
        data_transformation_config = config.get_data_transformation_config
        # DataIngestion sınıfını başlat
        data_transformation = DataTransfrom(config=data_transformation_config)
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation()
        # DataIngestion sınıfını başlat
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.initiate_model_trainer(train_array=train_arr, test_array=test_arr)