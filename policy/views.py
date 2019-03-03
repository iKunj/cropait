from django.shortcuts import render

#Returns the base template of the policy page
def home(request):
 	return render(request,'home/policy.html')

#When farmers applies to the policy this view is called
def apply(request):
	s_name = request.POST['scheme']
	content = {
		'title' : s_name,
		'fname' : request.user.username,
	}
	return render(request, 'home/apply.html',content)