import json
import os


from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
import yaml


def index(request, path):
    appContext = {}
    appContext["path"] = path

    config_path = os.path.join(settings.CONFIG_PATH, path)

    if os.path.isdir(config_path):
        for dirpath, dirnames, files in os.walk(config_path):           
            if not files or not files.__contains__("config.yaml"):
                raise Http404(f"No configured tutorial found for /{path}")
            
            config_file_path = os.path.join(config_path, "config.yaml") 
            with open(config_file_path, 'r') as stream:
                try:
                    config_data = yaml.load(stream)
                    appContext["content"] = config_data
                except yaml.YAMLError as exc:
                    raise HttpResponseServerError(exc)

    return render(request, "vue-app.html", context={"context": json.dumps(appContext)})
