from django.shortcuts import render
from qrcode import *

data=None
def INDEX(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")
    else:
        pass
    return render(request,"index.html",{'data':data})
