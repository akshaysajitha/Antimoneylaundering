from django.shortcuts import render

# Create your views here.
import mysql.connector
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import date
# Create your views here.

def index(request):
    return render(request,'index.html')



def loginvalidate(request):
    a=request.GET.get("username")
    print(a)
    b=request.GET.get("password")
    print(b)
    if a=='admin' and b=='admin':
        return render(request,'adminhome.html')
    else:
        return render(request,'adminlogin.html',{'ermsg':'invalid'})
def adminhome(request):
    return render(request,'adminhome.html')
def adminlogin(request):
    return render(request,'adminlogin.html')


def userlogin(request):
    return render(request,'userlogin.html')


def userregistervalidate(request):
    a=request.GET.get('name')
    print(a)
    b=request.GET.get('Phone')
    print(b)
    c=request.GET.get('address')
    print(c)
    d=request.GET.get('Age')
    print(d)
    e=request.GET.get('email')
    print(e)
    f=request.GET.get('UserName')
    print(f)
    g=request.GET.get('Password')
    print(g)
    h=request.GET.get('gender')
    print(h)
    mydb=mysql.connector.connect(host="localhost",password="akshaysajitha",user="root",database="mylastprojweb")
    mycursor=mydb.cursor()
    if d is not None:
       
      q='insert into user (name,phone,address,age,email,username,password,gender) values("'+str(a)+'","'+str(b)+'","'+str(c)+'","'+str(d)+'","'+str(e)+'","'+str(f)+'","'+str(g)+'","'+str(h)+'")'
      print(q)
      mycursor.execute(q)
      mydb.commit()
      mydb.close()
      return render(request,'userregister.html')
    else:
        return render(request,'userregister.html')
    return render(request,'userregister.html')

def userloginvalidate(request):
    a=request.GET.get("username")
    print(a)
    b=request.GET.get("password")
    print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from user where username="'+str(a)+'" and password="'+str(b)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchone()
    print(rows)
    mydb.close()
    if rows is  None:
        return render(request,'userlogin.html',{'er':'enter the valid details'})
    else:
        x=rows
        request.session['unum']=x[0]
        request.session['uname']=x[1]
        return render(request,'userhome.html',{'user':request.session['uname'],'drows':rows})
    

