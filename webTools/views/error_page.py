from django.shortcuts import render, redirect, HttpResponse


def bad_request(request, exception=400):
    return render(request, "400.html")


def permission_denied(request, exception=403):
    return render(request, "403.html")


def page_not_found(request, exception=404):
    return render(request, "404.html")


def error(request, exception=500):
    return render(request, "500.html")
