from django.shortcuts import render

# Create your views here.
from .models import Test
from .tables import TestTable
from django.core import serializers
from qsstats import QuerySetStats
from django.db.models import Sum, Count



def test1(request):
    table = TestTable(Test.objects.order_by('id').all())
    table.paginate(page=request.GET.get("page", 1), per_page=13)
    return render(request, "gsapi/first_page.html", {"table": table})


def test2(request):
    table = TestTable(Test.objects.order_by('id').all())
    table.paginate(page=request.GET.get("page", 1), per_page=13)

    data = serializers.serialize("python", Test.objects.order_by('id').all())

    dates = list(map(lambda x: x['fields']['delivery_date'], data))
    start_date = min(dates)
    end_date = max(dates)

    queryset = Test.objects.all()
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, date_field='delivery_date', aggregate=Sum('price_usd'))

    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='days')
    values = list(map(lambda x: (x[0], int(x[1])) if x[1] else (x[0], 0), values))

    total = int(sum(map(lambda x: x['fields']['price_usd'], data)))

    context = {
        'table': table,
        'values': values,
        'total': total
    }
    # return render_to_response('template.html', {'values': values})
    return render(request, 'gsapi/second_page.html', context)