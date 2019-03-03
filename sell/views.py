from django.shortcuts import render,redirect
from .models import buyer_demand,farmer_crops

#Base page for the Sell_Here module of the farmer app
def home(request):
    crops_d = farmer_crops.objects.all()
    crops_d = crops_d.filter(farmer_name__contains= request.user.username) #Filtering the data based on the farmer loggedin 
    buyer_d = buyer_demand.objects.all()
    content = {
        'crops': crops_d,
        'buy': buyer_d,
    }
    return render(request,'sell/sell.html', content)

#Crop add Feature view is defined here to render the request
def add(request):
    return render(request, 'sell/add.html')


#Confirmation page is handled here with various parameters
def add_confirm(request):
    if request.method == 'POST':  
        fname = request.POST['fname']
        fprice = request.POST['price']
        fquantity = request.POST['quan']
        temp = farmer_crops(farmer_name = request.user.username ,crop_name = fname, amount = fprice, quantity = fquantity)
        temp.save() #Saving the values into the model or table in sqlite
        return redirect('sell-home')

#View is triggered when some buyer want the order to be placed and then lock is done so that any other buyer doesnt purchase it 
def add_confirm_attach(request):
    print('Hello')
    id_temp = request.POST['id']
    print(id_temp)
    temp = buyer_demand.objects.get(id = id_temp)
    temp.bought = request.user.username
    temp.flag = 1
    temp.save()
    return redirect('sell-home')