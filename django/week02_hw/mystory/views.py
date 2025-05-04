from django.shortcuts import render
from django.views.generic import TemplateView

# FBV : 자기소개 
def introduceView(request):
    return render(request, 'introduce.html', {
        'name': '이주원',
        'age': 24,
        'mbti' : 'ISTJ',
        'university': '숙명여자대학교',
        'major': '인공지능공학부',
        'hobby': '산책하기, 영화보기, 노래듣기',
    })
    
# CBV : 일기
class DiaryView(TemplateView):
    template_name = 'diary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = '2025년 5월 4일'
        context['weather'] = '맑고 따뜻한 날'
        context['content'] = (
            "오늘은 외출 나가기 전 오전에 일찍 과제를 끝내고자 한다."
            "처음 공부하는 장고라 너무 어렵긴 하지만, 열심히 공부 중이다."
            "그래도 이렇게 실습이나 과제 따"
        )
        return context