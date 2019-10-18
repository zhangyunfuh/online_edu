from django.db import models
from datetime import datetime



class CityInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市名称",default='长沙')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name


class OrgInfo(models.Model):
    image = models.ImageField(upload_to='org/', max_length=200, verbose_name="机构封面")
    name = models.CharField(max_length=20, verbose_name="机构名称")
    course_num = models.IntegerField(default=0, verbose_name="课程数")
    study_num = models.IntegerField(default=0, verbose_name="学习人数")
    address = models.CharField(max_length=200, verbose_name="机构地址")
    desc = models.CharField(max_length=200, verbose_name="机构简介")
    detail = models.TextField(verbose_name='机构详情')
    love_num = models.IntegerField(default=0, verbose_name="收藏数")
    click_num = models.IntegerField(default=0, verbose_name="访问量")
    category = models.CharField(choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')), max_length=10,
                                verbose_name="机构类别")
    cityinfo = models.ForeignKey(CityInfo, verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name

class TeacherInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="教师姓名")
    image = models.ImageField(upload_to='teachers/%y/%m/%d', verbose_name="教师头像")
    age = models.IntegerField(default=30, verbose_name="教师年龄")
    work_year = models.IntegerField(default=3, verbose_name="工作年限")
    work_position = models.CharField(max_length=20, verbose_name="工作职位")
    work_company = models.CharField(max_length=20, verbose_name="就职公司")
    work_style = models.CharField(max_length=20, verbose_name="教学特点")
    click_num = models.IntegerField(default=0, verbose_name="访问量")
    love_num = models.IntegerField(default=0, verbose_name="收藏人数")
    gender = models.CharField(choices=(('boy','男'),('girl','女')),max_length=10,verbose_name="讲师性别",default='boy')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name