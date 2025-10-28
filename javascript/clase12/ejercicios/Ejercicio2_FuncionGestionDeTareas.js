//Ejercicio 2: 
function createTaskManager() {

  let tasks = [];
  let nextId = 1; // para asignar IDs únicos a cada tarea

  return {

    // Con esta funcion agregamos una nueva tarea
    addTask: function(taskName) {
      const task = {
        id: nextId++,
        name: taskName,
        completed: false
      };
      tasks.push(task);
      console.log(`Tarea agregada: "${taskName}"`);
    },

    // Marcamos la tarea como completada
    completeTask: function(taskId) {
      const task = tasks.find(t => t.id === taskId);
      if (task) {
        task.completed = true;
        console.log(`Tarea completada: "${task.name}"`);
      } else {
        console.log("Tarea no encontrada");
      }
    },

    // Listamos todas las tareas
    listTasks: function() {
      console.log(" Lista de tareas:");
      if (tasks.length === 0) {
        console.log("No hay tareas registradas");
      } else {
        tasks.forEach(t => {
          console.log(`ID: ${t.id} | ${t.name} | Estado: ${t.completed ? "Completada" : "Pendiente"}`);
        });
      }
    }

  };
}


const myTasks = createTaskManager();

myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");

myTasks.listTasks();       // se muestran las dos tareas pendientes
myTasks.completeTask(1);   // marca la primera como completada
myTasks.listTasks();       // muestra el cambio
