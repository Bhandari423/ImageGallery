from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import ImageDetail
from .forms import UploadForm


# Create your views here.
def ShowImage(request):
    images = ImageDetail.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'index.html', {'images': images})

def Detail(request, id):
    photo = ImageDetail.objects.get(id=id)
    return render(request, 'new.html', {'photo': photo})

def FormView(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('gallery')
    else:
        form = UploadForm()

    return render(request, 'form_page.html', {'form': form})