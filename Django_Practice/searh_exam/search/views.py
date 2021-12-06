from django.shortcuts import render
from django.views.generic import ListView, DetailView
from search.models import Item, Category, Tag
from django.views import generic
from django.contrib import messages
from django.db.models import Q

from functools import reduce
from operator import and_

# Create your views here.


class IndexListView(generic.ListView):
    model = Item
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        stock = self.request.GET.get('stock')
        shipping = self.request.GET.get('shipping')
        all_items = self.request.GET.get('all_items')
        new = self.request.GET.get('new')
        name = self.request.GET.get('name')

        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''

            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i

            query = reduce(
                and_, [Q(name__icontains=q) | Q(price__icontains=q) for q in q_list]
            )
            queryset = queryset.filter(query)
            print(queryset)

            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        if stock:
            query = reduce(
                and_, [Q(stock__iexact=stock)]
                )
            queryset = queryset.filter(query)
            print(queryset)

        if shipping:
            queryset = queryset.filter(shipping__iexact=shipping)

        if all_items:
            queryset = queryset.filter(all_items__iexact=all_items)

        if new:
            queryset = queryset.filter(new__iexact=new)

        if name:
            queryset = queryset.filter(name__iexact=name)
        order_by_price = self.request.GET.get('order_by_price', 0)
        if order_by_price == '1':
            queryset = queryset.order_by('price')
        elif order_by_price == '2':
            queryset = queryset.order_by('-price')


        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.GET.get('name', '')
        context["keyword"] = self.request.GET.get('keyword', '')
        order_by_price =self.request.GET.get('order_by_price', 0)
        if order_by_price == '1':
            context['ascending'] = True
        elif order_by_price == '2':
            context['descending'] = True
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail.html'

