from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vare')
def vare():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Vare")
    varer = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('vare.html', varer=varer)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
