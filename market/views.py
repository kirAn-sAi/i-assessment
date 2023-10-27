from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Location, Department, Category, SubCategory, SKU
from .baseviewset import BaseViewSet
from .sku_form import SKUFilterForm
from .model_serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)


class LocationViewSet(BaseViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(methods=['get'], detail=True)
    def department(self, request, pk):
        """
        sample url:  'host:port/market/api/v1/location/1/department/'
        returns: list of categories (name, description) that are related to location with id 1
        """
        loc = Location.objects.get(pk=pk)
        q = loc.department_set.all()
        resp = DepartmentSerializer(q, many=True)
        return Response(resp.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path="department/(?P<dep_id>[^/.]+)/category")
    def category(self, request, pk, dep_id=None):
        """
        sample url: host:port/market/api/v1/location/2/department/3/category/
        returns: list of categories (name, description) that are related to
                    location with id 2
                    department with id 3
        """
        cats = Category.objects.filter(department_id=dep_id).filter(department__location__id=pk).all()
        resp = [(row.name, row.description) for row in cats]
        return Response({"response": resp}, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True,
            url_path="department/(?P<dep_id>[^/.]+)/category/(?P<cat_id>[^/.]+)/subcategory")
    def subcategory(self, request, pk, dep_id, cat_id):
        """
        sample url: host:port/market/api/v1/location/2/department/3/category/4/subcategory/
        returns: list of sub categories (name, description) that are related to
                    location with id 2
                    department with id 3
                    category with id 4
        """
        subs = SubCategory.objects.filter(category_id=cat_id).filter(
            category__department_id=dep_id).filter(category__department__location__id=pk).all()
        # cats = Category.objects.filter(department_id=dep_id).filter(department__location__id=pk).all()
        resp = [(row.name, row.description) for row in subs]
        return Response({"response": resp}, status=status.HTTP_200_OK)


class DepartmentViewSet(BaseViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(BaseViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SKUViewSet(BaseViewSet):
    # form = SKUForm
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    @staticmethod
    def get_matched_skus(request):
        data = request.POST
        qry = SKU.objects.values_list(

            'id', 'name', 'subcategory__category__department__location__name',
            'subcategory__category__department__name',
            'subcategory__category__name', 'subcategory__name',
        ).filter(
            subcategory__name=data.get("subcategory").strip(),
            subcategory__category__name=data.get("category").strip(),
            subcategory__category__department__name=data.get("department").strip(),
            subcategory__category__department__location__name=data.get("location").strip(),
        )
        return qry

    @action(methods=['GET', 'POST'], detail=False, url_path='findsku')
    def find_sku(self, request):
        """
        sample url: host:port/market/api/v1/sku/findsku/
        return: Details of SKU Along with lined Parent objects
        """
        if request.method == "GET":
            return render(request, "find_sku.html", {"form": SKUFilterForm()})
        else:
            resp = self.get_matched_skus(request)
            data = [row for row in resp] if resp else []
            return Response({"response": data})

