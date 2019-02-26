from flask import flask

app=Flask(__name__)

# For the homepage
@app.route('/')

def home():
    return "This is a website!"

if __name__ == "__main__":
    app.run(debug=True)
