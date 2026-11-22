from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import ProductForm
from catalog.models import Contact, Product


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"
    paginate_by = 6
    ordering = "id"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"

    def get_success_url(self):
        return reverse(
            "product_detail",
            kwargs={"pk": self.object.pk},
        )


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse(
            "product_detail",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("home")


class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.order_by("id").first()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and phone and message:
            result = "Спасибо! Ваше обращение успешно принято."
        else:
            result = "Заполните все поля формы."

        context = self.get_context_data()
        context["result"] = result

        return render(
            request,
            self.template_name,
            context,
        )