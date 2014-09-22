"""This module is a crude mock of the sublime module."""

import sys
from unittest.mock import MagicMock

DRAW_EMPTY_AS_OVERWRITE = 0
DRAW_NO_FILL = 0
DRAW_NO_OUTLINE = 0
DRAW_SOLID_UNDERLINE = 0
DRAW_SQUIGGLY_UNDERLINE = 0
DRAW_STIPPLED_UNDERLINE = 0
HIDDEN = 0

platform = MagicMock(return_value=sys.platform)
view = MagicMock()


class Region:
    def __init__(self, a, b):
        self.a = a
        self.b = b
