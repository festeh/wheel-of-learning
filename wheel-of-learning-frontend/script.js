import palette from "./palette";
import Winwheel from "./Winwheel";

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
  let taskItems = Array.from(document.getElementById("daily-list").children);
  let myPalette = palette("mpn65", taskItems.length);
  let segments = taskItems.map((item, idx) => {
    return { fillStyle: "#" + myPalette[idx], text: idx.toString() };
  });
  let theWheel = new Winwheel(
    {
      numSegments: taskItems.length,
      textFontSize: 50,
      textAlignment: "outer",
      segments: segments,
      animation: {
        type: "spinToStop",
        duration: 5,
        spins: 8,
      },
    },
    true
  );
});
