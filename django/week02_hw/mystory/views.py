from django.shortcuts import render
from django.views.generic import TemplateView

# FBV : 자기소개 
def introduceView(request):
    if request.method == 'POST':
        name = request.POST.get('name', '이주원')
        age = request.POST.get('age', '24')
        mbti = request.POST.get('mbti', 'ISTJ')
        return render(request, 'introduce.html', {
            'submitted': True,
            'name': name,
            'age': age,
            'mbti': mbti,
        })
    else:
        return render(request, 'introduce.html', {'submitted': False})

    
# CBV : 일기
class DiaryView(TemplateView):
    template_name = 'diary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submitted'] = False
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['submitted'] = True
        context['date'] = request.POST.get('date', '2025년 5월 4일')
        context['weather'] = request.POST.get('weather', '맑고 따뜻한 날')
        context['content'] = request.POST.get('content', '기본 일기 내용')
        return self.render_to_response(context)
