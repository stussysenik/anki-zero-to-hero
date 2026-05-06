#!/usr/bin/env python3
"""Build Spacemacs Zero-to-Hero Anki deck. ~200 cards from first principles to advanced."""

import genanki
import random
import time

OUTPUT = "/home/senik/Desktop/Spacemacs_Zero_to_Hero.apkg"
DECK_ID = random.randrange(1 << 30, 1 << 31)
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# ── Model ──────────────────────────────────────────────────────────────────────
model = genanki.Model(
    MODEL_ID,
    "Spacemacs Q&A",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": '<div class="front">{{Front}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>',
        }
    ],
    css="""
        .card {
            font-family: "Helvetica Neue", Arial, sans-serif;
            font-size: 22px;
            text-align: center;
            color: #ddd;
            background-color: #1e1e2e;
            padding: 20px;
        }
        .front { font-weight: bold; margin-top: 60px; }
        .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
        code, pre {
            font-family: "Fira Code", "Monaco", "Consolas", monospace;
            background: #313244;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 18px;
        }
        hr { border-color: #444; }
    """,
)

# ── Deck hierarchy ─────────────────────────────────────────────────────────────
ROOT = DECK_ID
decks = {
    "Fundamentals":    genanki.Deck(ROOT + 1, "Spacemacs::Zero2Hero::01-Fundamentals"),
    "EvilMovement":    genanki.Deck(ROOT + 2, "Spacemacs::Zero2Hero::02-Evil-Movement"),
    "EmacsMovement":   genanki.Deck(ROOT + 3, "Spacemacs::Zero2Hero::03-Emacs-Movement"),
    "EvilEditing":     genanki.Deck(ROOT + 4, "Spacemacs::Zero2Hero::04-Evil-Editing"),
    "Buffers":         genanki.Deck(ROOT + 5, "Spacemacs::Zero2Hero::05-Buffers"),
    "Files":           genanki.Deck(ROOT + 6, "Spacemacs::Zero2Hero::06-Files"),
    "Windows":         genanki.Deck(ROOT + 7, "Spacemacs::Zero2Hero::07-Windows-Layouts"),
    "Search":          genanki.Deck(ROOT + 8, "Spacemacs::Zero2Hero::08-Search"),
    "Projects":        genanki.Deck(ROOT + 9, "Spacemacs::Zero2Hero::09-Projects"),
    "Magit":           genanki.Deck(ROOT + 10, "Spacemacs::Zero2Hero::10-Git-Magit"),
    "OrgMode":         genanki.Deck(ROOT + 11, "Spacemacs::Zero2Hero::11-Org-Mode"),
    "Help":            genanki.Deck(ROOT + 12, "Spacemacs::Zero2Hero::12-Help-System"),
    "Elisp":           genanki.Deck(ROOT + 13, "Spacemacs::Zero2Hero::13-Elisp"),
    "Config":          genanki.Deck(ROOT + 14, "Spacemacs::Zero2Hero::14-Config"),
    "Advanced":        genanki.Deck(ROOT + 15, "Spacemacs::Zero2Hero::15-Advanced"),
}

