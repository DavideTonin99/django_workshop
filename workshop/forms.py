from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
