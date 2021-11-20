from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from blog.models import Article #アプリ」のblogで定義したmodelsのArticleをインポート
from mysite.forms import UserCreationForm
from django.contrib import messages

def index(request):
    objs = Article.objects.all()[:3]  # クラス定義したArticleのモデルの全てのテーブルを取る。[:3]で記事数制限
    return render(request, 'mysite/index.html', context={
        'title': 'Really Site', #単に文字列をcontextに渡して表示
        'articles': objs, #変数objsにモデル全てのテーブルをarticlesに代入して表示
    })



class Login(LoginView):
    template_name = 'mysite/auth.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了！！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'エラーあり')
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, '登録完了！！')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)


def mypage(request):
    context = {}
    return render(request, 'mysite/mypage.html', context)
