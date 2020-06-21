from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)
STATIC_URL = '/static/'  

# ** Home Page 
@app.route('/')
def home():
    return render_template('index.html')
    

# *! About Page
@app.route('/about/')
def about():
    return "About Page Here"
    

if __name__ == "__main__":
    app.run(debug=True)