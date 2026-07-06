from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    """Run a quick CLI demo of the PawPal+ logic layer."""
    owner = Owner("Jordan")

    dog = Pet("Mochi", "dog", age=3)
    cat = Pet("Luna", "cat", age=5)

    dog.add_task(Task("Evening walk", "18:00", "daily"))
    dog.add_task(Task("Morning feeding", "08:00", "daily"))
    cat.add_task(Task("Medication", "09:00", "daily"))
    cat.add_task(Task("Grooming appointment", "15:30", "weekly"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    today_schedule = scheduler.get_today_schedule()

    print(f"Today's Schedule for {owner.name}")
    print("-" * 32)
    for task in today_schedule:
        status = "done" if task.completed else "open"
        print(
            f"{task.scheduled_time} | {task.description} "
            f"({task.frequency}, {status})"
        )


if __name__ == "__main__":
    main()
