# File:        nlbl.py
# Description: Disable linter messages
# Maintainer:  Florian Preinstorfer <nblock@archlinux.org>
# License:     same as vim itself

import re
import vim

def update_line():
    """Update the current line with a linter exception string."""
    vim.command('SyntasticSetLoclist')
    loclist = vim.eval('getloclist(0)')
    if loclist:
        lnum, _ = vim.current.window.cursor
        for entry in loclist:
            if lnum == int(entry['lnum']):
                vim.current.line = _build_shutup_line(
                    vim.current.line, _get_linter_token(entry))
                break


def _get_linter_token(entry):
    """Get the linter token based on the current loclist entry."""
    patterns = [
        (r'^\[([-a-z]+)\] ', '  # pylint: disable={}'), # pylint
        (r'\[([A-Z][0-9]*)\]$', '  # noqa: {}'),        # flake8
    ]
    for pattern, msg in patterns:
        mo = re.search(pattern, entry['text'])
        if mo:
            return msg.format(mo.group(1))


def _build_shutup_line(line, linter_string):
    """Build the updated line"""
    if not linter_string:
        return line

    return ''.join((line.rstrip(), linter_string))
