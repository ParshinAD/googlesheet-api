import django_tables2 as tables
from .models import Test


class TestTable(tables.Table):
    class Meta:
        model = Test
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "th" : {
                "_ordering": {
                    "orderable": "sortable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
