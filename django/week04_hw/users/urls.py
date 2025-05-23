from django.urls import path
from .views import signup, user_detail, update_user, delete_user

__all__ = ['urlpatterns']

urlpatterns = [
    path('signup/', signup),                 # 회원가입 (POST)
    path('<int:pk>/', user_detail),          # 회원정보 조회 (GET)
    path('<int:pk>/update/', update_user),   # 회원정보 수정 (PUT/PATCH)
    path('<int:pk>/delete/', delete_user),   # 회원 탈퇴 (DELETE)
]