def adminviewuser(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from user'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'adminviewuser.html',{'drows':rows})


def userprofile(request):
    a=request.session['unum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from user where userid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'userprofile.html',{'user':request.session['uname'],'drows':rows})

def userhome(request):
    return render(request,'userhome.html' ,  {'user':request.session['uname']})




def userprofileupdate(request):
    a=request.session['unum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from user where userid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchone()
    print(rows)
    mydb.close()
    return render(request,'userprofileupdate.html',{'user':request.session['uname'],'drows':rows})




def upupdate(request):
    a=request.GET.get('phone')
    b=request.GET.get('email')
    c=request.GET.get('address')
    d=request.GET.get('username')
    e=request.GET.get('password')
    f=request.session['unum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='update user set phone="'+str(a)+'",email="'+str(b)+'",address="'+str(c)+'",username="'+str(d)+'",username="'+str(e)+'"where userid="'+str(f)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return userprofileupdate(request)




def inspectorregistervalidate(request):
    a=request.GET.get('name')
    print(a)
    b=request.GET.get('email')
    print(b)
    c=request.GET.get('Phone') 
    print(c)
    e=request.GET.get('address')
    print(e)
    f=request.GET.get('UserName')
    print(f)
    g=request.GET.get('Password')
    print(g)
    h=request.GET.get('designation')
    print(h)
    i=request.GET.get('gender')
    print(i)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    if c is not None:
         q='INSERT into inspector (name,phone,address,email,username,password,designation,gender) values("'+str(a)+'","'+str(c)+'","'+str(e)+'","'+str(b)+'","'+str(f)+'","'+str(g)+'","'+str(h)+'","'+str(i)+'")'
         print(q)
         mycursor.execute(q)
         mydb.commit()
         mydb.close()
         return render(request,'inspectorregister.html')
    else:
         return render(request,'inspectorregister.html')

    
      
    





def inspectorlogin(request):
    a=request.GET.get('username')
    b=request.GET.get('password')
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from inspector where username="'+str(a)+'" and password="'+str(b)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchone()
    print(rows)
    mydb.close()
    if rows is None:
        return render(request,'inspectorlogin.html',{'not':'enter valid details'})
    else:
        x=rows
        request.session['insnum']=x[0]
        request.session['insname']=x[1]
        return render(request,'inspectorhome.html',{'inname':request.session['insname'],'insprow':rows})
    


def viewinspector(request):
    a=request.session['insnum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from inspector where inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'viewinspector.html',{'inname':request.session['insname'],'irows':rows})


def insprofileupdate(request):
    a=request.session['insnum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from inspector where inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchone()
    print(rows)
    mydb.close()
    return render(request,'insprofileupdate.html',{'ins':request.session['insname'],'irows':rows})

def inspectorhome(request):
    return render(request,'inspectorhome.html')



def insupdate(request):
    a=request.GET.get('designation')
    print(a)
    b=request.GET.get('phone')
    print(b)
    c=request.GET.get('email')
    print(c)
    d=request.GET.get('address')
    print(d)
    e=request.session['insnum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='update inspector set designation="'+str(a)+'",phone="'+str(b)+'",email="'+str(c)+'",address="'+str(d)+'"where inid="'+str(e)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return insprofileupdate(request)




def adminviewinspector(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from inspector'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'adminviewinspector.html',{'irows':rows})


def userdelete(request):
    a=request.GET.get('dluser')
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='delete from user where userid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewuser(request)


def inpectordelete(request):
    a=request.GET.get('insdlt')
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='delete from inspector where inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewinspector(request)



def usercomplaint(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from inspector'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'usercomplaint.html',{'insrows':rows}) 

    
def complaintsend(request):
    a=request.GET.get('inspid')
    b=request.GET.get('inspname')
    request.session['inspid']=a
   
    print(a)
    request.session['inspname']=b
    iname= request.session['inspname']
    print(iname)
    return render(request,'complaint.html')





def complaintform(request):
    a=request.session['unum']
    print(a)
    b=request.session['uname'] 
    print(b)
    c=request.GET.get('area')
    print(c)
    d=request.GET.get('areas')
    print(d)
    day=date.today()
    e=request.session['inspid']
    print(e)
    f=request.session['inspname']
    print(f)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='insert into complaints (userid,username,cmplaint,cmplaintdetails,date,inid,inspectorname) values("'+str(a)+'","'+str(b)+'","'+str(c)+'","'+str(d)+'","'+str(day)+'","'+str(e)+'","'+str(f)+'")'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render(request,'complaint.html')




def adminviewcomplaints(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from complaints'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    ins='select* from inspector'
    mycursor.execute(ins)
    insname=mycursor.fetchall()

    print(rows)
    mydb.close()
    return render(request,'adminviewcomplaints.html',{'cmprows':rows,'ins':insname})



def approvecomplaints(request):
    a=request.GET.get('cmpapp')
    print(a)
    insdetial=request.GET.get('dropd')
    print(insdetial)
    print(type(insdetial))
    sp=insdetial.split("+")
    iname=sp[0].strip()
    id=sp[1].strip()
    print(id)
    print(iname)
    


    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()

    q='UPDATE complaints SET status="approved", inid="'+str(id)+'", inspectorname="'+str(iname)+'"  where cmpno="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewcomplaints(request)

def deleteaction(request):
    a=request.GET.get('cmpapp')
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='delete from complaints where cmpno="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewcomplaints(request)

def inspectorviewcomplaints(request):
    a=request.session['insnum']
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from complaints where status="approved" and inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'inspectorviewcomplaints.html',{'cmprows':rows})



def replycomplaint(request):
    a=request.GET.get('sendrem')
    b=request.session['insnum']
    c=request.GET.get('complaintnumber')
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='update complaints set remarks="'+str(a)+'" where  inid="'+str(b)+'" and cmpno="'+str(c)+'" '
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render(request,'insreplycomplaint.html')


def userviewcomplaints(request):
    a=request.session['unum']
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from complaints where userid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'userviewcomplaints.html',{'box':rows})


def trackcomplaints(request):
    a=request.session['insnum']
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from complaints where status="approved" and inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'trackcomplaints.html',{'track':rows})




def insfeedback(request):
    a=request.session['insnum']
    print(a)
    b=request.session['insname']
    print(b)
    c=request.GET.get('feedback')
    print(c)
    d=request.GET.get('textarea')
    print(d)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    if d is not None:
         q='insert into insfeedback(inid,name,rating,feedback) values("'+str(a)+'","'+str(b)+'","'+str(c)+'","'+str(d)+'")'
         print(q)
         mycursor.execute(q)
         mydb.commit()
         mydb.close()
         return render(request,'insfeedback.html')
    else:
        return render(request,'insfeedback.html')
   



def userfeedback(request):
    

    uid= request.session['unum']
    uname= request.session['uname']

    print(uname)
    c=request.GET.get('feedback')
    print(c)
    d=request.GET.get('textarea')
    print(d)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    if d is not None:
            q='insert into feedback(userid,name,rating,feedback) values("'+str(uid)+'","'+str(uname)+'","'+str(c)+'","'+str(d)+'")'
            print(q)
            mycursor.execute(q)
            mydb.commit()
            mydb.close()
            return render(request,'userfeedback.html')
    else:
        return render(request,'userfeedback.html')

   




def inspectorseefeedback(request):
    a=request.session['insnum']
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from insfeedback where inid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'inspectorseefeedback.html',{'feedrow':rows})



def userviewfeedback(request):
    a=request.session['unum']
    print(a)
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from feedback where userid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'userviewfeedback.html',{'userfeed':rows})


def adminuserfeedback(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from feedback'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'adminuserfeedback.html',{'fullfeed':rows})

    
def admininspectorfeedback(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="akshaysajitha",database="mylastprojweb")
    mycursor=mydb.cursor()
    q='select * from insfeedback'
    print(q)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print(rows)
    mydb.close()
    return render(request,'adminuserfeedback.html',{'fullfeed':rows})

