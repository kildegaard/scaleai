import java.io.Serializable;
import java.time.LocalDate;

public class Task implements Serializable {
    private String title;
    private int priority;
    private LocalDate dueDate;

    public Task(String title, int priority, LocalDate dueDate) {
        this.title = title;
        this.priority = priority;
        this.dueDate = dueDate;
    }

    public String getTitle() {
        return title;
    }

    public int getPriority() {
        return priority;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    @Override
    public String toString() {
        return "Task{" +
                "title='" + title + '\'' +
                ", priority=" + priority +
                ", dueDate=" + dueDate +
                '}';
    }
}
