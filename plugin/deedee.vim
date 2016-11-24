if !has('python3') && !has('python')
    finish
endif

" Global Variables {{{
let g:DeedeeSize = 6
let g:DeedeeMode = 'a'
let g:DeedeeAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
" }}}

" get plugin path
let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! Deedee()
    exe 'py3file ' . escape(s:plugin_path, ' ') . '/deedee.py'
endfunc

command! Deedee call Deedee()
