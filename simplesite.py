from flask import Flask

# This "__name__" gets the name of the Python script.
app=Flask(__name__)

# For the homepage
@app.route('/')

def home():
    return "This is a website!"

# When you execute a script, this is true.
# When  you import a script, __name__ is given the name of the script.
if __name__ == "__main__":
    app.run(debug=True)
