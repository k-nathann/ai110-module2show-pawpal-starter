from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    """Represents one pet care activity."""

    description: str
    scheduled_time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def is_recurring(self) -> bool:
        """Return whether this task repeats."""
        return self.frequency.lower() in ["daily", "weekly"]


@dataclass
class Pet:
    """Stores one pet and its tasks."""

    name: str
    species: str
    age: int = 0
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_description: str) -> None:
        """Remove a task by description."""
        self.tasks = [
            task
            for task in self.tasks
            if task.description.lower() != task_description.lower()
        ]

    def get_tasks(self) -> list[Task]:
        """Return this pet's tasks."""
        return self.tasks


@dataclass
class Owner:
    """Stores the owner and their pets."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name."""
        self.pets = [pet for pet in self.pets if pet.name.lower() != pet_name.lower()]

    def get_all_tasks(self) -> list[Task]:
        """Return tasks for all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Organizes tasks for an owner."""

    def __init__(self, owner: Owner):
        """Create a scheduler for one owner."""
        self.owner = owner

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by scheduled time."""
        return sorted(tasks, key=lambda task: task.scheduled_time)

    def filter_tasks(
        self,
        tasks: list[Task],
        pet_name: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> list[Task]:
        """Filter tasks by pet name or completion status."""
        filtered_tasks = tasks

        if pet_name is not None:
            matching_pet = None
            for pet in self.owner.pets:
                if pet.name.lower() == pet_name.lower():
                    matching_pet = pet
                    break

            if matching_pet is None:
                return []

            filtered_tasks = [
                task for task in filtered_tasks if task in matching_pet.get_tasks()
            ]

        if completed is not None:
            filtered_tasks = [
                task for task in filtered_tasks if task.completed == completed
            ]

        return filtered_tasks

    def detect_conflicts(self, tasks: list[Task]) -> list[str]:
        """Find possible schedule conflicts."""
        conflicts = []
        seen_times = {}

        for task in tasks:
            if task.scheduled_time in seen_times:
                conflicts.append(
                    f"Conflict at {task.scheduled_time}: "
                    f"{seen_times[task.scheduled_time]} and {task.description}"
                )
            else:
                seen_times[task.scheduled_time] = task.description

        return conflicts

    def get_today_schedule(self) -> list[Task]:
        """Return today's organized schedule."""
        return self.sort_by_time(self.owner.get_all_tasks())
