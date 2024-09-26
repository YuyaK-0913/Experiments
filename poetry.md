### poetryの使い方

1. **初期化**
    ```bash
    poetry init
    ```
    もしくは
    ```bash
    poetry new
    ```

2. **パッケージの追加**
    ```bash
    poetry add <package>
    ```
    
3. **requirement.txtのエクスポート**
    ```bash
    poetry export -f requirements.txt -o requirements.txt --without-hashes
    
    poetry export -f requirements.txt -o requirements.txt --without-hashes --without-annotations
    ```
