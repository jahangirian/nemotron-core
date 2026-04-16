# Development Guide - Nemotron-Core

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git
- pip or conda

### Environment Setup

```bash
# Clone repository
git clone https://github.com/jahangirian/nemotron-core.git
cd nemotron-core

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

### IDE Setup

#### VS Code

Create `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

#### PyCharm

1. File → Settings → Project → Python Interpreter
2. Select `venv/bin/python`
3. Enable code inspection

---

## 🧪 Testing

### Run All Tests

```bash
# Quick test
python run_tests.py

# With coverage
python run_tests.py --coverage

# Specific test file
pytest tests/test_alchemical_uncertainty.py -v

# Specific test
pytest tests/test_alchemical_uncertainty.py::TestAlchemicalUncertainty::test_basic_uncertainty_computation -v

# Watch mode (auto-rerun on changes)
pytest-watch tests/
```

### Test Coverage Requirements

- Minimum: 80% coverage
- Critical paths: 100% coverage
- Generate report: `pytest --cov-report=html`

### Writing Tests

```python
import pytest
import numpy as np

class TestFeature:
    """Test suite for new feature"""
    
    @pytest.fixture
    def setup(self):
        """Set up test fixtures"""
        return {"data": np.random.randn(10)}
    
    def test_example(self, setup):
        """Test description"""
        assert setup["data"].shape == (10,)
```

---

## 🚀 Running the Server

### Local Development

```bash
# Simple start
python run_server.py

# With debug mode
export FLASK_DEBUG=true
python run_server.py

# On specific port
export SERVER_PORT=8000
python run_server.py
```

### Using Docker

```bash
# Build image
docker build -t nemotron-core .

# Run container
docker run -p 5000:5000 nemotron-core

# With environment variables
docker run -p 5000:5000 \
  -e ALERT_THRESHOLD=0.8 \
  -e SLACK_WEBHOOK_URL="..." \
  nemotron-core

# Using docker-compose
docker-compose up
```

### Testing API Endpoints

```bash
# Health check
curl http://localhost:5000/health

# Single query
curl -X POST http://localhost:5000/query \
  -H "Content-Type: application/json" \
  -d '{
    "user_input": [0.1, 0.2],
    "manifold": [[0.1, 0.2], [0.3, 0.4]],
    "threshold": 0.75
  }'

# View logs
docker logs -f nemotron-core
```

---

## 📝 Code Style

### PEP 8 Compliance

```bash
# Format code
black . --line-length 100

# Check style
flake8 . --max-line-length 100

# Sort imports
isort .

# Type checking
mypy . --ignore-missing-imports

# All checks
make lint  # if Makefile exists
```

### Naming Conventions

- **Variables**: `snake_case`
- **Functions**: `snake_case()`
- **Classes**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`

### Docstring Format (Google Style)

```python
def function_name(param1: int, param2: str) -> bool:
    """Brief description (one line).
    
    Longer description if needed. Can span multiple paragraphs.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
    
    Returns:
        Description of return value.
    
    Raises:
        ValueError: When input is invalid.
    
    Example:
        >>> result = function_name(1, "test")
        >>> print(result)
        True
    """
    pass
```

---

## 🔍 Debugging

### Using pdb

```python
# In code
import pdb; pdb.set_trace()

# Or Python 3.7+
breakpoint()
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

### Profiling

```bash
# Profile CPU usage
python -m cProfile -s cumtime run_server.py

# Memory profiling
pip install memory-profiler
python -m memory_profiler script.py
```

---

## 📚 Project Structure

```
nemotron-core/
├── .github/
│   └── workflows/
│       ├── tests.yml          # CI/CD tests
│       └── deploy.yml         # Deployment
├── src/
│   ├── __init__.py
│   └── backend/
│       ├── __init__.py
│       └── server.py
├── tests/
│   ├── __init__.py
│   ├── test_alchemical_uncertainty.py
│   └── test_neural_cache.py
├── alchemical_uncertainty.py
├── neural_cache.py
├── config.py
├── run_server.py
├── run_tests.py
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
├── DEVELOPMENT.md
└── LICENSE
```

---

## 🔧 Adding New Features

### Step 1: Create Feature Branch

```bash
git checkout -b feature/my-feature
```

### Step 2: Implement Feature

- Write implementation in appropriate module
- Add type hints and docstrings
- Follow PEP 8 style guide

### Step 3: Add Tests

```python
# tests/test_my_feature.py
def test_my_feature():
    """Test my new feature"""
    assert my_feature(input) == expected_output
```

### Step 4: Run Tests

```bash
pytest tests/ -v
```

### Step 5: Commit and Push

```bash
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```

### Step 6: Create Pull Request

On GitHub, open PR from `feature/my-feature` → `main`

---

## 🐛 Debugging Common Issues

### ImportError: No module named 'X'

```bash
pip install -r requirements.txt
```

### ModuleNotFoundError: No module named 'src'

```bash
# Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Port Already in Use

```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>

# Or use different port
export SERVER_PORT=5001
python run_server.py
```

### Tests Failing

```bash
# Run with verbose output
pytest tests/ -vv -s

# Run with warnings
pytest tests/ -W ignore::DeprecationWarning

# Clear cache
pytest tests/ --cache-clear
```

---

## 📦 Publishing to PyPI

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to TestPyPI (test first!)
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*
```

---

## 🚀 Performance Optimization

### Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
your_function()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
```

### Benchmarking

```bash
# Using timeit
python -m timeit "import alchemical_uncertainty; alchemical_uncertainty(...)"

# Custom benchmark
python benchmarks/benchmark_uncertainty.py
```

---

## 📋 Checklist Before Merging PR

- [ ] Code follows PEP 8
- [ ] All tests pass (`pytest -v`)
- [ ] Code coverage > 80% (`pytest --cov`)
- [ ] Type hints added (mypy passes)
- [ ] Docstrings added
- [ ] No hardcoded values
- [ ] No security issues
- [ ] Performance acceptable
- [ ] Commits are clean and descriptive
- [ ] PR description is clear

---

## 🔗 Useful Commands

```bash
# Development
python run_server.py              # Start server
python run_tests.py              # Run tests
python run_tests.py --coverage   # With coverage

# Code Quality
black .                           # Format
flake8 .                          # Lint
mypy .                            # Type check
isort .                           # Sort imports

# Docker
docker build -t nemotron-core .
docker run -p 5000:5000 nemotron-core
docker-compose up

# Git
git status                        # Check status
git log --oneline                 # View commits
git diff                          # View changes
```

---

## 📞 Getting Help

- **Code Review**: Tag maintainers in PR
- **Issues**: GitHub Issues with detailed description
- **Discussions**: GitHub Discussions
- **Discord**: [Community Discord]

---

## 📄 License

MIT - See LICENSE file

---

**Last Updated**: 2026-04-16
**Version**: 1.0.0
