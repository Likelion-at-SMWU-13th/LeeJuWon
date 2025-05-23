from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

# 1) 회원가입
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "회원가입에 성공하셨습니다 !"})
    return Response(serializer.errors, status=400)

# 2. 회원정보 조회
@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "존재하지 않는 사용자입니다 !"}, status=404)

    serializer = UserSerializer(user)
    return Response(serializer.data)

# 3) 회원정보 수정
@api_view(['PUT', 'PATCH'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "존재하지 않는 사용자입니다 !"}, status=404)

    serializer = UserSerializer(user, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# 4) 탈퇴 
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "존재하지 않는 사용자입니다 !"}, status=404)

    user.delete()
    return Response({"message": "회원 삭제가 완료되었습니다 !"})
