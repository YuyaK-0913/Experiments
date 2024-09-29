# docker composeのログ

-f オプション:
"follow" の略で、リアルタイムでログを追跡することができる

- 全サービスのログを表示
    ```
    docker compose logs -f
    ```

- 特定のサービスのログのみを表示
    ```
    docker compose logs -f service_name
    ```

- 最後のN行のログから表示を開始：
    ```
    docker compose logs -f --tail=100
    ```