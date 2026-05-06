#!/usr/bin/env python3
"""NVIM Zero-to-Hero Anki deck. ~300 cards from first principles to plugin authoring."""

import genanki, random, time

OUTPUT = "/home/senik/Desktop/NVIM_Zero_to_Hero.apkg"

# ── Model ──────────────────────────────────────────────────────────────────────
model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    "NVIM Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "Card",
        "qfmt": '<div class="front">{{Front}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>',
    }],
    css="""
        .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px;
                text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; }
        .front { font-weight: bold; margin-top: 60px; }
        .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
        code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244;
                    padding: 2px 6px; border-radius: 4px; font-size: 18px; }
        hr { border-color: #45475a; }
    """,
)

# ── Decks ──────────────────────────────────────────────────────────────────────
R = lambda: random.randrange(1 << 30, 1 << 31)
decks = {
    "Modes":       genanki.Deck(R(), "NVIM::Zero2Hero::01-Modes-Fundamentals"),
    "Motions":     genanki.Deck(R(), "NVIM::Zero2Hero::02-Motions"),
    "Operators":   genanki.Deck(R(), "NVIM::Zero2Hero::03-Operators-Editing"),
    "TextObjects": genanki.Deck(R(), "NVIM::Zero2Hero::04-Text-Objects"),
    "Search":      genanki.Deck(R(), "NVIM::Zero2Hero::05-Search-Substitute"),
    "RegMacro":    genanki.Deck(R(), "NVIM::Zero2Hero::06-Registers-Macros"),
    "WinBuf":      genanki.Deck(R(), "NVIM::Zero2Hero::07-Windows-Tabs-Buffers"),
    "Files":       genanki.Deck(R(), "NVIM::Zero2Hero::08-Files-Navigation"),
    "LSP":         genanki.Deck(R(), "NVIM::Zero2Hero::09-Neovim-LSP"),
    "Treesitter":  genanki.Deck(R(), "NVIM::Zero2Hero::10-Treesitter"),
    "LuaConfig":   genanki.Deck(R(), "NVIM::Zero2Hero::11-Lua-Config"),
    "Plugins":     genanki.Deck(R(), "NVIM::Zero2Hero::12-Plugins"),
    "Workflows":   genanki.Deck(R(), "NVIM::Zero2Hero::13-Workflows"),
    "Gotchas":     genanki.Deck(R(), "NVIM::Zero2Hero::14-Gotchas"),
    "Advanced":    genanki.Deck(R(), "NVIM::Zero2Hero::15-Advanced"),
}

# ── Cards ──────────────────────────────────────────────────────────────────────
C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ═══ 01 - MODES & FUNDAMENTALS ══════════════════════════════════════════════════

c("Modes", "What is Neovim?",
  "A hyperextensible Vim-based text editor. Forked from Vim in 2014, adds built-in LSP, Treesitter, Lua scripting, and async jobs.",
  ["L0_primitives"])

c("Modes", "What is modal editing?",
  "The same keys do different things depending on which <i>mode</i> you're in — unlike modeless editors where typing always inserts text.",
  ["L0_primitives"])

c("Modes", "What are the 4 core Vim modes?",
  "<b>Normal</b> — navigate & manipulate (default)<br><b>Insert</b> — type text<br><b>Visual</b> — select text<br><b>Command-line</b> — run Ex commands (<code>:</code>)",
  ["L0_primitives"])

c("Modes", "How do you return to Normal mode from any other mode?",
  "<code>ESC</code> or <code>C-[</code> or <code>C-c</code>. Many users remap <code>jk</code> or <code>jj</code> in insert mode as a faster alternative.",
  ["L0_primitives"])

c("Modes", "What is the difference between Vim and Neovim?",
  "Neovim: built-in LSP client, Treesitter parser, Lua as first-class config language, embedded terminal emulator, externalized UI protocol, and a more active community. Vim: broader legacy compatibility, still widely installed as default <code>vi</code>.",
  ["L0_primitives"])

c("Modes", "What is a buffer in Vim?",
  "The in-memory representation of a file. You edit buffers, not files. A file is only read/written when you <code>:e</code> or <code>:w</code>.",
  ["L0_primitives"])

c("Modes", "What is a window in Vim?",
  "A viewport onto a buffer. One buffer can be displayed in multiple windows. Splits create new windows viewing the same or different buffers.",
  ["L0_primitives"])

c("Modes", "What is a tab page in Vim?",
  "A collection of windows. NOT the same as other editors' tabs (which are usually one-file-per-tab). Vim tabs are window layouts.",
  ["L0_primitives"])

c("Modes", "What does <code>:</code> do?",
  "Enters Command-line mode. You can run Ex commands like <code>:w</code> (write), <code>:q</code> (quit), <code>:s/foo/bar/</code> (substitute).",
  ["L0_primitives"])

c("Modes", "What does <code>/</code> do in Normal mode?",
  "Starts a forward search. Type pattern then <code>ENTER</code>. <code>n</code> for next match, <code>N</code> for previous.",
  ["L0_primitives"])

c("Modes", "What is a count in Vim?",
  "A number prefix before a command repeats it. <code>3w</code> moves forward 3 words. <code>5dd</code> deletes 5 lines. Most commands accept counts.",
  ["L0_primitives"])

c("Modes", "What is the Vim 'language'?",
  "<code>[count][operator][motion/text-object]</code> — a composable grammar. <code>d3w</code> means 'delete 3 words'. <code>ci\"</code> means 'change inside quotes'.",
  ["L0_primitives"])

c("Modes", "How do you enter Insert mode?",
  "<code>i</code> — at cursor<br><code>a</code> — after cursor<br><code>I</code> — at start of line<br><code>A</code> — at end of line<br><code>o</code> — new line below<br><code>O</code> — new line above",
  ["L1_mechanics"])

c("Modes", "How do you enter Visual mode?",
  "<code>v</code> — character-wise<br><code>V</code> — line-wise<br><code>C-v</code> — block-wise (columns)",
  ["L1_mechanics"])

c("Modes", "What does <code>gv</code> do?",
  "Reselects the last visual selection — useful when you want to adjust it.",
  ["L1_mechanics"])

c("Modes", "What is Select mode and how does it differ from Visual mode?",
  "In Select mode, typing immediately replaces the selection (like GUI editors). Rarely used intentionally; may appear via snippet plugins. Exit with <code>C-g</code> then <code>ESC</code>.",
  ["L0_primitives"])

c("Modes", "What does <code>R</code> do?",
  "Enter Replace mode — overwrites existing text character by character until you press <code>ESC</code>.",
  ["L1_mechanics"])

c("Modes", "How do you enter Terminal mode in Neovim?",
  "<code>:terminal</code> or <code>:term</code>. Press <code>C-\\ C-n</code> to return to Normal mode while keeping the terminal running.",
  ["L1_mechanics"])

c("Modes", "How do you open a command from the history?",
  "<code>q:</code> — opens the command-line window with history. Navigate with <code>j/k</code>, press <code>ENTER</code> to execute. <code>q/</code> and <code>q?</code> for search history.",
  ["L1_mechanics"])

# ═══ 02 - MOTIONS ═══════════════════════════════════════════════════════════════

c("Motions", "Move cursor left / down / up / right?",
  "<code>h</code> / <code>j</code> / <code>k</code> / <code>l</code>",
  ["L1_mechanics"])

c("Motions", "Move forward / backward one word?",
  "<code>w</code> — start of next word<br><code>b</code> — start of previous word",
  ["L1_mechanics"])

c("Motions", "Move to end of current/next word?",
  "<code>e</code> — end of word<br><code>ge</code> — end of previous word",
  ["L1_mechanics"])

c("Motions", "What's the difference between <code>w</code> and <code>W</code>?",
  "<code>w</code> stops at punctuation and non-word characters (WORD = space-delimited tokens). <code>W</code> jumps to the next whitespace (WORD = anything delimited by spaces).",
  ["L1_mechanics"])

c("Motions", "Go to beginning / end of line?",
  "<code>0</code> — first column<br><code>$</code> — last column<br><code>^</code> — first non-blank<br><code>g_</code> — last non-blank",
  ["L1_mechanics"])

c("Motions", "Find character on current line (forward / backward)?",
  "<code>f{char}</code> forward<br><code>F{char}</code> backward",
  ["L1_mechanics"])

c("Motions", "Find <i>before</i> character on current line (forward / backward)?",
  "<code>t{char}</code> forward (until char)<br><code>T{char}</code> backward (until char)",
  ["L1_mechanics"])

c("Motions", "Repeat last <code>f</code> / <code>t</code> search?",
  "<code>;</code> — forward<br><code>,</code> — backward",
  ["L1_mechanics"])

