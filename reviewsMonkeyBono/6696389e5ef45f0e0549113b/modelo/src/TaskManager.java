import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TaskManager {

    private static final String TASK_FILE = "tasks.dat";
    private static final Logger LOGGER = Logger.getLogger(TaskManager.class.getName());
    private final List<Task> tasks;
    private final ExecutorService executor;

    public TaskManager() {
        this.tasks = loadTasks();
        this.executor = Executors.newSingleThreadExecutor(); // Use a single thread for file operations
    }

    public synchronized void addTask(Task task) {
        validateTask(task);
        executor.execute(() -> {
            tasks.add(task);
            saveTasks();
            LOGGER.info("Task added: " + task);
        });
    }

    public synchronized List<Task> getAllTasks() {
        // Create a new list to avoid concurrent modification
        List<Task> taskCopy = new ArrayList<>(tasks);
        return taskCopy;
    }

    public synchronized void deleteTask(String title) {
        executor.execute(() -> {
            boolean removed = tasks.removeIf(task -> task.getTitle().equals(title));
            if (removed) {
                saveTasks();
                LOGGER.info("Task deleted: " + title);
            } else {
                LOGGER.warning("Task not found: " + title);
            }
        });
    }

    private void validateTask(Task task) {
        if (task.getTitle() == null || task.getTitle().isEmpty()) {
            throw new IllegalArgumentException("Task title cannot be empty.");
        }
        if (task.getPriority() < 1 || task.getPriority() > 5) {
            throw new IllegalArgumentException("Task priority must be between 1 and 5.");
        }
        if (task.getDueDate().isBefore(LocalDate.now())) {
            throw new IllegalArgumentException("Due date cannot be in the past.");
        }
    }

    private synchronized void saveTasks() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(TASK_FILE))) {
            oos.writeObject(tasks);
            LOGGER.info("Tasks saved to file.");
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error saving tasks to file.", e);
        }
    }

    @SuppressWarnings("unchecked")
    private synchronized List<Task> loadTasks() {
        List<Task> loadedTasks = new ArrayList<>();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(TASK_FILE))) {
            loadedTasks = (List<Task>) ois.readObject();
            LOGGER.info("Tasks loaded from file.");
        } catch (IOException | ClassNotFoundException e) {
            LOGGER.log(Level.WARNING, "Error loading tasks from file. Starting with an empty list.", e);
        }
        return loadedTasks;
    }
}