# learn-celery

Celeryの学習用プロジェクトです。基本的な使い方からDjangoとの統合まで、段階的にCeleryの機能を学習できます。

## 概要

このプロジェクトは、分散タスクキューシステムであるCeleryの学習を目的としています。以下の内容を含んでいます：

- Celeryの基本的な使い方
- Djangoとの統合
- 非同期タスクの実行
- スケジュールタスクの設定
- エラーハンドリング

## 必要な環境

- Python 3.11以上
- Redis（メッセージブローカーとして使用）
- Docker（Redisコンテナの実行用）

## 依存関係

```toml
dependencies = [
    "celery>=5.5.2",
    "django>=5.2.1", 
    "django-celery-beat>=2.8.1",
    "flower>=2.0.1",
    "redis>=6.1.0",
]
```

## プロジェクト構成

```
learn-celery/
├── first-step/          # Celeryの基本的な使い方
│   ├── tasks.py         # 基本的なタスク定義
│   ├── main.py          # タスクの実行例
│   ├── docker-compose.yml
│   └── README.md
├── django-integration/  # DjangoとCeleryの統合
│   ├── proj/           # Djangoプロジェクト設定
│   │   ├── settings.py
│   │   ├── celery.py   # Celery設定
│   │   └── ...
│   ├── polls/          # Djangoアプリケーション
│   │   ├── tasks.py    # 非同期タスク
│   │   ├── views.py    # ビュー
│   │   └── ...
│   ├── manage.py
│   ├── docker-compose.yml
│   └── README.md
├── pyproject.toml      # プロジェクト設定
└── README.md          # このファイル
```

## 学習の進め方

### 1. 基本的なCeleryの使い方 (`first-step/`)

Celeryの最も基本的な機能を学習します。

**含まれる内容：**
- 基本的なタスクの定義
- タスクの実行
- エラーハンドリング

**実行手順：**
```bash
cd first-step/

# Redisコンテナの起動
docker compose up -d

# Celeryワーカーの起動（別ターミナル）
celery -A tasks worker --loglevel=INFO

# タスクの実行
python main.py
```

**学習できること：**
- `@app.task`デコレータの使い方
- 同期・非同期でのタスク実行
- タスクの結果取得
- 例外処理

### 2. DjangoとCeleryの統合 (`django-integration/`)

実際のWebアプリケーションでCeleryを使用する方法を学習します。

**含まれる内容：**
- DjangoプロジェクトでのCelery設定
- `@shared_task`デコレータの使用
- Webリクエストからの非同期タスク実行
- スケジュールタスクの設定

**実行手順：**
```bash
cd django-integration/

# Redisコンテナの起動
docker compose up -d

# Celeryワーカーの起動（別ターミナル）
celery -A proj worker --loglevel=INFO

# Django開発サーバーの起動（別ターミナル）
python manage.py runserver

# タスクの実行テスト
curl http://localhost:8000/polls/
```

**学習できること：**
- DjangoでのCelery設定方法
- Webリクエストからの非同期タスク実行
- `@shared_task`の使い方
- 長時間実行タスクの処理

## 高度な機能

### Flowerによる監視

Celeryタスクの実行状況を監視できます：

```bash
cd django-integration/
celery -A proj flower
```

ブラウザで `http://localhost:5555` にアクセスして監視画面を確認できます。

### スケジュールタスクの実行

定期的にタスクを実行する場合：

```bash
cd django-integration/
celery -A proj beat --loglevel=INFO
```

## 参考資料

- [Celery公式ドキュメント](https://docs.celeryproject.org/)
- [Django-Celery統合ガイド](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
- [Redis公式ドキュメント](https://redis.io/documentation)

## ライセンス

このプロジェクトは学習目的で作成されています。
