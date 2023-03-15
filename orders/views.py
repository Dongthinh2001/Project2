from django.http import HttpResponse
from django.shortcuts import render


from django.shortcuts import get_object_or_404, render,get_list_or_404
from accounts.models import Account
from equipments.models import Equipment

from footballpitchs.models import FootballPitch
from orders.models import Order


def index(request, id_pitch):
    football_pitch = get_object_or_404(FootballPitch, pk=id_pitch)
    equipments = get_list_or_404(Equipment)
    return render(request, 'orders/index.html', {"id_pitch": id_pitch, "FootballPitch":football_pitch,"equipments":equipments})

def place_order(request, id_pitch):
    user_name = request.POST["user_name"]
    time_slot = request.POST["time_slot"]
    ordered_date = request.POST["ordered_date"]
    football_pitch = get_object_or_404(FootballPitch, pk=id_pitch)
        
    user = Account.objects.get(user_name = user_name )
    if user is None:
        user = Account(user_name = user_name)
        user.save()
    
    success = True
    try:
        
        order = Order(id_pitch=football_pitch, time_slot = time_slot, 
                    ordered_date = ordered_date, user_name=user)
        
        order.save()
    except:
        success  = False
    return render(request, "orders/place_order_result.html",{"success":success})