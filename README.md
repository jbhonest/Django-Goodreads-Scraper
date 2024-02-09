# Django Goodreads Scraper

This Django project is designed to scrape information about books from Goodreads and display it on a web page. It also provides a REST API endpoint to access the book information.

## Features

- **Scraping:** Utilizes a management command to scrape book information (title, author, average rating, cover image URL) from Goodreads.
- **Web Page:** Displays the scraped book information on a web page.
- **REST API:** Exposes a REST API endpoint to retrieve book information.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Requests
- BeautifulSoup
- Django Rest Framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/django-goodreads-scraper.git
    cd django-goodreads-scraper
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the admin interface at `http://127.0.0.1:8000/admin/` to add books manually or use the management command to scrape them.

7. Access the web page at `http://127.0.0.1:8000/bookscraper/book-list/` to view the scraped books.

8. Access the API at `http://127.0.0.1:8000/bookscraper/api/books/` to retrieve book information via the REST API.

## Usage

### Scraping Books

To scrape books from Goodreads, run the following management command:

```bash
python manage.py scrape_books
