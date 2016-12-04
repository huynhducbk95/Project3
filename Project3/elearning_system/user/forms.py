

from django import forms

class RegistryUserForm(forms.Form):
    username = forms.CharField(label='Username',
                               max_length=30,
                               help_text='Enter your username',)
    account_name =forms.CharField(label='Account Name',
                                  max_length=30,
                                  help_text='Enter your account name',)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,)
    repassword = forms.CharField(label='Repeat Password',
                                 widget=forms.PasswordInput,
                                 help_text='Enter your password again')
    email = forms.EmailField(label='Email',
                             help_text='Enter your email')

    def clean(self):
        cleaned_data = super(RegistryUserForm,self).clean()
        username = cleaned_data.get('username')
        account_name = cleaned_data.get('accountname')
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        email = cleaned_data.get('email')
        if password != repassword:
            msg = 'repassword is not match password'
            self.add_error('repassword',msg)
        return cleaned_data



