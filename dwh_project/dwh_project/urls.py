"""
URL configuration for dwh_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from metrics.views import *
from django.urls import path


urlpatterns = [
    # Эндпоинты для создания/получения метрик и графика (весь функционал)
    path('admin/', admin.site.urls),
    path('', MetricListCreateView.as_view(), name='metric-list-create'), #интерфейс встроенный реста. все записи
    path('post/', create_metric, name='create-metric'), #добавить метрику через форму

    path('get/<str:metric_name>/<int:metric_id>/', MetricGraphView.as_view(), name='metric-graph-id'),
    path('get/<str:metric_name>/', MetricGraphView.as_view(), name='metric-graph'), #получить метрику (нужно ввести name интересующей метрики)

    path('put/<str:metric_name>/<int:metric_id>/', MetricGraphView.as_view(), name='metric-put'),#изменить метрику (нужно ввести name интересующей метрики и ее Id)

    path('delete/<str:metric_name>/<int:metric_id>/', MetricGraphView.as_view(), name='metric-delete'),#удалить метрику (нужно ввести name интересующей метрики и ее id)


    #построить график, делал второпях, на других данных не проверял. сделал для total_number_of_note и total_number_of_objects
    #http://127.0.0.1:8000/graph/total_number_of_note/total_number_of_objects у меня через 8000 порт работает так. может на маках все по-другому как-то
    path('graph/<int:metric_id_1>/<int:metric_id_2>/', visualize_metrics, name='visualize-metrics') #нужно ввести id интересующих метрик
]




