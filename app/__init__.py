from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:black'>do i have to sudo restart everytime lol  WSHOW UP DATES NOW PLEASEASUGFIUESGFUISGRHFUISGRIUFBPLEASE WOROOOK I love that this works!! Hello There!</h1>"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=3000)
