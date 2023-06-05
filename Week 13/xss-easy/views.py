from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from imghost.models import Image
import requests
import os

def index(request):
    return render(request, "index.html")

def add_new(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            link = request.POST['link']

            image = Image(link=link, alt_txt=title)
            image.save()
            return redirect(reverse('view-image', kwargs={"id": image.id}))
        except:
            messages.error(request, 'Failed to add new image.')
    return render(request, "add.html")

def view_image(request, id):
    img = Image.objects.get(id=id)
    return render(request, "view.html", context={'image': img})

def report_image(request, id):
    img_url = reverse('view-image', kwargs={"id": id})
    ADMIN_REPORT_URL = os.getenv("ADMIN_REPORT_URL", "http://admin-report:5000")
    HOST_URL = os.getenv("HOST_URL", "http://web:80")
    requests.post(ADMIN_REPORT_URL, json={'url': f'{HOST_URL}{img_url}'})
    messages.success(request, "Thank you for your report!")
    return redirect(img_url)
