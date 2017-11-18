" File:        nlbl.vim
" Description: Disable linter messages
" Maintainer:  Florian Preinstorfer <nblock@archlinux.org>
" License:     same as vim itself

" Init
if exists('loaded_nlbl') || &cp"
  finish
endif
let loaded_nlbl = 1"

" Setup command
command! -nargs=0 NoLinterBadLinter call nlbl#AddLinterException()
