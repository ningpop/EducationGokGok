from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder':'15자 이내로 입력 가능합니다.',
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                }),
            'password' : forms.PasswordInput(attrs={
                'class': 'form-control',
                }),
        }
        labels = {
            'username': '이름',
            'email': '이메일',
            'password': '패스워드',
        }
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'phone']
        widget ={
            'age': forms.TextInput(),
            # 'gender' : forms.
            'phone' : forms.TextInput()
        }

        labels = {
            'age': '나이',
            # 'gender' : '성별',
            'phone': '휴대폰 번호',
        }