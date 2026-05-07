import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Vim"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Modes":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Modes-Fundamentals"),
    "Motions":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Motions"),
    "Operators":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Operators-Editing"),
    "TextObjects": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Text-Objects"),
    "Search":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Search-Substitute"),
    "RegMacro":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Registers-Macros"),
    "WinBuf":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Windows-Buffers"),
    "Workflows":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Workflows"),
    "Gotchas":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::09-Gotchas"),
    "Advanced":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::10-Advanced"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ============================================================
# DECK 01: MODES — Fundamentals
# ============================================================

# L0 — Primitives: modes concept
c("Modes", "What are the four main Vim modes?", "<code>Normal</code>, <code>Insert</code>, <code>Visual</code>, <code>Command-line</code>", "L0_primitives")
c("Modes", "What mode does Vim start in?", "<code>Normal</code> mode — for navigation and issuing commands", "L0_primitives")
c("Modes", "What is Normal mode for?", "Navigation, deletion, yanking, and issuing commands (the 'home' mode)", "L0_primitives")
c("Modes", "What is Insert mode for?", "Typing text into the buffer", "L0_primitives")
c("Modes", "What is Visual mode for?", "Selecting text visually before operating on it", "L0_primitives")
c("Modes", "What is Command-line mode for?", "Running Ex commands (<code>:</code>), searches (<code>/</code> <code>?</code>), and filter commands (<code>!</code>)", "L0_primitives")
c("Modes", "What does 'modal editing' mean?", "Keys have different meanings depending on which mode you are in — <code>j</code> is motion in Normal but types 'j' in Insert", "L0_primitives")
c("Modes", "What do you press to enter Insert mode before the cursor?", "<code>i</code>", "L0_primitives")
c("Modes", "What do you press to enter Insert mode at the beginning of the line?", "<code>I</code>", "L0_primitives")
c("Modes", "What do you press to enter Insert mode after the cursor?", "<code>a</code> (append)", "L0_primitives")
c("Modes", "What do you press to enter Insert mode at the end of the line?", "<code>A</code>", "L0_primitives")
c("Modes", "What do you press to return to Normal mode from any other mode?", "<code>Esc</code> or <code>C-[</code>", "L0_primitives")
c("Modes", "What do you press to open a new line below and enter Insert mode?", "<code>o</code>", "L0_primitives")
c("Modes", "What do you press to open a new line above and enter Insert mode?", "<code>O</code>", "L0_primitives")
c("Modes", "What do you press to enter Visual mode character-wise?", "<code>v</code>", "L1_mechanics")
c("Modes", "What do you press to enter Visual mode line-wise?", "<code>V</code>", "L1_mechanics")
c("Modes", "What do you press to enter Visual mode block-wise?", "<code>C-v</code>", "L1_mechanics")
c("Modes", "What do you press to enter Replace mode?", "<code>R</code>", "L1_mechanics")
c("Modes", "What do you press to replace a single character without entering Insert mode?", "<code>r</code> followed by the replacement character", "L1_mechanics")
c("Modes", "What do you press to enter Command-line mode?", "<code>:</code>", "L1_mechanics")
c("Modes", "What does <code>gR</code> do in Vim?", "Virtual Replace mode — replaces characters but respects tab stops (treats tabs as spaces)", "L1_mechanics")
# TODO: add more cards for Modes

# ============================================================
# DECK 02: MOTIONS — Navigation
# ============================================================

# L0 — Core motion concept
c("Motions", "What is a 'motion' in Vim?", "A movement command that moves the cursor — often combined with operators to form actions", "L0_primitives")
c("Motions", "What is the Vim grammar: <code>operator + motion</code>?", "A keybinding composed of an <b>operator</b> (like <code>d</code> delete, <code>c</code> change) followed by a <b>motion</b> (where to act). For example, <code>dw</code> = delete word.", "L0_primitives")
c("Motions", "What does a <code>[count]</code> prefix do before a motion or operator?", "Repeats the action <code>[count]</code> times, e.g. <code>5j</code> moves down 5 lines, <code>3dw</code> deletes 3 words", "L0_primitives")

# L1 — hjkl & basic
c("Motions", "What do you press to move the cursor left?", "<code>h</code>", "L1_mechanics")
c("Motions", "What do you press to move the cursor down?", "<code>j</code>", "L1_mechanics")
c("Motions", "What do you press to move the cursor up?", "<code>k</code>", "L1_mechanics")
c("Motions", "What do you press to move the cursor right?", "<code>l</code>", "L1_mechanics")

# L1 — Word motions
c("Motions", "What do you press to move to the start of the next word?", "<code>w</code>", "L1_mechanics")
c("Motions", "What do you press to move to the start of the previous word?", "<code>b</code>", "L1_mechanics")
c("Motions", "What do you press to move to the end of the current/next word?", "<code>e</code>", "L1_mechanics")
c("Motions", "What does <code>W</code> do differently from <code>w</code>?", "<code>W</code> moves by <b>WORD</b> (whitespace-separated), ignoring punctuation. <code>w</code> moves by <b>word</b> (stops at punctuation)", "L1_mechanics")
c("Motions", "What does <code>B</code> do?", "Move backward by <b>WORD</b> (whitespace-separated)", "L1_mechanics")
c("Motions", "What does <code>E</code> do?", "Move to end of current/next <b>WORD</b> (whitespace-separated)", "L1_mechanics")
c("Motions", "What do you press to move to the next occurrence of the character under the cursor on the current line?", "<code>f{char}</code>", "L1_mechanics")
c("Motions", "What do you press to move to the previous occurrence of a character on the current line?", "<code>F{char}</code>", "L1_mechanics")
c("Motions", "What do you press to move just before the next occurrence of a character on the line?", "<code>t{char}</code> ('till')", "L1_mechanics")
c("Motions", "What do you press to move just before the previous occurrence of a character on the line?", "<code>T{char}</code> (reverse 'till')", "L1_mechanics")
c("Motions", "What do you press to repeat the last <code>f</code>, <code>F</code>, <code>t</code>, or <code>T</code> motion forward?", "<code>;</code>", "L1_mechanics")
c("Motions", "What do you press to repeat the last <code>f</code>, <code>F</code>, <code>t</code>, or <code>T</code> motion backward?", "<code>,</code>", "L1_mechanics")

