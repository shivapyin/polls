from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world your at poll index")
