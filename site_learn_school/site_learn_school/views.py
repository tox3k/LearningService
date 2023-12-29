from django.shortcuts import render

def main_page_teacher(request):
    return render(request, 'teachers.html')

def main_page_student(request):
    return render(request, 'home.html')

def sign_in(request):
    return render(request, 'ending.html')

def results_test(request):
    return render(request, 'result.html')

def test(request):
    return render(request, 'test.html')

def test_done(request):
    return render(request, 'ending.html')