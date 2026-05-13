from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask (__name__)  
DB_PATH = "stage2_data_analysis/database.db"

def record_visit(page):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
               CREATE TABLE IF NOT EXISTS visits (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               page TEXT
               )
               """)
    conn.execute("INSERT INTO visits (page) VALUES (?)", (page,))
    conn.commit()
    conn.close()

@app.route("/") 
def index():
    record_visit("Home")
    return render_template("index.html")    

@app.route("/about")
def about():
    record_visit("About")
    return render_template("about.html")

@app.route("/data")
def data():
    record_visit("Data")
    df = pd.read_csv("stage2_data_analysis/final_merged_data.csv")
    data = df [["Country Name", "Year", "GDP", "Population", "GHG"]].head(20).values.tolist()
    return render_template("data.html", data=data)
                           
@app.route("/visualizations")
def visualizations():
    record_visit("Visualizations")
    return render_template("visualizations.html")

@app.route("/tracking")
def tracking():
    conn = sqlite3.connect(DB_PATH)

    tracking_data = conn.execute("""
                                 SELECT page, COUNT(*)
                                 FROM visits
                                 GROUP BY page
                                 """).fetchall()
    conn.close()
    return render_template("tracking.html", tracking_data=tracking_data)

if __name__ == "__main__":
    app.run(debug=False)


    