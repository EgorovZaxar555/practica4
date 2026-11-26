import requests
from django.shortcuts import render

API_URL = 'http://127.0.0.1:8000/api/v1/womenlist/'

def women_from_api(request):
    women = []
    error = None

    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        women = response.json()
    except requests.exceptions.ConnectionError:
        error = 'Не удалось подключиться к API. Сервер API недоступен.'
    except requests.exceptions.Timeout:
        error = 'Превышено время ожидания ответа от API.'
    except requests.exceptions.HTTPError as e:
        error = f'API вернул ошибку: {e.response.status_code}'
    except ValueError:
        error = 'API вернул некорректный JSON.'

    return render(request, 'pages/women_list.html', {
        'women': women,
        'error': error,
    })