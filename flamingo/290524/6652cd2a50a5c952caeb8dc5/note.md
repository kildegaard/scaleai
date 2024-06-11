Tasker: qa_coder_mena_2009@remotasks.com+outlier

# Prompts

add docstring to this function
```py
def simulated_annealing(points, initial_control_points, max_iterations=1000, initial_temp=100.0, cooling_rate=0.99):
    def objective(control_points):
        bezier_points = bezier_curve(control_points)
        return sum(np.linalg.norm(np.array(p.toTuple()) - np.array(b.toTuple())) for p, b in zip(points, bezier_points))

    def neighbor(control_points):
        idx = random.randint(0, len(control_points) - 1)
        new_control_points = control_points[:]
        new_control_points[idx] = QPointF(control_points[idx].x() + random.uniform(-10, 10),
                                         control_points[idx].y() + random.uniform(-10, 10))
        return new_control_points

    current_control_points = initial_control_points
    current_cost = objective(current_control_points)
    best_control_points = current_control_points
    best_cost = current_cost
    temp = initial_temp

    for i in range(max_iterations):
        new_control_points = neighbor(current_control_points)
        new_cost = objective(new_control_points)
        if new_cost < current_cost or random.uniform(0, 1) < np.exp((current_cost - new_cost) / temp):
            current_control_points = new_control_points
            current_cost = new_cost
            if new_cost < best_cost:
                best_control_points = new_control_points
                best_cost = new_cost
        temp *= cooling_rate

    return best_control_points

```

Y otros re chotos. No tienen contenido casi por fuera del código.


# Feedback

Although the subject of this assignment is documentation, the prompt needs to be interesting and semi-complex and give some context for what is to be analyzed. The general idea is that the prompt should be solvable by “a recent college grad that is starting their first job as a junior programmer”.
In your case, there is almost no prompt at all, just the code. The code is somewhat interesting but lacks lots of complexity, it's a function with no more context. The code to be explained and documented should have more content and uniqueness.
Additionally, the justifications are vague and imply that the docstrings and inline comments generated were not thoroughly examined.
Please, consider all these suggestions when redoing the task, and provide a more content-rich prompt with a code to document.
