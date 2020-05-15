from allauth.account.adapter import get_adapter
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.http import Http404
from django.shortcuts import redirect
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class ConfirmEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, *args, **kwargs):
        try:
            return self.post(*args, **kwargs)
        except Http404:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(self.request)

        redirect_url = self.get_redirect_url()
        return redirect(redirect_url)

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise Http404()
        return emailconfirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

    def get_redirect_url(self):
        return get_adapter(self.request).get_email_confirmation_redirect_url(
            self.request)
