#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Andrew Kvalheim
# Copyright (c) 2014 Andrew Kvalheim
#
# License: MIT
#

"""This module exports the Check_elixir_syntax plugin class."""

import json
from SublimeLinter.lint import Linter, util


class Check_elixir_syntax(Linter):

    """Provides an interface to check_elixir_syntax."""

    syntax = 'elixir'
    cmd = 'check_elixir_syntax'
    version_requirement = '0.0.1'
    line_col_base = (0, 0)
    error_stream = util.STREAM_STDOUT

    def find_errors(self, output):
        for result in json.loads(output):

            match = True
            line = result['line'] - 1
            col = None
            error = result['type'] == 'error'
            warning = result['type'] == 'warning'
            message = result['message']
            near = result['token'].strip("[]'")

            yield match, line, col, error, warning, message, near
