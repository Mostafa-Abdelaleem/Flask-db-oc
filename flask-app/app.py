import os
import ibm_db
from flask import Flask
app = Flask(__name__)

conn=ibm_db.connect(os.environ['dbcred'], "", "")

@app.route("/")
def main():
    try:
         sql = ''' CREATE TABLE values(id int,name varchar(50)) '''
         stmt = ibm_db.exec_immediate(conn,sql)
         err="Table Values Created In Db2 Database"
    except:
        err="Table Values Already Exists"
    return "<h1 style='color:green;text-align:center;''>Flask App Is Online!:D</br></h1>" \
            +"<h2 style='text-align:center;''>Creating Table Values In Db2 Database ...</br></h2>" \
            +f" <h3 style='color:blue;text-align:center;'>{err}</h3>"


@app.route('/db2')
def access_db():
    try:
        sql = ''' SELECT * FROM values '''
        stmt = ibm_db.exec_immediate(conn,sql)
        dictionary = ibm_db.fetch_both(stmt)
        if(dictionary):
            return "<h1 style='text-align:center;'>Table Values</br></h1>"\
                    +f"<h2 style='color:blue;text-align:center;'></br>{dictionary['NAME']}</h2>"
        else:
            return "<h1 style='color:red;text-align:center;'>Table Values Is Empty"
            
    except:
        return "<h1 style='color:red;text-align:center;'>Table Values Doesn't Exist"


@app.route('/insertname')
def abd_db():
        try:
            sql=''' INSERT INTO values (id,name) VALUES ('1','Mostafa Abdelaleem') ; '''
            ibm_db.exec_immediate(conn,sql) 
            return "<h1 style='color:green;text-align:center;'> Table now has name: mostafa abdelelaeem</h1>"
        except:
            return "<h1 style='color:red;text-align:center;'>There Is No Table To Insert In</br>\
                Please Create The Table And Try Again </h1>"
        
        

@app.route('/deletetable')
def mos_db():
    try:
        sql = ''' DROP TABLE values; '''
        ibm_db.exec_immediate(conn,sql)
        return "<h1 style='color:green;text-align:center;'>Table Values Is Now Deleted</h1>"
    except:
        return "<h1 style='color:red;text-align:center;'>Table Values Doesn't Exist Already</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
