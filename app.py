import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

@app.route('/')
def home():
    # Ye ab templates folder se index.html uthayega
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        mobile = request.form.get('mobile')

        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, password, mobile) VALUES (%s, %s, %s, %s)",
                    (name, email, password, mobile))
        conn.commit()
        cur.close()
        conn.close()
        
        return "<h1>Data Save ho gaya!</h1><br><a href='/'>Wapas form par jayein</a>"
    
    except Exception as e:
        return f"<h1>Error aaya:</h1> {str(e)}<br><a href='/'>Try again</a>"

if __name__ == '__main__':
    app.run()