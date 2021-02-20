from django.urls import path

from . import views

##### modo normal ######
#app_name = 'polls'
#urlpatterns = [
#path('', views.index, name='index'),
#    path('<int:question_id>/', views.detail, name='detail'),
#    # exemplo: /polls/5/results/
#    path('<int:question_id>/results/', views.results, name='results'),
#    # exemplo: /polls/5/vote/
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#    path('owner', views.owner, name='owner'),]
#########################

# modo de vistas genéricas
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('owner', views.owner, name='owner')
]