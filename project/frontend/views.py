from django.shortcuts import redirect, render
import mysql.connector 
# This is the view that you imported in the frontend/urls.py

def homeView(request , *args, **kwargs):
    return render(request, 'frontend/index.html', None)

def aboutView(request , *args, **kwargs):
    return render(request, 'frontend/about.html', None)

def contactView(request , *args, **kwargs):
    return render(request, 'frontend/contact.html', None)


def showTable(tablename):
    global mydb
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="sample"
    )
    mycursor = mydb.cursor()
    query = "select * from "+ tablename
    mycursor.execute(query)
    table = mycursor.fetchall()
    return table

def artView(request):    
    table = showTable('Art_Piece')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        artid = request.POST.get('artid')
        atype = request.POST.get('atype')
        aprice = request.POST.get('aprice')
        astat = request.POST.get('astat')
        cron = request.POST.get('cron')
        aname = request.POST.get('aname')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Art_Piece (Art_ID, Art_Type, Price, A_status, Created_On, AName) VALUES (%s, %s, %s,%s,%s, %s)"
            val = (artid, atype, aprice, astat, cron, aname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(artView)
            
        if operation == 'delete':
            sql = "DELETE FROM Art_Piece WHERE Art_ID = '"+artid +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(artView)
            
        if operation == 'update':
            sql = "UPDATE Art_Piece SET Art_Type = %s, Price = %s, A_status = %s, Created_On = %s, AName = %s  WHERE Art_ID = %s"
            val = (atype, aprice, astat, cron, aname, artid)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(artView)           
    return render(request, "frontend/articles.html", {'table' : table})

def artistView(request):    
    table = showTable('Artist')
    
    if request.method == 'POST':
        operation = request.POST.get('operationid')
        aname = request.POST.get('aname')
        isalive = request.POST.get('isalive')
        amobile = request.POST.get('amobile')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Artist (AName, Is_Alive, AMobile) VALUES (%s, %s, %s)"
            val = (aname, isalive, amobile)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(artistView)
            
        if operation == 'delete':
            sql = "DELETE FROM Artist WHERE AName = '"+aname+"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(artistView)
            
        if operation == 'update':
            sql = "UPDATE Art_Piece SET AMobile = %s, Is_Alive = %s WHERE AName = %s"
            val = (amobile, isalive, aname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(artistView)          
        

    return render(request, "frontend/artists.html", {'table' : table})


def galleryView(request):    
    table = showTable('All_Galleries')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        gname = request.POST.get('GName')
        gmobile = request.POST.get('GMobile')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO All_Galleries (GName, GMobile) VALUES (%s, %s)"
            val = (gname, gmobile)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(galleryView)
            
        if operation == 'delete':
            sql = "DELETE FROM All_Galleries WHERE GName = '"+gname +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(galleryView)
            
        if operation == 'update':
            sql = "UPDATE All_Galleries SET GMobile = %s WHERE GName = %s"
            val = (gmobile, gname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(galleryView)
    return render(request, "frontend/galleries.html", {'table' : table})


def exhibView(request):
    table = showTable('Exhibitions')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        ename = request.POST.get('ename')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        place = request.POST.get('place')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Exhibitions (EName, Start_Date, End_Date, Place) VALUES (%s,%s,%s, %s)"
            val = (ename, sdate, edate, place)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(exhibView)
            
        if operation == 'delete':
            sql = "DELETE FROM Exhibitions WHERE EName = '"+ename +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(exhibView)
            
        if operation == 'update':
            sql = "UPDATE Exhibitions SET Start_Date = %s, End_Date =%s, Place=%s WHERE EName = %s"
            val = (sdate, edate, place, ename)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(exhibView)
    return render(request, 'frontend/exhibitions.html', {'table' : table})


def holdView(request):
    table = showTable('Holdings')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        aid = request.POST.get('aid')
        gname = request.POST.get('gname')
        since = request.POST.get('since')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Holdings (Art_ID, GName, Since) VALUES (%s, %s, %s)"
            val = (aid, gname, since)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(holdView)
            
        if operation == 'delete':
            sql = "DELETE FROM Holdings WHERE Art_ID = '"+aid +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(holdView)
            
        if operation == 'update':
            sql = "UPDATE Holdings SET GName = %s, Since = %s WHERE Art_ID = %s"
            val = (gname, since, aid)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(holdView)
    return render(request, 'frontend/holdings.html', {'table' : table})


def showView(request):
    table = showTable('Showcases')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        aid = request.POST.get('aid')
        ename = request.POST.get('ename')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Showcases (Art_ID,EName) VALUES (%s, %s)"
            val = (aid, ename)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(showView)
            
        if operation == 'delete':
            sql = "DELETE FROM Showcases WHERE Art_ID = '"+ aid +"' AND '"+ename+"'" 
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(showView)

    return render(request, 'frontend/showcases.html', {'table' : table})


def purView(request):
    table = showTable('Purchase')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        aid = request.POST.get('aid')
        pname = request.POST.get('pname')
        tid = request.POST.get('tid')
        price = request.POST.get('price')
        puron = request.POST.get('puron')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Purchase (Art_ID, PName, TransactionID, Price, Purchased_On) VALUES (%s, %s, %s, %s, %s)"
            val = (aid, pname, tid, price, puron)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(purView)
            
        if operation == 'delete':
            sql = "DELETE FROM Purchase WHERE Transaction_ID = '"+ tid +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(purView)
            
        if operation == 'update':
            sql = "UPDATE Purchase SET Art_ID = %s, PName = %s, Price = %s, Purchased_On = %s WHERE TransactionID = %s"
            val = (aid, pname, price, puron, tid)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(purView)
    return render(request, 'frontend/purchases.html', {'table' : table})


def purchasersView(request):
    table = showTable('Purchasers')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        pname = request.POST.get('pname')
        pmobile = request.POST.get('pmobile')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Purchasers (PName, PMobile) VALUES (%s, %s)"
            val = (pname, pmobile)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(purchasersView)
            
        if operation == 'delete':
            sql = "DELETE FROM Purchasers WHERE PName = '"+pname +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(purchasersView)
            
        if operation == 'update':
            sql = "UPDATE Purchasers SET PMobile = %s WHERE PName = %s"
            val = (pmobile, pname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(purchasersView)
    return render(request, 'frontend/purchasers.html', {'table' : table})

def insurView(request):
    table = showTable('Insurance')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        aid = request.POST.get('aid')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        prem = request.POST.get('prem')
        icname = request.POST.get('icname')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Insurance (Art_ID, Start_Date, End_Date, Premium, ICName) VALUES (%s,%s,%s,%s, %s)"
            val = (aid, sdate, edate, prem, icname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(insurView)
            
        if operation == 'delete':
            sql = "DELETE FROM Insurance WHERE Art_ID = '"+ aid +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(insurView)
            
        if operation == 'update':
            sql = "UPDATE Insurance SET Start_Date = %s, End_Date = %s, Premium = %s, ICName = %s WHERE Art_ID = %s"
            val = (sdate, edate, prem, icname,aid)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(galleryView)
    return render(request, 'frontend/insurances.html', {'table' : table})



###### Remaining ########
def icompView(request):
    table = showTable('Insurance_Company')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        icname = request.POST.get('icname')
        icmobile = request.POST.get('icmobile')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Insurance_Company (ICName, ICMobile) VALUES (%s, %s)"
            val = (icname, icmobile)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(icompView)
            
        if operation == 'delete':
            sql = "DELETE FROM Insurance_Company WHERE ICName = '"+icname +"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(icompView)
            
        if operation == 'update':
            sql = "UPDATE Insurance_Company SET ICMobile = %s WHERE ICName = %s"
            val = (icmobile, icname)
            mycursor.execute(sql, val)
            mydb.commit()
    return render(request, 'frontend/insurance_companies.html', {'table' : table})

def orgView(request):
    table = showTable('Organizers')

    if request.method == 'POST':
        operation = request.POST.get('operationid')
        ename = request.POST.get('ename')
        gname = request.POST.get('gname')
        mycursor = mydb.cursor()
        print(operation)
        
        if operation == 'insert':
            sql = "INSERT INTO Organizers (EName, GName) VALUES (%s, %s)"
            val = (ename, gname)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(orgView)
            
        if operation == 'delete':
            sql = "DELETE FROM Organizers WHERE GName = '"+gname +"' AND EName ='" +ename+"'"
            mycursor.execute(sql)
            print(mycursor)
            mydb.commit()
            return redirect(orgView)
            
    return render(request, 'frontend/organizers.html', {'table' : table})