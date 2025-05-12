# Django Forms 정리

Django 5.2 공식 문서([Forms](https://docs.djangoproject.com/en/5.2/topics/forms/))를 기반으로 폼 기능을 간략히 정리

## Django Forms란?
- 사용자 입력 수집 및 검증
- HTML 폼 렌더링, 데이터 검증, Python 타입 변환
- CSRF 등 보안 처리
- 모델 기반(ModelForm) 또는 독립형(Form)으로 사용

## 폼 생성
`django.forms.Form`을 상속하여 폼 정의

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="이름")
    email = forms.EmailField(label="이메일")
    message = forms.CharField(widget=forms.Textarea, label="메시지")


- 필드: CharField, EmailField 등으로 입력 타입 지정
- 위젯: widget으로 렌더링 방식 설정(예: Textarea)
- 레이블: label로 필드 이름 지정

## 템플릿에서 폼 렌더링
폼을 템플릿에 전달해 렌더링

### 1. 단락 형식:
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">제출</button>
</form>


- form.as_p : 각 필드를 <p> 태그로 감쌈


### 2. 테이블 형식:

- {{ form.as_table }}: 필드를 테이블 행으로 렌더링


### 3. 수동 렌더링:
<form method="post">
    {% csrf_token %}
    <div>
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>
    <button type="submit">제출</button>
</form>


- HTML 구조 완전 제어

{% csrf_token %}은 POST 폼에서 필수


## 폼 제출 처리
뷰에서 폼 데이터 처리
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # 데이터 처리(예: DB 저장, 이메일 전송)
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


form.is_valid(): 데이터 검증.
form.cleaned_data: 검증된 데이터 접근.

## 주요 특징
- 검증: 필드별 자동 검증, 커스텀 검증 가능
- 위젯 커스터마이징: CSS 클래스, 속성 추가 가능
- ModelForm: 모델과 연계하여 폼 자동 생성

