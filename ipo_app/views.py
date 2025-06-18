from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IPO
from .serializers import IPOSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({'message': 'Hello from Django API!'})

@api_view(['GET'])
def ipo_detail(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    serializer = IPOSerializer(ipo)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def ipo_list(request):
    if request.method == 'GET':
        ipos = IPO.objects.all()
        serializer = IPOSerializer(ipos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IPOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
