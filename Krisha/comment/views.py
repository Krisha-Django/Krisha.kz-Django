from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from .models import Comment
from .serializers import CommentFullSerializer, CommentShortSerializer,CommentSerializer


# Create your views here.
class CommentViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return CommentFullSerializer
            return CommentShortSerializer
        else:
            return CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

# class CommentList(APIView):
#     def get(self, request, format=None):
#         comments = Comment.objects.all()
#         serializer = CommentShortSerializer(comments, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CommentFullSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CommentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Comment.objects.get(pk=pk)
#         except Comment.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         comment = self.get_object(pk)
#         serializer = CommentFullSerializer(comment)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         comment = self.get_object(pk)
#         serializer = CommentFullSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
