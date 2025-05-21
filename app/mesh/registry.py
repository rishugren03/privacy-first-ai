import importlib
import json
from pathlib import Path
from typing import Callable, Dict, Any

mesh_tasks: Dict[str, Dict[str, Any]] = {}

def register_task(name: str, func: Callable, metadata: dict):
  if name in mesh_tasks:
    raise ValueError(f"Task '{name}' is already registered.")
  
  mesh_tasks[name] = {
    "function": func,
    "metadata": metadata
  }

def get_task(name: str) -> callable:
  task = mesh_tasks.get(name)
  return task["function"] if task else None  

def get_all_plugins():
  return [
    {
      "name": name,
      "description": data["metadata"].get("description"),
      "input_type": data["metadata"].get("input_type"),
      "output_type": data["metadata"].get("output_type")
    }
    for name, data in mesh_tasks.items()
  ]

def auto_register_tasks():
  base_path = Path(__file__).resolve().parent.parent / "tasks"
  for task_dir in base_path.iterdir():
    if task_dir.is_dir():
      plugin_file = task_dir / "plugin.json"
      logic_file = task_dir / "logic.py"

      if plugin_file.exists() and logic_file.exists():
        try:
          # Load plugin metadata
          with open(plugin_file, "r") as f:
            metadata = json.load(f)

          task_name = metadata["name"]

          # Import logic module dynamically
          module_path = f"app.tasks.{task_dir.name}.logic"
          logic_module = importlib.import_module(module_path)

          if hasattr(logic_module, "run"):
            register_task(task_name, logic_module.run, metadata)
          else:
            print(f"[WARNING] No 'run' function in {module_path}")  
        except Exception as e:
           print(f"[ERROR] Failed to register task from {task_dir.name}: {e}")