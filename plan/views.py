from django.shortcuts import render_to_response
import time

def test(request):
    temp = getTemp();
    alert = 0

    if temp > 50:
        alert = 1
    else:
        alert = 0

    return render_to_response("plan/demo.html", {'string': 'Kevin', 'alert': alert, 'temp': temp})

def getTemp():
    with open('temp') as f:
        return int(f.readline())
