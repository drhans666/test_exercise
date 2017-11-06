from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


def parser(event):
    text = event.split()
    categories = []
    persons = []

    for i in text:
        if i.startswith('@'):
            i = i[1:]
            persons.append(i)
        if i.startswith('#'):
            i = i[1:]
            categories.append(i)
    return categories, persons
