# tests/conftest.py
import sys
from pathlib import Path

# Add the repository root directory to Python path so tests can import main.py
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
