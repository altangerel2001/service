from django.shortcuts import render, redirect
import requests, json
from requests.exceptions import JSONDecodeError
import hashlib 
# Create your views here.
def dt_login(request):
    requestJSON = {}
    ctx = {}
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['passw']
        # print(username,passw)
        requestJSON["action"] = "login"
        requestJSON["email"] = username
        requestJSON["passw"] = passw

        r = requests.post('http://127.0.0.1:8001/users/',
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'},
                            )

        # pled validation bolon busad exeption-uud shalgah
        # print(r)
        resultCode = r.json()['resultCode']
        resultMessage = r.json()['resultMessage']
        # print(resultCode, resultMessage)
        # ctx = r.json()
        ctx['resultCode'] = resultCode
        ctx['resultMessage'] = resultMessage
        if resultCode == 1002:
            ctx['email'] = r.json()["data"][0]["email"]
            ctx['firstname'] = r.json()["data"][0]["firstname"]
            ctx['lastname'] = r.json()["data"][0]["lastname"]
            # ctx = r.json()
            print(r.json(), " aaaaaa ",r.json()["data"][0]["email"])
            return render(request,"dashboard.html", ctx)
        
        
    return render(request, "login.html",ctx)


def dt_dashboard(request):
    return render (request, "dashboard.html")

def dt_register(request):
    requestJSON = {}
    ctx = {}
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['passw']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']

        requestJSON["action"] = "register"
        requestJSON["email"] = username
        # passw = passw.encode('utf-8')
        requestJSON["passw"] = hashlib.md5(hashlib.md5(passw.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()
        requestJSON["firstname"] = firstname
        requestJSON["lastname"] = lastname

        r = requests.post('http://localhost:8001/users/',
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'},
                            )

        resultCode = r.json()['resultCode']
        resultMessage = r.json()['resultMessage']

        ctx['resultCode'] = resultCode
        ctx['resultMessage'] = resultMessage

        ctx['inputemail'] = username
        ctx['inputfirstname'] = firstname
        ctx['inputlastname'] = lastname


        if resultCode == 1001:
            email = r.json()['data'][0]['email']
            firstname = r.json()['data'][0]['firstname']
            lastname = r.json()['data'][0]['lastname']
            ctx['email'] = email
            ctx['firstname'] = firstname
            ctx['lastname'] = lastname
            return render(request, "login.html", ctx)
        else:
            email = r.json()['data'][0]['email']
            ctx['email'] = email
    
    return render (request, "register.html", ctx)
