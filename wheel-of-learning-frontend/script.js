async function getTasks() {
  const response = await fetch(`/api/tasks`);
  if (response.status !== 200) {
    throw new Error(response.statusText);
  }
  const tasks = await response.json();
  return tasks;
}
//
function renderTasks() {
  const tasksElem = document.getElementById("task-list");
  tasksElem.innerHTML = "";
  getTasks()
    .then((tasks) => {
      for (let task of tasks) {
        const taskElem = document.createElement("div");
        const taskText = document.createElement("span")
        taskElem.className = "task-item";
        taskText.textContent = task;
        taskElem.appendChild(taskText);
        tasksElem.appendChild(taskElem);
      }
      //     table.innerHTML = '';
      //     tasks.forEach(task => {
      //         const tr = document.createElement('tr');
      //         const td = document.createElement('td');
      //         td.innerHTML = task.title;
    })
    .catch((error) => {
      tasksElem.innerText = error.message;
      console.log("Error", error);
    });
}

renderTasks();
