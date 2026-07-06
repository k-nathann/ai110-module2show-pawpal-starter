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
        pass

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        pass

    def is_recurring(self) -> bool:
        """Return whether this task repeats."""
        pass


@dataclass
class Pet:
    """Stores one pet and its tasks."""

    name: str
    species: str
    age: int = 0
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        pass

    def remove_task(self, task_description: str) -> None:
        """Remove a task by description."""
        pass

    def get_tasks(self) -> list[Task]:
        """Return this pet's tasks."""
        pass


@dataclass
class Owner:
    """Stores the owner and their pets."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        pass

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name."""
        pass

    def get_all_tasks(self) -> list[Task]:
        """Return tasks for all pets."""
        pass


class Scheduler:
    """Organizes tasks for an owner."""

    def __init__(self, owner: Owner):
        """Create a scheduler for one owner."""
        self.owner = owner

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by scheduled time."""
        pass

    def filter_tasks(
        self,
        tasks: list[Task],
        pet_name: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> list[Task]:
        """Filter tasks by pet name or completion status."""
        pass

    def detect_conflicts(self, tasks: list[Task]) -> list[str]:
        """Find possible schedule conflicts."""
        pass

    def get_today_schedule(self) -> list[Task]:
        """Return today's organized schedule."""
        pass