# L1 — Line motions
c("Motions", "What do you press to go to the beginning of the line (first non-blank character)?", "<code>^</code>", "L1_mechanics")
c("Motions", "What do you press to go to the first character of the line (column 1)?", "<code>0</code>", "L1_mechanics")
c("Motions", "What do you press to go to the end of the line?", "<code>$</code>", "L1_mechanics")
c("Motions", "What does <code>g_</code> do?", "Go to the last non-blank character of the line", "L1_mechanics")

# L1 — Paragraph & block motions
c("Motions", "What does <code>{</code> do in Normal mode?", "Jump to the beginning of the current/previous paragraph", "L1_mechanics")
c("Motions", "What does <code>}</code> do in Normal mode?", "Jump to the beginning of the next paragraph", "L1_mechanics")
c("Motions", "What does <code>(</code> do in Normal mode?", "Jump to the beginning of the current/previous sentence", "L1_mechanics")
c("Motions", "What does <code>)</code> do in Normal mode?", "Jump to the beginning of the next sentence", "L1_mechanics")

# L1 — File motions
c("Motions", "What do you press to go to the top of the file?", "<code>gg</code>", "L1_mechanics")
c("Motions", "What do you press to go to the bottom of the file?", "<code>G</code>", "L1_mechanics")
c("Motions", "What does <code>5G</code> or <code>5gg</code> do?", "Go to line number 5", "L1_mechanics")
c("Motions", "How do you go to a specific line number?", "<code>:{number}</code> or <code>{number}G</code> or <code>{number}gg</code>", "L1_mechanics")
c("Motions", "What does <code>H</code> do?", "Move cursor to the <b>H</b>igh (top) of the visible window", "L1_mechanics")
c("Motions", "What does <code>M</code> do?", "Move cursor to the <b>M</b>iddle of the visible window", "L1_mechanics")
c("Motions", "What does <code>L</code> do?", "Move cursor to the <b>L</b>ow (bottom) of the visible window", "L1_mechanics")

# L1 — Scrolling
c("Motions", "What does <code>C-f</code> do?", "Scroll forward one full page (<b>F</b>orward)", "L1_mechanics")
c("Motions", "What does <code>C-b</code> do?", "Scroll backward one full page (<b>B</b>ackward)", "L1_mechanics")
c("Motions", "What does <code>C-d</code> do?", "Scroll down half a page (<b>D</b>own)", "L1_mechanics")
c("Motions", "What does <code>C-u</code> do?", "Scroll up half a page (<b>U</b>p)", "L1_mechanics")
c("Motions", "What does <code>C-e</code> do?", "Scroll the viewport down one line (cursor stays if possible)", "L1_mechanics")
c("Motions", "What does <code>C-y</code> do?", "Scroll the viewport up one line (cursor stays if possible)", "L1_mechanics")
c("Motions", "What does <code>zz</code> do?", "Center the current line in the viewport", "L1_mechanics")
c("Motions", "What does <code>zt</code> do?", "Move the current line to the <b>t</b>op of the viewport", "L1_mechanics")
c("Motions", "What does <code>zb</code> do?", "Move the current line to the <b>b</b>ottom of the viewport", "L1_mechanics")

# L1 — Matching & jump motions
c("Motions", "What do you press to jump to the matching bracket/parenthesis?", "<code>%</code>", "L1_mechanics")

# L1 — Search motions
c("Motions", "What does <code>/pattern</code> do?", "Search forward for <code>pattern</code>", "L1_mechanics")
c("Motions", "What does <code>?pattern</code> do?", "Search backward for <code>pattern</code>", "L1_mechanics")
c("Motions", "What do you press to go to the next search match?", "<code>n</code>", "L1_mechanics")
c("Motions", "What do you press to go to the previous search match?", "<code>N</code>", "L1_mechanics")
c("Motions", "What does <code>*</code> do?", "Search forward for the word under the cursor (whole word)", "L1_mechanics")
c("Motions", "What does <code>#</code> do?", "Search backward for the word under the cursor (whole word)", "L1_mechanics")
c("Motions", "What does <code>g*</code> do?", "Search forward for the word under the cursor (partial match)", "L1_mechanics")
c("Motions", "What does <code>g#</code> do?", "Search backward for the word under the cursor (partial match)", "L1_mechanics")

# ============================================================
# DECK 03: OPERATORS — Editing
# ============================================================

# L0 — Operator concept
c("Operators", "What is an 'operator' in Vim's grammar?", "A command that performs an action (<code>d</code>, <code>c</code>, <code>y</code>, etc.) and waits for a motion or text object to define what to act on", "L0_primitives")

# L1 — Delete
c("Operators", "What do you press to delete the character under the cursor?", "<code>x</code>", "L1_mechanics")
c("Operators", "What do you press to delete the character before the cursor?", "<code>X</code>", "L1_mechanics")
c("Operators", "What does <code>dd</code> do?", "Delete (cut) the current line", "L1_mechanics")
c("Operators", "What does <code>dw</code> do?", "Delete from cursor to the start of the next word", "L1_mechanics")
c("Operators", "What does <code>daw</code> do?", "Delete a word (including trailing whitespace)", "L1_mechanics")
c("Operators", "What does <code>D</code> do?", "Delete from cursor to end of line", "L1_mechanics")
c("Operators", "What does <code>d$</code> do?", "Delete from cursor to end of line (same as <code>D</code>)", "L1_mechanics")
c("Operators", "What does <code>d0</code> do?", "Delete from cursor to beginning of line", "L1_mechanics")
c("Operators", "What does <code>dG</code> do?", "Delete from cursor to end of file", "L1_mechanics")
c("Operators", "What does <code>dgg</code> do?", "Delete from cursor to beginning of file", "L1_mechanics")

# L1 — Change
c("Operators", "What does the <code>c</code> operator do?", "<b>Change</b> — deletes the motion/text-object and enters Insert mode", "L1_mechanics")
c("Operators", "What does <code>cc</code> do?", "Change the entire current line (clear and enter Insert)", "L1_mechanics")
c("Operators", "What does <code>cw</code> do?", "Change from cursor to the start of the next word", "L1_mechanics")
c("Operators", "What does <code>C</code> do?", "Change from cursor to end of line", "L1_mechanics")
c("Operators", "What do you press to change the character under the cursor and stay in Normal mode?", "<code>s</code> (substitute character — deletes char and enters Insert)", "L1_mechanics")
c("Operators", "What does <code>S</code> do?", "Substitute entire line (delete and enter Insert)", "L1_mechanics")

