#encoding=utf-8

from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        '''
        :summary: 返回对象的字符串表示
        '''
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, verbose_name="e-mail")

    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)    # 与Author是多对多关系
    publisher = models.ForeignKey(Publisher)    # 外键，对应Publisher
    publication_date = models.DateField(blank=True, null=True)  # 允许为空

    def __unicode__(self):
        return self.title