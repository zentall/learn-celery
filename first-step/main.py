from tasks import add, fail

result = add.delay(4, 4)

# タスクが完了したかを確認する
print("[1]", result.ready())

# タイムアウトを指定して同期呼び出しする
print("[2]", result.get(timeout=1))


# タスクが例外を発生させた場合、 get()メソッドが例外を発生させる。
result2 = fail.delay()
try:
    result2.get()
except Exception as e:
    print("[3]", repr(e))

# propagate引数を指定して例外を発生させないようにすることが可能
print("[4]", result2.get(propagate=False))

# タスクが例外を発生させた場合は、tracebackで元のトレースバックにアクセス可能
print("[5]", result2.traceback)
