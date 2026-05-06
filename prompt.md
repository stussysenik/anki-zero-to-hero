# Anki Deck Generator — Zero-to-Hero Mastery Prompt

## How to use
Feed this entire file to an LLM along with your topic:
```
Create a deck on "{TOPIC}" using the instructions in @deck-prompt.md
```

The LLM will research, scaffold, and output a Python script that builds a comprehensive `.apkg` Anki deck.

---

## Phase 0 — Scope Calibration (internal reasoning, do not skip)

Before writing any cards, internally map the topic's **mastery landscape**. Think in levels:

| Level | Label | What it covers |
|-------|-------|---------------|
| L0 | Primitives | Definitions, first principles, the "what" — no prior knowledge assumed |
| L1 | Mechanics | Syntax, keybindings, operations, the "how" — muscle memory |
| L2 | Composition | Composing primitives into workflows, patterns, conventions |
| L3 | Design | Trade-offs, architecture decisions, why things are built a certain way |
| L4 | Diagnosis | Debugging, anti-patterns, common mistakes, error recovery |
| L5 | Opinion | When to use X over Y, idiosyncratic best practices, style |
| L6 | Innovation | Extending, scripting, plumbing internals, creating new abstractions |

For **tools/editors/languages**, weight heavily on L0–L2 (people need reps). For **conceptual topics**, weight L3–L5. Always include at least 5 cards at L6 — these are the "staff engineer" cards that separate deep users from surface users.

---

## Phase 1 — Research (do this in parallel via web search + reasoning)

Research these categories before writing. For each, produce a bullet list in your internal scratchpad:

1. **First principles** — What are the 10–20 foundational concepts someone must understand before anything makes sense?
2. **Core operations** — What are the 50–100 most frequent actions a practitioner performs daily? Prioritize by frequency, not by "coolness."
3. **Workflows** — What are the 5–10 common end-to-end workflows (e.g., "clone → branch → edit → commit → push")?
4. **Sharp edges** — What are the 10–20 most common mistakes, confusing behaviors, or gotchas?
5. **Opinions & taste** — What do experts disagree about? What are the "correct" ways that aren't obvious? What do staff-level practitioners know that seniors don't?
6. **Extension points** — How do you script/automate/extend the thing? What internals matter?
7. **Reference cheat-sheet** — What facts are pure lookup (keybindings, flags, syntax) that benefit from spaced repetition?

If the topic has an official documentation site, cheat-sheet page, or keyboard-shortcut reference, **fetch it** via web search and extract cards from it.

---

## Phase 2 — Card Writing Rules

### One concept per card. Always.
Bad: "What are the movement keys in vim?" (too broad — 4+ answers)
Good: "Move cursor left in normal mode?" → `<code>h</code>`

### Front (question) rules:
- Ask from the user's perspective: "How do you..." / "What is..." / "Which key..."
- Include just enough context to disambiguate — e.g. "(Emacs style)" prefix
- Never use pronouns without antecedent
- Make it the thing you'd actually ask yourself during practice

### Back (answer) rules:
- Answer first, elaboration after a line break if needed
- Use `<code>` tags for keybindings, commands, code
- Use `<br>` for multi-part answers (not multiple paragraphs)
- For keybinding cards, the key IS the answer — put it in code
- For concept cards, definition first, then a brief "why it matters" sentence

### Muscle memory cards:
For any physical action (keybinding, mouse gesture, CLI flag), format:
```
Front: "What do you press to {action}?"
Back:  "<code>{keys}</code>"
```
These are the majority of cards for tool/editor topics. They create the mechanical recall that makes you fluid.

### Depth tagging:
Add a tag to each note indicating the level: `L0_primitives`, `L1_mechanics`, `L2_composition`, `L3_design`, `L4_diagnosis`, `L5_opinion`, `L6_innovation`. This lets the user filter by depth.

### Card count targets (per topic):
- Simple tool (e.g., `jq`, `sed`): 80–120 cards
- Editor/IDE (e.g., Spacemacs, Helix): 180–300 cards  
- Language (e.g., Rust, Elixir): 250–500 cards
- Conceptual (e.g., DSPy, Distributed Systems): 120–200 cards
- Framework (e.g., React, Kubernetes): 200–350 cards

Err on the side of MORE cards. The user controls how many they study per day. It's better to have a card you suspend than to miss a concept.

Err on the side of MORE cards. The user controls how many they study per day. It's better to have a card you suspend than to miss a concept.

---

## Phase 3 — Deck Organization

Use **genanki** to create the deck. Structure:

```python
import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)

# Model with Front/Back fields and clean CSS (dark theme, monospace code)
model = genanki.Model(
    R(), "{Topic} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""".card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px;
                text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; }
           .front { font-weight: bold; margin-top: 60px; }
           .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
           code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244;
                       padding: 2px 6px; border-radius: 4px; font-size: 18px; }
           hr { border-color: #45475a; }"""
)

# Subdecks using :: hierarchy separator (Anki auto-groups into tree)
decks = {
    "Fundamentals":  genanki.Deck(R(), "{Topic}::Zero2Hero::01-Fundamentals"),
    "CoreOps":       genanki.Deck(R(), "{Topic}::Zero2Hero::02-Core-Operations"),
    "Patterns":      genanki.Deck(R(), "{Topic}::Zero2Hero::03-Common-Patterns"),
    "Workflows":     genanki.Deck(R(), "{Topic}::Zero2Hero::04-Workflows"),
    "Gotchas":       genanki.Deck(R(), "{Topic}::Zero2Hero::05-Gotchas"),
    "Expert":        genanki.Deck(R(), "{Topic}::Zero2Hero::06-Expert-Techniques"),
    "Internals":     genanki.Deck(R(), "{Topic}::Zero2Hero::07-Internals-Extending"),
}

# Use a convenience function — cleaner than a literal list for 100+ cards
C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# Cards: one c() call per concept. Write them inline below.
c("Fundamentals", "What is X?",
  "Definition — why it matters.",
  ["L0_primitives"])

# ... all other c() calls ...

# Build & write
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))
genanki.Package(list(decks.values())).write_to_file("{Topic}_Zero_to_Hero.apkg")
print(f"Built {len(C)} cards across {len(decks)} decks")
```

