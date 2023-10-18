
from django.shortcuts import render, redirect
from .forms import MetricForm
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .serializers import MetricSerializer
from .utils import add_hardcoded_metrics #импорт захардкоженных данных из utils.py
import matplotlib.pyplot as plt

#основной класс, реализует get и post запросы к API
class MetricListCreateView(APIView):
    def get(self, request):
        # Получаем все метрики
        metrics = Metric.objects.all()
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Добавить метрику, используя переданный JSON
        data = request.data
        serializer = MetricSerializer(data=data)

        if serializer.is_valid():
            # Сохраняем новую метрику
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#основной класс, реализует get (не все, а отдельную) put и delete запросы к API
class MetricGraphView(APIView):
    #функция позволяет обращаться к апи и забирать записи либо по name, либо по name+id и названию для уточнения

    def get(self, request, metric_name, metric_id=None):
        if metric_id is not None:
            # Получаем метрику по id и name
            metric = get_object_or_404(Metric, id=metric_id, name=metric_name)
            serializer = MetricSerializer(metric)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Получаем метрику только по name
            metrics = Metric.objects.filter(name=metric_name)
            if not metrics:
                return Response({"detail": "No metrics found for the given name."}, status=status.HTTP_404_NOT_FOUND)
            serializer = MetricSerializer(metrics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, metric_name, metric_id):
        # Обновляем данные метрики
        metric = get_object_or_404(Metric, id=metric_id, name=metric_name)
        data = request.data
        serializer = MetricSerializer(metric, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, metric_name, metric_id):
        # Удаляем метрику
        metric = get_object_or_404(Metric, id=metric_id, name=metric_name)
        metric.delete()
        return Response({"detail": "Metric successfully deleted."}, status=status.HTTP_204_NO_CONTENT)



def create_metric(request):
    #форма для создания новой записи

    if request.method == 'POST':
        form = MetricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('metric-list-create')
    else:
        form = MetricForm()

    return render(request, 'create_metrics.html', {'form': form})


def visualize_metrics(request, metric_id_1, metric_id_2):
    # Дергаем данные из модели по идентификаторам
    metric1 = get_object_or_404(Metric, id=metric_id_1)
    metric2 = get_object_or_404(Metric, id=metric_id_2)

    # Присваиваем полям интересующие нас данные

    event_ids = [metric1.name, metric2.name]  # ID и имя чтобы понятно
    values = [metric1.value, metric2.value]  # Значение для визуализации

    # Построение диаграммы
    plt.bar(range(len(values)), values, tick_label=event_ids)

    # Подписи заголовка и осей
    plt.xlabel('metrics name')
    plt.ylabel('Количество')
    plt.title(f'Metrics Visualization. id: {metric1.id} and id:{ metric2.id}')

    # Сохранение графика в файл
    plt.savefig('graph.png')

    # Передача изображения пользователю
    with open('graph.png', 'rb') as img:
        response = HttpResponse(img, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="graph.png"'
        return response


# Вызываем функцию для добавления хардкодированных данных

add_hardcoded_metrics()