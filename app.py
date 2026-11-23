from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    if request.method == "POST":
        nama = request.form["nama"].title()
    return render_template("index.html", nama=nama)

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"

@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return '''
    <form method="post">
      <input name="name">
      <button>Send</button>
    </form>'''

if __name__ == "__main__":
    app.run(debug=True)

