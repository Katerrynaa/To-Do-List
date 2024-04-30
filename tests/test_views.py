from unittest.mock import patch
from pytest import fixture

from src.managers import ToDoManager
from src.models import ToDoModel


class TestCreateToDoView:
    @fixture(scope="class")
    def manager_create_mock(self, tasks_data):
        with patch.object(ToDoManager, "create") as mock:
            mock.return_value = ToDoModel(**tasks_data)
            yield mock

    @fixture(scope="class", autouse=True)
    def create_task(self, test_client, manager_create_mock, tasks_data):
        return test_client.post("/create", json=tasks_data)
    
    def test_manager_called(self, manager_create_mock, tasks_data):
        manager_create_mock.assert_called_once_with(tasks=tasks_data)

    def test_result(self, create_task):
        assert create_task.json() == {"message": "Successfully!"}
    
    