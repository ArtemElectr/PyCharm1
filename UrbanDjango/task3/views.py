from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    return render(request, 'platform.html')


def games(request):
    context = {
        'game1': 'Atomic Heart',
        'game2': 'Cyberpunk 2077',
        'game3': 'PayDay 2',
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')

# class Shop(TemplateView):
#     template_name = 'platform.html',
#
#     def get_context_data(self, **kwargs):
#         context = super(Shop, self).get_context_data(**kwargs)
#         context.update({'game1': 'Atomic Heart', 'game2': 'Cyberpunk 2077', 'game3': 'PayDay 2'})
#         return context
