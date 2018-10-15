from django.template import loader
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("pessoas/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
