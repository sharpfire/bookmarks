from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(User,related_name='actions',db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj')
    #target_ct：一个ForeignKey字段指向ContentType模型（model）。
    target_id = models.PositiveIntegerField(blank=True,null=True,db_index=True)
    #target_id：一个PositiveIntegerField用来存储被关联对象的primary key。
    target = GenericForeignKey('target_ct','target_id')
    #target：一个GenericForeignKey字段指向被关联的对象基于前面两个字段的组合之上。
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    class Meta:
        ordering = ('-created',)


