from django.shortcuts import render


def platform_page(request):
    context = {'title': 'Стартовая страница'}
    return render(request, 'fourth_task/platform.html', context)


def games_page(request):
    context = {
        'title': 'Игры',
        'title1': 'Сегодня мы предлагаем:',
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2', 'Alone in the Dark']}
    return render(request, 'fourth_task/games.html', context)


def cart_page(request):
    context = {'title': 'Корзина',  'text': 'Извините, Ваша корзина пуста.',
               'text1': 'Пожалуйста, сделайте свой выбор!'}
    return render(request, 'fourth_task/cart.html', context)
