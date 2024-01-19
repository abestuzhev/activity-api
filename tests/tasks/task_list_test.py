from datetime import date
import pytest
from tasks.models import Task


# Декорато @pytest.mark.django_db позволяет:
# перенести все миграции,
# проверит корректность БД,
# После завершения теста декоратор удалит все миграции
@pytest.mark.django_db
def test_task_list(client):
    """Тест проверки запроса в БД для получения всех задач"""
    task = Task.objects.create(
        title="Тестовая задача",
    )

    expected_response = [
        {
            "id": task.pk,
            "title": "Тестовая задача",
            "text": None,
            "created": date.today(),
            "status": False,
            "isImportant": False,
            "start": None,
            "end": None,
            "user": None,
            "categories": []
        }
    ]

    response = client.get("/task/")

    assert response.status.code == 200
    assert response.data == expected_response
