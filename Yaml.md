# Yamlの書き方のTips

- リテラルブロック記法

    - YAML形式で複数行の文字列を表現するための記法．
    
    - 改行や空白、インデントがそのまま保存されるため、スクリプトや設定値などの複数行にわたるデータを正確に表現可能．

    ```
    command: ["bash", "-c"]
    args:
    - |
      apt update &&
      apt install -y curl &&
      curl -s http://example.com/script.sh | bash
    ```
    ```
    command:
    - bash
    - -c
    - |
      apt update &&
      apt install -y curl &&
      curl -s http://example.com/script.sh | bash

    ```