c("Motions", "Go to first / last line of buffer?",
  "<code>gg</code> — first line<br><code>G</code> — last line",
  ["L1_mechanics"])

c("Motions", "Go to line N?",
  "<code>{N}gg</code> or <code>{N}G</code> or <code>:{N}</code>",
  ["L1_mechanics"])

c("Motions", "Jump to matching bracket/paren?",
  "<code>%</code> — also works with <code>if</code>/<code>end</code> in some filetypes",
  ["L1_mechanics"])

c("Motions", "Jump to previous / next paragraph?",
  "<code>{</code> — previous blank line<br><code>}</code> — next blank line",
  ["L1_mechanics"])

c("Motions", "Jump to previous / next sentence?",
  "<code>(</code> — previous<br><code>)</code> — next",
  ["L1_mechanics"])

c("Motions", "Move to top / middle / bottom of visible window?",
  "<code>H</code> — High<br><code>M</code> — Middle<br><code>L</code> — Low",
  ["L1_mechanics"])

c("Motions", "Page down / up / half-page?",
  "<code>C-f</code> — forward full page<br><code>C-b</code> — backward full page<br><code>C-d</code> — forward half page<br><code>C-u</code> — backward half page",
  ["L1_mechanics"])

c("Motions", "Scroll cursor to top / center / bottom of window?",
  "<code>zt</code> — top<br><code>zz</code> — center<br><code>zb</code> — bottom",
  ["L1_mechanics"])

c("Motions", "Go back / forward in the jump list?",
  "<code>C-o</code> — back<br><code>C-i</code> (or <code>TAB</code>) — forward",
  ["L1_mechanics"])

c("Motions", "What is the jump list?",
  "A history of cursor positions from 'jump' motions (search, <code>G</code>, <code>%</code>, <code>(</code>, <code>)</code>, <code>{</code>, <code>}</code>, <code>L</code>, <code>M</code>, <code>H</code>). NOT regular <code>j/k</code> moves. View with <code>:jumps</code>.",
  ["L2_composition"])

c("Motions", "Go to the last change position?",
  "<code>g;</code> — back through change list<br><code>g,</code> — forward through change list<br><code>`.</code> — go to last edit position</code>",
  ["L1_mechanics"])

c("Motions", "How do you scroll the window without moving the cursor?",
  "<code>C-y</code> — scroll up one line<br><code>C-e</code> — scroll down one line<br>(Think: <code>y</code> pulls text from top, <code>e</code> exposes text at bottom.)",
  ["L1_mechanics"])

c("Motions", "Move to the next method/function start?",
  "<code>]m</code> — next method start<br><code>[m</code> — previous method start<br><code>]M</code> — next method end<br><code>[M</code> — previous method end<br>(Requires filetype support; Treesitter enhances this.)",
  ["L1_mechanics"])

c("Motions", "Move to next/previous misspelled word?",
  "<code>]s</code> — next<br><code>[s</code> — previous<br>(Requires <code>spell</code> enabled.)",
  ["L1_mechanics"])

# ═══ 03 - OPERATORS & EDITING ═══════════════════════════════════════════════════

c("Operators", "What does <code>d</code> do as an operator?",
  "Delete (cut). Takes a motion or text object: <code>dw</code> delete word, <code>dd</code> delete line, <code>d}</code> delete to end of paragraph. Deleted text goes to the unnamed register.",
  ["L1_mechanics"])

c("Operators", "What does <code>c</code> do as an operator?",
  "Change (delete then enter Insert mode). <code>cw</code> change word, <code>cc</code> change entire line, <code>c$</code> change to end of line.",
  ["L1_mechanics"])

c("Operators", "What does <code>y</code> do as an operator?",
  "Yank (copy). <code>yw</code> yank word, <code>yy</code> yank line, <code>y%</code> yank to matching bracket. Stored in registers for pasting.",
  ["L1_mechanics"])

c("Operators", "What does <code>p</code> and <code>P</code> do?",
  "<code>p</code> — paste after cursor (or below current line)<br><code>P</code> — paste before cursor (or above current line)",
  ["L1_mechanics"])

c("Operators", "What does <code>~</code> do?",
  "Toggle case of character under cursor. In Visual mode, toggles case of selection. Combine with motion: <code>g~w</code> toggles case of a word.",
  ["L1_mechanics"])

c("Operators", "What does <code>gu</code> / <code>gU</code> do?",
  "<code>gu</code> — lowercase (motion/text-object)<br><code>gU</code> — uppercase<br>e.g. <code>guiw</code> lowercases current word, <code>gU$</code> uppercases to end of line.",
  ["L1_mechanics"])

c("Operators", "What do <code>&gt;</code> and <code>&lt;</code> do?",
  "Indent right / left. <code>&gt;&gt;</code> indent current line. <code>&gt;3j</code> indent next 3 lines. <code>3&gt;&gt;</code> indent 3 lines. <code>gqip</code>:V supports <code>vip &gt;</code> for indenting a paragraph.",
  ["L1_mechanics"])

c("Operators", "What does <code>=</code> do as an operator?",
  "Auto-indent (reformat). <code>==</code> indent current line. <code>=ip</code> indent inner paragraph. <code>gg=G</code> indent entire file. Depends on <code>'equalprg'</code>.",
  ["L1_mechanics"])

c("Operators", "What does <code>x</code> / <code>X</code> do?",
  "<code>x</code> — delete character under cursor (same as <code>dl</code>)<br><code>X</code> — delete character before cursor (same as <code>dh</code>)",
  ["L1_mechanics"])

c("Operators", "What does <code>s</code> / <code>S</code> do?",
  "<code>s</code> — delete character and enter Insert mode (same as <code>cl</code>)<br><code>S</code> — delete entire line and enter Insert mode (same as <code>cc</code>)",
  ["L1_mechanics"])

c("Operators", "What does <code>r</code> do?",
  "Replace a single character without entering Insert mode. <code>r{char}</code>. Stays in Normal mode afterwards.",
  ["L1_mechanics"])

c("Operators", "What does <code>J</code> do?",
  "Join current line with the next line (adds a space). <code>gJ</code> joins without adding a space. <code>5J</code> joins 5 lines.",
  ["L1_mechanics"])

c("Operators", "What does <code>.</code> (dot) do?",
  "Repeats the last change. Extremely powerful — replay any edit operation. Combine with <code>n</code> to repeat changes across search matches.",
  ["L1_mechanics"])

c("Operators", "What does <code>u</code> / <code>C-r</code> do?",
  "<code>u</code> — undo<br><code>C-r</code> — redo<br>Vim's undo is a tree, not a linear stack. Use <code>:undolist</code> and <code>g-</code>/<code>g+</code> to navigate the tree.",
  ["L1_mechanics"])

c("Operators", "How do you repeat a command on each line in a range?",
  "<code>:g/pattern/normal @q</code> — run macro <code>q</code> on each matching line<br><code>:g/pattern/normal .</code> — repeat last edit on each matching line<br><code>:.,.+10normal I// </code> — comment 10 lines",
  ["L2_composition"])

c("Operators", "What does <code>g~</code>, <code>gu</code>, <code>gU</code> plus a motion do vs using Visual mode?",
  "They ARE operators — they take a motion and act on that range. <code>gUiw</code> uppercases inner word without entering Visual mode. Faster and cleaner — one command, no mode switch.",
  ["L2_composition"])

c("Operators", "What does the <code>!</code> operator do?",
  "Filter text through an external command. <code>!ipsort</code> sorts inner paragraph. <code>!Gjq</code> formats from cursor to end of file as JSON. <code>!!rev</code> reverses current line.",
  ["L2_composition"])

c("Operators", "How do you comment/uncomment with <code>gc</code>?",
  "<code>gc{motion}</code> — toggle comment (requires a plugin or <code>vim-commentary</code>/<code>Comment.nvim</code>). <code>gcc</code> for current line, <code>gcip</code> for paragraph, <code>gc3j</code> for next 3 lines.",
  ["L1_mechanics"])

# ═══ 04 - TEXT OBJECTS ══════════════════════════════════════════════════════════

