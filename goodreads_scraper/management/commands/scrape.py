import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from goodreads_scraper.models import Book, Group
from scraperproject.local_settings import PAGE_COUNT


class Command(BaseCommand):
    help = 'Scrape books or groups information from goodreads.com and store them in database'

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(
            dest='subcommand', help='Subcommands')

        # Add the 'book' subcommand
        book_parser = subparsers.add_parser('book', help='Search a book')
        book_parser.add_argument(
            'book_name', type=str, help='Name of the book')

        # Add the 'group' subcommand
        group_parser = subparsers.add_parser(
            'group', help='Search a group')
        group_parser.add_argument(
            'group_name', type=str, help='Name of the group')

    def handle(self, *args, **options):
        subcommand = options['subcommand']

        if subcommand == 'book':
            book_name = options['book_name']
            self.handle_book(book_name)
        elif subcommand == 'group':
            group_name = options['group_name']
            self.handle_group(group_name)
        else:
            self.stdout.write(self.style.ERROR('Invalid subcommand'))

    def handle_book(self, book_name):

        # List of URLs to scrape
        urls = [
            f"https://www.goodreads.com/search?query={book_name}&search_type=books&tab=books&page={i}" for i in range(1, PAGE_COUNT+1)]

        try:
            # Removing all the existing records
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
                'Successfully scraped and stored books information.'))
        except Exception as exp:
            print(exp)

    def handle_group(self, group_name):
        # List of URLs to scrape
        urls = [
            f"https://www.goodreads.com/search?query={group_name}&search_type=groups&tab=groups&page={i}" for i in range(1, PAGE_COUNT+1)]

        try:
            # Removing all the existing records
            Group.objects.all().delete()

            for url in urls:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Extracting data from {url}")

                    soup = BeautifulSoup(response.text, "html.parser")
                    groups = soup.find_all("tr")

                    for group in groups:

                        # Extracting group name
                        name_tag = group.find("a",  class_='groupName')
                        name = name_tag.text.strip() if name_tag else None

                        # Extracting group members
                        members_tag = group.find("span", class_="greyText")
                        if members_tag:
                            members_text = members_tag.text.strip().split()
                            try:
                                members = int(members_text[0])
                            except:
                                members = -1
                        else:
                            members = None

                        # Extracting group cover image URL
                        cover_img_tag = group.find("img")
                        cover_image_url = (
                            cover_img_tag["src"] if cover_img_tag else None
                        )

                        # Creating Group object
                        Group.objects.create(
                            name=name,
                            members=members,
                            cover_image_url=cover_image_url
                        )

                else:
                    print(f"Failed to download HTML code from {url}")
                    return
            self.stdout.write(self.style.SUCCESS(
                'Successfully scraped and stored groups information.'))
        except Exception as exp:
            print(exp)
