from django.urls import path,include
from rest_framework.routers import DefaultRouter

# from product_api.urls import urlpatterns
from .views import *

router=DefaultRouter()
router.register(r'products',ProductViewset)
router.register(r'categories',CategoryViewset)

urlpatterns=[
    path('',include(router.urls)),
]