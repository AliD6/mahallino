from django.urls import path

from .views import   PerTrans , PubTrans  , Refahi , Security

urlpatterns = [
    path('sec', Security.as_view() , name='security'),
    path('per', PerTrans.as_view() , name='pertrans'),
    path('pub', PubTrans.as_view() , name='pubtrans'),
    path('ref', Refahi.as_view() , name='refahi'),
]