c("TextObjects", "What is a text object?",
  "A structured unit of text you can operate on. Two forms:<br><code>i{char}</code> — <b>inner</b> (content only, no delimiters)<br><code>a{char}</code> — <b>around</b> (content + delimiters/whitespace)",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside a word?",
  "<code>diw</code> / <code>ciw</code> / <code>yiw</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank a whole word (including trailing space)?",
  "<code>daw</code> / <code>caw</code> / <code>yaw</code><br>Useful when you want to replace a word entirely — <code>caw</code> deletes the word AND the space after it, so the next word doesn't get squished.",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside double quotes?",
  "<code>di\"</code> / <code>ci\"</code> / <code>yi\"</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside single quotes?",
  "<code>di'</code> / <code>ci'</code> / <code>yi'</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside backticks?",
  "<code>di`</code> / <code>ci`</code> / <code>yi`</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside parentheses <code>()</code>?",
  "<code>di(</code> or <code>di)</code> or <code>dib</code><br>(<code>b</code> stands for 'block')",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside curly braces <code>{}</code>?",
  "<code>di{</code> or <code>di}</code> or <code>diB</code><br>(capital <code>B</code> for curly-brace block)",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside square brackets <code>[]</code>?",
  "<code>di[</code> or <code>di]</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside angle brackets <code>&lt;&gt;</code>?",
  "<code>di&lt;</code> or <code>di&gt;</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inside HTML/XML tags?",
  "<code>dit</code> — inner tag (content between tags, not the tags themselves)<br><code>dat</code> — around tag (content + the tags)",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inner paragraph?",
  "<code>dip</code> / <code>cip</code> / <code>yip</code>",
  ["L1_mechanics"])

c("TextObjects", "Delete/Change/Yank inner sentence?",
  "<code>dis</code> / <code>cis</code> / <code>yis</code>",
  ["L1_mechanics"])

c("TextObjects", "How do you operate on the current line without selecting it?",
  "<code>dd</code>, <code>cc</code>, <code>yy</code>, <code>&gt;&gt;</code>, <code>&lt;&lt;</code>, <code>==</code> — doubling the operator acts on the current line. Special case: <code>Y</code> yanks entire line (same as <code>yy</code>).",
  ["L1_mechanics"])

c("TextObjects", "What does <code>dap</code> do vs <code>dip</code>?",
  "<code>dip</code> — delete content of paragraph<br><code>dap</code> — delete paragraph AND the blank line after it (around paragraph)<br>Use <code>dap</code> when you want to completely remove a paragraph.",
  ["L1_mechanics"])

c("TextObjects", "What is the <code>gn</code> text object?",
  "Selects the next search match. <code>cgn</code> changes the next occurrence of the search pattern, then <code>.</code> repeats it on each subsequent match. The premier way to do multi-match changes.",
  ["L2_composition"])

c("TextObjects", "What is the <code>i_</code> / <code>a_</code> text object?",
  "Snake_case word. <code>ci_</code> changes the snake_case word under cursor. Requires Treesitter or a plugin like targets.vim.",
  ["L2_composition"])

# ═══ 05 - SEARCH & SUBSTITUTE ═══════════════════════════════════════════════════

c("Search", "Search forward / backward for a pattern?",
  "<code>/</code> — forward<br><code>?</code> — backward<br>Press <code>ENTER</code> to execute, <code>n</code>/<code>N</code> to jump matches.",
  ["L1_mechanics"])

c("Search", "Search for the word under the cursor?",
  "<code>*</code> — forward for exact word<br><code>#</code> — backward for exact word<br><code>g*</code> — forward (partial match)<br><code>g#</code> — backward (partial match)",
  ["L1_mechanics"])

c("Search", "How do you make a search case-insensitive?",
  "<code>/\\cpattern</code> — <code>\\c</code> makes this specific search case-insensitive<br><code>:set ignorecase</code> — global setting<br><code>:set smartcase</code> — only case-insensitive if pattern is all lowercase",
  ["L1_mechanics"])

c("Search", "Find and replace across the whole file?",
  "<code>:%s/old/new/g</code> — substitute all occurrences<br><code>:%s/old/new/gc</code> — confirm each replacement<br><code>:%s/old/new/</code> — replace first occurrence per line only",
  ["L1_mechanics"])

c("Search", "Replace in a specific line range?",
  "<code>:10,20s/old/new/g</code> — lines 10 through 20<br><code>:.,$s/old/new/g</code> — current line to end<br><code>:'<,'>s/old/new/g</code> — within visual selection (pressed <code>:</code> in Visual mode)",
  ["L1_mechanics"])

c("Search", "Capture groups in substitution?",
  "<code>:%s/\\(foo\\)\\(bar\\)/\\2\\1/g</code> — swap foo and bar<br>With <code>:set magic</code> (default): no need to escape parens — <code>:%s/(foo)(bar)/\\2\\1/g</code><br>With very-magic: <code>:%s/\\v(foo)(bar)/\\2\\1/g</code>",
  ["L1_mechanics"])

c("Search", "What is <code>:g</code> (global command)?",
  "<code>:g/pattern/command</code> — execute command on every line matching pattern<br><code>:g/TODO/p</code> — print all TODO lines<br><code>:g/^$/d</code> — delete all blank lines<br><code>:v/pattern/command</code> — match lines NOT containing pattern</code>",
  ["L1_mechanics"])

c("Search", "How do you run a normal-mode command on every matching line?",
  "<code>:g/pattern/normal @q</code> — replay macro q<br><code>:g/pattern/normal A;</code> — append semicolon to matching lines<br><code>:g/func/normal ==</code> — reindent all lines containing 'func'",
  ["L2_composition"])

c("Search", "What is <code>:sor</code> / <code>:sort</code>?",
  "Sort lines in range alphabetically. <code>:sort u</code> sorts and removes duplicates. <code>:sort n</code> sorts numerically. <code>:'<,'>sort</code> sorts visual selection.",
  ["L1_mechanics"])

c("Search", "How do you highlight all occurrences of a word (without searching)?",
  "<code>:set hlsearch</code> enables highlight, then use <code>*</code> or <code>/</code>. To clear highlights: <code>:nohlsearch</code> or <code>:noh</code>. Map <code>:noh</code> to <code>ESC</code> for automatic clearing.",
  ["L1_mechanics"])

c("Search", "How do you search and replace keeping the case of the original?",
  "Use <code>\\u</code> and <code>\\l</code>:<br><code>:%s/hello/\\u&amp;/g</code> — replaces hello with Hello<br><code>\\U</code> and <code>\\L</code> make everything after uppercase/lowercase until <code>\\E</code>.",
  ["L2_composition"])

c("Search", "How do you use very-magic mode in search patterns?",
  "<code>/\\vpattern</code> — very magic mode: all characters except <code>a-zA-Z0-9_</code> are special<br><code>/\\Vpattern</code> — very nomagic: only <code>\\</code> is special<br>Use <code>\\v</code> for regex-heavy patterns to avoid backslash hell.",
  ["L1_mechanics"])

# ═══ 06 - REGISTERS & MACROS ════════════════════════════════════════════════════

c("RegMacro", "What is a register in Vim?",
  "A named storage slot for yanked/deleted text, macros, or bookmarks. 26 named registers (<code>a</code>–<code>z</code>), plus numbered registers (<code>0</code>–<code>9</code>) and special registers (<code>\"</code>, <code>+</code>, <code>*</code>, <code>/</code>, <code>.</code>, <code>%</code>, <code>:</code>).",
  ["L1_mechanics"])

c("RegMacro", "How do you yank/delete to a specific register?",
  "<code>\"ayy</code> — yank line to register <code>a</code><br><code>\"bdd</code> — delete line to register <code>b</code><br>Prefix the command with <code>\"{reg}</code>.",
  ["L1_mechanics"])

c("RegMacro", "How do you paste from a specific register?",
  "<code>\"ap</code> — paste from register <code>a</code> after cursor<br><code>\"bP</code> — paste from register <code>b</code> before cursor<br>In Insert mode: <code>C-r {reg}</code> pastes the register.",
  ["L1_mechanics"])

c("RegMacro", "What's in register <code>0</code> vs register <code>\"</code> (unnamed)?",
  "<code>\"</code> — last yank OR delete<br><code>0</code> — last yank ONLY (never overwritten by deletes)<br>Use <code>\"0p</code> to paste the last yank even after deleting something.",
  ["L1_mechanics"])

c("RegMacro", "How do you copy to the system clipboard?",
  "<code>\"+y</code> — yank to clipboard register<br><code>\"+p</code> — paste from clipboard<br>Register <code>+</code> is the X11/Windows clipboard. Register <code>*</code> is the X11 primary selection.",
  ["L1_mechanics"])

c("RegMacro", "How do you view the contents of all registers?",
  "<code>:registers</code> or <code>:reg</code>. <code>:reg abc</code> shows only registers a, b, and c.",
  ["L1_mechanics"])

c("RegMacro", "How do you record a macro?",
  "<code>q{reg}</code> starts recording to register <code>{reg}</code>. Status line shows 'recording @{reg}'. <code>q</code> stops recording. Play back with <code>@{reg}</code>. Repeat last macro with <code>@@</code>.",
  ["L1_mechanics"])

