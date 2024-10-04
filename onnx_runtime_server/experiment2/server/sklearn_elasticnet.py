import os
import logging
from typing import Dict

import numpy as np
import pandas as pd

from sklearn.linear_model import ElasticNet
import joblib

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnx

logger = logging.getLogger(__name__)

ELASTICNET_DEFAULT_PARAMS = {
    'alpha': 0.5,
    'l1_ratio': 0.5,
}

class ElasticNetRegression:
    def __init__(self, params=ELASTICNET_DEFAULT_PARAMS):
        self.params: Dict = params
        self.model = None

        self.reset_model()

    def reset_model(self):
        self.model = ElasticNet(**self.params)
        logger.info(f'initialized model: {self.model}')

    def train(
            self,
            X_train: np.ndarray | pd.DataFrame,
            y_train: np.ndarray | pd.DataFrame,
            ):
        logger.info(f'start training model: {self.model}')

        self.model.fit(X_train, y_train)

    def predict(
            self,
            x: np.ndarray | pd.DataFrame,
            ) -> np.ndarray:
        logger.info(f'start prediction with model: {self.model}')

        predictions = self.model.predict(x)
        return predictions

    def save(
        self,
        filepath: str,
    ) -> str:
        logger.info(f'saving model to: {filepath}')

        file, ext = os.path.splitext(filepath)
        if ext != '.joblib':
            filepath = f'{file}.joblib'

        joblib.dump(self.model, filepath)
        return filepath

    def save_as_onnx(self, filepath: str, input_shape: int):
        logger.info(f'saving model as onnx: {filepath}')

        file, ext = os.path.splitext(filepath)
        if ext != '.onnx':
            filepath = f'{file}.onnx'

        initial_type = [('float_input', FloatTensorType([None, input_shape]))]
        onnx_model = convert_sklearn(self.model, initial_types=initial_type)

        onnx.save_model(onnx_model, filepath)


def main():

    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    
    digits = load_digits()
    X, y = digits.data, digits.target  # Our train data shape is (x, 64) where x is total samples
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    model = ElasticNetRegression()
    model.train(X_train, y_train)
    model.predict(X_test)

    model_directory = "./models/"
    os.makedirs(model_directory, exist_ok=True)

    filepath = './models/elasticnet.onnx'
    input_shape = X_train.shape[1]
    model.save_as_onnx(filepath, input_shape)

    model.save('./models/elasticnet.joblib')


if __name__ == '__main__':
    main()