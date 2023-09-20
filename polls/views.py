from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuthorModel
from .serializer import AuthorSerializer




# Create your views here.




class ListAPiView(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) == 'AnonymousUser':
            return Response({'warning!': 'You have not loged yet!'})
        all = AuthorModel.objects.filter(status=True)
        serializer = AuthorSerializer(all, many=True)
        return Response(serializer.data)

class CreateAPiView(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                serializer = AuthorSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'warning!': "you don't have permission!"})
        else:
            return Response({"warning!": "you don't have permission!"})
        

class UpdateStatus(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:

                news = get_object_or_404(AuthorModel, id=kwargs['author_id'])
                serializer = AuthorSerializer(news, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'warning!': "you don't have permission!"})

        return Response({"warning!": "you don't have permission!"})
