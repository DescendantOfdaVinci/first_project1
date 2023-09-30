from django.http import HttpResponse
from django.shortcuts import render


def junior(request):
    main = 'Junior Developer'
    requirements1 = ['Опыт написания простых SQL-запросов', 'Опыт работы с HTML и верстки макетов (HTML, CSS, JavaScript)',
    'Понимание основ ООП', 'Желание развиваться как разработчик', 'Владение английским на уровне чтения технической документации',
    'HTML5, CSS, JavaScript, React', 'Знание современных подходов к вёрстке']
    salary = {'min': 15000,
    'max': 90000}
    context = {'main':main,
               'requirements': requirements1,
               'salary': salary}
    return render(request, 'junior.html', context=context)

def middle(request):
    main = 'Middle Developer'
    requirements1 = ['Опыт работы от 1 года', 'Знание Python 3.10+',
    'Уверенный пользователь Linux', 'Базовые знания Docker, Docker Compose', 'Владение английским на уровне B2',
    'Опыт работы с система контроля версий Git', 'Знание современных подходов к вёрстке']
    salary = {'min': 85000,
    'max': 280000}
    context = {'main':main,
               'requirements': requirements1,
               'salary': salary}
    return render(request, 'middle.html', context=context)

def senior(request):
    main = 'Senior Developer'
    requirements1 = ['Опыт работы 3-6 лет', 'Cильный разработчик с коммерческим опытом',
    'Отличное знание Python', 'Написание веб-приложения', 'Готовность взаимодействовать с командой разработчиков, дизайнеров и методистов на понятном для них языке',
    'Django Framework, PostgreSQL, Docker, VueJS, React', 'Уровень английского: B2-C1', 'Умение читать и понимать чужой код'
    'Понимание ООП, паттернов проектирования, понимание принципов SOLID', 'Опыт использования ORM (Hibernate, JPA), Query Builder']
    salary = {'min': 140000,
    'max': 350000}
    context = {'main':main,
               'requirements': requirements1,
               'salary': salary}
    return render(request, 'senior.html', context=context)
