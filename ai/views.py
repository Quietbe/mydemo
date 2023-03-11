from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.


class LoginView(View):

    def get(self, request):

        return render(request, 'index.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/ai/index/')
        else:
            return render(request, 'index.html', {'error': '用户名或密码错误'})


class IndexView(LoginRequiredMixin, View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'index_.html')

    def post(self, request):
        return HttpResponse('这是index的 post页面')


from ai.abc import Gpt

class GetView(LoginRequiredMixin, View):

    def get(self, request):
        return HttpResponse('Get页面，为登录进入不了')

    def post(self, request):
        data = request.POST.get('text')
        content, data = Gpt.generate_text(self, data)
        content = {
            'content': content
        }
        print(data)
        # print(f"接收到的数据{data}")
        return JsonResponse(content)


class LogoutView(View):
    """退出登录"""
    def get(self, request):
        logout(request)
        return redirect(reverse('ai:index'))

    def post(self,request):
        logout((request))
        return redirect(reverse('ai:index'))
