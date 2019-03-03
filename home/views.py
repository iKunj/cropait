from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from fertilizer_shop.models import fertilizer_data
from sell.models import buyer_demand,farmer_crops

#Base comparing view so as to seperate different user interface pages
def home(request):
	#Check if the user is already loggedin
	if request.user.is_authenticated:
		#If the user is buyer then it is redirected to the buyer home page
		if 'buyer' in str(request.user):
			print('buyer')
			fertilizer = fertilizer_data.objects.all()
			fertilizer = fertilizer.filter(buyer__contains= request.user.username)
			return render(request, 'fertilizer_shop/index.html', {'fertilizer': fertilizer})
		#If the user is company then it is redirected to the company home page
		elif 'company' in str(request.user):
				crops_d = farmer_crops.objects.all()
				buyer_d = buyer_demand.objects.all()
				buyer_d = buyer_d.filter(buyer_name__contains= request.user.username)
				content = {
					'crops': crops_d,
					'buy': buyer_d,
				}
				return render(request,'company/company.html', content)
		#He/She is farmer
		else:
			print('farmer')
			return render(request,'home/index.html')
	#If the user is not already loggedin then it is rendered to login page
	else:
		return render(request,'home/login.html')

#Base view to redirect to youtube 
def ysearch(request):
	return render(request, 'home/youtube.html')

#Login process of the user
def login_view(request):
	if request.method == 'POST':  
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if 'buyer' in username:
				fertilizer = fertilizer_data.objects.all()
				fertilizer = fertilizer.filter(buyer__contains= request.user.username)
				return render(request, 'fertilizer_shop/index.html',{'fertilizer': fertilizer})
			elif 'company' in username:
				crops_d = farmer_crops.objects.all()
				buyer_d = buyer_demand.objects.all()
				buyer_d = buyer_d.filter(buyer_name__contains= request.user.username)
				content = {
					'crops': crops_d,
					'buy': buyer_d,
				}
				return render(request,'company/company.html', content)
			else:
				return redirect('home-index')
		else:
			return render(request, 'home/login.html')

#Base view for the help module of the app
def help(request):
	return render(request, 'home/help.html')