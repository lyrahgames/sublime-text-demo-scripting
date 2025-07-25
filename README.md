# Sublime Text Demo Scripting

A Sublime Text package designed to facilitate a live scripting workflow for demo projects by sending code from your source file to a corresponding `.fdm` file.
This plugin is ideal for developers who use a separate process or viewer that monitors a file for input, allowing you to send code snippets, blocks, or entire files for execution or display without leaving your editor.

## Core Concept

The plugin works by taking the text you want to send and writing it to a file with the same name as your source file, but with a `.fdm` extension (filesystem domain message, FDM) appended.

    Source File: ~/project/script.lua
    Target File: ~/project/script.lua.fdm

The writing process is atomic, meaning the target file is updated instantly and safely, preventing race conditions or partially written files.

## Installation

    cd ~/.config/sublime-text/Packages
    git clone https://github.com/lyrahgames/sublime-text-demo-scripting.git demo-scripting

## Usage

Commands can be accessed from the Command Palette, the file-based context menu, and the main menu under the entry `Tools`.

    Demo Scripting: Run All
    Sends the entire content of the current file.

    Demo Scripting: Run Line(s) or Selection(s)
    This is the primary context-aware command. For each cursor:
        If you have text selected, it sends the selection.
        If it's just a cursor with no selection, it sends the entire line that the cursor is on.

    Demo Scripting: Run Lua-like Block
    For each cursor:
        If you have text selected, it sends the selection.
        If it's just a cursor, it uses the custom block-finding logic to identify and send the surrounding code block.

## Copyright and License

The copyright for the code is held by the contributors of the code.
The revision history in the version control system is the primary source of authorship information for copyright purposes.
Please see individual source files for appropriate copyright notices.

`sublime-text-demo-scripting` is free software, distributed under the terms of the GNU General
Public License as published by the Free Software Foundation,
version 3 of the License (or any later version).  For more information,
see the [GNU General Public License][GPLv3] or the file [`COPYING.md`](COPYING.md).

`sublime-text-demo-scripting` is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Copyright years on `sublime-text-demo-scripting` source files may be listed using range notation, e.g., 1987-2012, indicating that every year in the range, inclusive, is a copyrightable year that could otherwise be listed individually.

Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.
This file is offered as-is, without any warranty.

[GNU-licenses]: https://www.gnu.org/licenses/ (GNU Licenses)
[GPLv3]: https://www.gnu.org/licenses/gplv3.html (GNU General Public License Version 3)
