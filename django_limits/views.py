from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def limit_exceeded_view(request, limit_exception, template=None):
    license_data = None
    if hasattr(limit_exception, "get_license_func"):
        get_license_func = limit_exception.get_license_func
        license_data = get_license_func() if get_license_func else None
    if template is None:
        template = "django_limits/limit_exceeded.html"
    return render(
        request,
        template,
        {
            "exception": limit_exception,
            "license": license_data,
            "model_name": limit_exception.model._meta.verbose_name,
            "model_name_plural": limit_exception.model._meta.verbose_name_plural
        },
        status=403
    )
