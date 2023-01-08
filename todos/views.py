from rest_framework import generics, status
from rest_framework.response import Response

from .models import Todo
from .serializer import TodoSerializer

class ViewTodos(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ViewTodo(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, pk):
        try:
            instance = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Erro": "Não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            instance = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Erro": "Não encontrado!"}, status=status.HTTP_404_NOT_FOUND)

