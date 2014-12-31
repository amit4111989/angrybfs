from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from django.contrib.auth import authentication, login, logout
from django.contrib.auth.decorators import login_required

from signup.models import UserProfile
from signup.forms import UserProfileForm, UserForm
# Create your views here.

def register(request):
	if request.method=='POST':
		pass
	else:
		context = RequestContext(request)
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('signup/main.html', {'user_form':user_form,'profile_form':profile_form},context)