import java.time.LocalDate;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager();

        // Add a new task
        taskManager.addTask(new Task("Finish project", 2, LocalDate.now().plusDays(5)));

        // Get all tasks
        List<Task> tasks = taskManager.getAllTasks();
        tasks.forEach(System.out::println);

        // Delete a task
        taskManager.deleteTask("Finish project");
    }
}
