import json
import os

import yaml
from deepmerge import Merger
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render

merger = Merger(
    # pass in a list of tuple, with the
    # strategies you are looking to apply
    # to each type.
    [(list, ["append"]), (dict, ["merge"]), (set, ["union"])],
    # next, choose the fallback strategies,
    # applied to all other types:
    ["override"],
    # finally, choose the strategies in
    # the case where the types conflict:
    ["override"],
)


def index(request, path):
    appContext = {}
    appContext["path"] = path

    app_config_path = os.path.join(settings.CONFIG_PATH, path)

    if os.path.isdir(app_config_path):
        for dirpath, dirnames, files in os.walk(app_config_path):
            if not files or not files.__contains__("config.yaml"):
                raise Http404(f"No configuration found for /{path}")

            global_config_file_path = os.path.join(settings.CONFIG_PATH, "global.yaml")
            with open(global_config_file_path, "r") as global_config_stream:
                try:
                    global_config_data = yaml.load(
                        global_config_stream, Loader=yaml.FullLoader
                    )
                except yaml.YAMLError as exc:
                    raise HttpResponseServerError(exc)

            app_config_file_path = os.path.join(app_config_path, "config.yaml")
            with open(app_config_file_path, "r") as app_config_stream:
                try:
                    app_config_data = yaml.load(
                        app_config_stream, Loader=yaml.FullLoader
                    )
                except yaml.YAMLError as exc:
                    raise HttpResponseServerError(exc)

            appContext["content"] = merger.merge(global_config_data, app_config_data)
    else:
        raise Http404(f"No configured tutorial found for /{path}")

    return render(request, "vue-app.html", context={"context": json.dumps(appContext)})
