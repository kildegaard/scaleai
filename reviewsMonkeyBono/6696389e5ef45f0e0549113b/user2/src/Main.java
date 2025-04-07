import java.time.LocalDate;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager();

        // Add a new task
        Future<?> addTaskFuture = taskManager.addTask(new Task("Finish project", 2, LocalDate.now().plusDays(5)));
        waitForFuture(addTaskFuture);

        // Get all tasks
        Future<List<Task>> getAllTasksFuture = taskManager.getAllTasks();
        List<Task> tasks = waitForFuture(getAllTasksFuture);
        if (tasks != null) {
            tasks.forEach(task -> LOGGER.info("Retrieved task: " + task));
        }

        // Delete a task
        Future<?> deleteTaskFuture = taskManager.deleteTask("Finish project");
        waitForFuture(deleteTaskFuture);

        // Get all tasks after deletion
        getAllTasksFuture = taskManager.getAllTasks();
        tasks = waitForFuture(getAllTasksFuture);
        if (tasks != null) {
            tasks.forEach(task -> LOGGER.info("Retrieved task: " + task));
        }
    }

    private static <T> T waitForFuture(Future<T> future) {
        try {
            return future.get();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            LOGGER.log(Level.SEVERE, "Thread interrupted while waiting for task completion", e);
        } catch (ExecutionException e) {
            LOGGER.log(Level.SEVERE, "Error executing task", e);
        }
        return null;
    }

    private static void waitForFuture(Future<?> future) {
        try {
            future.get();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            LOGGER.log(Level.SEVERE, "Thread interrupted while waiting for task completion", e);
        } catch (ExecutionException e) {
            LOGGER.log(Level.SEVERE, "Error executing task", e);
        }
    }
}