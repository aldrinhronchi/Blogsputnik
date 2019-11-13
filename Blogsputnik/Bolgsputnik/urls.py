#from Blogsputnik.urls import urlpatterns
from Bolgsputnik.views import  postsList,postsNew,postsUpdate,postsDelete
from django.urls import path


urlpatterns = [
    path('list/',postsList, name="postsList"),
    path('new/', postsNew, name="postsNew"),
    path('update/<int:id>/', postsUpdate, name="postsUpdate"),
    path('delete/<int:id>/', postsDelete, name="postsDelete"),

    ]
