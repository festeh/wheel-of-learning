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
  taskText.innerText = task;
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

function randInt(low, high) {
  return (
    Math.floor(Math.random() * (high - low + 1)) + low + Math.random() * 0.1
  );
}

renderTasks("task-list", "/api/tasks");
renderTasks("daily-list", "/api/daily").then(() => {
  let taskItems = Array.from(document.getElementById("daily-list").children);
  let myPalette = palette("mpn65", taskItems.length);
  taskItems.forEach((taskItem, idx) => {
    let box = document.createElement("div");
    box.style.backgroundColor = "#" + myPalette[idx];
    box.style.display = "inline-block";
    box.style.width = "40px";
    box.style.height = "40px";
    box.style.justifyContent = "center";
    box.style.textAlign = "center";
    box.style.fontSize = "25px";
    box.style.fontWeight = "bold";
    box.style.verticalAlign = "middle";
    box.innerText = idx.toString();
    taskItem.appendChild(box);
  });
  let segments = taskItems.map((item, idx) => {
    return {
      fillStyle: "#" + myPalette[idx],
      text: idx.toString(),
      textFillStyle: "white",
    };
  });
  let theWheel = new Winwheel(
    {
      numSegments: taskItems.length,
      textFontSize: Math.max(10, 120 - 14 * taskItems.length),
      textAlignment: "outer",
      segments: segments,
      animation: {
        type: "spinToStop",
        duration: randInt(4, 7),
        spins: randInt(5, 12),
        callbackFinished: (segment) => {
          const idx = parseInt(segment.text);
          let name = taskItems[idx].innerText;
          fetch("api/focus", {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ name: name }),
          }).then((response) => {
            renderFocus();
          });
        },
      },
    },
    true
  );

  let spinButton = document.getElementById("spin");
  spinButton.addEventListener("click", () => {
    theWheel.stopAnimation(false);
    theWheel.rotationAngle = 0;
    theWheel.draw();
    theWheel.startAnimation();
  });
});

async function renderFocus() {
  const focusElem = document.getElementById("focus");
  focusElem.innerHTML = "";
  try {
    const tasks = await getTasks("/api/focus");
    if (tasks.length === 0) {
      focusElem.innerText = "Choose your focus";
    } else {
      focusElem.innerText = tasks[0];
    }
  } catch (error) {
    focusElem.innerText = error.message;
    console.log("Error", error);
  }
}

renderFocus();
