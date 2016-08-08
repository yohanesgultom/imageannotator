import os
import json
import pickle
from django.shortcuts import render
from django.http import JsonResponse

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC = "static"
CONFIG = "_config"
FRAME_PATH = "images/video"


def get_dirs(mypath):
    res = []
    for f in os.listdir(mypath):
        if os.path.isdir(os.path.join(mypath, f)):
            res.append(f)
    return res


def get_files(path, dir):
    res = []
    mypath = os.path.join(path, dir)
    relpath = os.path.join(os.path.join(STATIC, FRAME_PATH), dir)
    for f in os.listdir(mypath):
        if os.path.isfile(os.path.join(mypath, f)):
            res.append(os.path.join(relpath, f))
    return res


def index(request):
    images = []
    config = []
    mypath = os.path.join(DIR_PATH, os.path.join(STATIC, FRAME_PATH))
    dirs = get_dirs(mypath)
    seldir = request.GET.get("seldir")
    # set default
    # seldir = dirs[0] if seldir is None and len(dirs) > 0 else seldir
    if seldir:
        images = get_files(mypath, seldir)
        images.sort()
        confpath = os.path.join(os.path.join(DIR_PATH, CONFIG), seldir)
        if os.path.isfile(confpath):
            with open(confpath, 'rb') as conffile:
                config = pickle.load(conffile)
                conffile.close()
    context = {
        "dirs": dirs,
        "seldir": seldir,
        "images": json.dumps(images),
        "config": json.dumps(config)
    }
    return render(request, "annotator/index.html", context)


def save(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        path = os.path.join(os.path.join(DIR_PATH, CONFIG), data['seldir'])
        output = open(path, 'w+')
        pickle.dump(data['config'], output)
        output.close()
        return JsonResponse({'success': True})
    return JsonResponse({'success': false, 'message': 'GET request not allowed'})
