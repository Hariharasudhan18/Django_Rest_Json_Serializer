from django.urls import path, include

from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'', views.EmployeeViewSet)


urlpatterns = [
    path('', views.homePageView),
    # path('', views.employee),
    # path('', include('employee.urls')),
    path('employee/', include(router.urls))
]