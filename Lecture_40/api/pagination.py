from rest_framework.pagination import PageNumberPagination

class MyPagePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 6
    last_page_strings= 'end'