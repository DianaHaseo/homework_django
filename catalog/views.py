from django.shortcuts import render

from catalog.models import Contact, Product

def home(request):
    products = Product.objects.order_by("-created_at", "-id")[:5]

    for product in products:
        print(product)

    return render(request, "home.html")

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

    context = {
        "result": result,
        "contact": contact,
    }

    return render(request, "contacts.html", context)