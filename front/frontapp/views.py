from django.shortcuts import render,redirect
import json

# Create your views here.
def dt_login(request):
    requestJSON={}
    ctx = {}
    username = request.POST["username"],
    passw = request.POST["password"]
    requestJSON["action"] = "login"
    requestJSON["email"] = username
    requestJSON["passw"] = passw
    
    r=request.post('http://127.0.0.1:8001/users/',
                   data=json.dumps(requestJSON),
                   header={"Content-Type":"application/json"},
                   )
    
    resultCode= r.json()['resultCode']
    resultMassage = r.json()['resultMassage']
    
    ctx['resultCode'] = resultCode
    ctx['resultMassage'] = resultMassage
    if resultCode == 1002:
        return redirect("dashboard")
       
    return render (request, "login.html",ctx)
def dt_dashboard(request):
    return render(request,"dashboard.html")
