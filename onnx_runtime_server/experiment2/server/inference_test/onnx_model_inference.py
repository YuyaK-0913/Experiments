import onnxruntime as rt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from joblib import load
from matplotlib import pyplot as plt

# load digits dataset
digits = load_digits()
X, y = digits.data, digits.target  # Our train data shape is (x, 64) where x is total samples
X_train, X_test, y_train, y_test = train_test_split(X, y)

# onnx model inference
filepath = '../models/elasticnet.onnx'

sess = rt.InferenceSession(filepath)
inp, out = sess.get_inputs()[0], sess.get_outputs()[0]
print(f"input name='{inp.name}' shape={inp.shape} type={inp.type}")
print(f"output name='{out.name}' shape={out.shape} type={out.type}")
# input name='float_input' shape=[None, 64] type=tensor(float)
# output name='variable' shape=[None, 1] type=tensor(float)

pred_onx = sess.run([out.name], {inp.name: X_test.astype(np.float32)})[0]
print(y_test.shape)
print(pred_onx.shape)

# joblib model inference
filepath = '../models/elasticnet.joblib'
model = load(filepath)
pred_joblib = model.predict(X_test)
print(pred_joblib.shape)

plt.figure(figsize=(5, 5))
plt.plot(pred_onx, pred_joblib, 'ro')
plt.title('ElasticNet inference (ONNX vs Joblib)') 
plt.xlabel('ONNX')
plt.ylabel('Joblib')
plt.savefig('./elasticnet.png')