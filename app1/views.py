from django.shortcuts import render_to_response,get_object_or_404
from app1.models import Order,MuhurthamOrder,Reception
from django.template import RequestContext
# Create your views here.

def orders(request):
	order_list = Order.objects.all()
	return render_to_response('app1/index.html',{'order_list':order_list})

def order_detail(request,order_id):
	p = get_object_or_404(Order,pk=order_id)
	m = get_object_or_404(MuhurthamOrder,pk=p.muhurtham_Order_id)
	if p.reception_Order_id is not None:
		r = get_object_or_404(Reception,pk=p.reception_Order_id)
	else:
		r = None
	return render_to_response('app1/order.html',{'order':p,'muhurtham':m,'reception':r,'title':'View Orders'},context_instance = RequestContext(request))
