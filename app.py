from flask import Flask, render_template
import sqlite3

app = Flask (__name__)  

conn = sqlite3.connect("stage2_data_analysis/database.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS visits (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               page TEXT
               )
               """)

conn.commit()
conn.close()

@app.route("/") 
def index():
    conn = sqlite3.connect("stage2_data_analysis/database.db")
    conn.execute("INSERT INTO visits (page) VALUES ('Home')")
    conn.commit()
    conn.close()
    return render_template("index.html")    

@app.route("/about")
def about():
    conn = sqlite3.connect("stage2_data_analysis/database.db")
    conn.execute("INSERT INTO visits (page) VALUES ('About')")
    conn.commit()
    conn.close()
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect("stage2_data_analysis/database.db")
    conn.execute("INSERT INTO visits (page) VALUES ('Data')")
    data = conn.execute("SELECT * FROM indicator LIMIT 20").fetchall()
    conn.commit()
    conn.close()
    return render_template("data.html", data=data)
                           
@app.route("/visualizations")
def visualizations():
    conn = sqlite3.connect("stage2_data_analysis/database.db")
    conn.execute("INSERT INTO visits (page) VALUES ('Visualizations')")
    conn.commit()
    conn.close()
    return render_template("visualizations.html")

@app.route("/tracking")
def tracking():
    conn = sqlite3.connect("stage2_data_analysis/database.db")

    tracking_data = conn.execute("""
                                 SELECT page, COUNT(*)
                                 FROM visits
                                 GROUP BY page
                                 """).fetchall()
    conn.close()
    return render_template("tracking.html", tracking_data=tracking_data)

if __name__ == "__main__":
    app.run(debug=True)

    