# L1 — Yank/Put
c("Operators", "What does the <code>y</code> operator do?", "<b>Yank</b> (copy) — copies text into the default register", "L1_mechanics")
c("Operators", "What does <code>yy</code> do?", "Yank (copy) the current line", "L1_mechanics")
c("Operators", "What does <code>yw</code> do?", "Yank from cursor to start of next word", "L1_mechanics")
c("Operators", "What does <code>Y</code> do?", "Yank from cursor to end of line (alias for <code>y$</code>)", "L1_mechanics")
c("Operators", "What do you press to paste after the cursor?", "<code>p</code>", "L1_mechanics")
c("Operators", "What do you press to paste before the cursor?", "<code>P</code>", "L1_mechanics")
c("Operators", "What does <code>p</code> paste with a line-wise yank?", "Pastes the yanked lines below the current line", "L1_mechanics")
c("Operators", "What does <code>P</code> paste with a line-wise yank?", "Pastes the yanked lines above the current line", "L1_mechanics")
c("Operators", "What does <code>gp</code> do?", "Paste after cursor and leave cursor after pasted text", "L1_mechanics")
c("Operators", "What does <code>gP</code> do?", "Paste before cursor and leave cursor after pasted text", "L1_mechanics")

# L1 — Indent & Join
c("Operators", "What does <code>&gt;&gt;</code> do?", "Indent the current line right by <code>shiftwidth</code>", "L1_mechanics")
c("Operators", "What does <code>&lt;&lt;</code> do?", "Indent the current line left by <code>shiftwidth</code>", "L1_mechanics")
c("Operators", "What does <code>&gt;ip</code> do?", "Indent the inner paragraph right", "L1_mechanics")
c("Operators", "What does <code>=ip</code> do?", "Auto-indent the inner paragraph", "L1_mechanics")
c("Operators", "What do you press to join the next line to the current line?", "<code>J</code>", "L1_mechanics")
c("Operators", "What does <code>gJ</code> do?", "Join lines without inserting a space between them", "L1_mechanics")

# L1 — Tilde & case
c("Operators", "What does <code>~</code> do?", "Toggle case of the character under the cursor (and move right)", "L1_mechanics")
c("Operators", "What does <code>g~</code> followed by a motion do?", "Toggle case over the motion (e.g. <code>g~w</code> toggles rest of word)", "L1_mechanics")
c("Operators", "What does <code>guw</code> do?", "Make a word lowercase (<code>gu</code> operator + <code>w</code> motion)", "L1_mechanics")
c("Operators", "What does <code>gUw</code> do?", "Make a word UPPERCASE (<code>gU</code> operator + <code>w</code> motion)", "L1_mechanics")
c("Operators", "What does <code>guu</code> do?", "Make the entire current line lowercase", "L1_mechanics")
c("Operators", "What does <code>gUU</code> do?", "Make the entire current line UPPERCASE", "L1_mechanics")

# L1 — Dot repeat & undo
c("Operators", "What does <code>.</code> (dot) do?", "Repeat the last change (edit) at the cursor position", "L1_mechanics")
c("Operators", "What do you press to undo the last change?", "<code>u</code>", "L1_mechanics")
c("Operators", "What does <code>U</code> do?", "Undo all changes on the current line (only last-edited line)", "L1_mechanics")
c("Operators", "What do you press to redo an undone change?", "<code>C-r</code>", "L1_mechanics")

# L2 — Combining operators with f/t
c("Operators", "What does <code>df{char}</code> do?", "Delete from cursor up to and including <code>{char}</code>", "L2_composition")
c("Operators", "What does <code>dt{char}</code> do?", "Delete from cursor up to (but not including) <code>{char}</code>", "L2_composition")
c("Operators", "What does <code>cf{char}</code> do?", "Change from cursor up to and including <code>{char}</code>, then enter Insert", "L2_composition")
c("Operators", "What does <code>ct{char}</code> do?", "Change from cursor up to (but not including) <code>{char}</code>, then enter Insert", "L2_composition")
c("Operators", "What does <code>yf{char}</code> do?", "Yank from cursor up to and including <code>{char}</code>", "L2_composition")
# TODO: add more cards for Operators

# ============================================================
# DECK 04: TEXT OBJECTS
# ============================================================

# L1 — Text object concept
c("TextObjects", "What is a 'text object' in Vim?", "A structured region of text (word, sentence, paragraph, tag, quote block) that can be operated on with <code>i</code> (inner) or <code>a</code> (around) prefixes", "L0_primitives")
c("TextObjects", "What does <code>i</code> mean in a text object (like <code>diw</code>)?", "<b>Inner</b> — operate on the contents, excluding surrounding whitespace or delimiters", "L1_mechanics")
c("TextObjects", "What does <code>a</code> mean in a text object (like <code>daw</code>)?", "<b>Around</b> (or 'a') — operate on the object plus surrounding whitespace or delimiters", "L1_mechanics")

# L1 — Word & WORD objects
c("TextObjects", "What does <code>iw</code> select?", "Inner <b>w</b>ord — the word under cursor, excluding surrounding whitespace", "L1_mechanics")
c("TextObjects", "What does <code>aw</code> select?", "A <b>w</b>ord — the word under cursor plus trailing whitespace", "L1_mechanics")
c("TextObjects", "What does <code>cw</code> do vs <code>ciw</code>?", "<code>cw</code> changes from cursor to end of word. <code>ciw</code> changes the entire inner word regardless of cursor position", "L1_mechanics")
c("TextObjects", "What does <code>iW</code> select?", "Inner <b>WORD</b> — whitespace-separated, ignoring punctuation", "L1_mechanics")

# L1 — Sentence & paragraph objects
c("TextObjects", "What does <code>is</code> select?", "Inner <b>s</b>entence", "L1_mechanics")
c("TextObjects", "What does <code>as</code> select?", "A <b>s</b>entence (including trailing whitespace)", "L1_mechanics")
c("TextObjects", "What does <code>ip</code> select?", "Inner <b>p</b>aragraph — lines of the paragraph, excluding surrounding blank lines", "L1_mechanics")
c("TextObjects", "What does <code>ap</code> select?", "A <b>p</b>aragraph — the paragraph plus the following blank line", "L1_mechanics")

