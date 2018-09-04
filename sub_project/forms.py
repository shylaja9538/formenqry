from django import forms
from .models import user
from sub_project.models import user_info,File

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    class Meta():
          model=user
          fields='__all__'

class FormName(forms.ModelForm):
     Name=forms.CharField()
     Contact=forms.CharField()
     Email=forms.EmailField()
     Lead_from=forms.CharField()
     Called_by=forms.CharField()
     Course=forms.CharField()
     Interview_type=forms.CharField()
     Education=forms.CharField()
     Specialization=forms.CharField()
     year_of_passing=forms.IntegerField()
     fresher_experience=forms.CharField()
     Time_in=forms.TimeField()
     Time_out=forms.TimeField()


     #botcatcher=forms.CharField(required=False,widget=forms.Hiddeninput,validators=[Validators.MaxlengthValidator(0)])
     class Meta():
         model=user_info
         fields='__all__'

class FileForm(forms.ModelForm):
      class Meta:
          model= File
          fields= ["filepath"]




     #botcatcher=forms.CharField(required=False,widget=forms.Hiddeninput,validators=[Validators.MaxlengthValidator(0)])
