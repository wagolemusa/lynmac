from urllib.parse import quote_plus 
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from django.db.models import Q
from .models import Post, Images
from .forms import PostForm, ImageForm
from django.forms import modelformset_factory

# Create your views here.
def post_list(request):
	qureyset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		qureyset_list = qureyset_list.filter(
			Q(title__icontains=query) | 
			Q(content__icontains=query)|
			Q(price__icontains=query)|
			Q(location__icontains=query)
			).distinct()
	paginator = Paginator(qureyset_list, 3)
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
	ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
	form = PostForm(request.POST or None, request.FILES or None)
	formset = ImageFormSet(request.POST or None, request.FILES or None,
                               queryset=Images.objects.none())
	if form.is_valid() and formset.is_valid():
		instance = form.save(commit=False)
		instance.save()

		for fx in formset.cleaned_data:
			image = fx['image']
			photo = Images(post=instance, image=image)
			photo.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request, "Not successfully Created")
	form = PostForm()
	formset = ImageFormSet(queryset=Images.objects.none())
	content = {
		"form": form,
		"formset": formset
	}
	return render (request, "post_form.html", content)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	qureyset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()
	paginator = Paginator(qureyset_list, 3)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)


	contex = {
		"title":instance.title,
		"instance": instance,
		"share_string": share_string,
		"object_list": querySet,
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
		return HttpResponseRedirect(instance.get_obsolute_url())
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


def about(request):
	return render (request, "about.html")


# List all properties 
def property_view(request):
	qureyset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		qureyset_list = qureyset_list.filter(
			Q(title__icontains=query) | 
			Q(content__icontains=query) 
			# Q(price__icontains=query)|
			# Q(location__icontains=query)
			).distinct()
	paginator = Paginator(qureyset_list, 6)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	contex = {
		"object_list": querySet,

	}
	return render(request, "properies.html", contex)


def latest(request):
	qureyset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		qureyset_list = Post.objects.all()
	paginator = Paginator(qureyset_list, 3)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	contex = {
		"object_list": querySet,

	}
	return render(request, "latest.html", contex)
