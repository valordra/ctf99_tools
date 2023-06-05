from django.forms import ModelForm
from portal.models import UserAccount

class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'