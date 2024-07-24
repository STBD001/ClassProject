from requests import get

def get_authors(search: str = None):
    authors = []
    query = get('https://wolnelektury.pl/api/authors/')
    for author_id, author in enumerate(query.json(), start=1):
        if search is None or search.lower() in author['name'].lower():
            authors.append({
                'author_id': author_id,
                'name': author.get('name'),
                'api_books_url': author.get('href') + 'books/'
            })

    return authors

authors = get_authors('Adam')
for author in authors:
    print(f'{author.get("author_id")}. {author.get("name")}')

query_author_id = int(input('Którego autora książki chcesz zobaczyć: '))
found_author = next(filter(lambda x: x.get('author_id') == query_author_id, authors))

for book in get(found_author.get('api_books_url')).json():
    print(book['title'])
