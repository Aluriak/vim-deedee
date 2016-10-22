if !has('python')
    finish
endif

" Global Variables {{{
let g:DeedeeSize = 4
let g:DeedeeMode = 'a'
let g:DeedeeAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
" }}}

function! Deedee()
    let a:plugin_path = escape(expand('<sfile>:p:h'), '\')
    exe 'py3file ' . escape(a:plugin_path, ' ') . '/plugin/deedee.py'
    "py3file deedee.py
endfunc

command! Deedee call Deedee()