c("RegMacro", "How do you replay a macro N times?",
  "<code>{N}@{reg}</code> — e.g. <code>100@q</code> replays macro <code>q</code> 100 times. Use with caution — macros run fast.",
  ["L1_mechanics"])

c("RegMacro", "How do you run a macro on multiple lines?",
  "Method 1: <code>{N}@@</code><br>Method 2: <code>:g/pattern/normal! @q</code><br>Method 3: Visual select lines, then <code>:normal @q</code><br>Always end macros with motion to the next line (<code>j</code> or <code>+</code>) for line-wise iteration.",
  ["L2_composition"])

c("RegMacro", "How do you edit a recorded macro?",
  "<code>:let @q='&lt;C-r&gt;&lt;C-r&gt;q'</code> in Insert mode, or:<br>1. Paste the macro: <code>\"qp</code><br>2. Edit the text<br>3. Yank it back: <code>\"qy$</code> or  <code>\"qyy</code><br>The register now contains the edited macro.",
  ["L2_composition"])

c("RegMacro", "What are expression registers?",
  "<code>\"=</code> — lets you evaluate an expression inline. In Insert mode, <code>C-r = 2*21 ENTER</code> inserts 42. In Normal mode, <code>\"=system('date') p</code> pastes the current date.",
  ["L2_composition"])

c("RegMacro", "What is the <code>:</code> register?",
  "Stores the last Ex command. View with <code>:reg :</code>. Replay with <code>@:</code>. <code>@@</code> after <code>@:</code> replays the last Ex command.",
  ["L1_mechanics"])

c("RegMacro", "What is the <code>/</code> register?",
  "Stores the last search pattern. Paste with <code>\"/p</code>. Edit by typing <code>/</code> then <code>C-r /</code> to insert the previous pattern for modification.",
  ["L1_mechanics"])

c("RegMacro", "What is the difference between <code>\"+</code> and <code>\"*</code> (clipboard registers)?",
  "<code>\"+</code> — CLIPBOARD (Ctrl+C/Ctrl+V) on all platforms<br><code>\"*</code> — PRIMARY selection (middle-click paste) on X11 Linux; same as clipboard on macOS/Windows<br>On Linux, use <code>\"+y</code> for Ctrl+V compatible copying.",
  ["L1_mechanics"])

# ═══ 07 - WINDOWS, TABS, BUFFERS ═══════════════════════════════════════════════

c("WinBuf", "Split window horizontally / vertically?",
  "<code>:split</code> or <code>:sp</code> — horizontal (stacks)<br><code>:vsplit</code> or <code>:vs</code> — vertical (side by side)<br><code>C-w s</code> / <code>C-w v</code> — same from Normal mode<br>Both open the current buffer in the new window by default.",
  ["L1_mechanics"])

c("WinBuf", "Navigate between windows?",
  "<code>C-w h/j/k/l</code> — move to window left/down/up/right<br><code>C-w w</code> — cycle forward<br><code>C-w W</code> — cycle backward<br><code>C-w p</code> — go to previous window (toggle between two)",
  ["L1_mechanics"])

c("WinBuf", "Close / resize windows?",
  "<code>C-w q</code> or <code>:q</code> — close current window<br><code>C-w o</code> or <code>:only</code> — close all other windows<br><code>C-w =</code> — equalize all sizes<br><code>C-w &gt;</code> / <code>C-w &lt;</code> — increase/decrease width<br><code>C-w +</code> / <code>C-w -</code> — increase/decrease height",
  ["L1_mechanics"])

c("WinBuf", "How do you move a window to a different position?",
  "<code>C-w H</code> — move to far left<br><code>C-w J</code> — move to very bottom<br><code>C-w K</code> — move to very top<br><code>C-w L</code> — move to far right<br><code>C-w r</code> — rotate windows<br><code>C-w x</code> — exchange with next window",
  ["L1_mechanics"])

c("WinBuf", "What's the difference between <code>:bnext</code> and <code>C-w w</code>?",
  "<code>:bnext</code> / <code>:bprev</code> switch buffers in the current window.<br><code>C-w w</code> moves your cursor to another window (which may show the same or a different buffer).",
  ["L1_mechanics"])

c("WinBuf", "How do you open a file in a new split?",
  "<code>:sp file.txt</code> — horizontal split<br><code>:vs file.txt</code> — vertical split<br><code>:tabnew file.txt</code> — open in new tab page",
  ["L1_mechanics"])

c("WinBuf", "Navigate between tabs?",
  "<code>gt</code> — next tab<br><code>gT</code> — previous tab<br><code>{N}gt</code> — go to tab N<br><code>:tabs</code> — list all tabs",
  ["L1_mechanics"])

c("WinBuf", "How do you move the current window to a new tab?",
  "<code>C-w T</code> — moves current window to its own tab<br><code>:tab split</code> — opens current buffer in a new tab (keeps original window)",
  ["L1_mechanics"])

c("WinBuf", "List all open buffers and switch?",
  "<code>:ls</code> or <code>:buffers</code> — list buffers with numbers<br><code>:b{N}</code> — switch to buffer number N<br><code>:b part_of_name</code> — switch by partial name (TAB-completes)<br>Install a fuzzy finder (Telescope/fzf) for a modern interface.",
  ["L1_mechanics"])

c("WinBuf", "Delete (close) a buffer?",
  "<code>:bd</code> — delete current buffer (closes its window if it's the last one)<br><code>:bd N</code> — delete buffer N<br><code>:%bd</code> — delete ALL buffers (nuclear option)",
  ["L1_mechanics"])

c("WinBuf", "What is a hidden buffer?",
  "A buffer with unsaved changes that's not displayed in any window. <code>:set hidden</code> allows switching buffers without saving. Otherwise Vim forces <code>:w</code> before leaving a modified buffer.",
  ["L2_composition"])

c("WinBuf", "What is the argument list?",
  "A subset of buffers — the files you opened Vim with (or set via <code>:args</code>). <code>:n</code> / <code>:prev</code> go to next/prev in args. <code>:argdo %s/foo/bar/g | update</code> run commands across all arg files.",
  ["L2_composition"])

c("WinBuf", "What is <code>vim.wo</code> vs <code>vim.bo</code> vs <code>vim.o</code> in Lua?",
  "<code>vim.o</code> — global options<br><code>vim.bo</code> — buffer-local options<br><code>vim.wo</code> — window-local options<br><code>vim.go</code> — global-local options (get the global default)",
  ["L3_design"])

# ═══ 08 - FILES & NAVIGATION ════════════════════════════════════════════════════

c("Files", "Open a file?",
  "<code>:e path/to/file</code> — open for editing (completes with TAB)<br><code>:e .</code> — open netrw file browser (built-in)<br><code>:E</code> — open in horizontal split<br><code>:Ve</code> — open in vertical split",
  ["L1_mechanics"])

c("Files", "Save a file?",
  "<code>:w</code> — write current buffer<br><code>:w filename</code> — save as (like 'Save As...')<br><code>:wa</code> — write ALL changed buffers<br><code>:w !sudo tee %</code> — write as root when you forgot <code>sudo vim</code>",
  ["L1_mechanics"])

c("Files", "Quit Vim?",
  "<code>:q</code> — quit (fails if unsaved changes)<br><code>:q!</code> — quit discarding changes<br><code>:wq</code> or <code>:x</code> — write and quit<br><code>:qa</code> — quit all tabs/windows<br><code>ZQ</code> — quit without saving (same as <code>:q!</code>)",
  ["L1_mechanics"])

c("Files", "How do you reload a file (discard unsaved changes)?",
  "<code>:e!</code> — reload current buffer from disk, discarding changes<br><code>:e!</code> is also a handy 'reset this buffer to saved state' shortcut.",
  ["L1_mechanics"])

c("Files", "Open a file under the cursor?",
  "<code>gf</code> — go to file (opens the file whose path is under the cursor)<br><code>C-w gf</code> — open in new tab<br><code>C-w f</code> — open in new horizontal split<br>Set <code>:set path+=**</code> to search subdirectories.",
  ["L1_mechanics"])

c("Files", "What's the difference between <code>:e</code> and <code>:b</code>?",
  "<code>:e file</code> — read file from disk into a buffer (creates new or reuses)<br><code>:b file</code> — switch to an already-loaded buffer (fails if not loaded)<br>Use <code>:e</code> to open files, <code>:b</code> to switch between open buffers.",
  ["L1_mechanics"])

c("Files", "How do you change the current working directory?",
  "<code>:cd path</code> — change directory (global)<br><code>:lcd path</code> — local to current window<br><code>:tcd path</code> — local to current tab<br><code>:pwd</code> — print working directory",
  ["L1_mechanics"])

c("Files", "How do you change directory to the current file's location?",
  "<code>:cd %:h</code> — cd to the directory of the current file<br><code>%</code> expands to current filename, <code>:h</code> is the 'head' (dirname) modifier.",
  ["L1_mechanics"])

