from django.shortcuts import render
from .tasks import send_email_task  
import json
from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from bus_app.models import Ticket, Terminal, Sale
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .tasks import send_email_task


def api_to_wallex(request, coin_name):
    
    url = "https://api.wallex.ir/v1/currencies/stats?key=()".format(coin_name)
    response = request.get(url)
    response = json.loads(response.content)
    price = response['price']
    return JsonResponse({'price': price*600000})







def send_email_view(request):  
    subject = 'Warning'  
    message = ''  
    recipient_list = ['abbas99abbas@example.com']  


    send_email_task.delay(subject, message, recipient_list)  

    return render(request, 'email_sent.html')