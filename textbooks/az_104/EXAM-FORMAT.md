# AZ-104 exam format

Retrieved 2026-11-01 from the sources listed at the end. This guide describes delivery, not content; content scope is in `CURRICULUM.md` and the chapters.

## Facts from official pages

| Item | What the sources state |
|---|---|
| Time | The exam page states 100 minutes. Microsoft's duration page lists 100 minutes for associate exams without labs and 120 minutes for associate exams that *may* contain labs. |
| Number of questions | Most Microsoft exams have 40–60 questions, but the number varies and can change. |
| Labs | The exam page says there may be interactive components. Microsoft does not publish which exams have labs because labs can be removed at any time; read the overview pages when you launch the exam. |
| Microsoft Learn | Available during role-based (associate) exams in a split pane. The timer keeps running, no extra time is added, and Q&A, practice assessments, and your profile are blocked. |
| Breaks | Unscheduled breaks are allowed, but the clock keeps running and you cannot return to questions seen before the break. No breaks in the middle of a lab or a problem-solution question set. |
| Retakes | 24 hours after the first failed attempt, then 14 days between later attempts, up to five attempts in 12 months. |
| Practice | The exam page offers an exam sandbox (look and feel of every question type) and a practice assessment. |

> **Verify:** The passing score (commonly 700 on a 1–1000 scale for Microsoft role-based exams) and the exact list of question types were not on the pages retrieved. Confirm both in the exam sandbox and the exam page before you rely on them.

## Question types and how to approach them

Open the official exam sandbox once; it lets you try each interface. The types below are the ones this book's mock exam supports (`mock_exams/az_104/`). Which ones appear in a given sitting varies.

| Type | Mock exam type | Approach |
|---|---|---|
| Single choice / multiple response | `single`, `multiple` | Eliminate options that break a stated requirement. For "choose N", count your selections. |
| Build list / ordering | `ordering` | Write the dependency chain first (for example, a vault must exist before you can protect a VM), then arrange. Each step usually enables the next. |
| Drag-and-drop matching | `matching` | Answers can often be reused. Match the easy pairs first, then use the rest by elimination. |
| Yes/No statement series | `yesno-series` | Judge each statement independently against the scenario; do not assume the answers are balanced. |
| Dropdown / hot area | `hotspot` | Read the whole completed sentence or command with your choice before moving on. |
| Case studies | (scenarios in `single`/`multiple`) | Read the requirements and existing environment first; skim questions, then refer back. Questions in a case study are locked once you leave the section, so answer before moving on. |
| Problem-solution sets | `single` | The same scenario is repeated with different proposed solutions; judge each one on its own and do not carry the earlier answer over. You cannot take a break during a set. |
| Labs / command tasks | `command` | Practice the portal and CLI tasks from [LABS.md](LABS.md). In the mock exam, type the command; accepted variants include short and long flags. |

> **Verify:** Locking behaviour for case studies and whether a given sitting contains labs are controlled by the exam. Read each section's instruction page.

## Preparing for lab-style tasks

Labs and performance tasks are practical: you work in a live portal or CLI. Plan to have done, not just read, the work in the chapters. See [LABS.md](LABS.md) for the official hands-on labs mapped to topics and outcomes.

## Sources

- Exam and certification page: <https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/>
- Exam duration and experience: <https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience>
- Retake policy: <https://learn.microsoft.com/en-us/credentials/support/retake-policy>
- Exam sandbox: <https://go.microsoft.com/fwlink/?linkid=2226877>
- Practice assessment: <https://aka.ms/AZ104-PA>
- Study guide: <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104>
