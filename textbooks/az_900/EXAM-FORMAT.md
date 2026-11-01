# AZ-900 exam format

Retrieved 2026-11-01 from the sources listed at the end. This guide describes delivery, not content; content scope is in `CURRICULUM.md` and the chapters.

## Facts from official pages

| Item | What the sources state |
|---|---|
| Time | The exam page states 45 minutes. Microsoft's duration page lists 45 minutes of exam time (65 minutes of seat time) for fundamentals exams. |
| Number of questions | Most Microsoft exams have 40–60 questions, but the number varies and can change. |
| Microsoft Learn | Not available during Fundamentals exams. |
| Breaks | Unscheduled breaks are allowed, but the clock keeps running and you cannot return to questions seen before the break. |
| Retakes | 24 hours after the first failed attempt, then 14 days between later attempts, up to five attempts in 12 months. |
| Practice | The exam page offers an exam sandbox (look and feel of every question type) and a practice assessment. |

> **Verify:** The passing score (commonly 700 on a 1–1000 scale for Microsoft exams) and the exact list of question types were not on the pages retrieved. Confirm both in the exam sandbox and the exam page.

## Question types and how to approach them

Open the official exam sandbox once to try each interface. The types below are the ones this book's mock exam supports (`mock_exams/az_900/`). Which ones appear in a sitting varies.

| Type | Mock exam type | Approach |
|---|---|---|
| Single choice / multiple response | `single`, `multiple` | Match the clue words (for example, "guest OS control" or "pay only when it runs") to the service model or service. For "choose N", count your selections. |
| Ordering | `ordering` | Think of the hierarchy or lifecycle first (for example, management group → subscription → resource group → resource), then arrange. |
| Matching | `matching` | Answers can often be reused. Do the certain pairs first and finish by elimination. |
| Yes/No statement series | `yesno-series` | Judge each statement independently; fundamentals statements often turn on one word such as "always" or "only". |
| Dropdown / hotspot | `hotspot` | Read the completed sentence with your choice to check that it is true. |
| Command tasks | `command` | AZ-900 mainly tests that you can identify the tool (portal, CLI, PowerShell, Cloud Shell), not write long commands, but short commands may be asked in the mock exam. |

## Hands-on preparation

Fundamentals questions are conceptual, but doing the exercises makes the vocabulary concrete. See [LABS.md](LABS.md).

## Sources

- Exam and certification page: <https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/>
- Exam duration and experience: <https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience>
- Retake policy: <https://learn.microsoft.com/en-us/credentials/support/retake-policy>
- Exam sandbox: <https://go.microsoft.com/fwlink/?linkid=2226877>
- Practice assessment: <https://aka.ms/AZ900-PA>
- Study guide: <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900>