# L1 — Quote & bracket objects
c("TextObjects", "What does <code>i&quot;</code> or <code>i'</code> select?", "Inner text inside double/single quotes (excluding the quotes)", "L1_mechanics")
c("TextObjects", "What does <code>a&quot;</code> or <code>a'</code> select?", "Text inside double/single quotes including the quote characters", "L1_mechanics")
c("TextObjects", "What does <code>i)</code> or <code>i(</code> or <code>ib</code> select?", "Inner block inside parentheses (excluding the parens)", "L1_mechanics")
c("TextObjects", "What does <code>a)</code> or <code>a(</code> or <code>ab</code> select?", "Block inside parentheses including the parentheses themselves", "L1_mechanics")
c("TextObjects", "What does <code>i]</code> or <code>i[</code> select?", "Inner block inside square brackets (excluding the brackets)", "L1_mechanics")
c("TextObjects", "What does <code>i}</code> or <code>i{</code> or <code>iB</code> select?", "Inner block inside curly braces (excluding the braces)", "L1_mechanics")
c("TextObjects", "What does <code>a}</code> or <code>a{</code> or <code>aB</code> select?", "Block inside curly braces including the braces", "L1_mechanics")

# L1 — Tag objects
c("TextObjects", "What does <code>it</code> select in HTML/XML?", "Inner contents of a tag block (between opening and closing tags, excluding the tags)", "L1_mechanics")
c("TextObjects", "What does <code>at</code> select in HTML/XML?", "A tag block — the complete tag including opening and closing tags", "L1_mechanics")

# L2 — Combining operators + text objects
c("TextObjects", "What does <code>ciw</code> do?", "Change inner word (delete the word under cursor and enter Insert mode)", "L2_composition")
c("TextObjects", "What does <code>ci&quot;</code> do?", "Change inner double-quoted text (delete contents between quotes, enter Insert)", "L2_composition")
c("TextObjects", "What does <code>dap</code> do?", "Delete around paragraph (delete paragraph plus following blank line)", "L2_composition")
c("TextObjects", "What does <code>yi)</code> do?", "Yank inner parentheses (copy contents inside parens)", "L2_composition")
c("TextObjects", "What does <code>ca[</code> do?", "Change around square brackets (delete brackets and contents, enter Insert)", "L2_composition")

# ============================================================
# DECK 05: SEARCH & SUBSTITUTE
# ============================================================

# L1 — Basic search
c("Search", "How do you search forward in Vim?", "<code>/pattern</code> then <code>Enter</code>", "L1_mechanics")
c("Search", "How do you search backward in Vim?", "<code>?pattern</code> then <code>Enter</code>", "L1_mechanics")
c("Search", "After a search, what does <code>n</code> do?", "Go to the <b>n</b>ext match in the same direction as the original search", "L1_mechanics")
c("Search", "After a search, what does <code>N</code> do?", "Go to the previous match (opposite direction of original search)", "L1_mechanics")
c("Search", "What does <code>*</code> do in Normal mode?", "Search forward for the exact word under the cursor (whole word match)", "L1_mechanics")
c("Search", "What does <code>#</code> do in Normal mode?", "Search backward for the exact word under the cursor (whole word match)", "L1_mechanics")
c("Search", "How do you clear search highlighting after a search?", "<code>:nohlsearch</code> or <code>:noh</code>", "L1_mechanics")
c("Search", "What does <code>:set hlsearch</code> do?", "Enables highlighting of all search matches", "L1_mechanics")
c("Search", "What does <code>:set incsearch</code> do?", "Shows matches as you type the search pattern (incremental search)", "L1_mechanics")
c("Search", "What does <code>:set ignorecase</code> do in searches?", "Makes searches case-insensitive", "L1_mechanics")
c("Search", "What does <code>:set smartcase</code> do in combination with <code>ignorecase</code>?", "Overrides <code>ignorecase</code> if the search pattern contains uppercase letters (makes search case-sensitive only when you use capitals)", "L1_mechanics")

# L2 — Substitute command
c("Search", "What does <code>:s/foo/bar/</code> do?", "Substitute <code>foo</code> with <code>bar</code> on the current line (first occurrence only)", "L2_composition")
c("Search", "What does <code>:s/foo/bar/g</code> do?", "Substitute <code>foo</code> with <code>bar</code> on the current line (all occurrences on that line)", "L2_composition")
c("Search", "What does <code>:%s/foo/bar/g</code> do?", "Substitute <code>foo</code> with <code>bar</code> on ALL lines in the file", "L2_composition")
c("Search", "What does the <code>c</code> flag do in <code>:s/foo/bar/gc</code>?", "Ask for <b>c</b>onfirmation before each substitution", "L2_composition")
c("Search", "What does the <code>i</code> flag do in <code>:s/foo/bar/gi</code>?", "Make the substitution case-<b>i</b>nsensitive", "L2_composition")
c("Search", "What does <code>:5,10s/foo/bar/g</code> do?", "Substitute <code>foo</code> with <code>bar</code> on lines 5 through 10 only", "L2_composition")
c("Search", "What does <code>:.,$s/foo/bar/g</code> do?", "Substitute from current line (<code>.</code>) to end of file (<code>$</code>)", "L2_composition")
c("Search", "What does <code>:.,+3s/foo/bar/g</code> do?", "Substitute from current line through current+3 lines", "L2_composition")
c("Search", "What does <code>&amp;</code> mean in a replacement string (substitute command)?", "The entire matched pattern — e.g. <code>:s/foo/&amp;&amp;/</code> doubles <code>foo</code> to <code>foofoo</code>", "L2_composition")
c("Search", "What do <code>\\1</code>, <code>\\2</code> mean in a replacement string?", "Backreferences to capture groups from the search pattern (<code>\\(...\\)</code>)", "L2_composition")

