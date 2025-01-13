from django.shortcuts import render


def platform_page(request):
    platform = {'Title': 'platform',
                'main_page': 'Главная страница',
                'text1': 'Главная',
                'text2': 'Магазин',
                'text3': 'Корзина'}
    return render(request, 'third_task/platform.html', platform)


def games_page(request):
    games = {'Title': 'Магазин',
             'name': 'Игры',
             'game1': 'Atomic Heart',
             'game2': 'Cyberpank 2077',
             'game3': 'PayDay 2'}
    return render(request, 'third_task/games.html', games)


def cart_page(request):
    text = 'Извините, Ваша корзина пуста'
    cart = {'Title': 'Корзина', 'text': text}
    return render(request, 'third_task/cart.html', cart)
