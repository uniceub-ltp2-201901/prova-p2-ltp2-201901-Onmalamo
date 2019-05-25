from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from prova2f import get_urls,get_db,associar_urls,get_random

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'url_holder'

@app.route('/')
def red():
    return redirect(url_for('inserir'))

@app.route('/principal')
def inserir():
    return render_template('principal.html')

@app.route('/atualizar',methods=['POST'])
def atualizar():

     url_antiga = request.form.get("url")
     conn, cursor = get_db(mysql)

     equal = associar_urls(conn,cursor,url_antiga,get_random())

     cursor.close()
     conn.close()

     return redirect(url_for('inserir'))

@app.route('/listar')
def lista():
    conn, cursor = get_db(mysql)
    url=get_urls(cursor)

    return render_template('listadelinks.html',urls=url)


if __name__ == '__main__':
    app.run(debug=True)