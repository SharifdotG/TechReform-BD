from .models import (
    CPU,
    Cooler,
    Motherboard,
    HDD,
    GPU,
    Casing,
    Keyboard,
    Headphone,
)
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import Group # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login as auth_login # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import logout # type: ignore
from .forms import (
    CPUForm,
    CoolerForm,
    CasingForm,
    MotherboardForm,
    HDDForm,
    GPUForm,
    KeyboardForm,
    HeadphoneForm,
)

# Create your views here.


def index(request):
    return render(request, "index.html")


def base(request):
    return render(request, "base.html")


def error_404(request):
    return render(request, "404.html")


def about_us(request):
    return render(request, "about-us.html")


def blog_grid_sidebar(request):
    return render(request, "blog-grid-sidebar.html")


def blog_single_sidebar(request):
    return render(request, "blog-single-sidebar.html")


def blog_single(request):
    return render(request, "blog-single.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def custom_logout(request):
    logout(request)
    # Perform any additional actions here (e.g., logging out analytics)
    return redirect("login")


def mail_success(request):
    return render(request, "mail-success.html")


def product_details(request, id):
    # For multiple models
    if CPU.objects.filter(id=id).exists():
        product = CPU.objects.get(id=id)
    elif Casing.objects.filter(id=id).exists():
        product = Casing.objects.get(id=id)
    elif Motherboard.objects.filter(id=id).exists():
        product = Motherboard.objects.get(id=id)
    elif Cooler.objects.filter(id=id).exists():
        product = Cooler.objects.get(id=id)
    elif GPU.objects.filter(id=id).exists():
        product = GPU.objects.get(id=id)
    elif HDD.objects.filter(id=id).exists():
        product = HDD.objects.get(id=id)
    elif Keyboard.objects.filter(id=id).exists():
        product = Keyboard.objects.get(id=id)
    elif Headphone.objects.filter(id=id).exists():
        product = Headphone.objects.get(id=id)
    else:
        product = None
    return render(request, "product-details.html", {"product": product})


def product_grids(request):
    cpu = CPU.objects.all()
    casing = Casing.objects.all()
    motherboard = Motherboard.objects.all()
    cooler = Cooler.objects.all()
    gpu = GPU.objects.all()
    hdd = HDD.objects.all()
    keyboard = Keyboard.objects.all()
    headphone = Headphone.objects.all()
    return render(
        request,
        "product-grids.html",
        {
            "cpu": cpu,
            "casing": casing,
            "motherboard": motherboard,
            "cooler": cooler,
            "gpu": gpu,
            "hdd": hdd,
            "keyboard": keyboard,
            "headphone": headphone,
        },
    )


def product_list(request):
    return render(request, "product-list.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Assign role (e.g., 'user', 'shopkeeper', or 'blogger') after registration
            role = request.POST.get("role")
            if role:
                group = Group.objects.get(name=role)
                user.groups.add(group)

            # Log the user in immediately after registration
            auth_login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def user_profile(request):
    return render(request, "user-profile.html")


def cpu_upload(request):
    form = CPUForm()

    if request.method == "POST":
        form = CPUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "cpu-upload.html", {"form": form})


def cooler_upload(request):
    form = CoolerForm()

    if request.method == "POST":
        form = CoolerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "cooler-upload.html", {"form": form})

def casing_upload(request):
    form = CasingForm()

    if request.method == "POST":
        form = CasingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "casing-upload.html", {"form": form})


def motherboard_upload(request):
    form = MotherboardForm()

    if request.method == "POST":
        form = MotherboardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "motherboard-upload.html", {"form": form})


def hdd_upload(request):
    form = HDDForm()

    if request.method == "POST":
        form = HDDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "hdd-upload.html", {"form": form})


def gpu_upload(request):
    form = GPUForm()

    if request.method == "POST":
        form = GPUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "gpu-upload.html", {"form": form})


