class TodoList {
    constructor() {
        this.tasks = [];
    }

    addTask(task) {
        if (task && typeof task === 'string') {
            this.tasks.push({ task, completed: false });
            return true;
        }
        return false;
    }

    removeTask(task) {
        const index = this.tasks.findIndex(t => t.task === task);
        if (index !== -1) {
            this.tasks.splice(index, 1);
            return true;
        }
        return false;
    }

    listTasks() {
        return this.tasks;
    }

    markCompleted(task) {
        const foundTask = this.tasks.find(t => t.task === task);
        if (foundTask) {
            foundTask.completed = true;
            return true;
        }
        return false;
    }
}

todoList = new TodoList();
todoList.addTask('Buy milk');
todoList.addTask('Buy eggs');
todoList.addTask('Buy bread');
todoList.addTask('Buy butter');
todoList.markCompleted('Buy milk');
todoList.removeTask('Buy bread');
console.log(todoList.listTasks());
