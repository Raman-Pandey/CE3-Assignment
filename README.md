# VE3 ASSIGNMENT

This is the assignment of VE3 for the role of pyhton developer intern.This is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Requirements

1. **Django Setup:**
    - Create a Django project and a Django app within the project.
    - Configure the project with a database (SQLite is used by default).

2. **File Upload Feature:**
    - Implement a form that allows users to upload CSV files.
    - Store the uploaded files temporarily for processing.

3. **Data Processing:**
    - Use pandas to read the uploaded CSV file.
    - Perform basic data analysis tasks such as:
        - Displaying the first few rows of the data.
        - Calculating summary statistics (mean, median, standard deviation) for numerical columns.
        - Identifying and handling missing values.

4. **Data Visualization:**
    - Generate basic plots using matplotlib or seaborn (integrated with pandas) such as:
        - Histograms for numerical columns.
    - Display the plots on the web page.

5. **User Interface:**
    - Use Django templates to create a simple and user-friendly interface.
    - Display the data analysis results and visualizations in a clear and organized manner.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/django-csv-analysis.git
    cd django-csv-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/UploadFile` to see the application.

## Usage

1. **Upload a CSV File:**
    - Navigate to the upload page.
    - Select a CSV file to upload.

2. **View Analysis Results:**
    - After uploading, the application will display:
        - The first few rows of the data.
        - Summary statistics (mean, median, standard deviation) for numerical columns.
        - Information about missing values.
        - Basic plots such as histograms for numerical columns.

## Project Structure

- `project/` - Django project directory.
- `app/` - Django app directory containing:
  - `templates/app` - HTML templates.
  - `views.py` - View functions for handling requests.
  - `forms.py` - Form definitions.
  - `urls.py` - URL routing.
- `manage.py` - Django management script.

## Dependencies

- Django
- pandas
- numpy
- matplotlib
- seaborn


