from app.models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import TodoSerializer

@api_view['GET']
def todo_list(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)
