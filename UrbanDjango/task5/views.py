from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

users = ['Alex', 'Artur', 'John']
info = dict()


async def check_data_request(username, password, repeat_password, age):
    if password != repeat_password:
        info.update({'error': 'Пароли не совпадают'})
    elif age < 18:
        info.update({'error': 'Вы должны быть старше 18'})
    elif username in users:
        info.update({'error': 'Пользователь уже существует'})
    if password == repeat_password and age >= 18 and username not in users:
        users.append(username)
        info.update({'success': f'Приветствуем, {username}'})


async def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        info.clear()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            info.update({'form': form})
            await check_data_request(username, password, repeat_password, age)
            return render(request, 'registration_page.html', info)

    else:
        return render(request, 'registration_page.html', info)


async def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        info.clear()
        info.update({'username': username, 'password': password, 'repeat_password': repeat_password,
                     'age': age})

        await check_data_request(username, password, repeat_password, age)
        return render(request, 'registration_page.html', info)

    else:
        return render(request, 'registration_page.html', info)