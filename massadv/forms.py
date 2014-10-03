from django.forms import ModelForm, PasswordInput
from massadv.models import StUsers

class StUsersForm(ModelForm):
    class Meta:
        model = StUsers
        widgets = {
            'password': PasswordInput()}
# Create your views here.
