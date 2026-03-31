# Issue Breakdown

This breakdown converts the PRD into thin, end-to-end implementation slices for a small FastAPI task API. Each slice is independently verifiable and small enough for a school assignment workflow.

## Proposed Slices

1. **Title**: Establish task domain structure
   **Type**: AFK
   **Blocked by**: None - can start immediately
   **User stories covered**: 1, 9, 10, 11, 13

   Define the core task model, valid status values, and the basic module boundaries for routes, schemas, service logic, and in-memory storage. This slice should leave the application runnable with the architecture in place, even if feature behavior is still minimal.

2. **Title**: Deliver list and create task flow
   **Type**: AFK
   **Blocked by**: Slice 1
   **User stories covered**: 2, 3, 6, 9, 10, 11, 12

   Implement the end-to-end flow for listing tasks and creating a new task with default `pending` status. This slice should include endpoint behavior, request/response models, service logic, in-memory persistence, and automated tests for successful creation and empty-list behavior.

3. **Title**: Enforce title validation
   **Type**: AFK
   **Blocked by**: Slice 2
   **User stories covered**: 4, 5, 9, 12

   Add validation that rejects missing or blank task titles through the public API. This slice is complete when invalid input is rejected consistently and tests verify the observable API behavior.

4. **Title**: Deliver complete-task flow
   **Type**: AFK
   **Blocked by**: Slice 2
   **User stories covered**: 7, 8, 10, 11, 12

   Implement the end-to-end flow for marking a task as completed with `PATCH /tasks/{id}`. This slice should include the route, service behavior, in-memory update logic, success tests, and `404` handling for unknown task IDs.

5. **Title**: Polish documentation and assignment readiness
   **Type**: AFK
   **Blocked by**: Slice 3, Slice 4
   **User stories covered**: 1, 12, 13

   Finalize lightweight project documentation so the assignment clearly communicates scope, architecture, and test coverage. This slice is complete when the README or equivalent project notes accurately describe the API, intentional in-memory scope, and how to run tests.

## Granularity Notes

- The slices are intentionally vertical rather than layer-based.
- Validation is split from basic create/list behavior so the project shows incremental planning without creating too many tickets.
- Documentation is kept as a final polish step rather than mixed into implementation slices.

## Questions For Review

1. Does this granularity feel right, or does it still feel too coarse for your assignment?
2. Do you want validation as its own slice, or merged into the create/list slice?
3. Do you want documentation as a separate finishing slice, or folded into the final feature slice?
