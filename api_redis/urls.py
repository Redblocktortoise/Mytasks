from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import  ItemList, ItemDetail

urlpatterns = {
    path('redis/', ItemList.as_view(), name="items"),
    path('redis/<slug:key>', ItemDetail.as_view(), name="single_item")
}
urlpatterns = format_suffix_patterns(urlpatterns)
