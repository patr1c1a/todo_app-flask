# To-do API

## Basic functionality:
* add a task
* delete unwanted task
* mark task as done
* list tasks (all/pending/complete)



## Endpoints:
### Add task:
**Parameters:** name, status (pending/complete)

**Returns:** task id

### Delete task:
**Parameters:** task id

**Returns:** true/false (was deleted/could not delete)

### Mark task as done:
**Parameters:** task id

**Returns:** true/false (was marked/could not mark)

### List tasks:
**Parameters:** type of listing (all tasks, only pending, only complete)

**Returns:** list of tasks