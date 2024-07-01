from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
# from rest_framework.decorators import api_view

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# @api_view(['GET'])
# def get_todos():
#     return jsonify({'todos': 'get all todos'})
