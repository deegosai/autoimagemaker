# from django.contrib.auth.models import User
# from django import forms
# from django.contrib.auth.forms import UserChangeForm

# class SignUpForm(UserCreationForm):
#  password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
#  class Meta:
#   model = User
#   fields = ['username', 'first_name', 'last_name', 'email']
#   labels = {'email': 'Email'}

# class EditUserProfileForm(UserChangeForm):
#     password = None
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control round-input', 'style':'color:#5cb85c;', 'placeholder':'Enter Admin User Name*', 'required':True}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control round-input', 'placeholder':'Enter Admin Firstname*', 'required':True}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control round-input', 'placeholder':'Enter Admin Lastname*', 'required':True}),
#             'email': forms.EmailInput(attrs={'class': 'form-control round-input', 'placeholder':'Enter Admin Email*', 'required':True}),
#         }

#         # labels = {'email': 'Email'}

# class EditAdminProfileForm(UserChangeForm):
#  password = None
#  class Meta:
#   model = User
#   fields = '__all__'
#   labels = {'email': 'Email'}
