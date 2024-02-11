# Django Goodreads Scraper

This Django project is designed to scrape information about books and groups from Goodreads and display them on separate web pages. It also provides REST API endpoints to access the book and group information.

## Features

- **Scraping:** Utilizes a management command to scrape book and group information from Goodreads.
- **Web Interface:** Displays the scraped book and group information on separate web pages.
- **REST API:** Exposes REST API endpoints to retrieve book and group information.


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

1. Scrape books containing art, for example, in their title or groups containing art, for example, in their name:

```bash
python manage.py scrape book art
python manage.py scrape group art
```



8. Run the development server:
```bash
python manage.py runserver
```

## Web Interface
* Book list: http://127.0.0.1:8000/books/
* Group list: http://127.0.0.1:8000/groups/


## API Endpoints
* Book List: http://127.0.0.1:8000/api/books/
* Book Detail: http://127.0.0.1:8000/api/books/{book_id}/

* Group List: http://127.0.0.1:8000/api/groups/
* Group Detail: http://127.0.0.1:8000/api/groups/{group_id}/

Use tools like curl, httpie, or Postman to interact with the API.


## Django Admin
First create an admin user:
```bash
python manage.py createsuperuser
```
Then access the Django admin interface at http://127.0.0.1:8000/admin/ to manage books.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)