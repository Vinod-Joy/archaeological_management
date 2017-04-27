from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def handler404(request):
    response = render_to_response('arch/../arch/templates/404.html',context_instance=RequestContext(request))
    response.status_code = 404
    return response

def hello(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return redirect("/admin")
        else:

            if request.user.groups.all()[0].name == "archaeologist":
                return redirect('/arch/archaeologist/' + str(request.user.user_profile.ArchaeologistSSN))
            else:
                return redirect("arch:index")
    else:
        return redirect("login")

def home(request):
    if request.user.is_superuser:
        return redirect('/arch')
    if request.user.groups.all()[0].name == "archaeologist":
        return redirect('/arch/archaeologist/'+str(request.user.user_profile.ArchaeologistSSN))
    else:
        return redirect('/arch')


