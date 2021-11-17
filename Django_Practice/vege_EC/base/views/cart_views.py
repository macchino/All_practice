from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from base.models import Item
from collections import OrderedDict
from django.contrib.auth.decorators import login_required


class CartListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'pages/cart.html'

    def get_queryset(self):  # get_querysetはListViewが持っているメソッド
        cart = self.request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            return redirect('/')
        self.queryset = []
        self.total = 0
        for item_pk, quantity in cart['items'].items():
            obj = Item.objects.get(pk=item_pk)
            obj.quantity = quantity  # obj.quantity,obj.subtotalはテンプレートで使うための一時的なもの
            obj.subtotal = int(obj.price * quantity) # databaseには入らない。
            self.queryset.append(obj)
            self.total += obj.subtotal
        self.tax_included_total = int(self.total * (settings.TAX_RATE + 1))
        cart['total'] = self.total
        cart['tax_included_total'] = self.tax_included_total
        self.request.session['cart'] = cart
        return super().get_queryset()

    def get_context_data(self, **kwargs):  # get_context_dataはListViewが持っているメソッド
        context = super().get_context_data(**kwargs)
        try:
            context["total"] = self.total
            context["tax_included_total"] = self.tax_included_total
        except Exception:
            pass
        return context


class AddCartView(LoginRequiredMixin, View):  # Viewはリクエストメソッド定義だけでpostメソッドで送信されたviewを記述できる
    def post(self, request): #postメソッドで送信された場合に処理がされる
        item_pk = request.POST.get('item_pk')  # item_pk, quantityという名前がhtmlから送られてきたらitem_pk, quantity
        quantity = int(request.POST.get('quantity')) #という変数に代入。htmlで最初に定義される名前をgetしている。
        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            items = OrderedDict()
            cart = {'items': items}
        if item_pk in cart['items']:
            cart['items'][item_pk] += quantity
        else:
            cart['items'][item_pk] = quantity
        request.session['cart'] = cart
        return redirect('/cart/')


@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', None)
    if cart is not None:
        del cart['items'][pk]
        request.session['cart'] = cart
    return redirect('/cart/')
