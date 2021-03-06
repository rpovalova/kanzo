# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import re


STR_MASK = '*' * 8
COLORS = {'nocolor': "\033[0m", 'red': "\033[0;31m",
          'green': "\033[32m", 'blue': "\033[34m",
          'yellow': "\033[33m"}


def color_text(text, color):
    """
    Returns given text string with appropriate color tag. Allowed values
    for color parameter are 'red', 'blue', 'green' and 'yellow'.
    """
    return '%s%s%s' % (COLORS[color], text, COLORS['nocolor'])


def mask_string(unmasked, mask_list=None, replace_list=None):
    """
    Replaces words from mask_list with MASK in unmasked string.
    If words are needed to be transformed before masking, transformation
    could be describe in replace list. For example [("'","'\\''")]
    replaces all ' characters with '\\''.
    """
    mask_list = mask_list or []
    replace_list = replace_list or []

    masked = unmasked
    for word in mask_list:
        if not word:
            continue
        for before, after in replace_list:
            word = word.replace(before, after)
        masked = masked.replace(word, STR_MASK)
    return masked


def state_format(msg, state, color, offset=60):
    """
    Formats state with offset according to given message.
    """
    _msg = '%s' % msg
    for clr in COLORS.values():
        _msg = re.sub(re.escape(clr), '', msg)
    space = offset - len(_msg) + len(state)

    state = '[ %s ]' % color_text(state, color)
    return state.rjust(space)


def state_message(msg, state, color):
    """
    Formats given message with colored state information.
    """
    return '%s%s' % (msg, state_format(msg, state, color))
