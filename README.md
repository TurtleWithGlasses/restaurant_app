**Restaurant Management Web Application**

This is a simple restaurant management web application that allows users to select food, drink, and dessert items, calculate totals including VAT, and generate a receipt. The application also saves each order to a SQLite database.

Features

Menu Selection: Users can choose food, drink, and dessert items from the menu.
Order Processing: Orders are processed, and preparation times are simulated.
Order Status: Items show status as "Being Prepared" and then "READY" when completed.
Receipt Generation: A receipt is generated and displayed once the order is ready.
Database Storage: Orders and their details are saved in a SQLite database.

Technologies Used

Frontend: HTML, CSS, Jinja2 templating
Backend: Flask (Python)
Database: SQLite
Other: SQLAlchemy ORM, Python subprocess for worker simulation

Installation Prerequisites
Python 3.7 or higher
Flask
SQLAlchemy

Setup
1-Clone the repository:
  git clone https://github.com/TurtleWithGlasses/restaurant-management-app.git
  cd restaurant-management-app

2-Create and activate a virtual environment:
  python3 -m venv my-virtualenv
  source my-virtualenv/bin/activate  # On Windows use `my-virtualenv\Scripts\activate`
3-Install dependencies:
  pip install -r requirements.txt
4-Set up the database:
  If you're running the app for the first time, the database will be created automatically. However, if you want to start with an existing database, upload it to your project directory.
5-Run the application:
  flask run
  Open your web browser and go to http://127.0.0.1:5000/.

Deployment
PythonAnywhere
1-Create a PythonAnywhere account and set up a new web app using Flask.
2-Upload your project files to your PythonAnywhere project directory.
3-Install dependencies using the provided requirements.txt:
  pip install -r requirements.txt
4-Configure your web app to point to your Flask application.
5-Run database migrations (if necessary) and ensure all files are correctly referenced.

Notes:
Make sure that your SQLALCHEMY_DATABASE_URI is correctly set to point to the database file on the server.
Ensure that worker.py is correctly located and accessible in the deployed environment.
Project Structure

restaurant-management-app/
├── app.py                 # Main Flask application
├── worker.py              # Worker process for handling orders
├── menu_data.py           # Menu data dictionaries
├── models.py              # SQLAlchemy database models
├── requirements.txt       # Python dependencies
├── restaurant.db          # SQLite database file (auto-created)
├── templates/
│   └── index.html         # Main HTML template
└── static/                # Static files (CSS, JS, images)

Usage
Select Menu Items: Choose quantities for food, drinks, and desserts.
Calculate Order: Click "Calculate & Save Order" to process the order.
Order Processing: The order will be processed, and the status will update.
Receipt: Once ready, a receipt will be displayed with order details and total amount.

Issues & Troubleshooting
Receipt Not Showing: Ensure the worker process is correctly handling the order and returning the expected status.
Database Issues: Verify that the database is correctly set up and accessible by the Flask app.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to PythonAnywhere for providing a platform to deploy this project.
Inspired by various restaurant management systems and tutorials.
