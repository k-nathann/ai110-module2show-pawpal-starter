from pawpal_system import Pet, Task


def test_mark_complete_changes_task_status():
    task = Task("Morning feeding", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "dog")
    task = Task("Evening walk", "18:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
