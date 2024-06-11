// Initialize the todo list array
let todoList = [];

// Function to add a new task to the list
function addTask() {
    let taskInput = document.getElementById('task-input');
    let dueDateInput = document.getElementById('due-date-input');
    let task = {
        text: taskInput.value,
        dueDate: dueDateInput.value,
        completed: false
    };
    todoList.push(task);
    taskInput.value = '';
    dueDateInput.value = '';
    renderList();
}

// Function to remove a task from the list
function removeTask(index) {
    todoList.splice(index, 1);
    renderList();
}

// Function to toggle the completed status of a task
function toggleCompleted(index) {
    todoList[index].completed = !todoList[index].completed;
    renderList();
}

// Function to render the todo list
function renderList() {
    let todoListElement = document.getElementById('todo-list');
    todoListElement.innerHTML = '';
    for (let i = 0; i < todoList.length; i++) {
        let task = todoList[i];
        let taskElement = document.createElement('li');
        let checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('click', () => toggleCompleted(i));
        taskElement.appendChild(checkbox);
        let text = document.createTextNode(task.text);
        taskElement.appendChild(text);
        if (task.completed) {
            taskElement.classList.add('completed');
        }
        let dueDate = document.createElement('span');
        dueDate.textContent = `Due: ${task.dueDate}`;
        taskElement.appendChild(dueDate);
        let removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', () => removeTask(i));
        taskElement.appendChild(removeButton);
        todoListElement.appendChild(taskElement);
    }
}

// Function to filter the todo list by due date
function filterByDueDate() {
    todoList.sort((a, b) => {
        let dateA = new Date(a.dueDate);
        let dateB = new Date(b.dueDate);
        return dateA - dateB;
    });
    renderList();
}

// Function to search for tasks
function searchTasks() {
    let searchInput = document.getElementById('search-input');
    let searchText = searchInput.value.toLowerCase();
    let todoListElement = document.getElementById('todo-list');
    todoListElement.innerHTML = '';
    for (let i = 0; i < todoList.length; i++) {
        let task = todoList[i];
        if (task.text.toLowerCase().includes(searchText)) {
            let taskElement = document.createElement('li');
            let checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.checked = task.completed;
            checkbox.addEventListener('click', () => toggleCompleted(i));
            taskElement.appendChild(checkbox);
            let text = document.createTextNode(task.text);
            taskElement.appendChild(text);
            if (task.completed) {
                taskElement.classList.add('completed');
            }
            let dueDate = document.createElement('span');
            dueDate.textContent = `Due: ${task.dueDate}`;
            taskElement.appendChild(dueDate);
            let removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.addEventListener('click', () => removeTask(i));
            taskElement.appendChild(removeButton);
            todoListElement.appendChild(taskElement);
        }
    }
}

// Initialize the application
function init() {
    let addTaskButton = document.getElementById('add-task-button');
    addTaskButton.addEventListener('click', addTask);
    let filterButton = document.getElementById('filter-button');
    filterButton.addEventListener('click', filterByDueDate);
    let searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', searchTasks);
    renderList();
}

// Call the init function when the page loads
window.addEventListener('load', init);