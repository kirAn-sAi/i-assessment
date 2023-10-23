from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
#url(r'^pdfreport/(?P<v_id>.*)/(?P<l_type>.*)$',pdfreport.pdfreport),
# router.register(r'api/v1/location/(?P<loc_id>\d+)/department/(?P<cat_id>\d+)/category', views.categories)
router.register(r"api/v1/location", views.LocationViewSet)
router.register(r'api/v1/department', views.DepartmentViewSet)
router.register(r'api/v1/category', views.CategoryViewSet)
router.register(r'api/v1/subcategory', views.SubCategoryViewSet)
router.register(r'api/v1/sku', views.SKUViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
