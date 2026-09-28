# Johnny

johnny assistant i building for my personal assistant.

## Features

- **Intent Detection**: Accurately classifies user requests (app operations, questions, searches, and actions).
- **Planner & Orchestrator**: Generates structured execution steps and runs them via an orchestration pipeline.
- **Permission Safety**: Manages action permissions with confirmation safeguards for destructive operations.
- **Extensible Tool Registry**: Built-in system, file, browser, and application tool execution.
- **Flexible AI Engines**:
  - `APIEngine`: Connect to Ollama, OpenAI, or compatible HTTP REST inference endpoints.
  - `LocalEngine`: Direct in-process GGUF inference support via `llama-cpp-python`.

## Project Structure

```
Johnny/
├── core/
│   ├── ai/
│   │   ├── api_engine.py
│   │   ├── engine.py
│   │   ├── local_engine.py
│   │   └── model_manager.py
│   ├── config.py
│   ├── intent.py
│   ├── orchestrator.py
│   ├── permissions.py
│   ├── planner.py
│   └── types.py
├── tools/
│   ├── apps.py
│   ├── browser.py
│   ├── files.py
│   ├── registry.py
│   └── system.py
├── tests/
│   ├── test_intent.py
│   ├── test_orchestrator.py
│   ├── test_permissions.py
│   ├── test_planner.py
│   └── test_registry.py
├── main.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests

```bash
python -m pytest
```

### 3. Run Johnny

```bash
python main.py
```