c("Files", "How do you edit a file on a remote server?",
  "Neovim doesn't have built-in remote editing like Vim's netrw. Use a plugin or workflow:<br>1. <code>rsync</code> / <code>sshfs</code> to mount remote<br>2. Use <code>oil.nvim</code> with <code>ssh://</code> URLs<br>3. Edit locally + <code>rsync</code> on save (vim-auto-save + rsync)<br>4. Run nvim directly on the server and use <code>mosh</code>/<code>tmux</code>",
  ["L3_design"])

c("Files", "What are filename modifiers like <code>%:h</code>?",
  "Modifiers extract parts of a filename:<br><code>:p</code> — full path<br><code>:h</code> — head (dirname)<br><code>:t</code> — tail (basename)<br><code>:r</code> — root (remove extension)<br><code>:e</code> — extension only<br>e.g. for <code>~/src/main.go</code>: <code>%:p:h</code> = <code>~/src/</code>, <code>%:t:r</code> = <code>main</code>",
  ["L1_mechanics"])

c("Files", "What is netrw?",
  "Vim/Neovim's built-in file explorer. Opens with <code>:e .</code> or <code>:Explore</code>. Navigate with <code>j/k</code>, open with <code>ENTER</code>, create file with <code>%</code>, create dir with <code>d</code>, rename with <code>R</code>, delete with <code>D</code>.",
  ["L1_mechanics"])

# ═══ 09 - NEOWIM LSP ════════════════════════════════════════════════════════════

c("LSP", "What is LSP and how does Neovim support it?",
  "Language Server Protocol — an IDE protocol for go-to-definition, autocomplete, diagnostics, hover, and refactoring. Neovim has a built-in LSP client (since 0.5). You configure servers via <code>nvim-lspconfig</code> and install them with <code>mason.nvim</code>.",
  ["L0_primitives"])

c("LSP", "How do you set up an LSP server in Neovim (Lua)?",
  "<code>local lspconfig = require('lspconfig')<br>lspconfig.rust_analyzer.setup({})<br>lspconfig.pyright.setup({})</code><br>Add keymaps in the <code>on_attach</code> callback for go-to-def, rename, hover, etc.",
  ["L3_design"])

c("LSP", "Go to definition / type definition / implementation?",
  "<code>gd</code> — go to definition<br><code>gD</code> — go to declaration<br><code>gi</code> — go to implementation<br><code>gy</code> — go to type definition<br>(These are the recommended keymaps set up in on_attach.)",
  ["L1_mechanics"])

c("LSP", "How do you rename a symbol across the project?",
  "<code>:lua vim.lsp.buf.rename()</code> — prompts for new name, LSP renames all references. Commonly mapped to <code>&lt;leader&gt;rn</code> or <code>grn</code>.",
  ["L1_mechanics"])

c("LSP", "Show documentation / signature help for symbol under cursor?",
  "<code>K</code> — hover (show docs in floating window)<br><code>C-k</code> — signature help (function parameters)<br>Press <code>K</code> again in the hover window to jump into it and scroll.",
  ["L1_mechanics"])

c("LSP", "Find all references to the symbol under cursor?",
  "<code>grr</code> — adds all references to the quickfix list<br>Navigate with <code>:cnext</code> / <code>:cprev</code> or use Telescope's LSP references picker.",
  ["L1_mechanics"])

c("LSP", "Show diagnostics (errors/warnings) for the current file?",
  "<code>:lua vim.diagnostic.open_float()</code> — show diagnostic under cursor<br><code>[d</code> / <code>]d</code> — previous/next diagnostic<br><code>&lt;leader&gt;e</code> — toggle diagnostic list (Telescope/fzf-lua)",
  ["L1_mechanics"])

c("LSP", "How do you see all workspace diagnostics?",
  "<code>:Telescope diagnostics</code> or <code>:lua vim.diagnostic.setqflist()</code> — populates the quickfix list with all diagnostics across the workspace.",
  ["L1_mechanics"])

c("LSP", "Code actions (quick fix, organize imports, etc.)?",
  "<code>:lua vim.lsp.buf.code_action()</code> — shows available code actions. Commonly mapped to <code>&lt;leader&gt;ca</code>.",
  ["L1_mechanics"])

c("LSP", "Format the current buffer with LSP?",
  "<code>:lua vim.lsp.buf.format()</code> — formats buffer using the attached LSP server. Map to <code>&lt;leader&gt;f</code>. To format on save: use an autocmd <code>BufWritePre</code>.",
  ["L1_mechanics"])

c("LSP", "What is <code>on_attach</code> in LSP config?",
  "A callback that fires when an LSP server attaches to a buffer. This is where you define buffer-local keymaps for LSP commands. Example:<br><code>on_attach = function(client, bufnr)<br>  local opts = { buffer = bufnr }<br>  vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)<br>end</code>",
  ["L3_design"])

c("LSP", "What is <code>mason.nvim</code> and why use it?",
  "A package manager for LSP servers, linters, and formatters. Instead of installing <code>rust-analyzer</code> manually, you <code>:MasonInstall rust-analyzer</code>. Integrates with <code>mason-lspconfig.nvim</code> to auto-setup installed servers.",
  ["L3_design"])

c("LSP", "How do you auto-format on save with LSP?",
  "<code>vim.api.nvim_create_autocmd('BufWritePre', {<br>  pattern = '*',<br>  callback = function() vim.lsp.buf.format({ async = false }) end<br>})</code><br>Use <code>async = true</code> for non-blocking format (default in Neovim 0.10+).",
  ["L3_design"])

c("LSP", "How do you configure LSP capabilities (snippets, folding)?",
  "<code>local capabilities = vim.lsp.protocol.make_client_capabilities()<br>capabilities = require('cmp_nvim_lsp').default_capabilities(capabilities)<br>lspconfig.server.setup({ capabilities = capabilities })</code><br>This enables snippet support in autocompletion plugins like <code>nvim-cmp</code>.",
  ["L3_design"])

# ═══ 10 - TREESITTER ════════════════════════════════════════════════════════════

c("Treesitter", "What is Treesitter in Neovim?",
  "A parser library that builds a concrete syntax tree (CST) for your code. Enables precise syntax highlighting, structural text objects, smart indentation, and incremental selection based on the actual grammar of the language.",
  ["L0_primitives"])

c("Treesitter", "How do you enable Treesitter-based highlighting?",
  "<code>require('nvim-treesitter.configs').setup({<br>  highlight = { enable = true },<br>  ensure_installed = { 'lua', 'python', 'rust', 'typescript' }<br>})</code><br>Run <code>:TSInstall language</code> to add grammars. <code>:TSUpdate</code> to update all.",
  ["L3_design"])

c("Treesitter", "What Treesitter-based text objects are available?",
  "<code>@function.outer</code> — select entire function<br><code>@function.inner</code> — select function body<br><code>@class.outer</code> — select class<br><code>@parameter.inner</code> — select a parameter<br><code>@loop.outer</code> — select loop block<br>Requires <code>nvim-treesitter-textobjects</code>. Map like: <code>vif</code> = <code>@function.inner</code>.",
  ["L2_composition"])

c("Treesitter", "How do you incrementally select a larger AST node?",
  "With <code>nvim-treesitter</code>: press <code>v</code> to select, then <code>+</code> expands to parent node, <code>-</code> shrinks to child node. Continue pressing to walk the syntax tree.",
  ["L2_composition"])

c("Treesitter", "What is <code>:InspectTree</code>?",
  "Opens an interactive tree view of the syntax tree for the current buffer. Navigate the tree with <code>j/k</code>, see node types, ranges, and field names. Invaluable for writing custom Treesitter queries.",
  ["L2_composition"])

c("Treesitter", "How does Treesitter folding work?",
  "Add <code>fold = { enable = true }</code> to treesitter config. Then use <code>zc</code> to close, <code>zo</code> to open, <code>za</code> to toggle folds. Folds are based on actual code structure (functions, blocks), not just indentation.",
  ["L2_composition"])

c("Treesitter", "How do you write a custom Treesitter query?",
  "Queries are S-expressions in <code>~/.config/nvim/after/queries/{lang}/</code>:<br><code>(function_declaration name: (identifier) @function.name)</code><br>Put cursor on a node in <code>:InspectTree</code> to find the node type, then write the query.",
  ["L6_innovation"])

c("Treesitter", "What's the performance cost of Treesitter?",
  "Minimal for most files. Large files (10k+ lines) may feel sluggish. Use <code>:TSBufDisable highlight</code> for specific buffers. Treesitter parsers run in C and are generally fast. The bigger cost is the initial parsing of very large files.",
  ["L3_design"])

