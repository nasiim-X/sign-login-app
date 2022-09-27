from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
sx=''
em=''
pswd=''

# Create your views here.
def signaction(request):
    global fn,ln,sx,em,pswd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                sx=value
            if key=="email":
                em=value
            if key=="password":
                pswd=value

        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,sx,em,pswd)
        cursor.execute(c)
        m.commit()
    
    return render(request,'signup_page.html')

