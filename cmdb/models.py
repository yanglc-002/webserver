from django.db import models

# Create your models here.

class group(models.Model):
    # gid = models.AutoField(primary_key=True)
    groupname = models.CharField(max_length=32)
    groupcreate_data = models.DateTimeField(auto_now_add=True, null=True)
    groupupdate_data = models.DateTimeField(auto_now_add=True, null=True)

class User(models.Model):
    # uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=32)
    gid = models.ForeignKey(to="group",on_delete=models.CASCADE)




class host_idc(models.Model):
    # 自定义自增列
    # id = models.AutoField(primary_key=True)
    idcname = models.CharField(max_length=64)
    idcagent = models.CharField(max_length=64)
    idcaddress = models.CharField(max_length=64)
    # billing_hostid = models.ForeignKey(to="host_list",on_delete=models.CASCADE)


class host_manager(models.Model):
    # id = models.AutoField(primary_key=True)
    hostuser =  models.CharField(max_length=64)
    hostpasswd = models.CharField(max_length=64)
    hostport = models.IntegerField()
    # shipping_hostid = models.ForeignKey(to="host_list",to_field='id')
    # hostlistid = models.ForeignKey(to="host_list",on_delete=models.CASCADE)

class host_list(models.Model):
    # id = models.AutoField(primary_key=True)
    hosttype =  models.CharField(max_length=64)
    hostname =  models.CharField(max_length=64)
    hostip =  models.GenericIPAddressField(protocol="ipv4",db_index=True)
    hostconfig = models.CharField(max_length=64)
    hostcreate_data =models.DateTimeField(auto_now_add=True)
    hostupdate_data = models.DateTimeField(auto_now_add=True)
    billing_idcid = models.ForeignKey(to="host_idc",on_delete=models.CASCADE)
    billing_managerid = models.ForeignKey(to="host_manager",on_delete=models.CASCADE)


