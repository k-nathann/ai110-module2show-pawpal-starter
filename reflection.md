# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

For the first version of PawPal+, I identified three core actions a user should be able to perform:

1. Add a pet to the owner profile with basic details like name and species.
2. Schedule a care task for a pet, such as feeding, walking, medication, grooming, or an appointment.
3. View today's tasks in an organized schedule so the owner knows what needs to happen next.

My initial UML design will use four main classes. `Owner` will manage the pet owner's name and list of pets. `Pet` will store each pet's details and care tasks. `Task` will represent one scheduled activity with details like description, time, frequency, and completion status. `Scheduler` will organize tasks across pets so the app can sort them, filter them, and detect possible schedule issues.

Building block brainstorm:

- `Owner`
  - Attributes: `name`, `pets`
  - Methods: `add_pet()`, `remove_pet()`, `get_all_tasks()`
- `Pet`
  - Attributes: `name`, `species`, `age`, `tasks`
  - Methods: `add_task()`, `remove_task()`, `get_tasks()`
- `Task`
  - Attributes: `description`, `scheduled_time`, `frequency`, `completed`
  - Methods: `mark_complete()`, `mark_incomplete()`, `is_recurring()`
- `Scheduler`
  - Attributes: `owner`
  - Methods: `sort_by_time()`, `filter_tasks()`, `detect_conflicts()`, `get_today_schedule()`

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
