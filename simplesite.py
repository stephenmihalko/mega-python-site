# render_template accesses an HTML file stored in the system and displays it
from flask import Flask, render_template

# This "__name__" gets the name of the Python script.
app=Flask(__name__)

# For the homepage
@app.route('/')

def home():
    # This needs to be a real thing in the "templates" folder.
    return render_template("home.html")

# When you execute a script, this is true.
# When  you import a script, __name__ is given the name of the script.
if __name__ == "__main__":
    app.run(debug=True)
