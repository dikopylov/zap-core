"""zapisator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from clients.views import ClientViewSet
from entries.car_entry.views import CarEntryViewSet
from entries.views import EntryViewSet
from files.views import UserFileViewSet
from locations.cities.views import CityViewSet
from locations.streets.views import StreetViewSet
from locations.views import LocationViewSet
from services.car_service.views import CarServiceViewSet
from services.views import ServiceViewSet
from suppliers.companies.views import CompanyViewSet
from suppliers.executors.human_executors.views import HumanExecutorViewSet
from suppliers.executors.schedules.views import ScheduleViewSet, LunchBreakViewSet
from suppliers.suppliers_employees.views import SupplierEmployeeViewSet
from suppliers.views import SupplierViewSet
from users.views import ConfirmEmailView
from zapisator import settings

router = routers.DefaultRouter()
router.register(r'supplier-employees', SupplierEmployeeViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'lunch-break', LunchBreakViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'car-services', CarServiceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'car-entries', CarEntryViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'streets', StreetViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'human-executors', HumanExecutorViewSet)
router.register(r'storage/users', UserFileViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Zapisator API",
      default_version='v1',
      description="Ядро Zapisator",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dikopylov10@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/register/', include('rest_auth.registration.urls')),
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
