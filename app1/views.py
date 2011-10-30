from django.shortcuts import render_to_response,get_object_or_404
from app1.models import Order
from django.template import RequestContext
# Create your views here.

def orders(request):
	order_list = Order.objects.all()
	return render_to_response('app1/index.html',{'order_list':order_list})

def order_detail(request,order_id):
	p = get_object_or_404(Order,pk=order_id)
	return render_to_response('app1/order.html',{'order':p},context_instance = RequestContext(request))
