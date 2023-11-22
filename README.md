# Introduction
This README provides detailed instructions on how to set up and run the YouthLab project on your local machine. 
The YouthLab project is a web application built with Flask, a lightweight WSGI web application framework in Python.

## Prerequisites
Before you begin, ensure you have the following installed on your local machine:

Python (version 3.x)
pip (Python package manager)
Git (version control system)

## Step-by-Step Guide
### 1. Clone the Repository
First, clone the YouthLab repository to your local machine using Git:

git clone [repository URL]

### Navigate to the cloned directory:

cd YouthLab

### 2. Set Up a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment for Python projects. 
This keeps your dependencies organized and separate from other projects. To create and activate a virtual environment, run:

python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

### 3. Install Dependencies
Install the necessary Python packages using pip:

pip install -r requirements.txt

Note: The project should include a requirements.txt file listing all the necessary packages. If it's missing, you'll need to install Flask (pip install flask) and any other required packages individually.

### 4. Run the Application
Start the Flask application with:

python app.py

After running this command, you should see output indicating that the server is running, typically on http://127.0.0.1:5000.