# L3 — Global command
c("Search", "What does <code>:g/pattern/command</code> do?", "Execute <code>command</code> on every line that matches <code>pattern</code>", "L2_composition")
c("Search", "What does <code>:g/pattern/d</code> do?", "Delete all lines matching <code>pattern</code>", "L2_composition")
c("Search", "What does <code>:v/pattern/d</code> do?", "Delete all lines NOT matching <code>pattern</code> (inverse of <code>:g</code>)", "L2_composition")
c("Search", "What does <code>:g/^$/d</code> do?", "Delete all blank lines in the file", "L2_composition")

# ============================================================
# DECK 06: REGISTERS & MACROS
# ============================================================

# L0 — Registers concept
c("RegMacro", "What is a 'register' in Vim?", "A named storage slot (like a clipboard) for holding text — there are 26 named registers <code>a-z</code>, plus special registers", "L0_primitives")
c("RegMacro", "What is the unnamed register (<code>\"\"</code>)?", "The default register — stores the last deleted/yanked/changed text automatically", "L0_primitives")
c("RegMacro", "What does the <code>\"{reg}</code> prefix do before a yank/delete/put?", "Specifies which register to use, e.g. <code>\"ayy</code> yanks into register <code>a</code>", "L1_mechanics")

# L1 — Register usage
c("RegMacro", "What do you press to yank into register <code>a</code>?", "<code>\"ay</code> + motion, or <code>\"ayy</code> for a line", "L1_mechanics")
c("RegMacro", "What do you press to paste from register <code>a</code>?", "<code>\"ap</code> (after cursor) or <code>\"aP</code> (before cursor)", "L1_mechanics")
c("RegMacro", "What does register <code>0</code> store?", "The text from the most recent <b>yank</b> (not delete/change) — safe copy register", "L1_mechanics")
c("RegMacro", "What does register <code>+</code> store?", "The system clipboard (X11/Windows/macOS) — use <code>\"+y</code> to copy to clipboard", "L1_mechanics")
c("RegMacro", "What does register <code>*</code> store?", "The X11 primary selection (middle-click paste) on Linux; clipboard on Windows/macOS", "L1_mechanics")
c("RegMacro", "What does register <code>%</code> store?", "The current file name (read-only)", "L1_mechanics")
c("RegMacro", "What does register <code>/</code> store?", "The last search pattern", "L1_mechanics")
c("RegMacro", "What does register <code>:</code> store?", "The last Ex command", "L1_mechanics")
c("RegMacro", "How do you view all register contents?", "<code>:registers</code> or <code>:reg</code>", "L1_mechanics")
c("RegMacro", "What does the numbered register <code>1</code> store?", "The text from the most recent <b>delete or change</b> (unless it was a tiny delete)", "L1_mechanics")
c("RegMacro", "What does the small delete register <code>-</code> store?", "Text from deletes/changes less than one line (character-level deletes)", "L1_mechanics")
c("RegMacro", "What does <code>\"_d</code> do?", "Delete into the black-hole register (<code>_</code>) — text is truly discarded, not stored in any register", "L1_mechanics")

# L2 — Macros
c("RegMacro", "How do you start recording a macro into register <code>q</code>?", "<code>qq</code> in Normal mode — records into register <code>q</code>. Press <code>q</code> again to stop recording", "L2_composition")
c("RegMacro", "How do you play back a macro recorded in register <code>q</code>?", "<code>@q</code> — executes the macro once", "L2_composition")
c("RegMacro", "After running <code>@q</code>, how do you repeat the last macro?", "<code>@@</code> — replays the most recently executed macro", "L2_composition")
c("RegMacro", "How do you run a macro on every line in a visual selection?", "Select lines with <code>V</code>, then <code>:normal @q</code>", "L2_composition")
c("RegMacro", "How do you run a macro <code>a</code> 100 times?", "<code>100@a</code>", "L2_composition")
c("RegMacro", "How do you append more commands to an existing macro in register <code>q</code>?", "<code>qQ</code> — uses capital <code>Q</code> to append to register <code>q</code> instead of overwriting", "L2_composition")

# ============================================================
# DECK 07: WINDOWS & BUFFERS
# ============================================================

# L0 — Windows/Buffers concept
c("WinBuf", "What is the difference between a buffer, window, and tab in Vim?", "A <b>buffer</b> is the in-memory text of a file. A <b>window</b> is a viewport onto a buffer. A <b>tab page</b> is a collection of windows.", "L0_primitives")
c("WinBuf", "What does a buffer represent in Vim?", "The in-memory representation of a file — you edit buffers, not files directly", "L0_primitives")

# L1 — Window splitting
c("WinBuf", "What do you press to split the window horizontally?", "<code>:split</code> or <code>:sp</code> or <code>C-w s</code>", "L1_mechanics")
c("WinBuf", "What do you press to split the window vertically?", "<code>:vsplit</code> or <code>:vs</code> or <code>C-w v</code>", "L1_mechanics")
c("WinBuf", "What does <code>C-w</code> do in Normal mode?", "Enters window command prefix mode — the next key operates on windows", "L1_mechanics")

# L1 — Window navigation
c("WinBuf", "What do you press to move to the window left?", "<code>C-w h</code>", "L1_mechanics")
c("WinBuf", "What do you press to move to the window down?", "<code>C-w j</code>", "L1_mechanics")
c("WinBuf", "What do you press to move to the window up?", "<code>C-w k</code>", "L1_mechanics")
c("WinBuf", "What do you press to move to the window right?", "<code>C-w l</code>", "L1_mechanics")
c("WinBuf", "What does <code>C-w w</code> do?", "Cycle to the next window", "L1_mechanics")
c("WinBuf", "What does <code>C-w p</code> do?", "Go to the previously active window", "L1_mechanics")
c("WinBuf", "What does <code>C-w o</code> do?", "Close all other windows (<b>o</b>nly this window)", "L1_mechanics")

# L1 — Window resizing & moving
c("WinBuf", "What does <code>C-w +</code> do?", "Increase the current window height by one line", "L1_mechanics")
c("WinBuf", "What does <code>C-w -</code> do?", "Decrease the current window height by one line", "L1_mechanics")
c("WinBuf", "What does <code>C-w &gt;</code> do?", "Increase the current window width", "L1_mechanics")
c("WinBuf", "What does <code>C-w &lt;</code> do?", "Decrease the current window width", "L1_mechanics")
c("WinBuf", "What does <code>C-w =</code> do?", "Make all windows equal size", "L1_mechanics")
c("WinBuf", "What does <code>C-w _</code> do?", "Maximize the current window height", "L1_mechanics")
c("WinBuf", "What does <code>C-w |</code> do?", "Maximize the current window width", "L1_mechanics")
c("WinBuf", "What does <code>C-w r</code> do?", "Rotate windows downward/rightward", "L1_mechanics")
c("WinBuf", "What does <code>C-w R</code> do?", "Rotate windows upward/leftward", "L1_mechanics")

