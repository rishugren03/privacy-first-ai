# 🏗️ Architecture Overview

## 🔐 Privacy-First Mesh LLM System

This system is designed to be modular, scalable, and privacy-aware — with the long-term goal of supporting a marketplace for pluggable micro-LLMs (mesh architecture).

---

## ⚙️ Current Architecture (Phase 2)

### 📁 Core Components

#### 1. **Task Registry**

- File: `app/mesh/registry.py`
- Purpose: Maintains a registry (`mesh_tasks`) of all available mesh tasks.
- Functions:
  - `register_task(name, func)`: Register a task.
  - `get_task(name)`: Retrieve a task by name.
  - `auto_register_tasks()`: Auto-loads all task modules on startup.

#### 2. **Task Implementations**

- Folder: `app/tasks/`
- Each `.py` file here contains task logic.
- Example:
  - `filter_private` task defined in `logic.py`
  - Uses the redactor from `app/services/`

#### 3. **API Layer**

- File: `app/mesh/router.py`
- Endpoints:
  - `GET /mesh/list-tasks` — List all registered tasks.
  - `POST /mesh/run-task` — Execute a task dynamically based on user input.
- Schema:
  - Request: `{ "task": "filter-private", "text": "..." }`
  - Response: Task-defined output.

#### 4. **Main Server**

- File: `main.py`
- Responsibilities:
  - Bootstraps FastAPI app.
  - Loads mesh system via `auto_register_tasks()`.
  - Includes mesh router.

---

## 🔁 Execution Flow

1. System starts → `auto_register_tasks()` loads all task modules.
2. User sends `POST /mesh/run-task` with a task name + input text.
3. Server fetches matching function via `get_task()`.
4. Executes the task and returns the result.

---

## 🔌 Future-Proof Design

This architecture is built to eventually support:

- A **plugin-based marketplace** for micro-LLMs.
- Dynamic loading of custom modules.
- Strict filtering & sandboxing for privacy-critical tasks.

---

✅ **Status:** Phase 2 complete. Task mesh is live and working.
