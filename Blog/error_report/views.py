from django.shortcuts import render, get_object_or_404, redirect
from .models import ErrorReport
# Create your views here.


def error_index(request):
    all_errors = ErrorReport.objects.all()
    return render(request, 'error_index.html', {'all_errors': all_errors})


def error_detail(request, id):
    # 각 객체를 구분해주는 키 값과 아이디값이 같으면 가지고 오고 아니면 404에러띄움
    unit_error = get_object_or_404(ErrorReport, pk=id)
    return render(request, 'error_detail.html', {'unit_error': unit_error})


def error_new(request):
    return render(request, 'error_new.html')


def error_create(request):
    new_error = ErrorReport()  # 새 객체 생성
    new_error.title = request.POST['title']
    new_error.lang = request.POST['lang']
    new_error.error = request.POST['error']
    new_error.sol = request.POST['sol']
    new_error.how = request.POST['how']
    new_error.image = request.FILES['image']
    new_error.save()
    return redirect('error:error_detail', new_error.id)


def error_edit(request, id):
    edit_error = ErrorReport.objects.get(id=id)
    return render(request, 'error_edit.html', {'edit_error': edit_error})


def error_update(request, id):
    update_error = ErrorReport.objects.get(id=id)  # 새 객체 생성
    update_error.title = request.POST['title']
    update_error.lang = request.POST['lang']
    update_error.error = request.POST['error']
    update_error.how = request.POST['sol']
    update_error.how = request.POST['how']
    update_error.save()
    return redirect('error:error_detail', new_error.id)


def error_delete(request, id):
    del_error = ErrorReport.objects.get(id=id)
    del_error.delete()
    return redirect('error:error_index')
