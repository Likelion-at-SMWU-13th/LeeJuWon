from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from .models import Post
from. forms import PostBasedForm, PostModelForm

# Create your views here.

#3주차 장고 세미나
def post_form_view(request):
    if request.method == "GET":
        form = PostBasedForm()
        context = {'form' : form}
        return render(request, 'posts/post_form2.html', context)
    else:
        return redirect('index')