# L1 — Buffer commands
c("WinBuf", "How do you open a file in a new buffer?", "<code>:e {filename}</code> or <code>:edit {filename}</code>", "L1_mechanics")
c("WinBuf", "How do you switch to the next buffer?", "<code>:bnext</code> or <code>:bn</code>", "L1_mechanics")
c("WinBuf", "How do you switch to the previous buffer?", "<code>:bprev</code> or <code>:bp</code>", "L1_mechanics")
c("WinBuf", "How do you list all open buffers?", "<code>:buffers</code> or <code>:ls</code> or <code>:files</code>", "L1_mechanics")
c("WinBuf", "How do you switch to buffer number 3?", "<code>:b3</code> or <code>:buffer 3</code>", "L1_mechanics")
c("WinBuf", "How do you delete (close) the current buffer?", "<code>:bdelete</code> or <code>:bd</code>", "L1_mechanics")
c("WinBuf", "How do you delete buffer 3 without closing the window?", "<code>:3bdelete</code> or <code>:3bd</code>", "L1_mechanics")

# L1 — Tabs
c("WinBuf", "How do you open a new tab page?", "<code>:tabnew</code> or <code>:tabe</code> or <code>:tabedit {file}</code>", "L1_mechanics")
c("WinBuf", "What do you press to go to the next tab?", "<code>gt</code> in Normal mode", "L1_mechanics")
c("WinBuf", "What do you press to go to the previous tab?", "<code>gT</code> in Normal mode", "L1_mechanics")
c("WinBuf", "How do you go to tab number 3?", "<code>3gt</code>", "L1_mechanics")
c("WinBuf", "How do you close a tab page?", "<code>:tabclose</code> or <code>:tabc</code>", "L1_mechanics")

# L2 — Window workflow
c("WinBuf", "How do you open a file for editing in a new horizontal split?", "<code>:split {file}</code>", "L2_composition")
c("WinBuf", "How do you open a file for editing in a new vertical split?", "<code>:vsplit {file}</code>", "L2_composition")

# L3 — Buffer vs Tab philosophy
c("WinBuf", "Why are buffers preferred over tabs for managing multiple files in Vim?", "Buffers are Vim's true multi-file mechanism. Tabs are just window layouts — a buffer can exist without being visible in any tab. Buffers scale better: 50 buffers is normal; 50 tabs is unusable.", "L3_design")

# ============================================================
# DECK 08: WORKFLOWS
# ============================================================

# L2 — Marks
c("Workflows", "What is a 'mark' in Vim?", "A saved cursor position that you can jump back to later", "L2_composition")
c("Workflows", "How do you set a local mark <code>a</code>?", "<code>ma</code> in Normal mode", "L2_composition")
c("Workflows", "How do you jump to the line of a local mark <code>a</code>?", "<code>'a</code> (single quote jumps to line)", "L2_composition")
c("Workflows", "How do you jump to the exact position of a local mark <code>a</code>?", "<code>`a</code> (backtick jumps to exact line and column)", "L2_composition")
c("Workflows", "What's the difference between local marks <code>a-z</code> and global marks <code>A-Z</code>?", "Local marks are per-file; global marks are shared across all files (you can jump between files with them)", "L2_composition")
c("Workflows", "How do you view all marks?", "<code>:marks</code>", "L2_composition")
c("Workflows", "What is the built-in mark <code>.</code>?", "The position of the last change", "L2_composition")
c("Workflows", "What is the built-in mark <code>^</code>?", "The position where Insert mode was last exited", "L2_composition")

# L2 — Jump list & changelist
c("Workflows", "What does <code>C-o</code> do?", "Jump to the <b>o</b>lder (previous) position in the jump list", "L2_composition")
c("Workflows", "What does <code>C-i</code> or <code>Tab</code> do?", "Jump to the <b>i</b>n (newer) position in the jump list", "L2_composition")
c("Workflows", "What does <code>g;</code> do?", "Jump to the previous change in the changelist", "L2_composition")
c("Workflows", "What does <code>g,</code> do?", "Jump to the next change in the changelist", "L2_composition")
c("Workflows", "How do you view the jump list?", "<code>:jumps</code>", "L2_composition")
c("Workflows", "How do you view the changelist?", "<code>:changes</code>", "L2_composition")

# L2 — Quickfix & location list
c("Workflows", "What is the Quickfix list in Vim?", "A global list of positions (often populated by <code>:make</code>, <code>:grep</code>, <code>:vimgrep</code>) that you can navigate through", "L2_composition")
c("Workflows", "How do you open the Quickfix window?", "<code>:copen</code>", "L2_composition")
c("Workflows", "How do you go to the next Quickfix entry?", "<code>:cnext</code> or <code>:cn</code>", "L2_composition")
c("Workflows", "How do you go to the previous Quickfix entry?", "<code>:cprev</code> or <code>:cp</code>", "L2_composition")
c("Workflows", "How do you search for a pattern across files and populate the Quickfix list?", "<code>:vimgrep /pattern/ **/*.py</code>, then <code>:copen</code>", "L2_composition")

# L2 — Filename completion & wildmenu
c("Workflows", "What does <code>Tab</code> do on the command line when typing a filename?", "Completes the filename; press again to cycle through matches", "L2_composition")
c("Workflows", "What does <code>C-d</code> do on the command line when typing a filename?", "Shows a list of possible completions", "L2_composition")
c("Workflows", "What does <code>:set wildmenu</code> enable?", "Enhanced command-line completion with a horizontal menu of completions", "L2_composition")

# L2 — Change list & repeats
c("Workflows", "What does <code>gv</code> do?", "Reselect the last Visual selection", "L2_composition")
c("Workflows", "What does <code>gi</code> do?", "Enter Insert mode at the position where Insert mode was last exited", "L2_composition")
c("Workflows", "What does <code>g;</code> give you that <code>u</code>/<code>C-r</code> can't?", "Navigates the changelist chronologically without undoing/redoing — you can visit past edit locations without altering text", "L2_composition")