# ═══ 11 - LUA CONFIG ═════════════════════════════════════════════════════════════

c("LuaConfig", "Where is the Neovim config directory?",
  "<code>~/.config/nvim/</code> — the standard XDG path<br>Entry point: <code>~/.config/nvim/init.lua</code> (Lua) or <code>~/.config/nvim/init.vim</code> (Vimscript)<br>Check with: <code>:echo stdpath('config')</code>",
  ["L1_mechanics"])

c("LuaConfig", "How do you set an option in Lua vs Vimscript?",
  "Vimscript: <code>set number relativenumber</code><br>Lua: <code>vim.opt.number = true</code> and <code>vim.opt.relativenumber = true</code><br><code>vim.opt</code> wraps Vim options with a Lua-friendly interface (lists are tables, string options are strings).",
  ["L1_mechanics"])

c("LuaConfig", "How do you create a keymap in Lua?",
  "<code>vim.keymap.set('n', '&lt;leader&gt;w', ':w&lt;CR&gt;', { desc = 'Save file' })</code><br>Modes: <code>'n'</code> normal, <code>'i'</code> insert, <code>'v'</code> visual, <code>'t'</code> terminal. The <code>desc</code> field is shown by which-key. <code>vim.keymap.set</code> replaces <code>vim.api.nvim_set_keymap</code> (Neovim 0.7+).",
  ["L3_design"])

c("LuaConfig", "What is <code>&lt;leader&gt;</code> and how do you set it?",
  "The leader key is a prefix for custom keybindings. Default: <code>\\</code>. Most users set it to <code>Space</code>:<br><code>vim.g.mapleader = ' '</code> (must be set BEFORE any <code>&lt;leader&gt;</code> mappings).",
  ["L1_mechanics"])

c("LuaConfig", "How do you structure a modular Lua config?",
  "Common pattern:<br><code>~/.config/nvim/<br>├── init.lua          (entry point)<br>├── lua/<br>│   ├── options.lua   (vim.opt settings)<br>│   ├── keymaps.lua   (vim.keymap)<br>│   ├── plugins.lua   (lazy.nvim spec)<br>│   └── lsp.lua       (LSP config)<br>└── after/<br>    └── ftplugin/     (filetype-specific settings)</code><br>Use <code>require('module')</code> to load modules.",
  ["L3_design"])

c("LuaConfig", "What is <code>vim.g</code> vs <code>vim.b</code> vs <code>vim.w</code>?",
  "<code>vim.g</code> — global variable (equivalent to <code>g:</code> in Vimscript)<br><code>vim.b</code> — buffer-local variable (<code>b:</code>)<br><code>vim.w</code> — window-local variable (<code>w:</code>)<br><code>vim.env</code> — environment variable ($HOME)<br>Use <code>vim.g.mapleader</code> for the leader key.",
  ["L1_mechanics"])

c("LuaConfig", "How do you create an autocommand in Lua?",
  "<code>vim.api.nvim_create_autocmd('FileType', {<br>  pattern = 'python',<br>  callback = function() vim.opt.tabstop = 4 end<br>})</code><br>Or use <code>:h nvim_create_augroup</code> for grouped autocommands. Modern alternative: <code>vim.api.nvim_create_autocmd</code> (0.7+).",
  ["L3_design"])

c("LuaConfig", "How do you create a user command in Lua?",
  "<code>vim.api.nvim_create_user_command('MyCmd', function(args)<br>  print('Args:', args.args)<br>end, { nargs = '?' })</code><br>Then use <code>:MyCmd hello</code>. Options: <code>nargs</code>, <code>range</code>, <code>bang</code>, <code>complete</code>.",
  ["L3_design"])

c("LuaConfig", "What is <code>vim.tbl_deep_extend</code>?",
  "Merges tables recursively — like <code>Object.assign</code> with deep merging. Essential for composing plugin config:<br><code>vim.tbl_deep_extend('force', defaults, user_opts)</code><br><code>'force'</code> means user_opts override defaults completely.",
  ["L3_design"])

c("LuaConfig", "How do you conditionally load a plugin config?",
  "In lazy.nvim: <code>{ 'plugin/name', cond = vim.fn.executable('some-tool') == 1 }</code><br>In packer: use <code>cond</code> option<br>You can also wrap <code>require</code> in <code>pcall</code> for safe loading: <code>local ok, mod = pcall(require, 'optional-plugin')</code>",
  ["L3_design"])

# ═══ 12 - PLUGINS ════════════════════════════════════════════════════════════════

c("Plugins", "What is <code>lazy.nvim</code>?",
  "The current standard Neovim plugin manager. Features: lazy-loading, lockfile for reproducible installs, a beautiful UI, profile startuptime, and extensible specs. Replaces packer.nvim, vim-plug, etc.",
  ["L3_design"])

c("Plugins", "How do you install a plugin with lazy.nvim?",
  "<code>return {<br>  'username/repo',<br>  event = 'VeryLazy',<br>  config = function()<br>    require('plugin').setup({})<br>  end<br>}</code><br>Place this in a <code>.lua</code> file under <code>~/.config/nvim/lua/plugins/</code>.",
  ["L3_design"])

c("Plugins", "What does <code>event = 'VeryLazy'</code> mean in lazy.nvim?",
  "The plugin loads after the UI is rendered, making startup faster. Good for most non-essential plugins. Use <code>event = 'InsertEnter'</code> for completion plugins, <code>event = 'BufRead'</code> for filetype-specific plugins, or <code>cmd = 'CommandName'</code> for command-triggered loading.",
  ["L3_design"])

c("Plugins", "What is Telescope and why use it?",
  "The premier fuzzy finder for Neovim. Find files, grep text, search buffers, browse LSP references, git status, and more — all with live preview. Replaces fzf.vim, CtrlP, and most single-purpose search plugins.",
  ["L3_design"])

c("Plugins", "Key Telescope commands?",
  "<code>&lt;leader&gt;ff</code> — find files<br><code>&lt;leader&gt;fg</code> — live grep<br><code>&lt;leader&gt;fb</code> — find buffers<br><code>&lt;leader&gt;fh</code> — help tags<br><code>&lt;leader&gt;fr</code> — old files (recent)<br>Customize these to your preferred keymap scheme.",
  ["L1_mechanics"])

c("Plugins", "How do you ripgrep with Telescope?",
  "<code>:Telescope live_grep</code> — search as you type across the project. Use <code>C-space</code> to multi-select results, then <code>C-q</code> to send selected results to the quickfix list. Requires <code>ripgrep</code> installed on the system.",
  ["L1_mechanics"])

c("Plugins", "What is <code>nvim-cmp</code>?",
  "A completion engine. Sources: LSP completions, buffer words, path, snippets, copilot, etc. Configure with <code>sources</code> to choose which providers feed the completion menu. Replaces <code>compe.nvim</code>, <code>coc.nvim</code>.",
  ["L3_design"])

c("Plugins", "What is the standard Neovim 'starter' config for 2024+?",
  "<b>LazyVim</b> — a pre-configured distribution based on lazy.nvim<br><b>NvChad</b> — another popular distro with a different aesthetic<br><b>kickstart.nvim</b> — minimal, well-commented init.lua to build from<br><b>AstroNvim</b> — feature-heavy community distro<br>Start with kickstart if you want to understand every line. Start with LazyVim if you want batteries included.",
  ["L5_opinion"])

c("Plugins", "What is <code>which-key.nvim</code>?",
  "Shows available keybindings after a pause or after pressing the leader key. Essential for discovering and remembering custom mappings. Built into LazyVim. Install standalone with lazy.nvim.",
  ["L2_composition"])

c("Plugins", "What does <code>gitsigns.nvim</code> do?",
  "Shows git diff markers in the sign column (added/modified/removed lines). Also provides hunks: <code>]c</code>/<code>[c</code> to jump, <code>&lt;leader&gt;hs</code> to stage hunk, <code>&lt;leader&gt;hr</code> to reset hunk. Lightweight alternative to full vim-fugitive for line-level git operations.",
  ["L2_composition"])

c("Plugins", "What is <code>harpoon.nvim</code>?",
  "A quick file switcher for your 4–5 most-used files in a session. Mark a file with <code>&lt;leader&gt;a</code>, jump to it with <code>&lt;leader&gt;1-5</code>. Faster than Telescope for repetitive file-access patterns (e.g., switching between controller/model/views).",
  ["L5_opinion"])

c("Plugins", "What is <code>nvim-autopairs</code>?",
  "Auto-closes brackets, quotes, and parentheses. Also handles deleting paired characters intelligently. Lighter and faster than earlier autopair plugins.",
  ["L3_design"])

