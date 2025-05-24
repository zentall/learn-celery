
- Redisコンテナの起動
```bash
docker compose up
```

- celeryワーカーの起動
```bash
celery -A proj worker --loglevel=INFO
```

- Django開発サーバーを起動
```
python manage.py runserver
```

- localhostにアクセス
```bash
$ curl http://localhost:8000/polls/
Email has been sent. [id=dd70642d-5972-4e66-98ad-97308ae7fa37]
```

- celery workerの出力
```bash
$ celery -A proj worker --loglevel=INFO

...

[tasks]
  . polls.tasks.send_email

[2025-05-24 02:59:16,025: INFO/MainProcess] Connected to redis://localhost:6379//
[2025-05-24 02:59:16,028: INFO/MainProcess] mingle: searching for neighbors
[2025-05-24 02:59:17,037: INFO/MainProcess] mingle: all alone
[2025-05-24 02:59:17,048: INFO/MainProcess] celery@DESKTOP-GKP7SRQ ready.
[2025-05-24 02:59:21,164: INFO/MainProcess] Task polls.tasks.send_email[dd70642d-5972-4e66-98ad-97308ae7fa37] received
[2025-05-24 02:59:21,165: WARNING/ForkPoolWorker-6] sending email...
[2025-05-24 02:59:21,165: WARNING/ForkPoolWorker-6] [0] working...
[2025-05-24 02:59:22,165: WARNING/ForkPoolWorker-6] [1] working...
[2025-05-24 02:59:23,166: WARNING/ForkPoolWorker-6] [2] working...
[2025-05-24 02:59:24,166: WARNING/ForkPoolWorker-6] done! user_id=123
[2025-05-24 02:59:24,171: INFO/ForkPoolWorker-6] Task polls.tasks.send_email[dd70642d-5972-4e66-98ad-97308ae7fa37] succeeded in 3.0063411000000997s: 123

```

- flowerで確認
```bash
celery -A proj worker --loglevel=INFO
```

- スケジュール実行
```bash
celery -A proj beat --loglevel=INFO
```