# L2 — Multi-file edits with arglist
c("Workflows", "What is the argument list (<code>args</code>) in Vim?", "A list of files to edit (set with <code>:args *.py</code>). Use <code>:next</code>/<code>:prev</code> to navigate.", "L2_composition")
c("Workflows", "How do you run a substitute command across all files in the argument list?", "<code>:argdo %s/foo/bar/g | update</code>", "L2_composition")
c("Workflows", "How do you run a command on every buffer in the buffer list?", "<code>:bufdo %s/foo/bar/g | update</code>", "L2_composition")
c("Workflows", "What does <code>:cfdo</code> do?", "Runs a command on each file in the <b>q</b>uick<b>f</b>ix list", "L2_composition")

# L2 — Diff mode
c("Workflows", "How do you start diff mode between two open windows?", "<code>:diffthis</code> in each window", "L2_composition")
c("Workflows", "How do you start Vim in diff mode from the command line?", "<code>vim -d file1 file2</code> or <code>vimdiff file1 file2</code>", "L2_composition")
c("Workflows", "What does <code>do</code> do in diff mode?", "<b>D</b>iff <b>o</b>btain — get the change from the other window into this one", "L2_composition")
c("Workflows", "What does <code>dp</code> do in diff mode?", "<b>D</b>iff <b>p</b>ut — push the change from this window to the other one", "L2_composition")
c("Workflows", "What does <code>]c</code> do in diff mode?", "Jump to the next difference", "L2_composition")
c("Workflows", "What does <code>[c</code> do in diff mode?", "Jump to the previous difference", "L2_composition")

# L2 — Folds
c("Workflows", "What does <code>zf</code> followed by a motion do?", "Create a <b>f</b>old over the motion (<code>zfip</code> = fold inner paragraph)", "L2_composition")
c("Workflows", "What do you press to open a fold under the cursor?", "<code>zo</code> (<b>o</b>pen fold)", "L2_composition")
c("Workflows", "What do you press to close a fold under the cursor?", "<code>zc</code> (<b>c</b>lose fold)", "L2_composition")
c("Workflows", "What does <code>za</code> do for folds?", "Toggle fold open/closed (<b>a</b>lternate)", "L2_composition")
c("Workflows", "What does <code>zR</code> do?", "Open all folds in the file (<b>R</b>eveal all)", "L2_composition")
c("Workflows", "What does <code>zM</code> do?", "Close all folds in the file (<b>M</b>inimize all)", "L2_composition")
c("Workflows", "What does <code>:set foldmethod=syntax</code> do?", "Automatically create folds based on syntax (language structure)", "L2_composition")
c("Workflows", "What does <code>:set foldmethod=marker</code> do?", "Create folds at <code>{{{</code> and <code>}}}</code> markers in the file", "L2_composition")

# ============================================================
# DECK 09: GOTCHAS (Diagnosis)
# ============================================================

# L4 — Diagnosis cards
c("Gotchas", "You paste code into Vim and the indentation cascades into chaos. What happened?", "Auto-indent is fighting the paste. Use <code>:set paste</code> before pasting, or use <code>\"+p</code> (from clipboard) if <code>paste</code> mode is set, or use <code>]p</code> for paste with indent adjustment.", "L4_diagnosis")
c("Gotchas", "You're stuck in Insert mode and <code>Esc</code> feels too far. What are faster alternatives?", "<code>C-[</code> (always works), or remap with <code>:inoremap jk &lt;Esc&gt;</code> or <code>:inoremap kj &lt;Esc&gt;</code>", "L4_diagnosis")
c("Gotchas", "You get <code>E212: Can't open file for writing</code>. What does this mean and how to fix?", "You don't have write permission or the directory doesn't exist. Use <code>:w !sudo tee %</code> to write with sudo, or <code>:w /tmp/file</code> to save elsewhere then move separately.", "L4_diagnosis")
c("Gotchas", "You see a <code>.swp</code> file warning when opening a file. What happened?", "A swap file exists from a previous Vim session that didn't close cleanly (crash, killed terminal). Choose <code>R</code> to Recover, <code>D</code> to Delete the swap, or <code>Q</code> to Quit.", "L4_diagnosis")
c("Gotchas", "You accidentally hit <code>C-z</code> and Vim disappeared. What happened and how do you get back?", "Vim was suspended to the background. Type <code>fg</code> in the terminal to bring it back to the foreground.", "L4_diagnosis")
c("Gotchas", "You see <code>-- INSERT (paste) --</code> at the bottom and can't auto-indent. What's wrong?", "You're in Paste mode. Disable it with <code>:set nopaste</code>. Paste mode disables auto-indent and auto-complete to preserve pasted formatting.", "L4_diagnosis")
c("Gotchas", "Your search/replace with <code>/</code> in <code>:s/foo/bar/g</code> fails. What's the likely culprit?", "Special regex characters need escaping: <code>.</code> <code>*</code> <code>[</code> <code>]</code> <code>/</code> etc. Use <code>\\</code> to escape them, or use the <code>\\V</code> very-magic prefix to disable most special meanings.", "L4_diagnosis")
c("Gotchas", "You press <code>q</code> and see <code>recording</code> in the status line but didn't mean to. How to stop?", "Press <code>q</code> again to stop recording. The keystrokes up to that point are saved in the <code>\"</code> register — you may want to clear it.", "L4_diagnosis")
c("Gotchas", "Why is <code>J</code> (join) inserting a space between joined lines?", "This is intended behavior: Vim inserts one space between joined lines. Use <code>gJ</code> to join without adding a space.", "L4_diagnosis")
c("Gotchas", "You typed <code>:</code> and can't exit because characters won't go away. How to cancel?", "Press <code>C-c</code> or <code>Esc</code> to cancel the command-line mode and return to Normal mode.", "L4_diagnosis")
c("Gotchas", "Vim won't let you backspace past where you started Insert mode. Why?", "Vim's default behavior limits backspace. Add to vimrc: <code>set backspace=indent,eol,start</code> to allow backspacing over everything.", "L4_diagnosis")
c("Gotchas", "You search and replace and some matches are skipped. What's happening?", "The <code>gdefault</code> option may be set, or <code>:s</code> without <code>/g</code> only replaces the first match per line. Also check <code>ignorecase</code> vs <code>smartcase</code> settings.", "L4_diagnosis")