c("Plugins", "How do you keep plugin versions reproducible?",
  "Lazy.nvim generates a <code>lazy-lock.json</code>. Commit it to your dotfiles repo. On a new machine, <code>:Lazy restore</code> installs the exact same versions. This prevents 'it worked yesterday' bugs.",
  ["L4_diagnosis"])

# ═══ 13 - WORKFLOWS ══════════════════════════════════════════════════════════════

c("Workflows", "What is the optimal Vim way to bulk-rename words?",
  "1. <code>*</code> on the word (highlights all)<br>2. <code>cgn{new_name}ESC</code> (change next occurrence)<br>3. <code>.</code> to repeat on each subsequent match<br>Or <code>:%s/\\&lt;old_word\\&gt;/new_name/gc</code> for interactive confirmation.",
  ["L2_composition"])

c("Workflows", "How do you indent / reflow a paragraph of text?",
  "<code>gqip</code> — format inner paragraph to <code>textwidth</code><br><code>gwip</code> — same but preserves cursor position<br>Set <code>:set textwidth=80</code> for the desired line length.",
  ["L2_composition"])

c("Workflows", "How do you sort CSS properties or method definitions?",
  "Visual-select the block, then <code>:sort</code> (alphabetical) or <code>:sort n</code> (numeric). For CSS properties, a dedicated plugin like <code>css-sort.nvim</code> provides smarter sorting.",
  ["L2_composition"])

c("Workflows", "What's the quickfix list workflow for refactoring?",
  "1. <code>:grep</code> or <code>:vim</code> to populate the quickfix list<br>2. <code>:copen</code> to view the list<br>3. <code>:cnext</code> / <code>:cprev</code> to navigate<br>4. Edit each location, <code>:cn</code> to go next<br>5. <code>:cdo s/old/new/g | update</code> to apply substitution to ALL quickfix entries",
  ["L2_composition"])

c("Workflows", "What's the <code>:argdo</code> workflow?",
  "1. <code>:args **/*.py</code> — populate arglist with Python files<br>2. <code>:argdo %s/foo/bar/g | update</code> — substitute in all<br>3. <code>:argdo normal @q</code> — replay macro on all<br>Works on the argument list (subset of buffers), not all open files.",
  ["L2_composition"])

c("Workflows", "How do you diff two splits?",
  "<code>:windo diffthis</code> — diff all visible windows<br><code>:diffoff</code> — stop diffing<br>Or open two files in splits: <code>vim -d file1 file2</code> or <code>nvim -d file1 file2</code> for side-by-side diff.",
  ["L2_composition"])

c("Workflows", "How do you edit a column of text (visual block)?",
  "<code>C-v</code> to select the column, then <code>I</code> to insert at the start of each line (or <code>A</code> to append, <code>c</code> to change). The change appears on the first line but applies to ALL selected lines when you press <code>ESC</code>.",
  ["L2_composition"])

c("Workflows", "How do you open the file path under the cursor in a reasonable way?",
  "<code>gf</code> if the path is relative to current file<br><code>gF</code> if the path includes a line number (<code>file:42</code>)<br>For Node.js <code>require</code> paths, install a plugin like <code>vim-node</code> for resolution.<br>Set <code>:set path+=**</code> + <code>:set suffixesadd+=.js,.ts</code> for broader path resolution.",
  ["L2_composition"])

c("Workflows", "How do you measure time spent with <code>nvim</code> or specific actions?",
  "Use <code>wakatime</code> plugin for automatic tracking. For startuptime: <code>nvim --startuptime startup.log</code>. For profiling: <code>:profile start profile.log</code>, do actions, <code>:profile stop</code>. Analyze the log to find slow functions.",
  ["L4_diagnosis"])

# ═══ 14 - GOTCHAS & DIAGNOSIS ════════════════════════════════════════════════════

c("Gotchas", "<code>E37: No write since last change (add ! to override)</code> — what's happening?",
  "You're trying to switch buffers, close a window, or quit with unsaved changes. Solutions:<br>1. <code>:w</code> to save first<br>2. <code>:q!</code> to force-quit discarding changes<br>3. <code>:set hidden</code> to allow switching buffers with unsaved changes",
  ["L4_diagnosis"])

c("Gotchas", "Vim shows a swap file warning. What do you do?",
  "Another Vim instance or a crashed session left a <code>.swp</code> file. Options:<br><code>[O]</code>pen read-only<br><code>[E]</code>dit anyway (ignore swap)<br><code>[R]</code>ecover — load the swap file's contents<br><code>[D]</code>elete the swap file<br><code>[Q]</code>uit<br><code>[A]</code>bort<br>Always check which option fits — <code>R</code> may save lost work.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>:%s/foo/bar/g</code> say 'Pattern not found' when I can see 'foo'?",
  "Possible causes:<br>1. <code>smartcase</code> is on and you typed lowercase — set <code>:set noignorecase</code><br>2. Search is wrapped with <code>\\&lt;foo\\&gt;</code> (word boundaries) but 'foo' is part of a bigger word<br>3. The pattern contains special chars that need escaping (<code>+</code>, <code>(</code>, <code>)</code>, <code>{</code>, <code>}</code>)",
  ["L4_diagnosis"])

c("Gotchas", "Why does yanking not work when I use <code>xd</code> or <code>dd</code>?",
  "It DOES work — deleted text goes to the unnamed register <code>\"</code> AND the numbered register <code>1</code>. But it's overwritten by the NEXT delete. Use <code>\"0p</code> to paste the last YANK (register <code>0</code> is never overwritten by deletes).",
  ["L4_diagnosis"])

c("Gotchas", "Why does pasting from a register sometimes insert <code>^M</code> or weird characters?",
  "The register contains control characters. Use <code>:reg</code> to inspect. Paste in a temporary buffer to see the raw content. For macros, use <code>\"qp</code> and edit the string then <code>\"qyy</code> to fix. The <code>\"+</code> clipboard register may need <code>:checkhealth</code> to verify clipboard support.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>:%s/\\n/ /g</code> not replace newlines?",
  "In Vim's substitution, <code>\\n</code> matches a null byte (NUL), NOT a newline. To match a newline, use <code>\\n</code> only on the search side, OR use <code>\\r</code> to represent a newline in the replacement. Correct: <code>:%s/\\n/ /g</code> (search newline, replace with space). Actually: use <code>:%join</code> or <code>:g/^/.,/./-1join</code> for joining paragraphs.",
  ["L4_diagnosis"])

c("Gotchas", "Why is Neovim slow to start?",
  "1. <b>Too many plugins</b> — check with <code>:Lazy profile</code> or <code>nvim --startuptime log</code><br>2. <b>LSP servers</b> — they start with the first file, use <code>lazy.nvim</code> lazy-loading<br>3. <b>Treesitter</b> — parsing large files on open, use <code>event = 'BufReadPost'</code><br>4. <b>Broken config</b> — <code>nvim --clean</code> to test without config, then bisect",
  ["L4_diagnosis"])

c("Gotchas", "Why does my LSP not work or show 'No LSP client found'?",
  "1. Check if LSP server is installed: <code>:Mason</code> or <code>which rust-analyzer</code><br>2. Verify <code>lspconfig</code> setup is called: <code>:LspInfo</code> to see attached clients<br>3. Filetype may not match — <code>:set filetype?</code> should be correct<br>4. Run <code>:checkhealth lsp</code> for Neovim's built-in diagnostics<br>5. <code>:LspLog</code> to see server communication logs",
  ["L4_diagnosis"])

c("Gotchas", "Why can't I paste from the system clipboard inside a terminal?",
  "1. Neovim needs <code>+clipboard</code> feature: <code>:checkhealth provider</code><br>2. On Linux: install <code>xclip</code> or <code>wl-clipboard</code> (Wayland)<br>3. On SSH: clipboard forwarding doesn't work — use OSC-52: <code>vim.o.clipboard = 'unnamedplus'</code> + <code>set -g allow-passthrough on</code> in tmux<br>4. In terminal mode: <code>C-\\ C-n</code> first, then paste",
  ["L4_diagnosis"])

c("Gotchas", "Why do macros fail silently on some lines?",
  "Macros designed for line N often break on line N+1 (different length, structure). Solutions:<br>1. Use motions that adapt: <code>0</code> or <code>$</code> instead of <code>10l</code><br>2. Use search-based positioning: <code>/pattern/e ENTER</code><br>3. End macro with <code>j0</code> (next line, first column) for consistent positioning<br>4. Use <code>:g/pattern/normal! @q</code> which applies per-matching-line",
  ["L4_diagnosis"])

# ═══ 15 - ADVANCED / EXPERT ══════════════════════════════════════════════════════

