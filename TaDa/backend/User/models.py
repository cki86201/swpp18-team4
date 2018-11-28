from django.db import models
from django_mysql.models import EnumField, ListCharField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, user_type, email, nickname, password = None):
        if not email:
            raise ValueError("User must have an email")
        if not user_type:
            raise ValueError("User must have an user_type")
        if not nickname:
            raise ValueError("User must have a nickname")
        user = self.model(
            user_type = user_type,
            email = self.normalize_email(email),
            nickname = nickname, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, user_type = 'ER', nickname = 'JaeHwan'):
        user = self.create_user(
            user_type = 'ER',
            email = self.normalize_email(email),
            nickname = 'JaeHwan',
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    user_type = EnumField(choices=['EE', 'ER'])
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    employee_region = EnumField(choices=['seoulip', 'nakdae', 'nokdu', 'snu', 'home',], null=True)
    employee_type = EnumField(choices=['work_scholarship_student', 'mentoring', 'experiment_arbeit', 'private_lesson', 
    'academy', 'survey', 'lecture', 'service', 'typing', 'outsourcing', 'extra'], null=True)
    employee_how_to_pay = EnumField(choices=['pay_hourly', 'pay_per_work', 'goods', 'random', 'uncertain'], null=True)
    employee_pay_limit = models.IntegerField(null=True)
    company_name = models.CharField(max_length=100, null=True)
    company_address = models.CharField(max_length=200, null=True)
    business_content = models.TextField(null=True)
    representative_name = models.CharField(max_length=50, null=True)
    employer_license_number = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(upload_to='uploads/') #modify
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['user_type', 'nickname']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


    
