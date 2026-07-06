from datetime import time
from typing import Optional

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


def get_owner() -> Owner:
    """Get the owner from Streamlit session state."""
    if "owner" not in st.session_state:
        st.session_state.owner = Owner("Jordan")
    return st.session_state.owner


def find_pet(owner: Owner, pet_name: str) -> Optional[Pet]:
    """Find a pet by name."""
    for pet in owner.pets:
        if pet.name == pet_name:
            return pet
    return None


def build_task_rows(owner: Owner, tasks: list[Task]) -> list[dict[str, str]]:
    """Convert tasks into dictionaries for a Streamlit table."""
    rows = []
    for pet in owner.pets:
        for task in pet.get_tasks():
            if task in tasks:
                rows.append(
                    {
                        "Pet": pet.name,
                        "Task": task.description,
                        "Time": task.scheduled_time,
                        "Frequency": task.frequency,
                        "Status": "done" if task.completed else "open",
                    }
                )
    return rows


owner = get_owner()
scheduler = Scheduler(owner)

st.title("🐾 PawPal+")
st.caption("Track pets, schedule care tasks, and view an organized daily plan.")

owner.name = st.text_input("Owner name", value=owner.name)

st.divider()

st.subheader("Add a Pet")
with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=40, value=1)
    add_pet_button = st.form_submit_button("Add pet")

if add_pet_button:
    if pet_name.strip():
        owner.add_pet(Pet(pet_name.strip(), species, int(age)))
        st.success(f"Added {pet_name.strip()} to {owner.name}'s pets.")
    else:
        st.warning("Enter a pet name before adding a pet.")

if owner.pets:
    st.write("Current pets:")
    st.table(
        [
            {"Name": pet.name, "Species": pet.species, "Age": pet.age}
            for pet in owner.pets
        ]
    )
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Schedule a Task")
if not owner.pets:
    st.info("Add a pet before scheduling a task.")
else:
    with st.form("add_task_form", clear_on_submit=True):
        selected_pet_name = st.selectbox("Pet", [pet.name for pet in owner.pets])
        task_description = st.text_input("Task description", value="Morning feeding")
        scheduled_time = st.time_input("Time", value=time(8, 0))
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
        add_task_button = st.form_submit_button("Add task")

    if add_task_button:
        selected_pet = find_pet(owner, selected_pet_name)
        if selected_pet and task_description.strip():
            selected_pet.add_task(
                Task(
                    task_description.strip(),
                    scheduled_time.strftime("%H:%M"),
                    frequency,
                )
            )
            st.success(f"Scheduled {task_description.strip()} for {selected_pet.name}.")
        else:
            st.warning("Choose a pet and enter a task description.")

st.divider()

st.subheader("Today's Schedule")
today_schedule = scheduler.get_today_schedule()

if today_schedule:
    st.table(build_task_rows(owner, today_schedule))
else:
    st.info("No tasks scheduled yet.")

conflicts = scheduler.detect_conflicts(today_schedule)
for conflict in conflicts:
    st.warning(conflict)