def keyboard_upload(request):
    form = KeyboardForm()

    if request.method == "POST":
        form = KeyboardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "keyboard-upload.html", {"form": form})


def headphone_upload(request):
    form = HeadphoneForm()

    if request.method == "POST":
        form = HeadphoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "headphone-upload.html", {"form": form})


def cpu_update(request, id):
    product = CPU.objects.get(pk=id)
    form = CPUForm(instance=product)
    if request.method == "POST":
        form = CPUForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "cpu-upload.html", {"form": form})


def cooler_update(request, id):
    product = Cooler.objects.get(pk=id)
    form = CoolerForm(instance=product)
    if request.method == "POST":
        form = CoolerForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "cooler-upload.html", {"form": form})


def casing_update(request, id):
    product = Casing.objects.get(pk=id)
    form = CasingForm(instance=product)
    if request.method == "POST":
        form = CasingForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "casing-upload.html", {"form": form})


def motherboard_update(request, id):
    product = Motherboard.objects.get(pk=id)
    form = MotherboardForm(instance=product)
    if request.method == "POST":
        form = MotherboardForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "motherboard-upload.html", {"form": form})


def hdd_update(request, id):
    product = HDD.objects.get(pk=id)
    form = HDDForm(instance=product)
    if request.method == "POST":
        form = HDDForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "hdd-upload.html", {"form": form})


def gpu_update(request, id):
    product = GPU.objects.get(pk=id)
    form = GPUForm(instance=product)
    if request.method == "POST":
        form = GPUForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "gpu-upload.html", {"form": form})


def keyboard_update(request, id):
    product = Keyboard.objects.get(pk=id)
    form = KeyboardForm(instance=product)
    if request.method == "POST":
        form = KeyboardForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "keyboard-upload.html", {"form": form})


def headphone_update(request, id):
    product = Headphone.objects.get(pk=id)
    form = HeadphoneForm(instance=product)
    if request.method == "POST":
        form = HeadphoneForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_grids")
    return render(request, "headphone-upload.html", {"form": form})


def cpu_delete(request, id):
    product = CPU.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "cpu-delete.html", {"product": product})


def cooler_delete(request, id):
    product = Cooler.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "cooler-delete.html", {"product": product})


def casing_delete(request, id):
    product = Casing.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "casing-delete.html", {"product": product})


def motherboard_delete(request, id):
    product = Motherboard.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "motherboard-delete.html", {"product": product})


def hdd_delete(request, id):
    product = HDD.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "hdd-delete.html", {"product": product})


def gpu_delete(request, id):
    product = GPU.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "gpu-delete.html", {"product": product})


def keyboard_delete(request, id):
    product = Keyboard.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "keyboard-delete.html", {"product": product})


def headphone_delete(request, id):
    product = Headphone.objects.get(pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("product_grids")
    return render(request, "headphone-delete.html", {"product": product})


def cpu_grids(request):
    cpu = CPU.objects.all()
    return render(request, "cpu-grids.html", {"cpu": cpu})


def cooler_grids(request):
    cooler = Cooler.objects.all()
    return render(request, "cooler-grids.html", {"cooler": cooler})


def casing_grids(request):
    casing = Casing.objects.all()
    return render(request, "casing-grids.html", {"casing": casing})


def motherboard_grids(request):
    motherboard = Motherboard.objects.all()
    return render(request, "motherboard-grids.html", {"motherboard": motherboard})


def hdd_grids(request):
    hdd = HDD.objects.all()
    return render(request, "hdd-grids.html", {"hdd": hdd})


def gpu_grids(request):
    gpu = GPU.objects.all()
    return render(request, "gpu-grids.html", {"gpu": gpu})


def keyboard_grids(request):
    keyboard = Keyboard.objects.all()
    return render(request, "keyboard-grids.html", {"keyboard": keyboard})


def headphone_grids(request):
    headphone = Headphone.objects.all()
    return render(request, "headphone-grids.html", {"headphone": headphone})
