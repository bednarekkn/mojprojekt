import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

# 1. Widok strony głównej
def index(request):
    return render(request, 'tasks/index.html')

# 2. API: Pobieranie listy (GET) i dodawanie zadania (POST)
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-created_at')
        return JsonResponse([task.to_dict() for task in tasks], safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title', '').strip()

            # Walidacja: puste zadanie nie przejdzie
            if not title:
                return JsonResponse({'error': 'Treść zadania nie powinna być pusta!'}, status=400)

            task = Task.objects.create(title=title)
            return JsonResponse(task.to_dict(), status=201)
        except Exception:
            return JsonResponse({'error': 'Nieprawidłowy format danych.'}, status=400)

    return JsonResponse({'error': 'Metoda niedozwolona.'}, status=405)

# 3. API: Zmiana statusu (PATCH) i usuwanie zadania (DELETE)
def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Zadanie o podanym ID nie istnieje.'}, status=404)

    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            if 'completed' in data:
                task.completed = bool(data['completed'])
            task.save()
            return JsonResponse(task.to_dict(), status=200)
        except Exception:
            return JsonResponse({'error': 'Błąd aktualizacji zadania.'}, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Usunięto pomyślnie.'}, status=200)

    return JsonResponse({'error': 'Metoda niedozwolona.'}, status=405)