from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    pass

# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 4
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6