from django.shortcuts import render


def index(request, path):
    return render(request, "vue-app.html", {"route": path})
