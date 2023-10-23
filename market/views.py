
from django.shortcuts import HttpResponse
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend


from .models import Location, Department, Category, SubCategory
from .baseviewset import BaseViewSet


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = "__all__"


class SKUSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    department = serializers.CharField(source="category.department.name")
    location = serializers.CharField(source="category.department.location.name")

    class Meta:
        model = SubCategory
        fields = ('name', 'category', 'department', 'location')


class SKUViewSet(BaseViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SKUSerializer
    search_fields = ['name', 'category']
    filter_backends = [SearchFilter]
    filterset_fields = ['name', 'category']

    def list(self,request):
        query_set = SubCategory.objects.select_related('category').all()
        resp = SKUSerializer(query_set, many=True)
        return Response(resp.data, status=status.HTTP_200_OK)


class LocationViewSet(BaseViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(methods=['get'], detail=True)
    def departments(self, request, pk):
        loc = Location.objects.get(pk=pk)
        q = loc.department_set.all()
        resp = DepartmentSerializer(q, many=True)
        return Response(resp.data, status=status.HTTP_200_OK)

    # @action(methods=["get"], detail=True, url_path="departments/(P<dep_id>\d+)/category/$")
    # # @action(methods=["get"], detail=True)
    # def categories(self, request, loc_id, dep_id):
    #     resp = {}
    #     import pdb; pdb.set_trace()
    #     return Response(resp, status=status.HTTP_200_OK)


class DepartmentViewSet(BaseViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(BaseViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

