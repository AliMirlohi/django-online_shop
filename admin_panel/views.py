from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView,UpdateView
from django.urls import reverse
from article_module.models import Article
from utils.my_decorators import permission_checker_decorator_factory


# Create your views here.
@permission_checker_decorator_factory('this is my data')
def index(request:HttpRequest):
    return render(request,'admin_panel/Home/index.html')

@method_decorator(permission_checker_decorator_factory('this is my cbv'),name='dispatch')
class ArticlesListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'admin_panel/articles/articles_list.html'
    def get_context_data(self,*args, **kwargs):
        context= super(ArticlesListView,self).get_context_data(*args,**kwargs)
        # context['date']= date2jalali(self.request.user.date_joined)
        return context
    def get_queryset(self):
        query= super(ArticlesListView,self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

@method_decorator(permission_checker_decorator_factory('this is my cbv'),name='dispatch')
class ArticleEditView(UpdateView):
    model = Article
    template_name = 'admin_panel/articles/edit_article.html'
    fields = '__all__'
    # success_url = reverse('admin_articles')
    success_url = '/admin-panel/articles/'

