from django.shortcuts import render
from django.template.context_processors import csrf

from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import SendTelegram
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    form = OrderForm
    price_table = PriceTable.objects.all()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form}
    return render(request, './index.html', dict_obj)

@csrf_exempt
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        context = {}
        context.update(csrf(request))
        SendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name,'phone':phone})
    else:
        return render(request, './thanks.html')