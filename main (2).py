from requests import get

class Author:
    def __init__(self, author_id: int, name: str, slug:str, api_books_url: str):
        self.author_id=author_id
        self.name=name
        self.api_books_url=api_books_url
        self.slug=slug

    def __str__(self):
        return f'{self.author_id}. {self.name}'

class WolneLekturyAdapter:
    API_URL ='https://wolnelektury.pl/api/'

    def get_authors(self, search: str = None):
        authors = []
        query = get(self.API_URL+'authors/')
        for author_id, author in enumerate(query.json(), start=1):
            if search is None or search.lower() in author['name'].lower():
                authors.append(Author(
                    author_id=author_id,
                    slug=author.get('slug'),
                    name= author.get('name'),
                    api_books_url= author.get('href') + 'books'
                ))

        return authors
    def get_books(self, author_slug: str):
        return get(f'{self.API_URL}authors/{author_slug}/books').json()
class Main:
    def main(self):
        adapter=WolneLekturyAdapter()
        authors = adapter.get_authors('Adam')
        for author in authors:
            print(author)

        query_author_id = int(input('Którego autora książki chcesz zobaczyć: '))
        found_author = next(filter(lambda x: x.author_id == query_author_id, authors))

        for book in adapter.get_books(found_author.slug):
            print(book['title'])

if __name__=='__main__':
    app=Main()
    app.main()