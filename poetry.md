# poetryとpyenvの使い方

1. **初期化**

    ```
    poetry init
    ```

2. **パッケージの追加**
    ```
    poetry add <package>
    ```
    
3. **パッケージのインストール**
    ```
    poetry install
    ```

4. **poetry環境でのpythonの実行**
    - 仮想環境に入らずに実行
    ```
    pyenv versions
    
    pyenv install 3.10.6

    pyenv global 3.10.6

    poetry run python <pythonファイル>
    ```
    
    - 仮想環境に入って実行
    ```
    poetry shell
    ``` 

5. **requirement.txtのエクスポート**
    ```
    poetry export -f requirements.txt -o requirements.txt --without-hashes
    ```


