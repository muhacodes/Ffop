from django.db import models

# Create your models here.
from django.db import models
from Department.models import Department

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, department, username, password=None):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			department=department
			
		)


		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			username,
			password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user



class User(AbstractBaseUser):

	objects 		= UserManager()
	email			= models.EmailField(verbose_name="email field",  max_length=254, unique=True)
	username		= models.CharField(max_length=100)
	name    		= models.CharField(max_length=250, null=True)
	address 		= models.CharField(max_length=100, null=True, blank=True)
	active 			= models.BooleanField(default=True)
	staff 			= models.BooleanField(default=False) # a admin user; non super-user
	admin 			= models.BooleanField(default=False) # a superuser
	department 		= models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True


	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True


	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		"Is the user active?"
		return self.active


	