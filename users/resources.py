from import_export import resources
from .models import Delegate

class DelegateResource(resources.ModelResource):
    class Meta:
        model = Delegate
        fields = ('first_name', 'last_name', 'email')