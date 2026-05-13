# Economy & Emissions

## Project Overview
This project is a Flask-based data visualization website that examines the relationship between economic growth and greenhouse gas emissions across countries. The website investigates whether countries with higher economic activity tend to emit more greenhouse gases, using datasets on GDP, population and greenhouse gas emissions. Users can explore datasets, visualizations, and website tracking statistics through multiple web pages.  

## Website Features
- “Home” page introducing the overall project
- “About” page explaining the research topic 
- “Data” page describing datasets and displaying sample database records
- “Visualization” page showing scatter plots of GDP and greenhouse gas emissions
- ”Tracking” page displaying website visit statistics 

## Client-side Components
The client-side of the project was built using HTML and CSS. HTML templates were used to structure the web pages, including navigation bars, tables, graphs, and content sections. CSS was used to style the website with a consistent green-themed design and organized page layouts, including card-based sections. 

## Server-side Components
The server-side of the project was built using Flask and SQLite. Flask was used to connect different web pages and display HTML templates. SQLite was used to store project data and website tracking information. Flask also retrieves data from the database and displays it on the website pages. 

## Interaction between Client and Server Components
When a user visits a webpage, the browser sends a request to the Flask server. The flask application processes the request, retrieves data from the SQLite database if needed, and renders the appropriate HTML template. The rendered webpage is then sent back to the browser and displayed to the user. 

## Data Sources
The project uses datasets from:
- UNFCCC greenhouse gas emissions data
- WorldBank GDP data
- WorldBank Population data

## Technologies Used 
- Python 
- Flask
- SQLite
- HTML
- CSS
- Pandas
- Matplotlib

## How to Run
1. Install required packages:
pip install -r requirements.txt
2. Run the Flask application:
python app.py
3. Open the browser and visit:
http://127.0.0.1:5000/

