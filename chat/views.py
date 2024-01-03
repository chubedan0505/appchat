# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#Xử lý dữ liệu khi bấm login nó sẽ lấy dữ liệu từ setting vào để tiến hành vào trang chat page
 
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)