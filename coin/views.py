from django.shortcuts import render


def api_to_wallex(request, coin_name):
    
    url = "https://api.wallex.ir/v1/currencies/stats?key=()".format(coin_name)
    request.get(url)

