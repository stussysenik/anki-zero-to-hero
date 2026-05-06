# Anki Zero-to-Hero

LLM-powered Anki deck generator for spaced-repetition mastery. One prompt → comprehensive flashcard deck → import into Anki.

## Table of Contents

- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Deck Index](#deck-index)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## How It Works

Three artifacts, one pipeline:

```
                      ┌──────────────────────┐
                      │     prompt.md        │  Master instruction set.
                      │  Phase 0-5 research, │  Feed to any LLM with
                      │  card rules, genanki │  a topic to generate the
                      │  template, verify    │  build script.
                      └─────────┬────────────┘
                                │ "Make deck on {TOPIC}"
                                ▼
                      ┌──────────────────────┐
                      │   build_{topic}.py   │  LLM-generated script.
                      │  genanki deck model, │  Self-contained — all
                      │  all c() card calls, │  card data inline.
                      │  subdeck structure   │
                      └─────────┬────────────┘
                                │  python build_{topic}.py
                                ▼
                      ┌──────────────────────┐
                      │  {Topic}_Z2H.apkg    │  Standalone Anki package.
                      │  Anki SQLite DB      │  Import via File → Import
                      │  hierarchical decks  │  or double-click.
                      │  dark theme CSS      │
                      └──────────────────────┘
```

1. **`prompt.md`** — The master prompt. A 5-phase instruction set that tells the LLM how to research a topic, write high-quality cards across 7 mastery levels, and output a runnable Python script. Includes formatting rules, genanki boilerplate, and self-verification checks.

2. **`scripts/*.py`** — The generated Python scripts. Each is self-contained, requires only `genanki`, and produces a single `.apkg` file. Cards follow the Zero-to-Hero methodology: L0 primitives → L6 innovation.

3. **`decks/*.apkg`** — The compiled Anki packages. Import directly into Anki Desktop/AnkiDroid/AnkiWeb. Each deck uses `::` hierarchy for subdeck organization.

### Mastery Levels

Each card is tagged by depth, letting you filter your study:

| Level | Label      | Focus                                          |
|-------|------------|------------------------------------------------|
| L0    | Primitives | First principles, definitions, the "what"      |
| L1    | Mechanics  | Syntax, keybindings, daily operations          |
| L2    | Composition| Workflows, patterns, combining primitives      |
| L3    | Design     | Trade-offs, architecture, why things work      |
| L4    | Diagnosis  | Debugging, anti-patterns, common mistakes      |
| L5    | Opinion    | When X over Y, style, best practices           |
| L6    | Innovation | Extending, scripting, internals, new patterns  |

## Project Structure

```
anki-zero-to-hero/
├── README.md          ← You are here
├── prompt.md          ← Master LLM prompt (the engine)
├── requirements.txt   ← Python dependency (genanki)
├── .gitignore
├── scripts/           ← 27 Python deck builders
│   ├── rust.py
│   ├── go.py
│   ├── zig.py
│   ├── nim.py
│   ├── ocaml.py
│   ├── gleam.py
│   ├── clojure.py
│   ├── rescript.py
│   ├── phoenix_elixir.py
│   ├── nextjs.py
│   ├── flutter.py
│   ├── tailwind_css.py
│   ├── gsap.py
│   ├── rive.py
│   ├── view_transitions_api.py
│   ├── zustand.py
│   ├── jotai.py
│   ├── xstate.py
│   ├── unreal_engine.py
│   ├── figma.py
│   ├── build_swift_deck.py
│   ├── build_jsts_deck.py
│   ├── build_react_deck.py
│   ├── build_python_stdlib_deck.py
│   ├── build_dspy_deck.py
│   ├── build_nvim_deck.py
│   └── build_spacemacs_deck.py
└── decks/             ← 27 importable Anki packages
    ├── Rust_Zero_to_Hero.apkg
    ├── Go_Zero_to_Hero.apkg
    ├── ... (24 more)
    └── Zustand_Zero_to_Hero.apkg
```

## Quick Start

### Use existing decks
```bash
# Import directly into Anki
open decks/Rust_Zero_to_Hero.apkg    # macOS
xdg-open decks/Rust_Zero_to_Hero.apkg  # Linux
```

### Generate a new deck
```bash
pip install -r requirements.txt

# Feed prompt.md to an LLM with your topic:
# "Create a deck on 'Kubernetes' using the instructions in @prompt.md"

# Save the output as scripts/build_kubernetes_deck.py, then:
python scripts/build_kubernetes_deck.py
# → Built 7 decks with 250 cards -> Kubernetes_Zero_to_Hero.apkg
```

## Deck Index

### Languages
| Deck | Cards | Focus |
|------|-------|-------|
| [Rust](decks/Rust_Zero_to_Hero.apkg) | ~60 | Ownership, borrow checker, traits, concurrency |
| [Go](decks/Go_Zero_to_Hero.apkg) | ~60 | Goroutines, channels, interfaces, patterns |
| [Zig](decks/Zig_Zero_to_Hero.apkg) | ~100 | Comptime, allocators, C interop, build system |
| [Nim](decks/Nim_Zero_to_Hero.apkg) | ~100 | Macros, pragmas, GC modes, metaprogramming |
| [OCaml](decks/OCaml_Zero_to_Hero.apkg) | ~100 | Modules, functors, GADTs, type system |
| [Gleam](decks/Gleam_Zero_to_Hero.apkg) | ~100 | BEAM interop, pipe, patterns, OTP |
| [Clojure](decks/Clojure_Zero_to_Hero.apkg) | ~100 | Macros, atoms, transducers, REPL workflow |
| [ReScript](decks/ReScript_Zero_to_Hero.apkg) | ~100 | Variants, pipe, bindings, React interop |
| [JS/TS](decks/JS_TS_Zero_to_Hero.apkg) | ~390 | Event loop, prototypes, TS advanced, DOM |

### Frameworks & Libraries
| Deck | Cards | Focus |
|------|-------|-------|
| [React](decks/React_Zero_to_Hero.apkg) | ~300 | Hooks, fiber, server components, patterns |
| [Next.js](decks/Next.js_Zero_to_Hero.apkg) | ~220 | App router, RSC, ISR, middleware |
| [Flutter](decks/Flutter_Zero_to_Hero.apkg) | ~100 | Widget tree, state, navigation, rendering |
| [Zustand](decks/Zustand_Zero_to_Hero.apkg) | ~50 | Store, slices, middleware, immer |
| [Jotai](decks/Jotai_Zero_to_Hero.apkg) | ~50 | Atoms, derived, async, scoped state |
| [XState](decks/XState_Zero_to_Hero.apkg) | ~100 | FSM, actors, guards, spawned machines |
| [GSAP](decks/GSAP_Zero_to_Hero.apkg) | ~100 | Timelines, scroll triggers, FLIP, plugins |
| [Rive](decks/Rive_Zero_to_Hero.apkg) | ~100 | State machines, bones, runtime API |

### CSS & Animation
| Deck | Cards | Focus |
|------|-------|-------|
| [Tailwind CSS](decks/Tailwind_CSS_Zero_to_Hero.apkg) | ~100 | Utility classes, config, dark mode, plugins |
| [View Transitions API](decks/View_Transitions_API_Zero_to_Hero.apkg) | ~70 | startViewTransition, ::view-transition-*, MPA |

### Platforms & Tools
| Deck | Cards | Focus |
|------|-------|-------|
| [Swift/Apple](decks/Swift_Apple_Zero_to_Hero.apkg) | ~380 | Swift, SwiftUI, Combine, Core ML, Xcode |
| [Unreal Engine](decks/Unreal_Engine_Zero_to_Hero.apkg) | ~100 | Blueprints, C++, replication, materials |
| [Figma](decks/Figma_Zero_to_Hero.apkg) | ~100 | Components, auto-layout, variables, dev-mode |
| [NVIM](decks/NVIM_Zero_to_Hero.apkg) | ~200 | Keybindings, Lua config, LSP, treesitter |
| [Spacemacs](decks/Spacemacs_Zero_to_Hero.apkg) | ~250 | Layers, evil, which-key, org-mode |

### Libraries & Specialized
| Deck | Cards | Focus |
|------|-------|-------|
| [Python Stdlib](decks/Python_Stdlib_Zero_to_Hero.apkg) | ~250 | itertools, pathlib, asyncio, dataclasses |
| [DSPy](decks/DSPy_Zero_to_Hero.apkg) | ~150 | Modules, optimizers, signatures, retrieval |
| [Phoenix/Elixir](decks/Phoenix_Elixir_Zero_to_Hero.apkg) | ~100 | LiveView, channels, Ecto, OTP |

> Card counts are approximate. Imports may differ slightly from script runs due to Anki's merging behavior. Run the corresponding script for exact counts.

## Dependencies

### For using existing decks
- [Anki](https://apps.ankiweb.net/) (Desktop) or [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) — no other dependencies.

### For generating new decks
- **Python 3.8+**
- **[genanki](https://github.com/kerrickstaley/genanki)** — `pip install genanki`

### For generating new decks via LLM
- Any capable LLM (Claude, GPT-4, DeepSeek, Gemini)
- Feed `prompt.md` as context + your topic as the instruction

## Contributing

1. Pick a topic missing from the [Deck Index](#deck-index)
2. Feed `prompt.md` to an LLM with: `Create a deck on "{TOPIC}" using the instructions in @prompt.md`
3. Save the output as `scripts/build_{topic}_deck.py`
4. Run `python scripts/build_{topic}_deck.py` to generate the `.apkg`
5. Move the `.apkg` to `decks/`
6. PR with the script and deck

### Script conventions
- Filename: `{lowercase_topic}.py` or `build_{topic}_deck.py`
- Uses `genanki` with random model/deck IDs
- Cards tagged with L0-L6 mastery levels
- Subdecks via `{Topic}::Zero2Hero::{NN-Category}` naming
- Dark theme CSS, Fira Code monospace
- Output filename: `{Topic}_Zero_to_Hero.apkg`

## License

MIT — the prompt, scripts, and decks are free to use, modify, and distribute.
