from django.shortcuts import render


# Create your views here.
def index(request):
    page = {"title": "TEST"}
    print(locals())
    return render(request, "index.html", locals())
