# Product Requirements Document

## Problem Statement

For this school assignment, the project needs to demonstrate planning, testing, and basic software architecture without becoming too large or complex. A very small FastAPI project can satisfy the assignment, but only if its scope is intentional and its structure is clear enough to show separation of concerns. The challenge is to keep the implementation simple while still making it look designed rather than unfinished.

## Solution

Build a minimal task management API using FastAPI with in-memory storage. The API will support listing tasks, creating tasks, and marking tasks as completed. Each task has a small lifecycle of `pending` to `completed`. The application will be structured so that HTTP handling, validation, business rules, and storage are separated, even though persistence remains in memory for the assignment.

## User Stories

1. As an instructor, I want to see a small but complete API, so that I can evaluate planning and implementation quality.
2. As an API client, I want to list all tasks, so that I can view the current state of the system.
3. As an API client, I want to create a task with a title, so that I can add new work items.
4. As an API client, I want task creation to reject missing titles, so that invalid data is not accepted.
5. As an API client, I want task creation to reject blank titles, so that task data stays meaningful.
6. As an API client, I want newly created tasks to start in `pending` status, so that task state is predictable.
7. As an API client, I want to mark a task as completed, so that I can update its lifecycle state.
8. As an API client, I want a missing task ID to return `404`, so that API errors are explicit and standard.
9. As a developer, I want request and response validation to be isolated from route logic, so that the code is easier to read and extend.
10. As a developer, I want business rules separated from HTTP endpoints, so that the application demonstrates basic architecture.
11. As a developer, I want storage isolated behind a simple module, so that persistence can be replaced later without rewriting the whole application.
12. As a tester, I want the API behavior covered by automated tests, so that the expected behavior is documented and verifiable.
13. As a student, I want the project to stay small, so that I can complete it confidently within assignment constraints.

## Implementation Decisions

- The system will use in-memory storage by design.
- The API will expose three endpoints only: list tasks, create task, and complete task.
- The task model will contain `id`, `title`, and `status`.
- The only valid task states will be `pending` and `completed`.
- New tasks will always be created in `pending` state.
- Creating a task requires a non-empty title.
- Completing a task requires a valid task identifier.
- Requests for missing task IDs will return `404`.
- The application will be organized into small modules for HTTP routing, data schemas, service logic, and storage.
- Route handlers will stay thin and delegate behavior to service-level logic.
- Storage logic will be simple and local to the project, with no database integration.
- The design should remain easy to explain in an academic setting and appropriate for a proof-of-concept implementation.

## Testing Decisions

- Good tests should verify external behavior through the API surface rather than internal implementation details.
- Tests should focus on observable results such as status codes, response payloads, and state changes.
- The API behavior to be tested includes:
  - listing tasks when no tasks exist
  - creating a task successfully
  - rejecting invalid task titles
  - marking a task as completed
  - returning `404` when completing a non-existent task
- Tests will primarily exercise the API endpoints and may also cover isolated service behavior if the architecture is split into modules.
- Existing tests in the codebase already establish endpoint-level testing with FastAPI's test client, so the project can extend that pattern consistently.

## Out of Scope

- Database or persistent storage
- Authentication or authorization
- Delete endpoint
- Full CRUD beyond the three core endpoints
- Pagination, filtering, or sorting
- Extra task fields such as due date, priority, description, or tags
- Multi-user behavior
- Deployment or production hardening

## Further Notes

This project should be presented as intentionally minimal, not incomplete. Its strength comes from clear scope control, readable module boundaries, and focused automated tests. The goal is not to build a production task manager, but to show that even a small API can reflect thoughtful planning and structure.
