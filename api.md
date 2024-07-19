# Tasks

Types:

```python
from paymanai.types import TaskCreateTaskResponse, TaskGetTaskResponse, TaskListTasksResponse, TaskUpdateTaskResponse
```

Methods:

- <code title="post /tasks">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">create_task</a>(\*\*<a href="src/paymanai/types/task_create_task_params.py">params</a>) -> <a href="./src/paymanai/types/task_create_task_response.py">TaskCreateTaskResponse</a></code>
- <code title="get /tasks/{id}">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">get_task</a>(id) -> <a href="./src/paymanai/types/task_get_task_response.py">TaskGetTaskResponse</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">list_tasks</a>(\*\*<a href="src/paymanai/types/task_list_tasks_params.py">params</a>) -> <a href="./src/paymanai/types/task_list_tasks_response.py">TaskListTasksResponse</a></code>
- <code title="put /tasks/{id}">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">update_task</a>(id, \*\*<a href="src/paymanai/types/task_update_task_params.py">params</a>) -> <a href="./src/paymanai/types/task_update_task_response.py">TaskUpdateTaskResponse</a></code>

## Assignments

Types:

```python
from paymanai.types.tasks import AssignmentCreateTaskAssignmentResponse, AssignmentListTaskAssignmentsResponse
```

Methods:

- <code title="post /tasks/{id}/assignments">client.tasks.assignments.<a href="./src/paymanai/resources/tasks/assignments.py">create_task_assignment</a>(id, \*\*<a href="src/paymanai/types/tasks/assignment_create_task_assignment_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/assignment_create_task_assignment_response.py">AssignmentCreateTaskAssignmentResponse</a></code>
- <code title="get /tasks/{id}/assignments">client.tasks.assignments.<a href="./src/paymanai/resources/tasks/assignments.py">list_task_assignments</a>(id, \*\*<a href="src/paymanai/types/tasks/assignment_list_task_assignments_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/assignment_list_task_assignments_response.py">AssignmentListTaskAssignmentsResponse</a></code>

## Submissions

Types:

```python
from paymanai.types.tasks import SubmissionListTaskSubmissionsResponse
```

Methods:

- <code title="get /tasks/{id}/submissions">client.tasks.submissions.<a href="./src/paymanai/resources/tasks/submissions.py">list_task_submissions</a>(id, \*\*<a href="src/paymanai/types/tasks/submission_list_task_submissions_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/submission_list_task_submissions_response.py">SubmissionListTaskSubmissionsResponse</a></code>

## Categories

Types:

```python
from paymanai.types.tasks import CategoryListTaskCategoriesResponse
```

Methods:

- <code title="get /tasks/categories">client.tasks.categories.<a href="./src/paymanai/resources/tasks/categories.py">list_task_categories</a>() -> <a href="./src/paymanai/types/tasks/category_list_task_categories_response.py">CategoryListTaskCategoriesResponse</a></code>

# Wallets

Types:

```python
from paymanai.types import WalletGetWalletResponse
```

Methods:

- <code title="get /wallets/{id}">client.wallets.<a href="./src/paymanai/resources/wallets.py">get_wallet</a>(id) -> <a href="./src/paymanai/types/wallet_get_wallet_response.py">WalletGetWalletResponse</a></code>

# Version

Methods:

- <code title="get /version">client.version.<a href="./src/paymanai/resources/version.py">get_server_version</a>() -> BinaryAPIResponse</code>
