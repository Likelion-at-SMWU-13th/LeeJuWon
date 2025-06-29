from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# 게시글 전체 조회 + 생성
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 게시글 단일 조회 + 수정 + 삭제
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
