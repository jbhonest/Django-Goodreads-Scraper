# Django Goodreads Scraper

This Django project is designed to scrape information about books from Goodreads and display it on a web page. It also provides a REST API endpoint to access the book information.

## Features

- **Scraping:** Utilizes a management command to scrape book information (title, author, average rating, cover image URL) from Goodreads.
- **Web Interface:** Displays the scraped book information on a web page.
- **REST API:** Exposes a REST API endpoint to retrieve book information.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jbhonest/django-goodreads-scraper.git
    ```

2. In **scraperproject** folder rename sample_settings.py to local_settings.py
3. Generate a SECRET_KEY and save it in local_settings.py

4. Navigate to the project directory:

```bash
cd django-goodreads-scraper
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Apply migrations to set up the database:
```bash
python manage.py migrate
```

7. Scrape books from Goodreads with the following management command:

```bash
python manage.py scrape_books
```

8. Run the development server:
```bash
python manage.py runserver
```

## Web Interface
* Open your browser and go to http://127.0.0.1:8000/ to access the web interface.


## API Endpoints
* Book List: http://127.0.0.1:8000/api/books
* Book Detail: http://127.0.0.1:8000/api/books/{book_id}/

Use tools like curl, httpie, or Postman to interact with the API.


## Django Admin
First create an admin user:
```bash
python manage.py createsuperuser
```
Then access the Django admin interface at http://127.0.0.1:8000/admin/ to manage books.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)