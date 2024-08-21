class Tarea:
    def __init__(self, id_tarea, descripcion, prioridad):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

class SistemaTareas:
    def __init__(self):
        self.tareas = {}

    def agregar_tarea(self, id_tarea, descripcion, prioridad):
        if id_tarea in self.tareas:
            raise ValueError(f"La tarea con ID {id_tarea} ya existe.")
        self.tareas[id_tarea] = Tarea(id_tarea, descripcion, prioridad)

    def actualizar_tarea(self, id_tarea, nueva_descripcion, nueva_prioridad):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con ID {id_tarea}.")
        tarea = self.tare[id_tarea]
        #borre unas letras de la varibale tareas para que el testing vea el error 
        tarea.descripcion = nueva_descripcion
        tarea.prioridad = nueva_prioridad

    def marcar_completada(self, id_tarea):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con ID {id_tarea}.")
        self.tareas[id_tarea].completada = True

    def eliminar_tarea(self, id_tarea):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con ID {id_tarea}.")
        del self.tareas[id_tarea]

    def listar_tareas(self, completadas=False):
        return [
            (tarea.id_tarea, tarea.descripcion, tarea.prioridad)
            for tarea in self.tareas.values()
            if tarea.completada == completadas
        ]
