from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  cmdb import models


def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        obj = models.User.objects.filter(username=user, password=pwd).first()
        if obj:
            # 去跳转到
            return redirect('/home')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"
    return render(request,'login.html', {'error_msg': error_msg})




def home(request):
    return render(request,'home.html')

def userinfo(request):
     if request.method == "GET":
        user_list = models.User.objects.all()
        # print(user_list.query)
        # QuerySet [obj,obj,]
        return render(request, 'user_info.html', {'user_list': user_list})
     elif request.method == 'POST':
         u = request.POST.get('user')
         p = request.POST.get('pwd')
         e = request.POST.get('email')
         g = request.POST.get('gid')
         models.User.objects.create(username=u, password=p,email=e,gid_id=g)
         return redirect('/userinfo')
         # user_list = models.User.objects.all()
         # return render(request, 'user_info.html', {'user_list': user_list})


def userdetail(request):
    return render(request,'home.html')

def userdel(request):
    return render(request,'home.html')

def useredit(request):
    return render(request,'home.html')






def orm(request):
    # 创建
    # group1 = models.group.objects.create(groupname='超级管理员')
    # group2 = models.group.objects.create(groupname='管理员')
    # models.User.objects.create(
    #     username='yanglc',
    #     password='123',
    #     email='yangc@taiwu.com',
    #     gid_id=2)
    # models.User.objects.create(username='wangzx', password='123', email='wangzx@taiwu.com', gid_id=2)



    # dic = {'username': 'eric', 'password': '666'}
    # models.UserInfo.objects.create(**dic)
    #
    # obj = models.UserInfo(username='alex',password='123')
    # obj.save()
    #
    # #查
    result = models.User.objects.all()
    # result = models.UserInfo.objects.filter(username='root',password='123')
    #
    # result,QuerySet => Django => []
    # [obj(id,username,password),obj(id,username,password), obj(id,username,password)]
    for row in result:
        print(row.id,row.username,row.password,row.email,row.gid_id)
    print(result)
    #
    # #删除
    # models.UserInfo.objects.filter(username="alex").delete()
    #
    # #更新
    # models.UserInfo.objects.filter(id=3).update(password="69")
    #
    return HttpResponse(result.values())




