from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"


# --------------------
# HOME PAGE
# --------------------
@app.route("/")
def home():
    return """
    <h1>GLA Lost & Found 🚀</h1>
    <a href='/login'>Login</a> |
    <a href='/dashboard'>Dashboard</a> |
    <a href='/logout'>Logout</a>
    """


# --------------------
# LOGIN PAGE
# --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple demo authentication
        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials"

    return """
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit">Login</button>
    </form>
    """


# --------------------
# DASHBOARD
# --------------------
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"<h2>Welcome {session['user']} 👋</h2>"
    else:
        return redirect(url_for("login"))


# --------------------
# LOGOUT
# --------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# --------------------
# LOCAL RUN ONLY
# --------------------
if __name__ == "__main__":
    app.run(debug=True)
