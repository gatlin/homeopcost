from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
# Register your models here.
#user groups
#basically anonymous account, no verification required.
class tierOne(Group):
	name = 'tier one'
	permissions = []
	objects = models.Manager()

#requires credit card verification, allows user to input custom house data
class tierTwo(Group):
	name = 'tier two'
	permissions = []
	objects = models.Manager()

#requires credit card verification, allows for 3rd party rater to come in and input data
class tierThree(Group):
	name = 'tier three'
	permissions = []
	objects = models.Manager()

#different class of users, the third party raters. Allowed to come in an edit data.
#ask curt! what does "editing data" entail?
class thirdPartyRater(Group):
	name = 'third party rater'
	permissions = []
	objects = models.Manager()