# ============================================================
# DECK 10: ADVANCED — Design, Opinion, Innovation
# ============================================================

# L3 — Design
c("Advanced", "Why is modal editing efficient?", "Each key gains power by context — the same key <code>w</code> moves a word in Normal mode but types 'w' in Insert mode. Keeps most-used operations (navigation, editing) on home row without chords.", "L3_design")
c("Advanced", "Why did Vim choose <code>hjkl</code> for cursor movement?", "The ADM-3A terminal that Bill Joy used had arrow keys printed on <code>h</code> <code>j</code> <code>k</code> <code>l</code>. Home-row movement became a Vim tradition and reduces hand strain.", "L3_design")
c("Advanced", "What is the <code>&lt;leader&gt;</code> key and why use it?", "A user-definable prefix key (default <code>\\</code>, commonly remapped to <code>Space</code> or <code>,</code>) for personal custom keybindings. It namespaces your custom mappings to avoid conflicts with built-in keys.", "L3_design")
c("Advanced", "What is the philosophy behind Vim's 'composable' command language?", "Commands follow the pattern <code>[count][operator][motion/text-object]</code>. Master ~12 operators and ~30 motions, and you can generate hundreds of precise editing operations. It's like learning vocabulary, not memorizing phrases.", "L3_design")
c("Advanced", "Why does Vim use registers instead of just one clipboard?", "Multiple registers enable complex workflows: record a macro in register <code>a</code>, yank text to register <code>b</code>, and paste from <code>c</code> — all without overwriting. The unnamed register is just the tip.", "L3_design")

# L5 — Opinion
c("Advanced", "vim-plug vs vundle vs Vim 8 native packages: which to use?", "Native packages (<code>~/.vim/pack/*/start/</code>) work without a plugin manager and ship with Vim 8+. vim-plug adds parallel installs, lazy loading, and post-update hooks. vundle is legacy. For pure Vim, native packages or vim-plug are the modern choices.", "L5_opinion")
c("Advanced", "relativenumber vs number: which is better?", "<code>relativenumber</code> shows line distances (great for <code>5j</code> <code>3dd</code> commands). <code>number</code> shows absolute line numbers. Many use both: <code>relativenumber</code> with <code>number</code> so the current line shows its absolute number.", "L5_opinion")
c("Advanced", "When should you use VS Code with a Vim plugin instead of pure Vim?", "When you need rich IDE features (IntelliSense, debugger GUI, markdown preview) with a shallow Vim learning curve. Pure Vim excels for terminal-native workflows, remote editing over SSH, and keyboard-only environments.", "L5_opinion")
c("Advanced", "What are 'sane defaults' for a minimal .vimrc?", "<code>set nocompatible hidden wildmenu showcmd hlsearch incsearch ignorecase smartcase backspace=indent,eol,start autoindent ruler laststatus=2 confirm</code> — plus <code>filetype plugin indent on</code> and <code>syntax on</code>", "L5_opinion")
c("Advanced", "What is the argument for NOT remapping <code>,</code> as leader?", "<code>,</code> is the reverse of <code>;</code> for <code>f/F/t/T</code> repetition. Remapping it costs a useful motion. <code>Space</code> as leader is popular because it's unused in Normal mode.", "L5_opinion")
c("Advanced", "Is <code>jk</code> or <code>kj</code> a better <code>Esc</code> mapping?", "Both work. <code>jk</code> is slightly more ergonomic (inward roll). The key is to pick one and build muscle memory. Caveat: you'll never type 'jk' or 'kj' in Insert mode — plan accordingly for words like 'Dijkstra'.", "L5_opinion")

# L6 — Innovation
c("Advanced", "What is an autocmd in Vim?", "An automatic command triggered by events: <code>:autocmd BufWritePre *.py %s/\\s\\+$//e</code> strips trailing whitespace from Python files before every save.", "L6_innovation")
c("Advanced", "How do you define an autocmd to set shiftwidth per filetype?", "<code>autocmd FileType python setlocal shiftwidth=4 tabstop=4</code> in your vimrc", "L6_innovation")
c("Advanced", "What is an <code>operatorfunc</code> custom operator?", "You can create your own operators by setting <code>operatorfunc</code> and using <code>g@</code>. Vim will call your function with the motion range. Used by plugins for commentary, alignment, etc.", "L6_innovation")
c("Advanced", "How do you create a custom text object?", "Use <code>:omap</code> or the <code>textobj-user</code> plugin. In pure Vim you can map custom sequences: e.g. <code>vnoremap a, :&lt;C-u&gt;normal! f,vt,&lt;CR&gt;</code> for comma-separated arguments.", "L6_innovation")
c("Advanced", "What is the minimal Vimscript boilerplate for a plugin?", "A file in <code>~/.vim/plugin/</code> or <code>~/.vim/pack/*/start/plugin/</code> with <code>if exists('g:loaded_myplugin') | finish | endif</code> guard, then <code>command!</code>, <code>nnoremap</code>, and function definitions.", "L6_innovation")
c("Advanced", "How do you customize the Vim statusline?", "Set <code>laststatus=2</code> and build a <code>statusline</code> string with format items like <code>%f</code> (filename), <code>%m</code> (modified flag), <code>%y</code> (filetype), <code>%=</code> (left/right split), <code>%l,%c</code> (line,column), <code>%P</code> (percentage).", "L6_innovation")
c("Advanced", "What does <code>:map-expression</code> (<code>map-expr</code>) allow?", "A mapping that evaluates a Vimscript expression to determine the resulting keys. E.g. <code>:nnoremap &lt;expr&gt; j v:count ? 'j' : 'gj'</code> wraps lines only when no count is given.", "L6_innovation")
c("Advanced", "How do you write a simple Vimscript function to toggle a setting?", "<pre><code>function! ToggleSpell()\n  setlocal spell!\n  echo &amp;spell ? 'Spell ON' : 'Spell OFF'\nendfunction\nnnoremap &lt;leader&gt;s :call ToggleSpell()&lt;CR&gt;</code></pre>", "L6_innovation")

# ============================================================
# ASSEMBLE & OUTPUT
# ============================================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
