from django.http import HttpResponse

def store(request):
    with open("store", "rb") as f:
        return HttpResponse(f.read(), content_type="application/octet-stream")
