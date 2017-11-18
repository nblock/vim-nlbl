# vim-nlbl
vim-nlbl (No linter, bad linter!) is a hackish [VIM](http://www.vim.org/)
plugin to selectively disable linter warnings.

## Requirements
vim-nlbl requires [VIM](http://www.vim.org/) with Python 3 support (`+python3`)
and the [Syntastic](https://github.com/vim-syntastic/syntastic) plugin.

## Installation
Use any plugin manager to install this plugin, e.g: vim-plug:

```vim
Plug 'nblock/vim-nlbl'
```

## Usage
* Edit a file until one of your linters complains
* Navigate to the flagged line
* Issue: `:NoLinterBadLinter`

## Example
Assume the following Python code with [Flake8](https://gitlab.com/pycqa/flake8)
installed: Use any plugin manager to install this plugin, e.g:
[vim-plug](https://github.com/junegunn/vim-plug/):

```python
foo='bar'
```

[Flake8](https://gitlab.com/pycqa/flake8) (via
[Syntastic](https://github.com/vim-syntastic/syntastic) will tell you the
following: "missing whitespace around operator [E225]". You might be happy with
this line, so issue `:NoLinterBadLinter` and the line will be transformed to:

```python
foo='bar'  # noqa: E225
```

## Supported linters
This plugin is just a hack and it currently only supports:
* [Flake8](https://gitlab.com/pycqa/flake8)
* [Pylint](https://www.pylint.org/)
