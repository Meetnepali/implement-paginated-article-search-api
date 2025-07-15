# Guidance for Task

This project is focused on implementing and validating a user profile management API module using FastAPI. The primary goal is to deliver fully functional CRUD endpoints for user profiles, utilizing Pydantic models for field validation, and returning consistent, structured error payloads for cases like validation failure, not found, or duplicate user scenarios. Data persistence will be handled in-memory using a Python dictionary, simulating a production environment suitable for demonstration and testing purposes.

## Requirements
- Create user profile CRUD API endpoints as described.
- Use Pydantic models to ensure robust data validation (for example: username conventions, email patterns, age boundaries).
- Implement custom exception handlers for common API errors to maintain a consistent error response structure.
- Organize API routes modularly using FastAPI routers.
- Persistence must remain in-memory (do not connect to an external database).
- Avoid implementing unrelated features such as authentication, database integration, or extra application logic.

## Verifying Your Solution
Check that your implementation creates, retrieves, updates, and deletes user profiles with appropriate request/response payloads and adheres to the specified data validation logic. Pay particular attention to the error responses—ensure that all validation and operational errors return structured, consistent error payloads and correct HTTP status codes. Review your code for maintainable structure, modularity, and clarity.