# ── Cards ──────────────────────────────────────────────────────────────────────
# Format: (deck_key, front, back)
cards = [
    # ═══ 01 - FUNDAMENTALS ═══════════════════════════════════════════════════════
    ("Fundamentals", "What is Emacs?",
     "An extensible, customizable, self-documenting real-time display editor."),

    ("Fundamentals", "What is Spacemacs?",
     "A community-driven Emacs distribution with curated layers, mnemonic <code>SPC</code> leader key, and both vim (evil) & emacs (holy) editing styles."),

    ("Fundamentals", "What is a buffer?",
     "An in-memory object holding text — often a file's contents. A buffer is NOT the same as a file on disk."),

    ("Fundamentals", "What is a window?",
     "A viewport into a buffer — the pane you see on screen. One buffer can appear in many windows."),

    ("Fundamentals", "What is a frame?",
     "A GUI window containing one or more Emacs windows. Think of it as the OS window."),

    ("Fundamentals", "What is a major mode?",
     "A mode specialized for a language or file type (e.g. <code>python-mode</code>). Only one major mode per buffer."),

    ("Fundamentals", "What is a minor mode?",
     "A mode that adds extra features on top of any major mode (e.g. <code>flycheck-mode</code>, <code>linum-mode</code>). Many can be active at once."),

    ("Fundamentals", "What is the leader key in Spacemacs?",
     "<code>SPC</code> — it opens a which-key menu of all commands organized by mnemonic letter."),

    ("Fundamentals", "What is a layer in Spacemacs?",
     "A curated collection of packages with configuration. Layers are the unit of features in Spacemacs (e.g. <code>python</code>, <code>git</code>, <code>org</code>)."),

    ("Fundamentals", "What is the minibuffer?",
     "The bottom line where Emacs prompts you for commands and input. When you press <code>M-x</code>, you interact with the minibuffer."),

    ("Fundamentals", "What is the mode line?",
     "The status line at the bottom of each window showing the buffer name, current modes, line number, and other info."),

    ("Fundamentals", "What is the echo area?",
     "The line below the mode line that displays messages and command feedback temporarily."),

    ("Fundamentals", "What is <code>C-u</code> (universal argument)?",
     "A prefix that modifies the next command. <code>C-u 10 some-cmd</code> runs <code>some-cmd</code> 10 times. Bare <code>C-u</code> = 4 times."),

    ("Fundamentals", "What is the point?",
     "The current cursor position in a buffer."),

    ("Fundamentals", "What is the mark?",
     "A saved position. When used with point, they define the region (selected text between them)."),

    ("Fundamentals", "What is the region?",
     "The text between point and mark — what gets acted upon by commands like <code>C-w</code> (kill) or <code>M-w</code> (copy)."),

    ("Fundamentals", "What is <code>C-g</code>?",
     "The universal abort key. Cancels any in-progress command, exits the minibuffer, closes menus. Press repeatedly if stuck."),

    ("Fundamentals", "How do you run any command by name?",
     "<code>SPC SPC</code> or <code>M-x</code> — opens a prompt for any command."),

    # ═══ 02 - EVIL (VIM) MOVEMENT ════════════════════════════════════════════════
    ("EvilMovement", "Move cursor left / down / up / right in normal mode?",
     "<code>h</code> / <code>j</code> / <code>k</code> / <code>l</code>"),

    ("EvilMovement", "Jump to start of next word?",
     "<code>w</code> (forward one word)"),

    ("EvilMovement", "Jump to start of previous word?",
     "<code>b</code> (back one word)"),

    ("EvilMovement", "Jump to end of current/next word?",
     "<code>e</code> (end of word)"),

    ("EvilMovement", "Go to beginning / end of current line?",
     "<code>0</code> — first column<br><code>$</code> — last column"),

    ("EvilMovement", "Go to first / last non-whitespace character on line?",
     "<code>^</code> — first non-blank<br><code>g_</code> — last non-blank"),

    ("EvilMovement", "Find character on current line (forward / backward)?",
     "<code>f{char}</code> forward to char<br><code>F{char}</code> backward to char"),

    ("EvilMovement", "Find <i>before</i> a character on current line (forward / backward)?",
     "<code>t{char}</code> forward (until char)<br><code>T{char}</code> backward (until char)"),

    ("EvilMovement", "Repeat last <code>f</code> / <code>t</code> search forward / backward?",
     "<code>;</code> — repeat forward<br><code>,</code> — repeat backward"),

    ("EvilMovement", "Go to first line / last line of buffer?",
     "<code>gg</code> — first line<br><code>G</code> — last line"),

    ("EvilMovement", "Go to a specific line number?",
     "<code>{N}gg</code> or <code>{N}G</code> — e.g. <code>42gg</code>"),

    ("EvilMovement", "Jump to matching bracket / paren?",
     "<code>%</code>"),

    ("EvilMovement", "Jump to previous / next paragraph?",
     "<code>{</code> — previous blank line<br><code>}</code> — next blank line"),

    ("EvilMovement", "Page down / up / half-page down / half-page up?",
     "<code>C-f</code> / <code>C-b</code> — full page<br><code>C-d</code> / <code>C-u</code> — half page"),

    ("EvilMovement", "Scroll to put cursor at top / center / bottom of window?",
     "<code>zt</code> — top<br><code>zz</code> — center<br><code>zb</code> — bottom"),

    ("EvilMovement", "Place cursor at the top / middle / bottom of the visible window?",
     "<code>H</code> — High (top)<br><code>M</code> — Middle<br><code>L</code> — Low (bottom)"),

    ("EvilMovement", "Go back / forward in the jump list?",
     "<code>C-o</code> — back<br><code>C-i</code> — forward"),

    ("EvilMovement", "Search for word under cursor forward / backward?",
     "<code>*</code> — forward<br><code>#</code> — backward"),

    ("EvilMovement", "Search forward / backward in buffer?",
     "<code>/</code> — forward<br><code>?</code> — backward"),

    ("EvilMovement", "Next / previous search match?",
     "<code>n</code> — next<br><code>N</code> — previous"),

    # ═══ 03 - EMACS (HOLY) MOVEMENT ══════════════════════════════════════════════
    ("EmacsMovement", "(Emacs style) Move forward / back one character?",
     "<code>C-f</code> — forward<br><code>C-b</code> — backward"),

    ("EmacsMovement", "(Emacs style) Move to next / previous line?",
     "<code>C-n</code> — next<br><code>C-p</code> — previous"),

    ("EmacsMovement", "(Emacs style) Move forward / backward one word?",
     "<code>M-f</code> — forward<br><code>M-b</code> — backward"),

    ("EmacsMovement", "(Emacs style) Go to beginning / end of line?",
     "<code>C-a</code> — beginning<br><code>C-e</code> — end"),

    ("EmacsMovement", "(Emacs style) Go to beginning / end of sentence?",
     "<code>M-a</code> — beginning<br><code>M-e</code> — end"),

    ("EmacsMovement", "(Emacs style) Go to beginning / end of paragraph?",
     "<code>M-{</code> — previous<br><code>M-}</code> — next"),

    ("EmacsMovement", "(Emacs style) Page down / page up?",
     "<code>C-v</code> — page down<br><code>M-v</code> — page up"),

    ("EmacsMovement", "(Emacs style) Go to beginning / end of buffer?",
     "<code>M-&lt;</code> — beginning<br><code>M-&gt;</code> — end"),

    ("EmacsMovement", "(Emacs style) Recenter screen around cursor?",
     "<code>C-l</code> — first press centers, second puts at top, third at bottom"),

    ("EmacsMovement", "(Emacs style) Go to a specific line number?",
     "<code>M-g g {N}</code> — e.g. <code>M-g g 42</code>"),

    # ═══ 04 - EVIL EDITING ═══════════════════════════════════════════════════════
    ("EvilEditing", "Enter insert mode before cursor / at end of line?",
     "<code>i</code> — insert at cursor<br><code>A</code> — append at end of line"),

    ("EvilEditing", "Enter insert mode at beginning of line?",
     "<code>I</code> — insert at first non-blank"),

    ("EvilEditing", "Open a new line below / above and enter insert mode?",
     "<code>o</code> — below<br><code>O</code> — above"),

    ("EvilEditing", "Delete character under / before cursor?",
     "<code>x</code> — under cursor<br><code>X</code> — before cursor"),

    ("EvilEditing", "Delete (cut) the current line?",
     "<code>dd</code> — also stores it in the kill ring (clipboard)"),

    ("EvilEditing", "Yank (copy) the current line?",
     "<code>yy</code>"),

    ("EvilEditing", "Paste after / before cursor?",
     "<code>p</code> — after<br><code>P</code> — before"),

    ("EvilEditing", "Undo / redo?",
     "<code>u</code> — undo<br><code>C-r</code> — redo"),

    ("EvilEditing", "Enter visual mode (char / line / block)?",
     "<code>v</code> — character<br><code>V</code> — line<br><code>C-v</code> — block"),

    ("EvilEditing", "Delete / Change / Yank with a motion?",
     "<code>d{motion}</code> — delete<br><code>c{motion}</code> — change (delete + insert)<br><code>y{motion}</code> — yank"),

    ("EvilEditing", "Delete / Change / Yank inside a word?",
     "<code>diw</code> / <code>ciw</code> / <code>yiw</code>"),

    ("EvilEditing", "Delete / Change / Yank inside quotes <code>\"</code>?",
     "<code>di\"</code> / <code>ci\"</code> / <code>yi\"</code>"),

    ("EvilEditing", "Delete / Change / Yank inside parentheses <code>()</code>?",
     "<code>di(</code> / <code>ci(</code> / <code>yi(</code> — also works with <code>)</code>, <code>b</code>"),

    ("EvilEditing", "Delete inside vs. around braces <code>{}</code>?",
     "<code>di{</code> — inside (just the content)<br><code>da{</code> — around (content + braces)"),

    ("EvilEditing", "Indent line / visual selection right or left?",
     "<code>&gt;&gt;</code> — indent line right<br><code>&lt;&lt;</code> — indent line left<br>In visual mode: <code>&gt;</code> / <code>&lt;</code>"),

    ("EvilEditing", "Repeat the last change?",
     "<code>.</code> — powerful: replays the last edit operation"),

    ("EvilEditing", "Replace a single character?",
     "<code>r{char}</code> — replace char under cursor and stay in normal mode"),

    ("EvilEditing", "Enter Replace (overwrite) mode?",
     "<code>R</code> — overwrite text until you press <code>ESC</code>"),

    ("EvilEditing", "Toggle case of character / visual selection?",
     "<code>~</code> — toggles uppercase ↔ lowercase"),

    ("EvilEditing", "Join current line with the next line?",
     "<code>J</code> — joins with a space. <code>gJ</code> joins without space."),

    ("EvilEditing", "Auto-indent a line or visual selection?",
     "<code>==</code> — current line<br><code>={motion}</code> — e.g. <code>=G</code> indent to end of buffer<br><code>=</code> — visual selection"),

    ("EvilEditing", "Delete and enter insert mode on the <i>same line</i>?",
     "<code>cc</code> — change entire line (delete it, enter insert at correct indent)"),

    ("EvilEditing", "Yank to system clipboard?",
     "<code>\"+y</code> with a motion, e.g. <code>\"+yy</code> for current line"),

    ("EvilEditing", "What is a text object?",
     "A structured unit of text: <code>iw</code> (inner word), <code>i\"</code> (inside quotes), <code>ip</code> (inner paragraph), <code>it</code> (inner tag)."),

    ("EvilEditing", "Make uppercase / lowercase of a motion?",
     "<code>gU{motion}</code> — uppercase<br><code>gu{motion}</code> — lowercase<br>e.g. <code>guiw</code> lowercases current word"),

    # ═══ 05 - BUFFERS ════════════════════════════════════════════════════════════
    ("Buffers", "Switch to another open buffer?",
     "<code>SPC b b</code> — helm-mini: search and switch"),

    ("Buffers", "Kill (close) the current buffer?",
     "<code>SPC b d</code>"),

    ("Buffers", "Switch to a buffer in another window?",
     "<code>SPC b B</code>"),

    ("Buffers", "Kill a buffer by name?",
     "<code>SPC b k</code>"),

    ("Buffers", "Go to the next / previous buffer?",
     "<code>SPC b n</code> — next<br><code>SPC b p</code> — previous"),

    ("Buffers", "Kill all buffers except the current one?",
     "<code>SPC b m</code>"),

    ("Buffers", "Save the current buffer?",
     "<code>SPC f s</code> or <code>SPC b s</code>"),

    ("Buffers", "Copy entire buffer content to clipboard?",
     "<code>SPC b Y</code>"),

    ("Buffers", "Toggle read-only on current buffer?",
     "<code>SPC b w</code>"),

    ("Buffers", "Revert buffer to its file on disk (discard unsaved changes)?",
     "<code>SPC b R</code>"),

    ("Buffers", "What is <code>SPC b i</code>?",
     "Toggle the imenu-list sidebar — a persistent outline of functions/classes in the current buffer."),

    # ═══ 06 - FILES ══════════════════════════════════════════════════════════════
    ("Files", "Open a file (with fuzzy search)?",
     "<code>SPC f f</code> — helm-find-files"),

    ("Files", "Save current file?",
     "<code>SPC f s</code> or <code>:w</code> (evil) or <code>C-x C-s</code> (emacs)"),

    ("Files", "Toggle the file tree sidebar?",
     "<code>SPC f t</code> (treemacs / neotree)"),

    ("Files", "Open a recently visited file?",
     "<code>SPC f r</code>"),

    ("Files", "Rename the current file?",
     "<code>SPC f R</code> — renames and updates all open buffers referencing that file"),

    ("Files", "Copy the current file's path to clipboard?",
     "<code>SPC f y</code>"),

    ("Files", "Delete the current file and kill its buffer?",
     "<code>SPC f D</code>"),

    ("Files", "Open a directory in dired (file manager)?",
     "<code>SPC f d</code>"),

    ("Files", "Reload the .spacemacs config?",
     "<code>SPC f e R</code> — syncs and applies changes"),

    ("Files", "Open .spacemacs for editing?",
     "<code>SPC f e d</code> — opens the config file"),

    ("Files", "How do you open a file as another user (root)?",
     "<code>SPC f E</code> — open file with sudo / <code>:e /sudo::/etc/hosts</code>"),

    # ═══ 07 - WINDOWS & LAYOUTS ═════════════════════════════════════════════════
    ("Windows", "Split window vertically (side by side)?",
     "<code>SPC w /</code>"),

    ("Windows", "Split window horizontally (stacked)?",
     "<code>SPC w -</code>"),

    ("Windows", "Toggle maximize / unmaximize current window?",
     "<code>SPC w m</code> — also <code>:only</code> in evil"),

    ("Windows", "Close (delete) the current window?",
     "<code>SPC w d</code> or <code>:q</code> in evil"),

    ("Windows", "Move focus to window left / down / up / right?",
     "<code>SPC w h</code> / <code>SPC w j</code> / <code>SPC w k</code> / <code>SPC w l</code>"),

    ("Windows", "Cycle forward / backward through windows?",
     "<code>SPC w w</code> — forward<br><code>SPC w W</code> — backward"),

    ("Windows", "Enter window transient state (for resizing/moving)?",
     "<code>SPC w .</code> — then use <code>h/j/k/l</code> to resize, any other key to exit"),

    ("Windows", "Make all windows the same size?",
     "<code>SPC w =</code> — balance equal"),

    ("Windows", "Swap window position with another?",
     "<code>SPC w x</code> — then choose destination window"),

    ("Windows", "Undo / redo the last window layout change?",
     "<code>SPC w u</code> — undo<br><code>SPC w U</code> — redo"),

    ("Windows", "What's a layout in Spacemacs?",
     "A named window arrangement. Save with <code>SPC l s</code>, load with <code>SPC l l</code>. Use <code>SPC l TAB</code> to toggle between last two."),

    # ═══ 08 - SEARCH ═════════════════════════════════════════════════════════════
    ("Search", "Interactive search in current buffer (shows all matches)?",
     "<code>SPC s s</code> — helm-swoop"),

    ("Search", "Search for text across all project files?",
     "<code>SPC s p</code> — uses ripgrep/silver-searcher"),

    ("Search", "Search for text in a specific directory?",
     "<code>SPC s d</code>"),

    ("Search", "Search across all open buffers?",
     "<code>SPC s b</code>"),

    ("Search", "Grep-style search in project?",
     "<code>SPC s g p</code> — helm-projectile-grep"),

    ("Search", "Search in all project files with ag (silver searcher)?",
     "<code>SPC s a p</code>"),

    ("Search", "Search for symbol (function/var) at point across project?",
     "<code>SPC s j</code> — imenu search across project"),

    ("Search", "List all symbols (functions/classes) in current file?",
     "<code>SPC s J</code> — imenu for current file"),

    ("Search", "Replace text across the project (find and replace)?",
     "<code>SPC s R</code> — then edit results and confirm. Or <code>SPC /</code> search then <code>cgn</code> to change each match."),

    ("Search", "Search in all files via the silver searcher?",
     "<code>SPC s a P</code> — search entire project asynchronously"),

    ("Search", "What's the difference between <code>SPC s s</code> and <code>SPC /</code>?",
     "<code>SPC /</code> is incremental vim-style <code>/</code> (one match at a time).<br><code>SPC s s</code> shows ALL matches in a helm buffer."),

    # ═══ 09 - PROJECTS (PROJECTILE) ══════════════════════════════════════════════
    ("Projects", "Switch to a different project?",
     "<code>SPC p p</code>"),

    ("Projects", "Find a file in current project (fuzzy)?",
     "<code>SPC p f</code>"),

    ("Projects", "Toggle between a source file and its test file?",
     "<code>SPC p t</code> — e.g. <code>foo.py</code> ↔ <code>test_foo.py</code>"),

    ("Projects", "Kill all buffers belonging to the current project?",
     "<code>SPC p k</code>"),

    ("Projects", "Switch between files with the same name in different directories?",
     "<code>SPC p a</code> — e.g. you have multiple <code>__init__.py</code> files"),

    ("Projects", "Compile (build) the current project?",
     "<code>SPC p c</code>"),

    ("Projects", "Run a shell command from the project root?",
     "<code>SPC p !</code>"),

    ("Projects", "Open project root in dired (file browser)?",
     "<code>SPC p D</code>"),

    ("Projects", "Regenerate the project cache (if new files aren't showing)?",
     "<code>SPC p G</code>"),

    ("Projects", "Save all buffers in the project?",
     "<code>SPC p s</code>"),

    ("Projects", "What makes Projectile recognize a directory as a project?",
     "Any VCS directory (<code>.git</code>, <code>.hg</code>) or a <code>.projectile</code> file in the root."),

    # ═══ 10 - GIT (MAGIT) ════════════════════════════════════════════════════════
    ("Magit", "Open the Magit status buffer?",
     "<code>SPC g s</code> — your starting point for all git operations"),

    ("Magit", "Show git blame for current file?",
     "<code>SPC g b</code> — then <code>n</code>/<code>p</code> to navigate commits. <code>RET</code> on a commit to see details."),

    ("Magit", "Stage a change in Magit status?",
     "<code>s</code> on the file/hunk — adds it to the staging area"),

    ("Magit", "Unstage a change?",
     "<code>u</code> on the staged change — removes it from staging"),

    ("Magit", "Commit staged changes?",
     "<code>c c</code> — opens commit message buffer. Write message, then <code>C-c C-c</code> to finalize."),

    ("Magit", "Push to the upstream branch?",
     "<code>P p</code> — push to upstream<br><code>P u</code> — push and set upstream (first push of a branch)"),

    ("Magit", "Pull from upstream (fetch + merge)?",
     "<code>F u</code> — fetch and merge upstream changes<br><code>F r</code> — rebase instead of merge"),

    ("Magit", "Checkout / switch to a branch?",
     "<code>b b</code> — then type branch name"),

    ("Magit", "Create a new branch?",
     "<code>b c</code> — type name, branch created at current HEAD"),

    ("Magit", "View commit log?",
     "<code>l l</code> — then <code>RET</code> on a commit to see details, <code>q</code> to go back"),

    ("Magit", "Toggle visibility of a section?",
     "<code>TAB</code> — hides/shows the diff of that file or hunk"),

    ("Magit", "Stash changes?",
     "<code>z z</code> — stash working tree<br><code>z p</code> — pop most recent stash"),

    ("Magit", "Discard (revert) uncommitted changes to a file?",
     "<code>k</code> on the unstaged file/hunk — confirms then reverts. Irreversible!"),

    ("Magit", "Show a diff of current changes?",
     "<code>d d</code> — show diff of unstaged changes<br><code>d r</code> — show range diff between two commits"),

    ("Magit", "How do you quit Magit?",
     "<code>q</code> — closes the Magit buffer. <code>Q</code> quits and restores previous window layout."),

    # ═══ 11 - ORG MODE ═══════════════════════════════════════════════════════════
    ("OrgMode", "What is Org Mode?",
     "A major mode for notes, TODO lists, project planning, literate programming, and document authoring — all in plain text."),

    ("OrgMode", "Open the Org Agenda (view scheduled tasks)?",
     "<code>SPC a o a</code> — shows your week's scheduled/deadline items across all org files"),

    ("OrgMode", "Quick-capture a TODO or note without breaking flow?",
     "<code>SPC a o c</code> — org-capture: pops up a template form"),

    ("OrgMode", "Cycle visibility of a heading?",
     "<code>TAB</code> — folded → show children → show everything"),

    ("OrgMode", "Cycle global visibility of the whole document?",
     "<code>S-TAB</code> — overview → contents → show all"),

    ("OrgMode", "Insert a new heading at the same level?",
     "<code>M-RET</code> — new heading after current content"),

    ("OrgMode", "Promote / Demote a heading?",
     "<code>M-LEFT</code> — promote (make higher level)<br><code>M-RIGHT</code> — demote (make lower level)"),

    ("OrgMode", "Move a heading / list item up or down?",
     "<code>M-UP</code> — move up<br><code>M-DOWN</code> — move down"),

    ("OrgMode", "Cycle TODO state of a heading?",
     "<code>C-c C-t</code> — TODO → DONE → [blank]"),

    ("OrgMode", "Cycle TODO state forward / backward?",
     "<code>S-RIGHT</code> — forward<br><code>S-LEFT</code> — backward"),

    ("OrgMode", "Schedule a heading for a specific date?",
     "<code>C-c C-s</code> — then pick date with calendar"),

    ("OrgMode", "Set a deadline on a heading?",
     "<code>C-c C-d</code> — then pick date"),

    ("OrgMode", "Insert a timestamp?",
     "<code>C-c .</code> — active (shows in agenda).<br><code>C-c !</code> — inactive (just a note)."),

    ("OrgMode", "Open a link under the cursor?",
     "<code>C-c C-o</code> — opens http/https/files/email links"),

    ("OrgMode", "Insert or edit a hyperlink?",
     "<code>C-c C-l</code> — prompts for link and description"),

    ("OrgMode", "Clock in / Clock out (start/stop time tracking)?",
     "<code>C-c C-x C-i</code> — clock in<br><code>C-c C-x C-o</code> — clock out"),

    ("OrgMode", "Export the org document to another format?",
     "<code>C-c C-e</code> — then choose format: HTML <code>h</code>, LaTeX <code>l</code>, PDF <code>p</code>, Markdown <code>m</code>"),

    ("OrgMode", "Create a table in org mode?",
     "Type <code>|Header|Col2|</code> and press <code>TAB</code> — org formats the table. Press <code>TAB</code> in table to navigate cells."),

    ("OrgMode", "Toggle a checkbox?",
     "<code>C-c C-c</code> — toggles <code>[ ]</code> ↔ <code>[X]</code>"),

    ("OrgMode", "Show a sparse tree filtered by tag or property?",
     "<code>C-c /</code> — then type <code>t</code> for tag, <code>m</code> for property match"),

    ("OrgMode", "What is a capture template?",
     "A pre-defined form for quickly capturing ideas/tasks. Configured in <code>dotspacemacs/user-config</code>. E.g. capture a TODO into your inbox org file without leaving what you're doing."),

    ("OrgMode", "Insert a source code block?",
     "<code>M-x org-insert-structure-template</code> or <code>&lt;s TAB</code> — then type language and <code>TAB</code> to edit."),

    ("OrgMode", "Execute code inside a source block?",
     "<code>C-c C-c</code> — evaluates the block and inserts results below"),

    ("OrgMode", "Narrow to current subtree (hide everything else)?",
     "<code>C-x n s</code> — focus on just this heading<br><code>C-x n w</code> — widen back"),

    # ═══ 12 - HELP SYSTEM ════════════════════════════════════════════════════════
    ("Help", "Search Spacemacs documentation?",
     "<code>SPC h SPC</code> — helm-spacemacs-help: search layers, keybindings, docs"),

    ("Help", "What does a specific function do?",
     "<code>SPC h d f</code> then type function name"),

    ("Help", "What does a specific keybinding do?",
     "<code>SPC h d k</code> then press the key sequence — tells you which command runs"),

    ("Help", "Describe a variable (what's its value, where defined)?",
     "<code>SPC h d v</code> then type variable name"),

    ("Help", "Describe a package (version, status, dependencies)?",
     "<code>SPC h d p</code> then type package name"),

    ("Help", "Describe the current major mode and its keybindings?",
     "<code>SPC h d m</code>"),

    ("Help", "Show all keybindings for the current buffer's modes?",
     "<code>C-h m</code> — full list of active keymaps"),

    ("Help", "Show all available keybindings?",
     "<code>C-h b</code> — complete keybinding list"),

    ("Help", "Go to the source code of a function/variable?",
     "<code>SPC h d S</code> — or <code>SPC h g f</code>"),

    ("Help", "Report a Spacemacs issue?",
     "<code>SPC h I</code> — opens the issue template on GitHub"),

    ("Help", "View the Spacemacs quick-help card?",
     "<code>SPC ?</code> — shows the leader key which-key overview"),

    ("Help", "What package provides a given feature (e.g. completion)?",
     "<code>SPC h d P</code> — describe package by feature name"),

    # ═══ 13 - ELISP BASICS ═══════════════════════════════════════════════════════
    ("Elisp", "What is an s-expression?",
     "A parenthesized list: <code>(function arg1 arg2 ...)</code>. Everything in Lisp is an s-expression."),

    ("Elisp", "How do you define a function?",
     "<code>(defun my-func (arg1 arg2)<br>  \"Doc string.\"<br>  (+ arg1 arg2))</code>"),

    ("Elisp", "How do you set a variable?",
     "<code>(setq my-var 42)</code> — <code>setq</code> sets one or more global variables"),

    ("Elisp", "How do you create local variables?",
     "<code>(let ((x 1) (y 2))<br>  (+ x y))</code><br><code>let*</code> allows later bindings to use earlier ones."),

    ("Elisp", "What is a hook?",
     "A variable holding a list of functions run at a specific time (e.g. after opening a file). Use <code>(add-hook 'python-mode-hook 'flycheck-mode)</code>"),

    ("Elisp", "What is <code>use-package</code>?",
     "A macro for clean package config: <code>(use-package flycheck<br>  :init (global-flycheck-mode)<br>  :config (setq flycheck-checker 'python-flake8))</code>"),

    ("Elisp", "How do you define an anonymous function?",
     "<code>(lambda (x) (* x 2))</code> — call it with <code>(funcall (lambda (x) (* x 2)) 5)</code>"),

    ("Elisp", "How do you call a function stored in a variable?",
     "<code>(funcall some-func arg1 arg2)</code><br><code>(apply some-func '(arg1 arg2))</code> — apply spreads a list into args"),

    ("Elisp", "How do you map a function over a list?",
     "<code>(mapcar #'1+ '(1 2 3))</code> → <code>(2 3 4)</code><br>Use <code>#'func</code> to reference a function by name."),

    ("Elisp", "How do you write a conditional?",
     "<code>(if test then-expr else-expr)</code><br><code>(cond (case1 result1) (case2 result2) (t default))</code>"),

    ("Elisp", "How do you make a function callable by <code>M-x</code>?",
     "Add <code>(interactive)</code> as the first body form. Optional: <code>(interactive \"sEnter name: \")</code> to prompt for args."),

    ("Elisp", "How do you print to the echo area?",
     "<code>(message \"Hello %s\" name)</code> — shows in echo area and <code>*Messages*</code> buffer"),

    ("Elisp", "What is a cons cell?",
     "The fundamental building block of lists. <code>(cons 'a 'b)</code> → <code>(a . b)</code><br><code>car</code> = first, <code>cdr</code> = rest."),

    ("Elisp", "How do you prepend to a list?",
     "<code>(push item my-list)</code> — adds to front and stores back<br><code>(pop my-list)</code> — removes from front"),

    ("Elisp", "How do you iterate over a list?",
     "<code>(dolist (item my-list)<br>  (message \"Got %s\" item))</code>"),

    ("Elisp", "What is a plist (property list)?",
     "<code>(:name \"Alice\" :age 30 :active t)</code><br>Read with <code>(plist-get plist :name)</code> — needs cl-lib loaded."),

    ("Elisp", "What is an alist (association list)?",
     "<code>((\"name\" . \"Alice\") (\"age\" . 30))</code><br>Lookup with <code>(alist-get \"name\" alist nil nil #'equal)</code> or <code>(assoc \"name\" alist)</code>"),

    ("Elisp", "How do you wrap/extend an existing function?",
     "<code>(advice-add 'existing-func :before #'my-before-hook)</code><br><code>:after</code>, <code>:around</code>, <code>:override</code> control when your code runs."),

    ("Elisp", "How do you load a file of elisp code?",
     "<code>(load \"path/to/file.el\")</code><br><code>(require 'feature-name)</code> — loads a package's feature (must be on load-path)"),

    ("Elisp", "How do you evaluate elisp code in a buffer?",
     "<code>C-x C-e</code> — eval last s-expression before point<br><code>C-M-x</code> — eval top-level form (e.g. a defun)<br><code>SPC m e l</code> — eval whole buffer (in emacs-lisp mode)"),

    # ═══ 14 - CONFIG & CUSTOMIZATION ══════════════════════════════════════════════
    ("Config", "Where is the main Spacemacs config file?",
     "<code>~/.spacemacs</code> — a single file with layers, init, and user config"),

    ("Config", "What is <code>dotspacemacs/layers</code>?",
     "The function where you list Spacemacs layers to load. Add or remove layer names here."),

    ("Config", "What is <code>dotspacemacs/user-config</code>?",
     "The function for your personal Emacs config. Runs AFTER all layers are loaded. Put <code>use-package</code>, hooks, custom keybindings here."),

    ("Config", "What is <code>dotspacemacs/user-init</code>?",
     "Code that runs BEFORE layers load. Use for settings that layers may depend on (e.g. <code>(setq python-shell-interpreter \"python3\")</code>)."),

    ("Config", "How do you reload the .spacemacs config?",
     "<code>SPC f e R</code> — syncs and reloads. Or restart with <code>SPC q r</code>."),

    ("Config", "How do you add an external (non-layer) package?",
     "Add it to <code>dotspacemacs-additional-packages</code> list, then configure it in <code>dotspacemacs/user-config</code>."),

    ("Config", "Where do custom (private) layers live?",
     "<code>~/.emacs.d/private/</code> — create your own layers here for reusable config. Declare in <code>dotspacemacs-configuration-layer-path</code>."),

    ("Config", "How do you install/update all Spacemacs packages?",
     "<code>SPC f e U</code> — updates all packages. <code>SPC f e I</code> — installs missing packages based on layers."),

    ("Config", "How do you see which packages are active?",
     "<code>SPC h d p</code> — describe a package. Or <code>SPC a P</code> — list all installed packages."),

    ("Config", "What is <code>dotspacemacs-editing-style</code>?",
     "Set to <code>'vim</code> for evil mode, <code>'emacs</code> for holy mode, or <code>'hybrid</code> for emacs insert mode + normal mode in other states."),

    # ═══ 15 - ADVANCED ════════════════════════════════════════════════════════════
    ("Advanced", "Restart Emacs from within?",
     "<code>SPC q r</code> — restart, keeping open files<br><code>SPC q q</code> — quit<br><code>SPC q Q</code> — quit without saving"),

    ("Advanced", "Open a shell in Emacs?",
     "<code>SPC '</code> — opens a shell in a popup window. Or <code>SPC p '</code> for shell at project root."),

    ("Advanced", "Jump to any visible character (Avy)?",
     "<code>SPC j c</code> — enter character, avy highlights matches, type the label key to jump there"),

    ("Advanced", "Jump to any word (Avy)?",
     "<code>SPC j w</code> — type partial word, labels appear, press label to jump"),

    ("Advanced", "Jump to any line (Avy)?",
     "<code>SPC j l</code> — pick any visible line without counting"),

    ("Advanced", "Record a keyboard macro?",
     "<code>SPC q r</code> (or <code>q r</code> in evil) — starts recording<br><code>SPC q R</code> (or <code>q</code> in evil) — stops<br><code>SPC q q</code> (or <code>@ q</code>) — replay"),

    ("Advanced", "Toggle line numbers?",
     "<code>SPC t n</code> — absolute line numbers<br><code>SPC t N</code> — relative line numbers (vim-style)"),

    ("Advanced", "Toggle syntax checking (flycheck)?",
     "<code>SPC t s</code> — on/off for current buffer<br><code>SPC t S</code> — global toggle"),

    ("Advanced", "Toggle fullscreen?",
     "<code>SPC t F</code> — Linux: <code>F11</code> style fullscreen"),

    ("Advanced", "Indent and align code at a regexp (e.g. <code>=</code>)?",
     "<code>SPC x a e</code> — align at <code>=</code> signs<br><code>SPC x a r</code> — align at arbitrary regexp"),

    ("Advanced", "Edit a file on a remote server via SSH?",
     "<code>SPC f f /ssh:user@host:/path/to/file</code> — TRAMP handles the rest. Also <code>/sudo::/etc/hosts</code> for local root files."),

    ("Advanced", "Open multiple cursors (edit in many places at once)?",
     "<code>SPC v</code> — enter iedit mode for symbol under cursor<br><code>C-'</code> — select next occurrence<br><code>v</code> inside visual — expand region"),

    ("Advanced", "How do you narrow to a region (hide everything else)?",
     "<code>C-x n n</code> — narrow to region<br><code>C-x n w</code> — widen (show everything again)<br><code>C-x n s</code> — narrow to org subtree"),

    ("Advanced", "How do you toggle between two most recent buffers?",
     "<code>SPC TAB</code> — fast flip back and forth (like alt-tab)"),

    ("Advanced", "Open the scratch buffer (throwaway notes / elisp playground)?",
     "<code>SPC b s c</code> — scratch buffer in current mode<br><code>:new</code> — vim-style new empty buffer"),

    ("Advanced", "What is <code>SPC h d s</code>?",
     "Describe a Spacemacs layer — see its documentation, packages, and keybindings."),

    ("Advanced", "What is Helms-Describe-System?",
     "<code>SPC h SPC</code> then type a layer name to see its README, keybindings, and config options."),

    ("Advanced", "How do you edit a file as root (sudo)?",
     "<code>SPC f E</code> then path, or <code>/sudo::/path/to/file</code> via TRAMP."),

    ("Advanced", "What is <code>SPC t h</code>?",
     "Toggle <code>which-key</code> — the hint popup that shows available keys after pressing <code>SPC</code>."),

    ("Advanced", "How do you comment / uncomment a line or region?",
     "<code>SPC c l</code> — toggle comment<br>In evil: <code>gc{motion}</code> — e.g. <code>gcc</code> for current line, <code>gc3j</code> for next 3 lines"),

    ("Advanced", "Show a list of errors/warnings across the project (flycheck)?",
     "<code>SPC e l</code> — helm flycheck error list<br><code>SPC e n</code> / <code>SPC e p</code> — next/previous error"),

    ("Advanced", "How do you show the definition of a symbol (LSP)?",
     "<code>SPC m g g</code> — go to definition<br><code>SPC m g t</code> — go to type definition<br><code>SPC m g r</code> — find references"),

    ("Advanced", "How do you rename a symbol across the project (LSP)?",
     "<code>SPC m r r</code> — rename symbol, LSP updates all references"),

    ("Advanced", "What is a transient state in Spacemacs?",
     "A temporary key mode (like vim's sub-modes). Enter with one key, then single keys do actions until you press another key or ESC. E.g. <code>SPC w .</code> for window resize transient state."),

    ("Advanced", "How do you open the LSP's documentation for symbol at point?",
     "<code>SPC m h h</code> — hover/docs for current symbol<br><code>SPC m h s</code> — display signature help"),
]

# ── Build deck ─────────────────────────────────────────────────────────────────
def build():
    for deck_key, front, back in cards:
        note = genanki.Note(model=model, fields=[front, back], tags=[deck_key])
        decks[deck_key].add_note(note)

    package = genanki.Package(list(decks.values()))
    package.write_to_file(OUTPUT)

    total = len(cards)
    print(f"Built deck: {OUTPUT}")
    print(f"Total cards: {total}")
    print(f"Subdecks: {len(decks)}")

if __name__ == "__main__":
    build()
