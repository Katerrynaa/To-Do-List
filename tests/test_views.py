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
        assert create_task.json() == { "message": "Successfully!" }



class TestGetToDoView:
    @fixture(scope="class")
    def manager_get_mock(self):
        with patch.object(ToDoManager, "get") as mock:
            yield mock 

    @fixture(scope="class", autouse=True)
    def task_data(self, test_client, manager_get_mock):
        return test_client.get("/get")
    
    def test_manager_called(self, manager_get_mock):
        manager_get_mock.assert_called_once_with()

    def test_result(self, task_data):
        assert task_data.json() == {}


class TestGetToDoViewNotFound:
    task_id = 1 

    @fixture(scope="class")
    def manager_get_by_id_mock(self):
        with patch.object(ToDoManager, "get_by_id") as mock:
            mock.return_value = None
            yield mock 

    @fixture(scope="class", autouse=True)
    def get_by_id_todo(self, test_client, manager_get_by_id_mock):
        return test_client.get(f"/get_by_id/{self.task_id}")
    
    def test_manager_called(self, manager_get_by_id_mock):
        manager_get_by_id_mock.assert_called_once_with(self.task_id)

    def test_result(self, get_by_id_todo):
        assert get_by_id_todo.json() == {
            "detail": "Task with such ID not found"
        }

    def test_status_code(self, get_by_id_todo):
        assert get_by_id_todo.status_code == 404


