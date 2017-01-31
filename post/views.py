from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list1(request):
	return HttpResponseRedirect("/")

def post_list(request):
	queryset = Post.objects.all().order_by("-dateshow")
	context = {
		"objects": queryset,
	}
	return render(request, "post_list.html", context)

def post_create(request):
	if request.user.is_staff:
		form = PostForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			storage = messages.get_messages(request)
			storage.used = True
			messages.success(request, "Successfully Created") # extra_tags="" can be added
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			storage = messages.get_messages(request)
			storage.used = True
			messages.success(request, "Not Successfully Created")
		context = {
			"form": form,
		}
	return render(request, "post_form.html", context)

def post_detail(request, id):
	queryset = get_object_or_404(Post, id=id)
	context = {
		"objects": queryset,
	}
	return render(request, "post_detail.html", context)

def post_delete(request, id):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("post:list")

def post_update(request, id):
	instance = get_object_or_404(Post, id=id)
	if request.user.is_staff:
		form = PostForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Successfully Updated")
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			messages.success(request, "Not Successfully Edited")
		context = {
			"form": form,
			"objects": instance,
		}
	return render(request, "post_form.html", context)