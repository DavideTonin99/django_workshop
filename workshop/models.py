from django.db import models

class Post(models.Model):
	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		unique_together = ('title', 'content', 'author')

	title = models.CharField(max_length=255, blank=False, null=False)
	content = models.TextField()
	author = models.CharField(max_length=255, blank=False, null=False)
	date = models.DateTimeField(auto_now=False, null=False, blank=False)

	def __str__(self):
		return ', '.join([self.title, self.author, str(self.date)])
