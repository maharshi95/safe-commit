from django.http.response import JsonResponse


# Create your views here.

def health_api(request):
    return JsonResponse(data={
        "status": "Running",
        "message": "Greetings from safe-commit :)"
    }, status=200)
