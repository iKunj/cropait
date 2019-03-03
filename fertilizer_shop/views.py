from django.shortcuts import render,redirect
from .models import fertilizer_data

#list of fertilizer along with the data
var = [
  {
    "Name": "Urea",
    "Price": 276
  },
  {
    "Name": "Am. Phos. Sulphate",
    "Price": 368
  },
  {
    "Name": "Complex NPK",
    "Price": 466
  },
  {
    "Name": "TSP",
    "Price": 418
  },
  {
    "Name": "Am. Chloride",
    "Price": 435
  },
  {
    "Name": "DAP",
    "Price": 1222
  },
  {
    "Name": "MAP",
    "Price": 910
  },
  {
    "Name": "Pot. Chloride",
    "Price": 872
  },
  {
    "Name": "SSP",
    "Price": 262
  }
]

#Adding of fertilizer 
def add(request):
    return render(request, 'fertilizer_shop/add.html')

#confirmation page
def add_confirm(request):
    if request.method == 'POST':  
        fname = request.POST['fname']
        fprice = request.POST['price']
        print(fname)
        print(fprice)
        temp = fertilizer_data(buyer = request.user.username ,name = fname, price = fprice)
        temp.save()
        return redirect('home-index')

def pricecheck(request):
        

  for i in range(len(var)):
          
    if int(var[i]['Price']) >= int(request.POST['pprice']):
        if request.method == 'POST':  
                fname = request.POST['fname']
                fprice = request.POST['pprice']
                print(fname)
                print(fprice)
                temp = fertilizer_data(buyer = request.user.username ,name = fname, price = fprice)
                temp.save()
                return redirect('home-index')

    else:
      status = 'Price exceeds MSP' + str(var[i]['Price']) + str(request.POST['pprice'])
       
      return render(request,'fertilizer_shop/pricecheck.html',{'status':status})