
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# ilerleyen aşamalarda bu datalar veritabanından gelicek

data = {
    "komedi": "komedi kategorisine ait filmler",
    "aksiyon": "aksiyon kategorisine ait filmler",
    "drama": "drama film kategorisine ait filmler",
    "ask": "ask kategorisine ait filmler"
}


def index(request):
    return render(request, 'movies/index.html')


def filmler(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('movies_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Film Listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)


def details(request, film_adi):
    return HttpResponse(f'{film_adi} detay sayfasi')


def getMoviesByCategory(request, category_name):
    try:
        category_text = data[category_name]

        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>yanlış kategori secimi</h1>")


def getMoviesByCategoryId(request, category_id):
    category_list = list(data.keys())
    category_name = category_list[category_id-1]
    redirect_url = reverse('movies_by_category', args=[category_name])
    return redirect(redirect_url)
