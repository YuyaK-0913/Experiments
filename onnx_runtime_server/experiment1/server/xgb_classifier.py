import os
import pickle
import numpy as np
import pandas as pd
from typing import Dict, List

import onnx
from onnxmltools.convert import convert_xgboost
from onnxmltools.convert.common import data_types

import xgboost as xgb

from logging import getLogger

logger = getLogger(__name__)

XGB_DEFAULT_PARAMS = {
    'max_depth': 3,
    'booster': 'dart',
    'eta': 0.3,
    'silent': 1,
    'n_estimators': 100,
    'num_class': 10
}

class XGBoostModel:
    def __init__(self, params=XGB_DEFAULT_PARAMS):
        
        self.params: Dict = XGB_DEFAULT_PARAMS
        self.model = None

        self.reset_model()

    def reset_model(self):
        self.model = xgb.XGBClassifier(**self.params)
        logger.info(f'initialized model: {self.model}')

    def train(
            self,
            X_train: np.ndarray | pd.DataFrame, 
            y_train: np.ndarray | pd.DataFrame,
            ):
        logger.info(f'start train for model: {self.model}')

        self.model.fit(X_train, y_train)
        

    def predict(
            self,
            x: np.ndarray | pd.DataFrame,
            ) -> np.ndarray:
        logger.info(f'start predict: {self.model}')

        predictions = self.model.predict(x)
        return predictions
    
    def save(
        self,
        filepath: str,
    ) -> str:
        logger.info(f'save model: {filepath}')

        file, ext = os.path.splitext(filepath)
        if ext != '.json':
            filepath = f'{file}.json'
        
        self.model.save_model(filepath)
    
    def save_as_onnx(self, filepath: str):
        logger.info(f'save model as onnx: {filepath}')

        file, ext = os.path.splitext(filepath)
        if ext != '.onnx':
            filepath = f'{file}.onnx'
        
        initial_type = [('float_input', data_types.FloatTensorType([1, 64]))]
        onnx_model = convert_xgboost(self.model, initial_types=initial_type, doc_string='Input size is (x, 64)')
        
        onnx.save(onnx_model, filepath)


# デバック用
if __name__ == '__main__':
    
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    
    digits = load_digits()
    X, y = digits.data, digits.target  # Our train data shape is (x, 64) where x is total samples
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    model = XGBoostModel()
    model.train(X_train, y_train)
    model.predict(X_test)
    model.save_as_onnx('./model/xgboost.onnx')