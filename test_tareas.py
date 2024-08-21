import pytest
from tarea import SistemaTareas

@pytest.fixture
def sistema():
    return SistemaTareas()

def test_agregar_tarea(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    assert len(sistema.listar_tareas()) == 1
    assert sistema.listar_tareas()[0] == (1, "Tarea 1", "alta")

def test_agregar_tarea_con_id_existente(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    with pytest.raises(ValueError):
        sistema.agregar_tarea(1, "Tarea 2", "baja")

def test_actualizar_tarea(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    sistema.actualizar_tarea(1, "Tarea Actualizada", "media")
    assert sistema.listar_tareas()[0] == (1, "Tarea Actualizada", "media")

def test_actualizar_tarea_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.actualizar_tarea(1, "Tarea No Existente", "baja")

def test_marcar_completada(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    sistema.marcar_completada(1)
    assert sistema.listar_tareas(completadas=True)[0] == (1, "Tarea 1", "alta")

def test_marcar_completada_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.marcar_completada(1)

def test_eliminar_tarea(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    sistema.eliminar_tarea(1)
    assert len(sistema.listar_tareas()) == 0

def test_eliminar_tarea_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.eliminar_tarea(1)

def test_listar_tareas(sistema):
    sistema.agregar_tarea(1, "Tarea 1", "alta")
    sistema.agregar_tarea(2, "Tarea 2", "baja")
    sistema.marcar_completada(2)
    assert sistema.listar_tareas() == [(1, "Tarea 1", "alta")]
    assert sistema.listar_tareas(completadas=True) == [(2, "Tarea 2", "baja")]
