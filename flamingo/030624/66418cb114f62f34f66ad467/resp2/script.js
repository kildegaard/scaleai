// Task list array
let tasks = [];

// Function to add task to list
const addTask = (taskName, dueDate) => {
    const task = {
        name: taskName,
        dueDate: dueDate,
        done: false,
    };
    tasks.push(task);
    renderTaskList();
};

// Function to remove task from list
const removeTask = (index) => {
    tasks.splice(index, 1);
    renderTaskList();
};

// Function to render task list
const renderTaskList = () => {
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";
    tasks.forEach((task, index) => {
        const taskListItem = document.createElement("li");
        const checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        checkBox.checked = task.done;
        checkBox.addEventListener("click", () => {
            task.done = !task.done;
            renderTaskList();
        });
        const taskNameSpan = document.createElement("span");
        taskNameSpan.textContent = task.name;
        if (task.done) {
            taskNameSpan.classList.add("crossed-out");
        }
        const dueDateSpan = document.createElement("span");
        dueDateSpan.textContent = `Due: ${task.dueDate}`;
        const removeBtn = document.createElement("button");
        removeBtn.textContent = "Remove";
        removeBtn.addEventListener("click", () => {
            removeTask(index);
        });
        taskListItem.appendChild(checkBox);
        taskListItem.appendChild(taskNameSpan);
        taskListItem.appendChild(dueDateSpan);
        taskListItem.appendChild(removeBtn);
        taskList.appendChild(taskListItem);
    });
};

// Function to filter tasks by due date
const filterTasksByDueDate = () => {
    tasks.sort((a, b) => {
        const dateA = new Date(a.dueDate);
        const dateB = new Date(b.dueDate);
        return dateA - dateB;
    });
    renderTaskList();
};

// Function to search tasks
const searchTasks = (searchTerm) => {
    const searchedTasks = tasks.filter((task) => {
        return task.name.toLowerCase().includes(searchTerm.toLowerCase());
    });
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";
    searchedTasks.forEach((task, index) => {
        const taskListItem = document.createElement("li");
        const checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        checkBox.checked = task.done;
        checkBox.addEventListener("click", () => {
            task.done = !task.done;
            renderTaskList();
        });
        const taskNameSpan = document.createElement("span");
        taskNameSpan.textContent = task.name;
        if (task.done) {
            taskNameSpan.classList.add("crossed-out");
        }
        const dueDateSpan = document.createElement("span");
        dueDateSpan.textContent = `Due: ${task.dueDate}`;
        const removeBtn = document.createElement("button");
        removeBtn.textContent = "Remove";
        removeBtn.addEventListener("click", () => {
            removeTask(index);
        });
        taskListItem.appendChild(checkBox);
        taskListItem.appendChild(taskNameSpan);
        taskListItem.appendChild(dueDateSpan);
        taskListItem.appendChild(removeBtn);
        taskList.appendChild(taskListItem);
    });
};

// Add event listeners
document.getElementById("add-task-btn").addEventListener("click", (e) => {
    e.preventDefault();
    const taskInput = document.getElementById("task-input");
    const dueDateInput = document.getElementById("due-date-input");
    addTask(taskInput.value, dueDateInput.value);
    taskInput.value = "";
    dueDateInput.value = "";
});

document.getElementById("filter-btn").addEventListener("click", () => {
    filterTasksByDueDate();
});

document.getElementById("search-input").addEventListener("input", (e) => {
    searchTasks(e.target.value);
});

// Initialize app
renderTaskList();