### A note on HTML in card text:
- Use `<code>` and `<br>` freely — they're standard HTML tags safe in Anki fields.
- **Raw `<` and `>` characters in non-code text** (like shell heredocs `<<EOF`, or visual selection ranges `:'<,'>`) will trigger genanki warnings. Escape them as `&lt;` and `&gt;` or wrap in `<code>` if they're keyboard references.
- Use `&lt;leader&gt;` for the leader key placeholder, `&lt;C-n&gt;` for control-keys in non-code contexts.

### Subdeck naming convention:
Use `{Topic}::Zero2Hero::{NN-Category}` where NN is a zero-padded number for ordering. Anki auto-groups `::` into a hierarchy.

Recommended categories (adapt to topic):
- `01-Fundamentals`
- `02-Core-Operations`
- `03-Workflows`
- `04-Common-Patterns`
- `05-Gotchas`
- `06-Expert-Techniques`
- `07-Internals-Extending`

### CSS:
Dark theme by default (developers study at night). Monospace for code. Large readable font (20–22px). Clean, no clutter.

---

## Phase 4 — Quality Verification

Before outputting the script, verify EVERY card against these rules:

1. **No compound cards** — Every card asks exactly one thing. Split "What does x do and why is it important?" into two cards.
2. **All keybindings reverse-searchable** — Could the user guess the question from the answer alone? If yes, the front is too vague.
3. **Level coverage** — At least 3 cards in each L0–L6 level. L0 and L1 should be ~50% of total cards for tool topics.
4. **No outdated info** — If the topic has version-specific behavior, note the version in the card.
5. **Tags are correct** — Each card tagged with exactly its mastery level tag(s).
6. **Genanki output is runnable** — The script requires only `genanki` (install via `pip install genanki`). No other imports needed.
7. **HTML hygiene** — No unescaped `<` or `>` outside `<code>` tags.

After writing the script, include this self-check snippet as a comment at the bottom and verify the script passes it:

```python
# VERIFICATION (run this block after build):
# import zipfile, sqlite3, json
# FILENAME = "{Topic}_Zero_to_Hero.apkg".replace(" ", "_")
# with zipfile.ZipFile(FILENAME) as z: z.extract("collection.anki2", "/tmp/")
# db = sqlite3.connect("/tmp/collection.anki2")
# n, c = db.execute("SELECT count(*) FROM notes").fetchone()[0], db.execute("SELECT count(*) FROM cards").fetchone()[0]
# decks = json.loads(db.execute("SELECT decks FROM col").fetchone()[0])
# print(f"Notes: {n}, Cards: {c}")
# for v in decks.values():
#     if v["name"] != "Default": print(f"  {v['name']}")
# assert n == c == len(C), f"Mismatch: {n} notes, {c} cards, {len(C)} defined"
```

---

## Phase 5 — Output

Output ONLY the Python script in a code block. The user will save and run it. No explanation, no summary — just the script.

The script should:
- Be self-contained (all card data inline)
- Use random IDs for model and decks (via `random.randrange(1<<30, 1<<31)`)
- Print `"Built {decks} decks with {total} cards -> {filename}"` on completion
- Save `.apkg` to the current directory with filename `{Topic}_Zero_to_Hero.apkg` (replace spaces with underscores)

---

## Example card triplets (few-shot)

```python
# L0 - Primitive
c("Fundamentals", "What is a buffer in Emacs?",
  "An in-memory object holding text — often a file's contents. NOT the same as the file on disk.",
  ["L0_primitives"])

# L1 - Mechanics (keybinding = muscle memory)
c("Navigation", "(Vim) Delete the current line?",
  "<code>dd</code> — also yanks it to the default register",
  ["L1_mechanics"])

# L2 - Composition
c("Workflows", "How do you rename a variable across the entire project using LSP?",
  "<code>SPC m r r</code> — LSP finds all references and renames them atomically",
  ["L2_composition"])

# L3 - Design
c("Design", "When should a Spacemacs layer be a 'private' layer vs a contributed layer?",
  "Private: personal config, company-specific tooling, experimental. Contributed: general-purpose, well-documented, follows Spacemacs conventions. Start private, promote to contributed when battle-tested.",
  ["L3_design"])

# L4 - Diagnosis
c("Gotchas", "You opened a file as root via TRAMP but changes won't save. Why?",
  "TRAMP uses a separate buffer with different permissions. Use <code>SPC f E</code> instead, or <code>:w /sudo::/path/to/file</code> to force write with elevated permissions.",
  ["L4_diagnosis"])

# L5 - Opinion
c("Opinion", "Should you use Treemacs or Neotree in Spacemacs?",
  "Treemacs: better for large projects, has follow-mode, git integration, and workspace support. Neotree: simpler, lighter. Use Treemacs unless on a very low-resource machine.",
  ["L5_opinion"])

# L6 - Innovation
c("Extending", "How do you add a custom which-key menu under SPC o?",
  "In <code>dotspacemacs/user-config</code>: <code>(spacemacs/declare-prefix \"ot\" \"my-tools\")</code> then <code>(spacemacs/set-leader-keys \"ott\" 'my-custom-tool)</code>",
  ["L6_innovation"])
```
