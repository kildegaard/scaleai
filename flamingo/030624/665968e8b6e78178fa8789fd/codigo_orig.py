def calculate_max_training_grades(num_test_cases, test_cases):
    results = []
    for case in test_cases:
        (
            num_periods,
            max_trainings_per_period,
            max_trainings_total,
            max_trainings_selected,
            periods,
        ) = case
        dp = [
            [(-float("inf"), []) for _ in range(max_trainings_total + 1)]
            for _ in range(num_periods + 1)
        ]
        dp[0][0] = (0, [])
        for i in range(1, num_periods + 1):
            for j in range(max_trainings_total + 1):
                best_grade = -float("inf")
                best_trainings = []
                for y in range(1, min(max_trainings_selected + 1, j + 1)):
                    prev_grade, prev_trainings = dp[i - 1][j - y]
                    current_trainings = sorted(periods[i - 1], reverse=True)[:y]
                    current_grade = sum(current_trainings)
                    if prev_grade + current_grade > best_grade:
                        best_grade = prev_grade + current_grade
                        best_trainings = prev_trainings + current_trainings
                dp[i][j] = (best_grade, best_trainings)
        max_grade, trainings = max(dp[num_periods], key=lambda x: x[0])
        if max_grade < 0:
            results.append("IMPOSSIBLE")
        else:
            trainings_str = " ".join(map(str, trainings))
            results.append(f"{max_grade} {trainings_str}")
    return results


if __name__ == "__main__":
    num_test_cases = int(input().strip())
    test_cases = []
    for _ in range(num_test_cases):
        (
            num_periods,
            max_trainings_per_period,
            max_trainings_total,
            max_trainings_selected,
        ) = map(int, input().strip().split())
        periods = []
        for _ in range(num_periods):
            period_grades = list(map(int, input().strip().split()))
            periods.append(period_grades)
        test_cases.append(
            (
                num_periods,
                max_trainings_per_period,
                max_trainings_total,
                max_trainings_selected,
                periods,
            )
        )
    results = calculate_max_training_grades(num_test_cases, test_cases)
    for result in results:
        print(result)
