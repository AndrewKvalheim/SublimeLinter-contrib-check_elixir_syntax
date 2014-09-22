"""This module tests the Elixirc plugin class."""

import unittest
from unittest.mock import MagicMock
from linter import Check_elixir_syntax


class TestElixirc(unittest.TestCase):

    """Tests the Elixirc plugin class."""

    def setUp(self):
        """Initialize the testing environment."""

        pass

    def lint(self, code):
        """Lint a file and return the results."""

        view = MagicMock()
        view.file_name = MagicMock(return_value=None)
        linter = Check_elixir_syntax(view, 'elixir')
        linter.reset(code, {})
        linter.lint(None)
        return linter

    def test_empty(self):
        """Detect no errors or warnings."""

        linter = self.lint('')
        self.assertEqual(linter.errors, {})

    def test_valid(self):
        """Detect no errors or warnings."""

        linter = self.lint('foo = 42')
        self.assertEqual(linter.errors, {})

    def test_syntax_errors(self):
        """Detect syntax errors."""

        linter = self.lint('foo = :42')
        self.assertEqual(linter.errors, {
            0: [(6, 'invalid token: :42')]
        })
        self.assertIsNotNone(linter.highlight.marks)
