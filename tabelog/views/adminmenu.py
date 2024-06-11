from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from tabelog.models import Store, Category, Review
from django.urls import reverse_lazy
from ..forms import StoreForm

class HomeView(TemplateView):
    template_name = 'admin_home.html'


class StoreListView(ListView):
    template_name = 'admin_store_list.html'
    model = Store
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        # フィルタリング
        if store_name := query.get('store_name'):
            queryset = queryset.filter(name__icontains=store_name).order_by('id')
        # ソート
        if sort_by := query.get('sort_by'):
            queryset = queryset.order_by(sort_by)
        # カテゴリ
        if category := query.get('category'):
            queryset = queryset.filter(category__exact=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_query'] = self.request.GET.get('top_query', '')
        context['store_name'] = self.request.GET.get('store_name', '')
        context['sort_by'] = self.request.GET.get('sort_by', '')
        context['select_category'] = self.request.GET.get('category')
        context['categorys'] = Category.objects.all()
        return context


class StoreDetailView(DetailView):
    template_name = 'admin_store_detail.html'
    model = Store

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(store__id=self.kwargs['pk'])
        context['user'] = self.request.user
        return context


class StoreEditView(UpdateView):
    template_name = 'admin_store_edit_form.html'
    model = Store
    form_class = StoreForm

    def get_success_url(self) -> str:
        return reverse_lazy('tabelog:admin-store-detail', kwargs={'pk': self.object.id})


