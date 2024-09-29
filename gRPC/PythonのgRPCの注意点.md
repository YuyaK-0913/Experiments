# PythonのgRPCの注意点

- **事象**

    - 生成されたコードをそのまま実行すると，下記のようなエラーがでる．

    ```
    Traceback (most recent call last):
  File "/app/client.py", line 3, in <module>
    import proto.helloworld_pb2_grpc as helloworld_pb2_grpc
  File "/app/proto/helloworld_pb2_grpc.py", line 6, in <module>
    import helloworld_pb2 as helloworld__pb2
  ModuleNotFoundError: No module named 'helloworld_pb2'
    ```

- **原因**

  - 生成されたコードの相対パスが通っていない（もしくは，間違っている）よう．

  - なぜ．．．

- **対処法**

  - protoディレクトリの__init__.pyに下記を記載してパスを通す．
  ```
  import sys
  from pathlib import Path

  sys.path.append(str(Path(__file__).parent))
  ```
  - sys.pathはPythonがモジュールを検索する際に参照するディレクトリのリスト

  - このコードは、現在の__init__.pyファイルが存在するディレクトリ（つまり、パッケージのルートディレクトリ）をsys.pathに追加している．