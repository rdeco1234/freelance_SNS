from django.forms import ModelForm
from app1.models import Ipaddress

class IpaddressForm(ModelForm):
    class Meta:
        model = Ipaddress
        fields = ('id', 'ipaddress', 'status', 'description')


