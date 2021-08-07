from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "dba"
     
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) 
 
@app.route('/')
def index(): 
    return render_template('index.html')


@app.route("/insert",methods=['POST','GET'])
def insert():
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if request.method == 'POST':
    fullname = request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    password_hash = request.form['password']
    password = generate_password_hash(password=password_hash)
    cur.execute("INSERT INTO users(fullname,username,email,password) values(%s,%s,%s,%s)",[fullname,username,email,password])
    conn.commit()
    cur.close()
    return jsonify('New Records added successfully')

if __name__ == "__main__":
    app.run(debug=True)