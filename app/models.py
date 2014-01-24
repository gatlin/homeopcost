from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import forms, stripe

#create permissions here
#end here

class UserManager(BaseUserManager):
	def create_superuser(self, first_name, last_name, email, password):
		user = User()
		user.email = email
		user.set_password(password)
		user.first_name = first_name
		user.last_name = last_name

	def create_user(self, first_name, last_name, email, password, tier, token):
		if not (email and first_name and last_name and password):
			raise ValueError('Not all fields. See REQUIRED_FIELDS.')
		else:
			user = User()
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.tier = tier
			user.set_password(password)
			user.save(using=self._db)

		if token:
			#perform stripe magic here
			#IMPORTANT: do not forget to include stripe.js in template
			#<script type="text/javascript" src="https://js.stripe.com/v2/"></script>
			amount = 50 #50 CENTS
			stripe.api_key = 'sk_test_WfMEMY5PfzRdZxPGZY0Y6OHb'
			try:
				stripe.Charge.create(amount=amount, currency='usd', card=token, description='HomeOpCost: Verification Charge')
				cc = Stripe(user = user, stripe_verified = True, group = 'tierTwo' )
				cc.save()
				return redirect('accountSuccess.html')
			
			except stripe.CardError, e:
				return redirect('cardFailure.html')

class User(AbstractBaseUser):
	email = models.CharField(max_length = 200, unique=True)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 200)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

class Stripe(models.Model):
	user = models.ForeignKey(User, primary_key = True)
	address = models.CharField(max_length = 200)
	stripe_id = models.CharField(max_length=255)
	stripe_verified = False
	created_at = models.DateTimeField(auto_now_add=True)
	group = None
