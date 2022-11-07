from flask import Flask,render_template,request,url_for,redirect
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("database.db") # DB 연결 
print("Opened database successfully")
cur = conn.cursor() # cursor라는 오브젝트는 데이터베이스의 인터페이스
print("Cursor has been set up successfully") 
cur.execute("""
CREATE TABLE IF NOT EXISTS Board(
    name TEXT,
    context TEXT
)
""")

cur.close()
conn.commit()
conn.close()

@app.route('/')
def board():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Board")
    rows = cur.fetchall()
    return render_template('board.html',rows=rows)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == 'POST':
        name = request.form["name"]
        context = request.form["context"]
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO Board (name,context) VALUES('{name}','{context}')")
            con.commit()
        return redirect(url_for("board"))
    else:
        return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)