from flask import Flask , render_template, url_for ,session , request , redirect , flash 
import sqlite3

app=Flask("__name__")
con=sqlite3.connect("dciprojects.db")
con.execute("create table if not exists company(id INTEGER  PRIMARY KEY , Invoiceno TEXT, Invoicevalue INTEGER, Invoicedate DATE, Vendorname TEXT, Projectno TEXT, Department TEXT, courierorshipment TEXT, file TEXT)")
con.close()

@app.route('/')
def home():
    return render_template("dciproject.html")


@app.route('/insert', methods=['GET'  ,  'POST'])
def insert():
    if request.method=='POST':
        try:
            InvoiceNo=request.form["InvoiceNo"]
            InvoiceDate=request.form["InvoiceDate"]
            Vendorname=request.form["Vendorname"]
            Invoicevalue=request.form["Invoicevalue"]
            projectNo=request.form["projectNo"]
            Department=request.form["Department"]
            CourierorShipmentNo=request.form["Courier/ShipmentNo"]
            Attachments=request.form["Attachments"]
            con.sqlite3.connect("dciprojects.db")
            cur=con.cursor()
            cur.execute("insert into company(Invoiceno,Invoicevalue,Invoicedate,Vendorname,Projectno,Department,courierorshipment,file )values(?,?,?,?,?,?,?,?)",(InvoiceNo,Invoicevalue,InvoiceDate,Vendorname,projectNo,Department,CourierorShipmentNo,Attachments))
            con.commit()
            session['Invoiceno']=InvoiceNo
            flash("record added" , "succeessful")
        except:
            flash("not records added", "successful")
        finally:
            con.close()
    return render_template("dciproject.html")

    

        
        

            
         
        






if  __name__=="__main__":
    app.run(debug=True)
