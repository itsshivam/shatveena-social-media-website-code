from django import forms
from .models import user_basic_detail, user_extra_detail

class login_form(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)

class signup_form(forms.Form):
    username = forms.CharField(max_length = 30)
    email = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    confirm_password = forms.CharField(max_length = 30)


class user_basic_form(forms.ModelForm):
    class Meta:
        model = user_basic_detail
        fields = ('name','address','intro')
        exclude = ('user_id','username')

class user_detail_form(forms.Form):
    date_of_birth  = forms.DateField(required = False)
    gender = forms.CharField( max_length = 20, required = False)
    website_link = forms.CharField(max_length  =40, required = False)
    relationship_status = forms.CharField(max_length = 40, required = False)
    profession = forms.CharField(max_length = 20, required = False)

class working_form(forms.Form):
    workplace = forms.CharField(max_length = 60)

class working_delete(forms.Form):
    work_id = forms.CharField(max_length = 30)

# class image_form(forms.Form):
#     image = FileField()
