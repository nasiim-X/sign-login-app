from django.shortcuts import render
import mysql.connector as sql

em=''
pswd=''

# Create your views here.
def loginaction(request):
    global em,pswd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pswd=value

        c="select * from users where email='{}' and password='{}'".format(em,pswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    
    return render(request,'login_page.html')

