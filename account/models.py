from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



class Contact(models.Model):
   user_from = models.ForeignKey(User,
                                 related_name='rel_from_set')
   user_to = models.ForeignKey(User,
                               related_name='rel_to_set')
   created = models.DateTimeField(auto_now_add=True,
                                  db_index=True)
   class Meta:
       ordering = ('-created',)
   def __str__(self):
       return '{} follows {}'.format(self.user_from,self.user_to)


# Add following field to User dynamically
User.add_to_class('following',
                   models.ManyToManyField('self',
                                          through=Contact,
                                          related_name='followers',
                                          symmetrical=False))
#你能看到上述代码中的关系包含了symmetrical=Flase来定义一个非对称（non-symmetric）
#关系。这表示如果我关注了你，你不会自动的关注我。

#如果你想要使用你的定制用户模型（model），可以访问
# https://docs.djangoproject.com/en/1.8/topics/auth/
# customizing/#specifying-a-custom-user-model
# 获得更多信息。



