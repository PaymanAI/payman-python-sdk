# Tasks

Types:

```python
from paymanai.types import (
    TaskCreateResponse,
    TaskRetrieveResponse,
    TaskUpdateResponse,
    TaskListResponse,
)
```

Methods:

- <code title="post /tasks">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">create</a>(\*\*<a href="src/paymanai/types/task_create_params.py">params</a>) -> <a href="./src/paymanai/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /tasks/{id}">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">retrieve</a>(id) -> <a href="./src/paymanai/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="put /tasks/{id}">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">update</a>(id, \*\*<a href="src/paymanai/types/task_update_params.py">params</a>) -> <a href="./src/paymanai/types/task_update_response.py">TaskUpdateResponse</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/paymanai/resources/tasks/tasks.py">list</a>(\*\*<a href="src/paymanai/types/task_list_params.py">params</a>) -> <a href="./src/paymanai/types/task_list_response.py">TaskListResponse</a></code>

## Assignments

Types:

```python
from paymanai.types.tasks import AssignmentCreateResponse, AssignmentListResponse
```

Methods:

- <code title="post /tasks/{id}/assignments">client.tasks.assignments.<a href="./src/paymanai/resources/tasks/assignments.py">create</a>(id, \*\*<a href="src/paymanai/types/tasks/assignment_create_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/assignment_create_response.py">AssignmentCreateResponse</a></code>
- <code title="get /tasks/{id}/assignments">client.tasks.assignments.<a href="./src/paymanai/resources/tasks/assignments.py">list</a>(id, \*\*<a href="src/paymanai/types/tasks/assignment_list_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/assignment_list_response.py">AssignmentListResponse</a></code>

## Submissions

Types:

```python
from paymanai.types.tasks import SubmissionListResponse
```

Methods:

- <code title="get /tasks/{id}/submissions">client.tasks.submissions.<a href="./src/paymanai/resources/tasks/submissions.py">list</a>(id, \*\*<a href="src/paymanai/types/tasks/submission_list_params.py">params</a>) -> <a href="./src/paymanai/types/tasks/submission_list_response.py">SubmissionListResponse</a></code>

## Categories

Types:

```python
from paymanai.types.tasks import CategoryListResponse
```

Methods:

- <code title="get /tasks/categories">client.tasks.categories.<a href="./src/paymanai/resources/tasks/categories.py">list</a>() -> <a href="./src/paymanai/types/tasks/category_list_response.py">CategoryListResponse</a></code>

# Wallets

Types:

```python
from paymanai.types import WalletRetrieveResponse
```

Methods:

- <code title="get /wallets/{id}">client.wallets.<a href="./src/paymanai/resources/wallets.py">retrieve</a>(id) -> <a href="./src/paymanai/types/wallet_retrieve_response.py">WalletRetrieveResponse</a></code>

# Version

Methods:

- <code title="get /version">client.version.<a href="./src/paymanai/resources/version.py">retrieve</a>() -> BinaryAPIResponse</code>

# Files

## Private

Methods:

- <code title="get /files/private/download">client.files.private.<a href="./src/paymanai/resources/files/private.py">download</a>(\*\*<a href="src/paymanai/types/files/private_download_params.py">params</a>) -> BinaryAPIResponse</code>
