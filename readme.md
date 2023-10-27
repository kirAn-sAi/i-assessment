
I have used **sqlite database** that comes by default 
with the **Django Project** for the sake of simplicity. 
We can configure any database of our choice. 

I have created the necessary models, their respective view sets and serializers.

### Below is the detailed summary of project URL's

- to list all locations: `host:port/market/api/v1/location/`
- to get the details of a particular location: `host:port/market/api/v1/location/1/`
> replace the term _location_ from above two urls with any of (department, category, subcategory or sku) to get the related data.
- To get the departments related to a specific location: `host:port/market/api/v1/location/1/department/`
- To get the categories related to a specific location and department: `host:port/market/api/v1/location/2/department/3/category/`
- To get the sub categories related to a specific location and department and category: `host:port/market/api/v1/location/2/department/3/category/4/subcategory/`
- To get the list of all the SKU's: `host:port/market/api/v1/sku`
- To find the SKU details `host:port/market/api/v1/sku/findsku/`

> Check the view specific methods for more details in views.py
