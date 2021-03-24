from datetime import datetime
import datetime as dt


from django.shortcuts import render
from .models import Post

#from django.http import HttpResponse
# posts = [
#     {'author': 'Orit Naor',
#      'title': 'Blog Post 1',
#      'content': 'First post content',
#      'date_posted': datetime.now()
#      },
#     {'author': 'Jane doe',
#      'title': 'Blog Post 2',
#      'content': 'Second post content',
#      'date_posted': datetime.now()+dt.timedelta(days=+1)
#      }
#
# ]
# Create your views here.
def home(request):
  #context = {'posts':posts}
  context = {'posts': Post.objects.all()}
  return render(request,'blog/home.html',context)
# return HttpResponse('<h1>Blog home</h1>')


def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
    #return HttpResponse('<h1>Blog about</h1>')
