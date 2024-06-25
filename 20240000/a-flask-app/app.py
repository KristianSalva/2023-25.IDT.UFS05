import os
from flask import Flask, render_template, request
import json
import requests 
import mysql.connector
from mysql.connector import Error


class User:
    username = None
    password = None
    email = None

    def __init__(self, u, p, e):
        self.username = u
        self.password = p
        self.email = e
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    '''def __str__(self):
        return f"User: {self.username}, {self.password}, {self.email}"
    '''
    def __repr__(self):
        return f"Lista utenti: username {self.username}, password {self.password}, e-mail {self.email}"
    


antonio = User("antonio", "123456", "antonio@itsrizzoli.it")
davide = User("davide", "ciao", "d.longo@itsrizzoli.it")
aimane = User('aimane', 'yolo', 'a.jrada@itsrizzoli.it')
kristian = User('kristian', 'ciaone', 'k.salva@itsrizzoli.it')
listaUser = [antonio, davide, aimane, kristian]


appWeb = Flask(__name__)

@appWeb.route("/listaUtenti")
def listaUtenti():
    '''print("<ul>")
    for obj in listaUser:
        print(f" <li>{repr(obj)}</li>")
    print("</ul>")'''
    return render_template("listaUtenti.html", paramList = listaUser)

#http://www.miosito.it
#definisco un endpoint / che risponde all'indirizzo http://127.0.0.1:5000/

@appWeb.route("/")
def home():
    #return "pagina iniziale da visualizzare"
    return render_template("home.html")


connection = None
try:
    connection = mysql.connector.connect(
        host="its-rizzoli-idt-mysql-kristian.mysql.database.azure.com",
        user="psqladmin",
        passwd="H@Sh1CoR3!",
        database="...."
    )
    print("Connection to MySQL DB successful")
except Error as e:
    print(f"The error '{e}' occurred")
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sample_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
    """
    try:
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#http://www.miosito.it/prova
@appWeb.route("/prova")
def prova():
    return "stringa da visualizzare come prova"

#http://www.miosito.it/presentazione
@appWeb.route("/presentazione")
def saluto():
    return "Buongiornoooooo"

@appWeb.route("/htmlsample")
def html():
    return "<html><body><h1>Titolo</h1><p>paragrafo da visualizzare</p><body></html>"


@appWeb.route("/indexhtml")
def funzionehtml():
    return render_template("index.html")


@appWeb.route("/login")
def login():
    return render_template("login.html")

@appWeb.route("/registrazione")
def registrazione():
    return render_template("registrazione.html")


@appWeb.route("/autenticazione", methods = ["POST"])
def autenticazione():
    usernameStr = request.form.get("username")
    passwordStr = request.form.get("password")
    for i in listaUser:
        u = i.getUsername()
        p = i.getPassword()
        if u == usernameStr and p == passwordStr:
            return render_template("home.html", paramUser = usernameStr)
                
    return render_template("fail.html") # messo fuori perché altrimenti non finisce il ciclo for, e si ferma alla prima iterazione
            
    '''if passwordStr == "123456":
        return render_template("home.html", paramUser = usernameStr)
    else:
        return render_template("fail.html")'''

    '''for i in listaUser:
        listaUser.append(usernameStr)
        return render_template("listaUser.html", paramUser = listaUser)'''

@appWeb.route("/saveuser", methods =["POST"])
def saveuser():
    usernameStr = request.form.get("username")
    passwordStr = request.form.get("password")
    emailStr = request.form.get("email")
    listaUser.append(User(usernameStr, passwordStr, emailStr))


    url ="https://nodered-65642.azurewebsites.net/ciaone?usernameStr={}&emailStr={}".format(usernameStr, emailStr)


# data = {'nome': 'anna', 'cognome': 'chiodo'}
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url)

#2) aggiungere il body alla req

#html = response.read()

    return render_template("listaUtenti.html", paramList = listaUser)

if __name__ == "__main__":
    # https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings
    # SERVER_PORT Read-only. The port the app should listen to.
    if "PORT" in os.environ:
        appWeb.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        appWeb.run(host="0.0.0.0")
