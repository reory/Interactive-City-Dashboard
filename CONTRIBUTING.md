# Contributing to Interactive City Dashboard

Thank you for your interest in contributing!  
This project follows a clean, modular architecture with a strong focus on clarity, testability, and maintainability.  
Whether you're fixing a bug, improving documentation, or adding a new feature, your help is most appreciated.

---

## 🧭 How to Contribute

### 1. Fork the Repository

Click **Fork** at the top of the GitHub page to create your own copy of the project.

---

### 2. Create a Feature Branch

Use a descriptive name:

```bash
git checkout -b feature/add-new-layout
```

--- 

### 3. Make Your Changes

Follow the project’s architecture principles:

- Pure functions for callback logic
- Separation of concerns (layout, callbacks, components, services, data)
- No hidden globals
- Consistent naming and formatting

If you add new UI components or callbacks, keep them modular and testable.

---

### 4. Run the Test Suite
```bash
pytest -q
```

All tests must pass before submitting a PR.
If you add new functionality, include appropriate tests.

---

## Testing Guidelines

This project uses:

- Unit tests for callbacks
- Layout tests for structure
- Integration tests using Dash’s callback registry
- Place new tests in the tests/ directory and follow existing patterns.

---

### Code Style

- Use PEP 8 conventions
- Keep functions small and focused
- Avoid duplication
- Prefer pure functions where possible
- Document complex logic with short, clear comments

---

### Submitting a Pull Request

Push your branch:


```bash
git push origin feature/add-new-layout
```

- Open a Pull Request on GitHub
- Describe your changes clearly
- Reference any related issues
- Ensure your PR title is concise and meaningful

A maintainer will review your PR and may request adjustments.

---

### Feature Ideas

Contributions are welcome in areas such as:

- New layout modes
- Additional charts or map layers
- Improved theme support
- Performance enhancements
- Accessibility improvements
- Documentation and examples

If you're unsure whether an idea fits the project, open an issue to discuss it first.

---

### Code of Conduct

Please be respectful, constructive, and collaborative.
We aim to maintain a friendly environment for all contributors. Thank you.