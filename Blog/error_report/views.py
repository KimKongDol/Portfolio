from django.shortcuts import render, get_object_or_404
from .models import ErrorReport
# Create your views here.


def error_index(request):
    all_errors = ErrorReport.objects.all()
    return render(request, 'error_index.html', {'all_errors': all_errors})


def error_detail(request, id):
    # 각 객체를 구분해주는 키 값과 아이디값이 같으면 가지고 오고 아니면 404에러띄움
    unit_error = get_object_or_404(ErrorReport, pk=id)
    return render(request, 'error_detail.html', {'unit_error': unit_error})
