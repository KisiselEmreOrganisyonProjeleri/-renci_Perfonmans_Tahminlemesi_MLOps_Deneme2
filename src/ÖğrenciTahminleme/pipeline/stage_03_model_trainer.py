from src.ÖğrenciTahminleme.config.configration import ConfigurationManager
from src.ÖğrenciTahminleme.components.model_trainer import ModelTrainer
from src.ÖğrenciTahminleme.components.data_transformation import DataTransfrom

from src.ÖğrenciTahminleme import logger
from src.ÖğrenciTahminleme.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
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

        obj = DataTransformationTrainingPipeline()
        train_arr, test_arr = obj.main()
        modeltrainer = ModelTrainer()
        modeltrainer.initiate_model_trainer(train_arr,test_arr)