# app/services/scheduler_service.py

from datetime import datetime, timedelta

# 🔹 Map user priority → numeric weight
PRIORITY_MAP = {
    "low": 1,
    "medium": 2,
    "high": 3
}

# Default duration if not provided (minutes)
DEFAULT_DURATION = 30


def calculate_priority_score(task) -> int:
    score = 0

    # 🔹 1. User-defined priority
    score += PRIORITY_MAP.get(task.priority, 2) * 10

    # 🔹 2. Deadline urgency
    if task.due_date:
        hours_left = (task.due_date - datetime.utcnow()).total_seconds() / 3600

        if hours_left <= 0:
            score += 100  # overdue = very urgent
        else:
            score += max(0, 50 - hours_left)

    # 🔹 3. Short task bonus
    if task.estimated_time:
        score += max(0, 30 - task.estimated_time)

    return int(score)


def prioritize_tasks(tasks):
    for task in tasks:
        task.priority_score = calculate_priority_score(task)

    return sorted(tasks, key=lambda t: t.priority_score, reverse=True)


def schedule_tasks(tasks, start_time=None):
    if not start_time:
        start_time = datetime.utcnow()

    current_time = start_time

    for task in tasks:
        # Skip completed tasks
        if task.status == "completed" or task.completed:
            continue

        duration = task.estimated_time or DEFAULT_DURATION

        task.scheduled_at = current_time

        current_time += timedelta(minutes=duration)

    return tasks


def generate_schedule(tasks):
    # 🔹 1. Filter active tasks
    active_tasks = [
        t for t in tasks
        if t.status != "completed" and not t.completed
    ]

    # 🔹 2. Prioritize
    prioritized = prioritize_tasks(active_tasks)

    # 🔹 3. Schedule
    scheduled = schedule_tasks(prioritized)

    return scheduled