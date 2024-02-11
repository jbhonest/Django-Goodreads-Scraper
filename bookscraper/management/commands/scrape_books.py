import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from bookscraper.models import Book
from scraperproject.local_settings import PAGE_COUNT


class Command(BaseCommand):
    help = 'Scrape book list from goodreads.com and store in the database'

    def handle(self, *args, **options):

        # List of URLs to scrape
        urls = [
            f"https://www.goodreads.com/list/show/449.Must_Read_Classics?page={i}" for i in range(1, PAGE_COUNT+1)]

        try:
            # Removing all the existing records in the table
            Book.objects.all().delete()

            for url in urls:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Extracting data from {url}")

                    soup = BeautifulSoup(response.text, "html.parser")
                    books = soup.find_all(
                        "tr", itemscope=True, itemtype="http://schema.org/Book")

                    for book in books:

                        # Extracting book title
                        title_tag = book.find("span", itemprop="name")
                        title = title_tag.text.strip(
                        ) if title_tag else None

                        # Extracting author
                        author_tag = book.find("span", itemprop="author")
                        author = (
                            author_tag.find(
                                "span", itemprop="name").text.strip()
                            if author_tag else None
                        )

                        # Extracting book rating
                        rating_tag = book.find("span", class_="minirating")
                        if rating_tag:
                            rating_text = rating_tag.text.strip().split()
                            try:
                                average_rating = float(rating_text[0])
                            except:
                                average_rating = -1
                        else:
                            average_rating = None

                        # Extracting book cover image URL
                        cover_img_tag = book.find("img", itemprop="image")
                        cover_image_url = (
                            cover_img_tag["src"] if cover_img_tag else None
                        )

                        # Creating Book object
                        Book.objects.create(
                            title=title,
                            author=author,
                            average_rating=average_rating,
                            cover_image_url=cover_image_url
                        )

                else:
                    print(f"Failed to download HTML code from {url}")
                    return
            self.stdout.write(self.style.SUCCESS(
                'Successfully scraped and stored book list.'))
        except Exception as exp:
            print(exp)
