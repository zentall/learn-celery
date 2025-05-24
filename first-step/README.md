
- Redisコンテナの起動
```bash
docker compose up
```

- cewleryワーカーの起動
```bash
celery -A tasks worker --loglevel=INFO
```

- main.pyでタスクを呼び出し
```
$ python main.py 
[1] False
[2] 8
[3] Exception('The task failed')
[4] The task failed
[5] Traceback (most recent call last):
  File "/home/zk/learn-celery/.venv/lib/python3.11/site-packages/celery/app/trace.py", line 453, in trace_task
    R = retval = fun(*args, **kwargs)
                 ^^^^^^^^^^^^^^^^^^^^
  File "/home/zk/learn-celery/.venv/lib/python3.11/site-packages/celery/app/trace.py", line 736, in __protected_call__
    return self.run(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zk/learn-celery/basic/tasks.py", line 14, in fail
    raise Exception("The task failed")
Exception: The task failed
```

- celery workerの出力
```bash
$ celery -A tasks worker --loglevel=INFO
 
 -------------- celery@DESKTOP-GKP7SRQ v5.5.2 (immunity)
--- ***** ----- 
-- ******* ---- Linux-4.19.128-microsoft-standard-x86_64-with-glibc2.31 2025-05-24 10:59:51
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         hello:0x7f9d424b3150
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     redis://localhost/
- *** --- * --- .> concurrency: 12 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add
  . tasks.fail

[2025-05-24 10:59:51,816: INFO/MainProcess] Connected to redis://localhost:6379//
[2025-05-24 10:59:51,818: INFO/MainProcess] mingle: searching for neighbors
[2025-05-24 10:59:52,826: INFO/MainProcess] mingle: all alone
[2025-05-24 10:59:52,838: INFO/MainProcess] celery@DESKTOP-GKP7SRQ ready.
[2025-05-24 11:00:16,698: INFO/MainProcess] Task tasks.add[2106c24d-be40-4aa3-805e-7fe8a5fe15f2] received
[2025-05-24 11:00:16,702: INFO/ForkPoolWorker-6] Task tasks.add[2106c24d-be40-4aa3-805e-7fe8a5fe15f2] succeeded in 0.0035261000000446074s: 8
[2025-05-24 11:00:16,704: INFO/MainProcess] Task tasks.fail[c44cf2d3-4a38-4ef2-9201-c936dcc1ed3a] received
[2025-05-24 11:00:16,707: ERROR/ForkPoolWorker-6] Task tasks.fail[c44cf2d3-4a38-4ef2-9201-c936dcc1ed3a] raised unexpected: Exception('The task failed')
Traceback (most recent call last):
  File "/home/zk/learn-celery/.venv/lib/python3.11/site-packages/celery/app/trace.py", line 453, in trace_task
    R = retval = fun(*args, **kwargs)
                 ^^^^^^^^^^^^^^^^^^^^
  File "/home/zk/learn-celery/.venv/lib/python3.11/site-packages/celery/app/trace.py", line 736, in __protected_call__
    return self.run(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zk/learn-celery/basic/tasks.py", line 14, in fail
    raise Exception("The task failed")
Exception: The task failed

```