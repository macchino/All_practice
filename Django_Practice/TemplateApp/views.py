from django.shortcuts import render


def index(request):
    val = 'GoodBye'
    return render(request, 'index.html', context={'value': val})


def home(request, first_name, last_name):
    my_name = f'{first_name} {last_name}'
    favorite_fruit = ['Apple', 'Grape', 'Lemon']
    my_info = {
        'name': 'Taro',
        'age': 23
    }
    status = 20
    return render(request, 'home.html',
                  context={
                      'my_name': my_name,
                      'favorite_fruit': favorite_fruit,
                      'my_info': my_info,
                      'status': status,
                  })


def sample1(request):
    return render(request, 'sample1.html')


def sample2(request):
    return render(request, 'sample2.html')


def sample(request):
    name = 'Ichiro Yamada'
    height = 175.5
    wight = 72
    bmi = wight / (height / 100)**2
    page_url = 'ホームページ: https://www.google.com'
    favorite_fruit = ['Apple', 'Grape', 'Lemon']
    msg = """hello
    may name is
    Ichiro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'fruit': favorite_fruit,
        'msg': msg,
        'msg2': msg2,
    })


class Country:

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


def sample3(request):
    country = Country('Japan', 100000000, 'Tokyo')
    return render(request, 'sample3.html', context={
        'country': country
    })
