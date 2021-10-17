from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def shop(request):
    if request.method == 'GET':
        # Shop db를 불러오겠다.
        shop = Shop.objects.all()
        # serializer는 db의 데이터를 보기 쉽게 json 형태로 바꿔주는 역할을 한다.
        # many=True는 shop이라는 데이터가 여러개여도 상관하지 않겠다는 뜻
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def menu(request):
    if request.method == 'GET':
        # Shop db를 불러오겠다.
        menu = Menu.objects.all()
        # serializer는 db의 데이터를 보기 쉽게 json 형태로 바꿔주는 역할을 한다.
        serializer = MenuSerializer(menu, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        

