"""
URL configuration for TechReform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from TechReformApp import views as t_views  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", t_views.index, name="index"),
    path("base/", t_views.base, name="base"),
    path("index/", t_views.index, name="index"),
    path("404/", t_views.error_404, name="error_404"),
    path("about-us/", t_views.about_us, name="about_us"),
    path("blog-grid-sidebar/", t_views.blog_grid_sidebar, name="blog_grid_sidebar"),
    path(
        "blog-single-sidebar/", t_views.blog_single_sidebar, name="blog_single_sidebar"
    ),
    path("blog-single/", t_views.blog_single, name="blog_single"),
    path("checkout/", t_views.checkout, name="checkout"),
    path("contact/", t_views.contact, name="contact"),
    path("faq/", t_views.faq, name="faq"),
    path("login/", t_views.login, name="login"),
    path("logout/", t_views.custom_logout, name="logout"),
    path("mail-success/", t_views.mail_success, name="mail_success"),
    path("<str:id>", t_views.product_details, name="product_details"),
    path("product-grids/", t_views.product_grids, name="product_grids"),
    path("product-list/", t_views.product_list, name="product_list"),
    path("register/", t_views.register, name="register"),
    path("user-profile/", t_views.user_profile, name="user_profile"),
    path("cpu-upload/", t_views.cpu_upload, name="cpu_upload"),
    path("cpu-update/<str:id>", t_views.cpu_update, name="cpu_update"),
    path("cpu-delete/<str:id>", t_views.cpu_delete, name="cpu_delete"),
    path("cpu-grids/", t_views.cpu_grids, name="cpu_grids"),
    path("cooler-upload/", t_views.cooler_upload, name="cooler_upload"),
    path("cooler-update/<str:id>", t_views.cooler_update, name="cooler_update"),
    path("cooler-delete/<str:id>", t_views.cooler_delete, name="cooler_delete"),
    path("cooler-grids/", t_views.cooler_grids, name="cooler_grids"),
    path("casing-upload/", t_views.casing_upload, name="casing_upload"),
    path("casing-update/<str:id>", t_views.casing_update, name="casing_update"),
    path("casing-delete/<str:id>", t_views.casing_delete, name="casing_delete"),
    path("casing-grids/", t_views.casing_grids, name="casing_grids"),
    path("motherboard-upload/", t_views.motherboard_upload, name="motherboard_upload"),
    path(
        "motherboard-update/<str:id>",
        t_views.motherboard_update,
        name="motherboard_update",
    ),
    path(
        "motherboard-delete/<str:id>",
        t_views.motherboard_delete,
        name="motherboard_delete",
    ),
    path("motherboard-grids/", t_views.motherboard_grids, name="motherboard_grids"),
    path("hdd-upload/", t_views.hdd_upload, name="hdd_upload"),
    path("hdd-update/<str:id>", t_views.hdd_update, name="hdd_update"),
    path("hdd-delete/<str:id>", t_views.hdd_delete, name="hdd_delete"),
    path("hdd-grids/", t_views.hdd_grids, name="hdd_grids"),
    path("gpu-upload/", t_views.gpu_upload, name="gpu_upload"),
    path("gpu-update/<str:id>", t_views.gpu_update, name="gpu_update"),
    path("gpu-delete/<str:id>", t_views.gpu_delete, name="gpu_delete"),
    path("gpu-grids/", t_views.gpu_grids, name="gpu_grids"),
    path("keyboard-upload/", t_views.keyboard_upload, name="keyboard_upload"),
    path("keyboard-update/<str:id>", t_views.keyboard_update, name="keyboard_update"),
    path("keyboard-delete/<str:id>", t_views.keyboard_delete, name="keyboard_delete"),
    path("keyboard-grids/", t_views.keyboard_grids, name="keyboard_grids"),
    path("headphone-upload/", t_views.headphone_upload, name="headphone_upload"),
    path(
        "headphone-update/<str:id>", t_views.headphone_update, name="headphone_update"
    ),
    path(
        "headphone-delete/<str:id>", t_views.headphone_delete, name="headphone_delete"
    ),
    path("headphone-grids/", t_views.headphone_grids, name="headphone_grids"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
