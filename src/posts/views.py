from urllib.parse import quote_plus 
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):

	qureyset_list = Post.objects.all()#.order_by("-timestamp")
	
	paginator = Paginator(qureyset_list, 6)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	contex = {
		"object_list": querySet,

	}
	return render (request, "post_list.html", contex)
	# return HttpResponse("<h1>Hello wise</h1>")

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not successfully Created")
	content = {
		"form": form
	}
	return render (request, "post_form.html", content)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(instance.content)
	contex = {
		"title":instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", contex)
	# return HttpResponse("<h1>Details All Posts</h1>")

def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Updated </a>Successfully", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	content = {
	"title": instance.title,
	"instance": instance,
	"form":form,
	}
	return render (request, "post_form.html", content)


def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")


