#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Author(models.Model):

    AuthorID = models.CharField('AuthorID',max_length=60,primary_key=True)
    Name = models.CharField('姓名',max_length=200,blank=True)
    Age = models.CharField('年龄',max_length=200,blank=True)
    Country = models.CharField('国籍',max_length=200,blank=True)
    
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name          
        db_table = "Author"
    
    def __unicode__(self):
        return self.Name
    
    
class Books(models.Model):

    ISBN          = models.CharField('ISBN',max_length=200,unique=True,primary_key=True)
    Title           = models.CharField('书名',max_length=200)
    AuthorID          = models.CharField('作者',max_length=200,blank=True)
    #Author = models.ForeignKey(Author.AuthorID, related_name='person_book')
    Publisher       = models.CharField('出版社',max_length=200,blank=True)
    Publishdate         = models.CharField('出版日期',max_length=200,blank=True)
    Price           = models.CharField('价格',max_length=200,blank=True)

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name        
        db_table = "Book"
    
    def __unicode__(self):
        return self.Title
    

    