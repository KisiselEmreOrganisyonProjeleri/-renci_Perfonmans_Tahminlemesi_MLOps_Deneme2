from src.ÖğrenciTahminleme import logger
from src.ÖğrenciTahminleme.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ÖğrenciTahminleme.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from src.ÖğrenciTahminleme.pipeline.stage_03_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME1 = 'data_ingestion'
STAGE_NAME2 = 'data_transformation'
STAGE_NAME3 = 'model_trainer'

if __name__ == '__main__':
    try:
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME1} started <<<<<<")
        obj = DataIngestionTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat
    
    try:
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME2} started <<<<<<")
        obj = DataTransformationTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME2} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat
    
    try:
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME3} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME3} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat
    
