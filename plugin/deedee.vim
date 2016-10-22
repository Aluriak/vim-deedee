if !has('python')
    finish
endif

" Global Variables {{{
let g:DeedeeSize = 4
let g:DeedeeMode = 'a'
let g:DeedeeAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
" }}}

function! Deedee()
    py3file .vim/plugin/deedee.py
endfunc

command! Deedee call Deedee()
