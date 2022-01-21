from django.conf.urls import url

from model.views import index
# from wenbenduikang import wenbenview



urlpatterns = [

    url(r'^model/$',index),

]