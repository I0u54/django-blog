from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required




from django.http import HttpResponse
from .models import Article,Category
# Create your views here.
class ArticleView:
    @staticmethod
    def index(request):
        data = Article.objects.all()
        return render(request,"index.html",{"articles":data})
    @staticmethod
    def createOrStore(request):
        if request.method == 'POST':
            title = request.POST.get("title")
            contnt = request.POST.get("content")
            category = Category.objects.get(pk=request.POST.get("category"))
            article = Article(title=title,content=contnt,category=category)
            article.save()



            return redirect('index')


        categories = Category.objects.all()
        return render(request,'form.html',{"categories":categories})
    
    @login_required(login_url='login')
    @staticmethod
    def destroy(request,id):
        try:

            article = Article.objects.get(pk=id)
            article.delete()
            return redirect('index')
        except:
            return redirect('index')
 


      