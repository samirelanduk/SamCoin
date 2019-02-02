from django.http import HttpResponse, JsonResponse
from django.conf import settings

def root(request):
    return JsonResponse({
     "version": settings.VERSION,
     "store as binary": "/store/"
    })


def store(request):
    with open("store", "rb") as f:
        return HttpResponse(f.read(), content_type="application/octet-stream")
