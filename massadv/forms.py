from django.forms import ModelForm, PasswordInput
from massadv.models import Users

class UsersForm(ModelForm):
    class Meta:
        exclude = []
        model = Users
        widgets = {
            'password': PasswordInput()}
# Create your views here.
