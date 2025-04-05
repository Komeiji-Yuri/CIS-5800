"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest
from django.http import HttpResponse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )