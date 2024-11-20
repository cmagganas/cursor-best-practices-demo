# Project Overview
A FastAPI-based demo application that guides developers through project setup best practices using AI assistance. The app provides an interactive setup process, demonstrating proper project structure, dependency management, and API configuration.

Target Users: Developers learning FastAPI and AI-assisted development
Primary Goal: Demonstrate best practices for project setup and AI-assisted development

Required Packages:
- fastapi: Web framework for building APIs
- pydantic: Data validation using Python type annotations
- anthropic: AI integration for guided assistance

# Core Functionalities
1. Project Setup Assistant
   a. File Structure Generation
      - Create standardized directory structure following FastAPI best practices
      - Generate essential files (main.py, requirements.txt, .env)
      - Setup config files (.cursorignore, .cursorrules) for AI assistance
   
   b. Dependencies Setup
      - Install and configure core packages (FastAPI, Pydantic, Anthropic)
      - Setup virtual environment for isolation
      - Generate comprehensive requirements.txt
   
   c. Initial API Setup
      - Create basic FastAPI application with health check
      - Configure environment variables and settings
      - Setup CORS and middleware for security
      - Implement example endpoints demonstrating best practices

# Doc
## Package Documentation & Examples

### FastAPI
Documentation: https://fastapi.tiangolo.com/
Key Features:
- Modern Python web framework
- Automatic OpenAPI documentation
- Type hints and data validation

Example Usage:
```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

### Pydantic
Documentation: https://docs.pydantic.dev/latest/
Key Features:
- Data validation using type annotations
- Schema definition and serialization
- Configuration management

Example Usage:
```python
from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        b'cheese': 7,
        'cabbage': '1',
    },
}

user = User(**external_data)
```

Expected Output:
```python
print(user.model_dump())
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
```

### Anthropic
Documentation: https://docs.anthropic.com/en/api/
Key Features:
- AI-powered assistance
- Context-aware responses
- Code generation support

Example Usage:
```python
import anthropic

client = anthropic.Anthropic(
    api_key="my_api_key",  # defaults to os.environ.get("ANTHROPIC_API_KEY")
)
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
```

# Current File Structure
```
fastapi-project/
├── LICENSE
├── README.md
├── .cursorignore
├── .cursorrules
├── .gitignore
├── best-practices-overview.md
├── instructions.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
```