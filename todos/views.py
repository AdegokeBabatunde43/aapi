from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todos.serializers import TodoSerializers
from todos.models import Todos

# Create your views here.
@api_view(['POST'])
def create(request):
    record = TodoSerializers(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)  
    # return render(request, 'todos.html')
    
@api_view(['GET'])
def alltodos(request):
    record = Todos.objects.all()
    record = TodoSerializers(record, many=True)
    return Response(record.data)

@api_view(['DELETE'])
def delete(request, id):
    record = Todos.objects.get(id=id)
    record.delete()
    return Response("Record deleted successfully")
