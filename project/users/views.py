from django.shortcuts import render

# Create your views here.
def mypage(request):
    user = request.user
    return render(request, 'users/mypage.html', {'user' : user})
