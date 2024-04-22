# Bank Transactions Django Project

This Django project is designed to store transaction details exported from a bank in an Excel file into a database.

## Setup

1. Clone the repository:

2. Install dependencies:

3. Run migrations:

4. Create a superuser to access the admin panel:

5. Start the Django development server:

6. Navigate to `http://127.0.0.1:8000/admin/` in your browser to access the admin panel. Log in with the superuser credentials created in step 4.

## Usage

1. Upload Transaction Data:
- Navigate to `http://127.0.0.1:8000/transactions/upload/` in your browser.
- Choose an Excel file containing transaction details and click "Upload".
- Once uploaded, the transactions will be stored in the database.

2. View Transactions:
- Navigate to the admin panel (`http://127.0.0.1:8000/admin/`) to view, add, edit, or delete transactions.

## Project Structure

- `bank_transactions/`: Django project directory.
- `transactions/`: Django app directory for handling transactions.
- `models.py`: Defines the `Transaction` model.
- `views.py`: Defines views for uploading transaction data.
- `forms.py`: Defines forms for file uploads.
- `admin.py`: Registers the `Transaction` model with the admin panel and customizes its display.
- `urls.py`: Defines URL patterns for the transactions app.
- `templates/`: Directory for HTML templates.
 - `upload.html`: Template for uploading transaction data.
 - `success.html`: Template for success message after uploading.

## Dependencies

- Django: Web framework for building the project.
- pandas: Library for data manipulation, used for reading Excel files.
