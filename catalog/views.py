from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from catalog.forms import ProductForm
from catalog.models import Contact, Product


def home(request):
    products = Product.objects.all()

    # Стабильный порядок товаров для постраничного вывода
    products = products.order_by("id")

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "home.html",
        {"page_obj": page_obj},
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        "product_detail.html",
        {"product": product},
    )


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm()

    return render(
        request,
        "product_form.html",
        {"form": form},
    )


def contacts(request):
    result = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and phone and message:
            result = "Спасибо! Ваше обращение успешно принято."
        else:
            result = "Заполните все поля формы."

    contact = Contact.objects.order_by("id").first()

    return render(
        request,
        "contacts.html",
        {
            "result": result,
            "contact": contact,
        },
    )