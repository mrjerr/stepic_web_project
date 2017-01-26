from django.shortcuts import HttpResponse

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')
