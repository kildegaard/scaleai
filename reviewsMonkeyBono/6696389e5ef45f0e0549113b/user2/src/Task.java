import java.io.Serializable;
import java.time.LocalDate;

public class Task implements Serializable {
    private static final long serialVersionUID = 1L;

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

    public void setTitle(String title) {
        this.title = title;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public void setDueDate(LocalDate dueDate) {
        this.dueDate = dueDate;
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