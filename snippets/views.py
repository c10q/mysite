from rest_framework import viewsets, permissions, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from snippets.models import Post, Cat
from snippets.serializers import UserSerializer, UserCreateSerializer, PostSerializer, CatSerializer
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    permission_classes = [permissions.BasePermission]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]


class CreateUser(mixins.CreateModelMixin, APIView):
    permission_classes = [permissions.AllowAny]

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return Response({"message": "ㅋㅋㄹㅃㅃ"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공"}, status=status.HTTP_201_CREATED)
        return Response({"message": "실패"}, status=status.HTTP_400_BAD_REQUEST)