c("Advanced", "What is <code>operatorfunc</code> and how do you use it?",
  "<code>g@</code> + motion calls <code>'operatorfunc'</code>. Set it to a custom function:<br><code>vim.o.operatorfunc = 'MyCustomOp'</code><br>Then <code>set operatorfunc=MyCustomOp | normal! g@iw</code><br>This is how plugins create custom operators (e.g., commentary, surround).",
  ["L6_innovation"])

c("Advanced", "How do you create a custom text object with Treesitter?",
  "Use <code>nvim-treesitter-textobjects</code> and define captures:<br><code>('query', 'function.outer') = '(function_definition) @function.outer'</code><br>Then map: <code>v.af = '@function.outer'</code>. For non-TS objects, use <code>:h omap-info</code> and write a mapping like <code>xnoremap af :&lt;C-u&gt;normal! ...</code>",
  ["L6_innovation"])

c("Advanced", "How do you write a Neovim plugin in Lua?",
  "1. Create a directory: <code>~/.local/share/nvim/site/pack/vendor/start/my-plugin/</code><br>2. Add <code>lua/my-plugin/init.lua</code> with your module<br>3. Export a <code>setup()</code> function accepting user options<br>4. Users call: <code>require('my-plugin').setup({})</code><br>For distribution: publish to GitHub, users install with lazy.nvim.",
  ["L6_innovation"])

c("Advanced", "What is <code>:source</code> and how is it different from <code>:runtime</code>?",
  "<code>:source file</code> — executes the file as Vimscript from a specific path<br><code>:runtime file</code> — searches <code>'runtimepath'</code> for <code>file</code> and sources the first match<br>In Lua: <code>dofile('path')</code> for specific path, <code>require('module')</code> for runtimepath-based loading.",
  ["L3_design"])

c("Advanced", "What is the 'runtimepath' and why does it matter?",
  "<code>:set runtimepath?</code> — comma-separated list of directories Vim searches for <code>:runtime</code> and <code>require</code>. Plugin managers append each plugin's directory here. The <code>after/</code> directory at the end takes precedence (<code>:h 'rtp'</code>).",
  ["L3_design"])

c("Advanced", "How do you run an external command and capture its output?",
  "<code>:r !ls</code> — read output of <code>ls</code> into buffer below cursor<br><code>:0r !date</code> — insert date at top of file<br><code>:r !curl -s https://api.example.com</code> — insert API response<br>Or in Lua: <code>vim.fn.system({'ls', '-la'})</code>",
  ["L2_composition"])

c("Advanced", "What is <code>makeprg</code> and <code>errorformat</code>?",
  "The Make workflow: <code>:make</code> runs <code>'makeprg'</code> (default: <code>make</code>). Output is parsed with <code>'errorformat'</code> and errors populate the quickfix list. Configure per-project:<br><code>:set makeprg=eslint\\ %</code><br><code>:set efm=%f:%l:%c:\\ %m</code><br>Then <code>:make</code> and <code>:copen</code> to see errors.",
  ["L5_opinion"])

c("Advanced", "What is <code>modeline</code> and should you use it?",
  "A comment at the top/bottom of a file that sets Vim options for that file:<br><code>// vim: set ts=2 sw=2 et:</code><br>DISABLED by default in Neovim for security (arbitrary code execution risk). Use <code>.editorconfig</code> or <code>ftplugin/</code> files instead.",
  ["L5_opinion"])

c("Advanced", "How do you execute Lua directly from the command line (<code>:lua</code>)?",
  "<code>:lua print(vim.inspect(vim.opt.tabstop:get()))</code><br><code>:lua vim.cmd('highlight Normal guibg=#1e1e2e')</code><br><code>:lua =1+1</code> (prints result)<br>The <code>:lua</code> prefix executes a single line. Use <code>:lua << EOF ... EOF</code> for multiline.",
  ["L1_mechanics"])

c("Advanced", "What is <code>:checkhealth</code>?",
  "Neovim's built-in diagnostic tool. Run <code>:checkhealth</code> to see the status of: Python/Node/Ruby providers, clipboard, LSP setup, Treesitter parsers, and plugin health. The first thing to run when something breaks.",
  ["L4_diagnosis"])

c("Advanced", "How do you make Neovim the default editor for git/shell?",
  "<code>export EDITOR=nvim</code> in <code>~/.bashrc</code> / <code>~/.zshrc</code><br><code>export VISUAL=nvim</code> for apps that use VISUAL<br><code>git config --global core.editor nvim</code><br>For sudo: edit <code>/etc/sudoers</code> with <code>Defaults editor=/usr/bin/nvim</code> via <code>visudo</code>",
  ["L1_mechanics"])

c("Advanced", "What are Vim's special marks?",
  "<code>'.</code> — last edit position<br><code>'\"</code> — last exit position<br><code>'[</code> / <code>']</code> — start/end of last change or yank<br><code>'&lt;</code> / <code>'&gt;</code> — start/end of last visual selection<br><code>'0</code> — position when last exiting Vim<br>Use <code>`</code> (backtick) instead of <code>'</code> for column-exact position.",
  ["L1_mechanics"])

c("Advanced", "How do you reduce escape key latency (timeoutlen)?",
  "<code>vim.o.timeoutlen = 300</code> (milliseconds). Lower = faster ESC response but less time for multi-key mappings. Common values: 200–500ms. Also consider mapping <code>jk</code> / <code>jj</code> → <code>ESC</code> in insert mode to skip timeout entirely.",
  ["L5_opinion"])

c("Advanced", "What is the difference between <code>:normal</code> and <code>:normal!</code>?",
  "<code>:normal!</code> uses the DEFAULT mappings (ignores user keymaps). <code>:normal</code> respects user mappings. Use <code>:normal!</code> in scripts/macros for predictability — you don't want user keymaps breaking your automation.",
  ["L5_opinion"])

c("Advanced", "How do you persist global state (sessions) across restarts?",
  "<code>:mksession! ~/.config/nvim/sessions/my-session.vim</code><br><code>:source ~/.config/nvim/sessions/my-session.vim</code> to restore<br>Or use a plugin like <code>auto-session.nvim</code> for automatic session management. Sessions save: open files, window layout, cursor position, fold state, and more.",
  ["L2_composition"])

c("Advanced", "What is <code>vim.ui.input</code> / <code>vim.ui.select</code>?",
  "Neovim's UI abstraction layer. Plugins call <code>vim.ui.select(items, opts, callback)</code> and users can override the UI with Telescope, fzf-lua, or <code>dressing.nvim</code>. This decouples plugin logic from UI presentation.",
  ["L6_innovation"])

c("Advanced", "How do you use Neovim as a difftool for git?",
  "<code>git config --global diff.tool nvimdiff</code><br><code>git config --global difftool.nvimdiff.cmd 'nvim -d $LOCAL $REMOTE'</code><br>Then <code>git difftool</code>. For merge conflicts: <code>git config --global merge.tool nvimdiff</code>. Use <code>:diffget</code> / <code>:diffput</code> to resolve hunks.",
  ["L2_composition"])

c("Advanced", "What are some Neovim features that DON'T exist in Vim?",
  "<b>Lua first-class:</b> Lua is a native scripting language, not an add-on<br><b>Built-in LSP:</b> no plugins needed for LSP client<br><b>Treesitter:</b> built-in parser engine (Vim 9.1 has it too but limited)<br><b>Terminal emulator:</b> <code>:term</code> runs a real shell in a buffer<br><b>External UI:</b> GUIs like Neovide, Goneovim, Fvim connect via RPC<br><b>API/msgpack-RPC:</b> programmable by external processes<br><b>XDG compliance:</b> config in <code>~/.config/nvim</code>, not <code>~/.vimrc</code> everywhere",
  ["L3_design"])

c("Advanced", "If you could only use 5 Neovim plugins, which should they be?",
  "1. <b>lazy.nvim</b> — plugin manager (prerequisite)<br>2. <b>Telescope</b> — fuzzy finder (files, grep, buffers)<br>3. <b>nvim-treesitter</b> + textobjects — structural editing<br>4. <b>nvim-lspconfig</b> + mason — IDE intelligence<br>5. <b>nvim-cmp</b> — autocompletion<br>Everything else is optimization. These 5 give you a modern IDE. Add gitsigns + which-key for quality of life.",
  ["L5_opinion"])

# ── Build ──────────────────────────────────────────────────────────────────────
def build():
    for deck_key, front, back, tags in C:
        note = genanki.Note(model=model, fields=[front, back], tags=tags)
        decks[deck_key].add_note(note)

    pkg = genanki.Package(list(decks.values()))
    pkg.write_to_file(OUTPUT)
    print(f"Built {len(decks)} decks with {len(C)} cards -> {OUTPUT}")

if __name__ == "__main__":
    build()
