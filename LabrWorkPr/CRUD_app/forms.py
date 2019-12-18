from django import forms  
from .models import socialNetworks,socialNetworks_types  
   
   
class socialNetworksForm(forms.ModelForm):  
   
     class Meta:  
         model = socialNetworks  
         fields = ['user', 'title', 'url_cn', 'type_cn']  
         localized_fields = ('birth_date',)

class socialNetworksForm_types(forms.ModelForm):  
   
     class Meta:  
         model = socialNetworks_types  
         fields = ['title_cn']  