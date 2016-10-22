import sys
import random

import vim


# Modes of doublons verification: search all opened files, only current buffer,
#  or no verification.
MODES = 'abn'  # All, Buffer, None

# Arbitrary number of tries before give up to find a tag
TRY_LIMIT = 10

# Read
SIZE = int(vim.eval('g:DeedeeSize'))
MODE = vim.eval('g:DeedeeMode')
ALPHABET = vim.eval('g:DeedeeAlphabet')


def random_tag(size:int, alphabet:iter) -> str:
    return ''.join(random.choice(alphabet) for _ in range(size))


def unique(tag:str, mode:str) -> bool:
    """Tag is the tag to verify as unique. mode is one in MODES"""
    if not tag: return False
    # buffers to explore
    if mode == 'a':
        buffers = tuple(vim.buffers)
    elif mode == 'b':
        buffers = [vim.current.buffer]
    elif mode == 'n':
        buffers = []
    else:  # invalid value
        print('vim-deedee: invalid mode value :', mode)
    # explore buffers
    if any(tag in line for buffer in buffers for line in buffer):
        return False
    return True


# find a unique tag
for _ in range(TRY_LIMIT):
    tag = random_tag(int(SIZE), tuple(ALPHABET))
    if unique(tag, MODE):
        # get position of cursor, where tag should be inserted
        buffer = vim.current.buffer
        window = vim.current.window
        row, col = window.cursor
        # insert the tag in the line after the cursor
        line = buffer[row-1]
        buffer[row-1] = line[:col] + tag + line[col:]
        exit()
else:  # no unique tag found
    print('All tags have been dispatched. No tag added.')
