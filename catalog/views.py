from django.shortcuts import render

def home(request):
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

    return render(request, "contacts.html", {"result": result})