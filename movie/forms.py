import random
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie, Review


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text="Letters, numbers, or _ only (no spaces).",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username (e.g. rahul_99)',
            'autocomplete': 'username',
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    password1 = forms.CharField(
        label="Password",
        help_text="At least 8 characters (not all numbers).",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a strong password',
            'autocomplete': 'new-password',
        }),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password',
            'autocomplete': 'new-password',
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if User.objects.filter(username__iexact=username).exists():
            suggestions = []
            for suffix in [random.randint(10, 99), random.randint(100, 999), 2026]:
                candidate = f"{username}{suffix}"
                if not User.objects.filter(username__iexact=candidate).exists():
                    suggestions.append(candidate)
            hint = f" Try: {', '.join(suggestions[:2])}" if suggestions else ""
            raise forms.ValidationError(f'"{username}" is already taken.{hint}')
        return username


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'genre', 'description', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Action, Thriller, Drama'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Short movie summary...'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }