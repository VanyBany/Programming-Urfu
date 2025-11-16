import json
import os
from django.shortcuts import render
from django.http import JsonResponse

def read_starships_data():
    """Чтение данных о кораблях из JSON файла"""
    # Пробуем разные пути
    possible_paths = [
        # Рядом с папкой проекта
        os.path.join(os.path.dirname(__file__), '..', '..', '..', 'starships_data.json'),
        # В корне проекта (рядом с manage.py)
        os.path.join(os.path.dirname(__file__), '..', '..', 'starships_data.json'),
        # Абсолютный путь (замените на ваш реальный путь)
        'E:/Photo and video/Mine/Для программирования/Работа с Питоном/my_django/starships_data.json'
    ]
    
    for file_path in possible_paths:
        absolute_path = os.path.abspath(file_path)
        print(f"Проверяем путь: {absolute_path}")
        
        if os.path.exists(absolute_path):
            print(f"Файл найден: {absolute_path}")
            try:
                with open(absolute_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    print(f"Файл успешно прочитан, тип данных: {type(data)}")
                    return data
            except Exception as e:
                print(f"Ошибка чтения файла: {e}")
                continue
    
    print("Файл starships_data.json не найден ни по одному пути!")
    return {}

def get_starships_list(request):
    """Список всех кораблей с диагностикой"""
    starships_data = read_starships_data()
    starships_list = []
    
    # ДИАГНОСТИКА
    print("=== ДИАГНОСТИКА STARSHIPS ===")
    print(f"Тип данных: {type(starships_data)}")
    print(f"Длина данных: {len(starships_data)}")
    
    if isinstance(starships_data, dict):
        print(f"Ключи: {list(starships_data.keys())}")
    
    # Если это словарь с полной структурой SWAPI
    if isinstance(starships_data, dict) and 'results' in starships_data:
        print("Обнаружена структура SWAPI с 'results'")
        actual_ships = starships_data['results']
        print(f"Кораблей в results: {len(actual_ships)}")
        
        for index, starship_info in enumerate(actual_ships):
            print(f"Корабль {index + 1}: {starship_info.get('name', 'Unknown')}")
            buff_dict = {
                'id': index + 1,
                'name': starship_info.get('name', 'Unknown'),
                'model': starship_info.get('model', 'Unknown'),
                'starship_class': starship_info.get('starship_class', 'Unknown'),
                'manufacturer': starship_info.get('manufacturer', 'Unknown')
            }
            starships_list.append(buff_dict)
            
    # Если это уже список кораблей
    elif isinstance(starships_data, list):
        print("Обнаружен список кораблей")
        for index, starship_info in enumerate(starships_data):
            buff_dict = {
                'id': index + 1,
                'name': starship_info.get('name', 'Unknown'),
                'model': starship_info.get('model', 'Unknown'),
                'starship_class': starship_info.get('starship_class', 'Unknown'),
                'manufacturer': starship_info.get('manufacturer', 'Unknown')
            }
            starships_list.append(buff_dict)
    
    # Если это словарь с кораблями по ID
    elif isinstance(starships_data, dict):
        print("Обнаружен словарь с кораблями")
        for starship_id, starship_info in starships_data.items():
            buff_dict = {
                'id': starship_id,
                'name': starship_info.get('name', 'Unknown'),
                'model': starship_info.get('model', 'Unknown'),
                'starship_class': starship_info.get('starship_class', 'Unknown'),
                'manufacturer': starship_info.get('manufacturer', 'Unknown')
            }
            starships_list.append(buff_dict)
    
    else:
        print("Неизвестный формат данных")
    
    print(f"Создано элементов для шаблона: {len(starships_list)}")
    print("=====================")
    
    context = {
        'starships': starships_list
    }
    return render(request, 'starships/starships_list.html', context)

def get_starship(request, id):
    """Детальная информация о корабле"""
    starships_data = read_starships_data()
    
    # Извлекаем корабли из results если нужно
    if isinstance(starships_data, dict) and 'results' in starships_data:
        starships_data = starships_data['results']
    
    # Ищем корабль по индексу (ID-1, так как индексы с 0)
    if isinstance(starships_data, list) and 0 <= id - 1 < len(starships_data):
        starship_info = starships_data[id - 1]
    elif isinstance(starships_data, dict):
        starship_info = starships_data.get(str(id))
    else:
        starship_info = None
    
    if not starship_info:
        return JsonResponse({'error': 'Starship not found'}, status=404)
    
    context = {
        'starship': starship_info,
        'starship_id': id
    }
    return render(request, 'starships/starship_detail.html', context)