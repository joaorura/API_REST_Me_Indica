from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from .views import LogicQuestionViewSet

merouter = merouters.DefaultRouter()
merouter.register(r'logicQuestions', LogicQuestionViewSet)

urlpatterns = [

]

urlpatterns += merouter.urls
