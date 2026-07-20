import os
import psycopg2
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Render mein set ki gayi DATABASE_URL ka use karo
DATABASE_URL = os.environ.get('DATABASE_URL')

@app.route('/')
def home():
    with open('index.html', 'r') as f:
        return render_template_string(f.read())

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # HTML form se data uthao
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        mobile = request.form.get('mobile')

        # Neon se connect karo
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Table mein insert karo
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