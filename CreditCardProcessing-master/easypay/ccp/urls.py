from django.urls import path
#from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    
   # path('signup', views.signup, name='signup'),
    # (r'^profiles/home1', home1),
    path('home1',views.home1,name="home1"),
    path('first',views.first,name="first"),
    path('logout',views.logout,name="logout"),
	path('home',views.home,name='home'),
	path('dis/<str:id>',views.display1,name='display1'),
	path('payment/<str:id>',views.payment,name='payment'),
	path('history1/<str:id>',views.history1,name='history1'),
    path('register', views.register, name='register'),
    path('registerf', views.registerf, name='registerf'),
	path('login',views.login,name='login'),
    path('yourhome/<str:id>',views.yourhome,name='yourhome'),
    #path('login',views.mylogin,name='mylogin'),
    
    #login,{ 'template_name':'./templates/login.html'}),
]