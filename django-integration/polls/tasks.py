import time
import random


from celery import shared_task


@shared_task()
def send_email(user_id):
    print("sending email...")

    for i in range(3):
        print(f"[{i}] working...")
        time.sleep(1)

    print(f"done! user_id={user_id}")
    return user_id


@shared_task()
def batch_task():
    print("starting some task...")

    times = random.randint(1, 3)

    for i in range(times):
        delay = random.randint(1, 5)
        print(f"[{i + 1}/{times}] working({delay}s to complete)...")
        time.sleep(delay)

    print(f"done! {times} process")
    return {"result": "ok"}
