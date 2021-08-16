from import_export import resources
from .models import Items

class ItemResource(resources.ModelResource):
    class Meta:
        model = Items
        