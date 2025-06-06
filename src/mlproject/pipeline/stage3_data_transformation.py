from mlproject.config.config import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path





class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                train,test = data_transformation.train_test_spliting()
                train_processed, test_processed = data_transformation.preprocess_features(train, test)

            else:
                raise Exception("You data schema is not valid")



