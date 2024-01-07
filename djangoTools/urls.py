from django.urls import include, path
urlpatterns = [
    # webtools路由
    path('', include('webTools.urls')),

]
