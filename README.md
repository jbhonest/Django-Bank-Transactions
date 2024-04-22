# Django Bank Transactions

This Django project is designed to store transaction details exported from a bank in an Excel file into a database.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/jbhonest/django-bank-transactions.git
```
2. Navigate to the project directory:

```bash
cd django-bank-transactions
```
3. In **bank_transactions** folder rename sample_settings.py to local_settings.py

4. Generate a SECRET_KEY and save it in local_settings.py

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

8. Start the Django development server:
```bash
python manage.py runserver
```

9. Navigate to `http://127.0.0.1:8000/admin/` in your browser to access the admin panel. Log in with the superuser credentials created in step 4.

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
