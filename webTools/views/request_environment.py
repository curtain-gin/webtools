from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.system_environment_from import *


def request_environmentl_list(request):
    if request.method == 'GET':
        forms = models.SystemEnvironment.objects.all().order_by("-environment_id")
        return render(request, "web/request_environment.html", {"fro": forms})
    else:
        return redirect("/request/environment/list/")

def request_environmentl_add(request):
    if request.method == "GET":
        forms = SystemEnvironmentAddForm()
        tille = "环境添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    elif request.method == "POST":
        form = SystemEnvironmentAddForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect("/request/environment/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})

    else:
        forms = models.SystemEnvironment.objects.all()
        return render(request, "web/request_environment.html", {"fro": forms})


def request_environmentl_edit(request, nid):
    row_object = models.SystemEnvironment.objects.filter(environment_id=nid).first()
    if request.method == "GET":
        tille = "环境编辑"
        forms = SystemEnvironmentAddForm(instance=row_object)
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    else:
        form = SystemEnvironmentAddForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/request/environment/list/")
        else:
            tille = "环境编辑"
            return render(
                request,
                "web/chenge.html",
                {
                    "form": form,
                    "tille": tille,
                },
            )


def request_environmentl_delet(request, nid):
    row_object = models.SystemEnvironment.objects.filter(environment_id=nid).first()
    if not row_object:
        return render(request, "web/request_environment.html")
    else:
        models.SystemEnvironment.objects.filter(environment_id=nid).delete()
        return redirect("/request/environment/list/")
