"""
Definition of urls for CIS_5800___Group_Project.
"""

from django.urls import path, include

urlpatterns = [
    path('', include('app.urls'))
]
