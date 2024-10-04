import numpy as np
import base64

# 1行64列のランダムなfloat32データを生成
data = np.random.rand(1, 64).astype(np.float32)

# バイナリデータをBase64エンコード
encoded_data = base64.b64encode(data.tobytes()).decode()
print(encoded_data)
