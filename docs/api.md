## Server Tests

### `GET /`

- **Response**

```json
{
  "message": "Mesh LLM System is Live!"
}
```

## 🧠 Mesh Task API

### `GET /mesh/list-tasks`

- **Description**: Lists all registered mesh tasks.
- **Response**

```json
{
  "tasks": ["filter-private"]
}
```

### `GET /mesh/run-task`

- **Description**: Runs the specified task name in body.
- **Body**:

```json
{
  "task": "filter-private",
  "text": "Hello, my name is Rishi and my email is rishu@web2docx.com"
}
```

- **Response**

```json
{
  "tasks": ["filter-private"]
}
```
