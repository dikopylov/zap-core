from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param

from utils.mixins.datetime import DateTimeMixin
from utils.mixins.soft_deletion import SoftDeletionMixin


class BaseModel(SoftDeletionMixin, DateTimeMixin):
    class Meta:
        abstract = True


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'first': self.get_first_link(),
                'previous': self.get_previous_link(),
                'current': self.get_current_link(),
                'next': self.get_next_link(),
                'last': self.get_last_link(),
                'total': self.page.paginator.count,
                'current_page': self.page.number,
                'last_page': self.page.paginator.num_pages,
                'per_page': self.page.paginator.per_page
            },

            'results': data
        })

    def get_first_link(self):
        if not self.page.paginator.num_pages > 0:
            return None

        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.page_query_param)

    def get_last_link(self):
        if not self.page.paginator.num_pages > 0:
            return None

        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, self.page.paginator.num_pages)

    def get_current_link(self):
        if not self.page.number > 0:
            return None

        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, self.page.number)
