from django.urls import include, path

from .views import views
from .views.TaskDetail import TaskDetail
from .views.TaskList import TaskList, TaskHighlight
from .views.User import *


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.api_root),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('tasks/<int:pk>/highlight/', TaskHighlight.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
