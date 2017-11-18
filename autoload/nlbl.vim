" File:        nlbl.vim
" Description: Disable linter messages
" Maintainer:  Florian Preinstorfer <nblock@archlinux.org>
" License:     same as vim itself

if !has('python3')
  echohl WarningMsg|echomsg "NoLinterBadLinter requires Vim to be compiled with Python 3"|echohl None
  finish
endif

" Plugin path
let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

" Python interface
function! nlbl#AddLinterException()
  exe 'py3file ' . escape(s:plugin_path, ' ') . '/nlbl.py'
  python3 update_line()
endfunction
