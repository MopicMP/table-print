"""Tests for table-print."""

import pytest
from table_print import print


class TestPrint:
    """Test suite for print."""

    def test_basic(self):
        """Test basic usage."""
        result = print("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            print("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = print(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
