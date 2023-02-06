async function getTasks(path) {
  const response = await fetch(path);
  if (response.status !== 200) {
    throw new Error(response.statusText);
  }
  const tasks = await response.json();
  return tasks;
}

function renderTask(tasksElem, task) {
  const taskElem = document.createElement("div");
  const taskText = document.createElement("span");
  taskElem.className = "task-item";
  taskText.textContent = task;
  taskElem.appendChild(taskText);
  tasksElem.appendChild(taskElem);
}

function renderTasks(id, api_path) {
  const tasksElem = document.getElementById(id);
  tasksElem.innerHTML = "";
  return getTasks(api_path)
    .then((tasks) => {
      tasks.forEach((task) => {
        renderTask(tasksElem, task);
      });
    })
    .catch((error) => {
      tasksElem.innerText = error.message;
      console.log("Error", error);
    });
}

renderTasks("task-list", "/api/tasks");
renderTasks("daily-list", "/api/daily").then(() => {
  const wheelElem = document.getElementById("wheel");
  Array.from(document.getElementById("daily-list").children).forEach(
    (child) => {
      wheelElem.appendChild(child.cloneNode(true));
    }
  );
});
