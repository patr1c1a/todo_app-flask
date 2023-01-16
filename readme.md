# To-do API

(this is a WIP)

## Basic functionality:
* add a task
* delete unwanted task
* mark task as done
* list tasks (all/pending/complete)



## /task endpoint:
### Add task (method: POST):
**Parameters:** task name, task status (pending/complete)

**Returns:** new task id

### Delete task (method: DELETE):
**Parameters:** task id

**Returns:** true/false (was deleted/could not delete)

### Mark task as done (method: PUT):
**Parameters:** task id

**Returns:** true/false (was marked/could not mark)

### List tasks (method: GET):
**Parameters:** status -optional (all tasks, only pending, only complete)

**Returns:** list of tasks



## To-do:

- Add proper http error messages and codes

- Tag fields to return a properly formed response (either use a dict or re-use the Task class)

- db_manager.py: run_query returns 2 values. Should we refactor?

- request body (json)

- implement orm (SQLALchemy)

- serializer (should we use Marshmallow?)

- custom exceptions
