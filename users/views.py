from django.shortcuts import render


def login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def registration(request):
    return render(request, 'users/register.html')
