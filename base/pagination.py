from django.core.paginator import Paginator
from rest_framework import pagination
from rest_framework.response import Response

class PokemonSimulatorPagination(Paginator):
    """
    p.count
        4
    p.num_pages
        2
    type(p.page_range)
        <class 'range_iterator'>
    p.page_range
        range(1, 3)

    page1 = p.page(1)

    page1
        <Page 1 of 2>

    page1.object_list
        ['john', 'paul']

    page2 = p.page(2)

    page2.object_list
        ['george', 'ringo']

    page2.has_next()
        False

    page2.has_previous()
        True

    page2.has_other_pages()
        True

    page2.next_page_number()
        EmptyPage: That page contains no results

    page2.previous_page_number()
        1

    page2.start_index()  # The 1-based index of the first item on this page
        3

    page2.end_index()  # The 1-based index of the last item on this page
        4
    """

    def __init__(self, objects, page_object_count):
        super().__init__(objects, page_object_count)