# Postgresの操作

- コンテナに入る
    
    ```docker exec -it postgres psql -U postgres -d mlflow_test```
    
    - ```psql``` はPostgreSQLのコマンドラインインターフェース.
    - ```-U postgres``` はPostgresユーザーでログインするという指定．
    - ```-d mlflow_test``` は、データベース名（ここではmlflow_test）を指定してそのデータベースに接続。

- テーブル一覧の表示

    ```\dt```

- 特定のテーブルスキーマを表示

    ```\dt テーブル名```

- データの表示

    ```SELECT * FROM テーブル名 LIMIT 10;```

- psqlセッションの終了

    ```\q```

