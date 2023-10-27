from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

#
# All the URLS are defined as requested in the test.
#
router.register(r"api/v1/location", views.LocationViewSet)
router.register(r'api/v1/department', views.DepartmentViewSet)
router.register(r'api/v1/category', views.CategoryViewSet)
router.register(r'api/v1/subcategory', views.SubCategoryViewSet)
router.register(r'api/v1/sku', views.SKUViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
