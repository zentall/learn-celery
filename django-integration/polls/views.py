from django.shortcuts import render
from django.http import HttpResponse

from polls.tasks import send_email


def index(request):
    user_id = 123
    result = send_email.delay(user_id)

    return HttpResponse(f"Email has been sent. [id={result.id}]\n")
