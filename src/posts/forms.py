from django import forms 
# from pagedown.widgets import PagedownWidget
# from django.forms.utils import flatatt

from .models import Post, Images


class PostForm(forms.ModelForm):
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