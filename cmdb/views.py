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
        group_list = models.group.objects.all()

        # print(user_list.query)
        # QuerySet [obj,obj,]
        return render(request, 'user_info.html', {'user_list': user_list,'group_list': group_list})
     elif request.method == 'POST':
         u = request.POST.get('user')
         p = request.POST.get('pwd')
         e = request.POST.get('email')
         g = request.POST.get('gid')
         models.User.objects.create(username=u, password=p,email=e,gid_id=g)
         return redirect('/userinfo')
         # user_list = models.User.objects.all()
         # return render(request, 'user_info.html', {'user_list': user_list})


def groupinfo(request):
    if request.method == "GET":
        group_list = models.group.objects.all()
        # print(user_list.query)
        # QuerySet [obj,obj,]
        return render(request, 'usergroup_info.html', {'group_list': group_list})
    elif request.method == 'POST':
        gid= request.POST.get('id')
        models.group.objects.create(groupname=gid)
        return redirect('/groupinfo')
        # user_list = models.User.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})

def userdetail(request,nid):
    obj = models.User.objects.filter(id=nid).first()
    # 去单挑数据，如果不存在，直接报错
    # models.User.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})


def userdel(request,nid):
    models.User.objects.filter(id=nid).delete()
    return redirect('/userinfo')


def useredit(request,nid):
    if request.method == "GET":
        obj = models.User.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        g = request.POST.get('gid')
        models.User.objects.filter(id=nid).update(username=u, password=p,email=e,gid_id=g)
        return redirect('/userinfo')


def hostinfo(request):
    if request.method == "GET":
        host_list = models.host_list.objects.all()
        # print(user_list.query)
        # QuerySet [obj,obj,]
        return render(request, 'host_info.html', {'host_list': host_list})
    elif request.method == 'POST':
        type = request.POST.get('hosttype')
        hostname = request.POST.get('hostname')
        hip = request.POST.get('hostip')
        config = request.POST.get("hostconfig")
        idc = request.POST.get('idcid')
        managerid = request.POST.get('mid')

        models.host_list.objects.create(hosttype=type,
                                        hostname=hostname,
                                        hostip=hip,
                                        hostconfig=config,
                                        billing_idcid_id=idc,
                                        billing_managerid_id=managerid)
        return redirect('/hostinfo')
        # user_list = models.host_list.objects.all()
        # return render(request, 'host_info.html', {'host_list': host_list})


def hostdetail(request,nid):
    obj = models.host_list.objects.filter(id=nid).first()

    # 去单挑数据，如果不存在，直接报错
    # models.User.objects.get(id=nid)
    return render(request, 'host_detail.html', {'obj': obj})


def hostedit(request,nid):
    if request.method == "GET":
        obj = models.host_list.objects.filter(id=nid).first()
        return render(request, 'host_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        type = request.POST.get('hosttype')
        hostname = request.POST.get('hostname')
        hip = request.POST.get('hostip')
        config = request.POST.get("hostconfig")
        idc = request.POST.get('idcid')
        managerid = request.POST.get('mid')
        models.host_list.objects.filter(id=nid).update(hosttype=type,
                                                       hostname=hostname,
                                                       hostip=hip,
                                                       hostconfig=config,
                                                       billing_idcid_id=idc,
                                                       billing_managerid_id=managerid)
        return redirect('/hostinfo')


def hostdel(request,nid):
    models.host_list.objects.filter(id=nid).delete()
    return redirect('/hostinfo')




def idcinfo(request):
    return render(request, 'idc_info.html')


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
    # models.host_list.objects.create(hosttype="虚拟机",
    #                                      hostname="SHTW-Messagequeue12",
    #                                      hostip="10.10.201.111",
    #                                      hostconfig="vCPU*8,8G内存，150G HD",
    #                                      billing_idcid_id=1,
    #                                      billing_managerid_id=1)

    # dic = {'username': 'eric', 'password': '666'}
    # models.UserInfo.objects.create(**dic)
    #
    # obj = models.UserInfo(username='alex',password='123')
    # obj.save()
    #
    # #查

    ##跨表查
    hostobj = models.host_list.objects.all()

    # result = models.User.objects.filter(id=1).first()
    # result = models.User.objects.all()
    # result = models.UserInfo.objects.filter(username='root',password='123')
    #
    # result,QuerySet => Django => []
    # [obj(id,username,password),obj(id,username,password), obj(id,username,password)]
    # for row in result:
    #     print(row.id,row.username,row.password,row.email,row.gid_id)
    # print(result)
    #
    # #删除
    # models.UserInfo.objects.filter(username="alex").delete()
    #
    # #更新
    # models.UserInfo.objects.filter(id=3).update(password="69")
    #
    return HttpResponse(hostobj.values())




