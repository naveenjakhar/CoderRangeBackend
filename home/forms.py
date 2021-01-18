from .models import Democlass,Democlass_otp,Profile
from django import forms

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model=UserProjects
#         fields=('projectname','Projectabout','Demo_img','Files')
# class BatchForm(forms.ModelForm):
#     class Meta:
#         model=batchtype
#         fields=('classtype')

# class ProfilehForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=''

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=Review
#         fields='__all__'

class Demo_Form(forms.ModelForm):
    class Meta:
        model=Democlass
        fields=['email','kidName','kid_Age','lapptop_availability']

class img_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['photo']
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','town','state','dist','country','schoolName','pincode']
# class img_Form(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=['photo']
class Demo_Form_otp(forms.ModelForm):
    class Meta:
        model=Democlass_otp
        fields=('email','kidName','kid_Age','lapptop_availability')

# class img_Form(forms.Form):
#     photo = forms.FileField()