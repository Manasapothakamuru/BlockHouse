from django.http import JsonResponse
from datetime import datetime, timedelta
import random


def candlestick_data(request):

    start_date = datetime(2023, 1, 1)
    data = []
    
    for i in range(7): 
        date = start_date + timedelta(days=i)
        open_price = random.uniform(100, 200)
        close_price = random.uniform(100, 200)
        high_price = max(open_price, close_price) + random.uniform(0, 10)
        low_price = min(open_price, close_price) - random.uniform(0, 10)
        
        data.append({
            "x": date.strftime("%Y-%m-%d"),
            "open": round(open_price, 2),
            "high": round(high_price, 2),
            "low": round(low_price, 2),
            "close": round(close_price, 2)
        })

    response_data = {
        "datasets": [
            {
                "label": "Candlestick Dataset",
                "data": data
            }
        ]
    }
    return JsonResponse(response_data)


def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 30, 40]
    }
    return JsonResponse(data)


def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C"],
        "data": [100, 150, 200]
    }
    return JsonResponse(data)


def pie_chart_data(request):
    data = {
        "labels": ["Red", "Blue", "Yellow"],
        "data": [300, 50, 100]
    }
    return JsonResponse(data)


def home(request):
    return JsonResponse({"message": "Welcome to the Chart API!"})