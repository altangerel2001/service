from django.shortcuts import render, redirect
import requests, json
from requests.exceptions import JSONDecodeError
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

        r = requests.post('http://localhost:8001/users/',
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
