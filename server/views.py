import samcoin
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def root(request):
    return JsonResponse({
     "version": settings.VERSION,
     "store as binary": "/store/"
    })


def store(request):
    if request.method == "POST":
        data = request.body
        body, sig = data[:2], data[2:]
        if samcoin.verify_sign(sig, body, samcoin.PK):
            with open(settings.COIN_STORE, "ab") as f:
                f.write(data)
            return JsonResponse({"message": "Thanks"})
        else:
            return JsonResponse({"message": "Not authorized!"}, status=403)

    with open(settings.COIN_STORE, "rb") as f:
        return HttpResponse(f.read(), content_type="application/octet-stream")
