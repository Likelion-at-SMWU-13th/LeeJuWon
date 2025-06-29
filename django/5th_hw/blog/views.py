from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# 게시글 전체 조회 + 생성
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 게시글 단일 조회 + 수정 + 삭제
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 댓글 전체 조회 및 생성
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# 댓글 단일 조회, 수정, 삭제
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer