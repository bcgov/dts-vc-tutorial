import os

from django.conf import settings
from django.shortcuts import render


def index(request):

    tutorial_list = []

    for confpath, dirnames, files in os.walk(settings.CONFIG_PATH):
        for appdir in dirnames:
            current_app_path = os.path.join(settings.CONFIG_PATH, appdir)
            for dirpath, dirnames, files in os.walk(current_app_path):
                if not files or not files.__contains__("tutorialConfig.yaml"):
                    print(dirpath, "empty")
                    continue
                tutorial_list.append(appdir)

        return render(request, "index.html", context={"tutorial_list": tutorial_list})
