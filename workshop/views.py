from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .models import Post
from .forms import PostForm

class BlogView(TemplateView):

    model = Post
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        post_list = Post.objects.all().order_by('-date')

        if (len(post_list) > 0):
            context['post_list'] = [
								({
									'title': post.title,
									'content': post.content,
									'author': post.author,
									'date': post.date
								})
								for post in post_list
								]
        else:
            context['error'] = 'Nessun post trovato'
        return context

def add_post_view(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog')
		else:
			args = {'form':form}
			return render(request, 'add_post.html', args)
	else:
		form = PostForm()
		args = {'form':form}
		return render(request, 'add_post.html', args)
