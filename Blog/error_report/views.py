from django.shortcuts import render
from .models import ErrorReport
# Create your views here.


def error_index(request):
    all_errors = ErrorReport.objects.all()
    return render(request, 'error_index.html', {'all_errors': all_errors})
