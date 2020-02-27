from django import forms 
# from pagedown.widgets import PagedownWidget
# from django.forms.utils import flatatt

from .models import Post, Images


class PostForm(forms.ModelForm):
	title = forms.CharField(label='Title', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	price = forms.CharField(label='Price', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	location = forms.CharField(label='Location', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	catagories = forms.CharField(label='Catagories', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	beds = forms.CharField(label='Beds', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	bath = forms.CharField(label='Bath', 
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

	# content = forms.CharField(widget=PagedownWidget)
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			"title",
			"price",
			"location",
			"catagories",
			"beds",
			"bath",
			"content",
			"image",
			"draft",
			"publish",
		]

class ImageForm(forms.ModelForm):
	image = forms.ImageField(label='Image')
	class Meta:
		model = Images
		fields = ('image', )