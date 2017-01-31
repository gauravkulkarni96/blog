from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	dateshow = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"timeshow",
			"dateshow"
			]