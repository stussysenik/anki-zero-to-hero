import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Zig"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Memory":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Memory-Management"),
    "CompileTime":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Comptime"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === ZIG FUNDAMENTALS ===

c("Fundamentals", "What is Zig?",
  "A general-purpose systems programming language and toolchain. Designed for robustness, optimality, and clarity. No hidden control flow, no hidden allocations, no preprocessor, no macros. Targets C ABI compatibility.",
  ["L0_primitives"])

c("Fundamentals", "What makes Zig different from Rust?",
  "Zig has no borrow checker, no lifetimes, no traits. Manual memory management with safety checks in debug mode. Simpler — you control allocation explicitly. Zig can compile C code natively; Rust needs bindings.",
  ["L0_primitives"])

c("Fundamentals", "What is Zig's approach to memory management?",
  "Explicit and manual — NO hidden allocations. All allocators are passed explicitly as parameters. Standard library provides: <code>page_allocator</code>, <code>GeneralPurposeAllocator</code> (debugging), <code>ArenaAllocator</code>, <code>FixedBufferAllocator</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>comptime</code> in Zig?",
  "Compile-time code execution. Any function can be run at compile time. Types are first-class values that can be computed at compile time. Replace macros, generics, and codegen with a single, unified mechanism.",
  ["L0_primitives"])

c("Fundamentals", "What is Zig's <code>build.zig</code>?",
  "The build system is written in Zig itself (not Make/CMake). <code>build.zig</code> is a Zig program that configures compilation, linking, cross-compilation, and testing. Fast, cross-platform, and hackable.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>defer</code> in Zig?",
  "Executes a statement when the current scope exits: <code>defer allocator.free(buf);</code>. Multiple defers execute in LIFO order (last declared, first executed). Replaces <code>goto cleanup</code> / RAII for resource cleanup.",
  ["L0_primitives"])

c("Fundamentals", "What is an error union type?",
  "<code>!T</code> — a value or an error. <code>fn foo() !i32 { return 42; }</code>. Must be handled: <code>const x = try foo();</code> (returns error) or <code>foo() catch |err| { ... }</code>. No exceptions — errors are values.",
  ["L0_primitives"])

c("Fundamentals", "What is an optional type in Zig?",
  "<code>?T</code> — either a value of type T or <code>null</code>. <code>var x: ?i32 = null;</code>. Unwrap: <code>if (x) |val| { ... }</code>. <code>x orelse 0</code> — default value. No implicit nulls — must be declared optional.",
  ["L0_primitives"])

c("Fundamentals", "What is Zig's <code>@cImport</code>?",
  "Direct inclusion of C headers in Zig code: <code>const c = @cImport({ @cInclude(\"stdio.h\"); });</code>. Zig bundles a C compiler — no external tooling. Call <code>c.printf()</code> directly. Zig IS a C compiler.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>struct</code> vs <code>packed struct</code> in Zig?",
  "Regular struct: compiler chooses field layout for alignment. <code>packed struct</code>: no padding between fields, bit-level layout guaranteed. <code>extern struct</code>: matches C ABI layout. Choose based on memory/ABI requirements.",
  ["L0_primitives"])

c("Fundamentals", "What is Zig's <code>anytype</code>?",
  "A placeholder for an inferred type: <code>fn max(a: anytype, b: anytype) { ... }</code>. The function is duplicated at compile time for each type combination (duck typing). No virtual dispatch — monomorphized like C++ templates.",
  ["L0_primitives"])

# === ZIG CORE OPERATIONS ===

c("CoreOps", "How do you declare a variable?",
  "<code>var x: i32 = 42;</code> — mutable. <code>const y: i32 = 42;</code> — immutable. <code>const z = 42;</code> — type inferred. <code>var x: i32 = undefined;</code> — uninitialized (unsafe, debug mode catches reads).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a function?",
  "<code>fn add(a: i32, b: i32) i32 { return a + b; }</code>. <code>fn main() !void { ... }</code> — with error union return. <code>fn noReturn() noreturn { while (true) {} }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create an array?",
  "<code>const arr = [_]i32{1, 2, 3};</code> — inferred size. <code>const arr: [3]i32 = [3]i32{1, 2, 3};</code> — explicit size. <code>arr.len</code> returns length. <code>&amp;arr</code> is a pointer to the first element.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a slice?",
  "<code>arr[0..3]</code> — slice of array, type is <code>[]i32</code>. Slices are fat pointers (pointer + length). <code>slice.len</code>. Functions that accept slices work with arrays and sub-slices generically.",
  ["L1_mechanics"])

c("CoreOps", "How do you allocate memory?",
  "Pass an allocator: <code>var list = std.ArrayList(i32).init(allocator);</code>. <code>defer list.deinit();</code>. Raw: <code>const buf = try allocator.alloc(u8, 1024);</code> <code>defer allocator.free(buf);</code>. No <code>malloc</code> hidden anywhere.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle errors?",
  "<code>const x = try mightFail();</code> — returns error to caller. <code>mightFail() catch |err| { handle(err); }</code>. <code>mightFail() catch 0</code> — default. <code>if (mightFail()) |val| { ... } else |err| { ... }</code>. Errors are values, not exceptions.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an if statement?",
  "<code>if (x &gt; 0) { positive(); } else if (x &lt; 0) { negative(); } else { zero(); }</code>. <code>if</code> as expression: <code>const s = if (x &gt; 0) \"pos\" else \"neg\";</code>. Optional unwrap: <code>if (opt) |val| { use(val); }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a for loop?",
  "<code>for (arr) |item| { ... }</code>. With index: <code>for (arr, 0..) |item, i| { ... }</code>. Range: <code>for (0..10) |i| { ... }</code>. Iterating maps: <code>for (map.keys()) |key| { ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a while loop?",
  "<code>while (condition) { ... }</code>. With continue expression: <code>while (i &lt; 10) : (i += 1) { ... }</code>. Optional/error unwrap: <code>while (stream.read()) |chunk| { ... } else |err| { ... }</code> — iterates until null or error.",
  ["L1_mechanics"])

c("CoreOps", "How do you create and use a struct?",
  "<code>const Point = struct { x: f64, y: f64 };</code>. Create: <code>const p = Point{ .x = 1.0, .y = 2.0 };</code>. Default: <code>const p: Point = .{ .x = 1.0, .y = 2.0 };</code> (type inferred). Access: <code>p.x</code>, <code>p.*</code> for pointer deref.",
  ["L1_mechanics"])

c("CoreOps", "How do you switch in Zig?",
  "<code>switch (value) { 0 =&gt; ..., 1, 2 =&gt; ..., else =&gt; ... }</code>. Expression: <code>const s = switch (x) { 0 =&gt; \"zero\", else =&gt; \"non\" };</code>. On tagged unions: <code>switch (u) { .int =&gt; |i| ..., .float =&gt; |f| ... }</code>. Must be exhaustive.",
  ["L1_mechanics"])

c("CoreOps", "How do you run Zig tests?",
  "<code>test \"my test\" { try std.testing.expect(1 + 1 == 2); }</code>. Run: <code>zig test file.zig</code>. In build.zig: add <code>exe.addTest(\"src/main.zig\");</code>. Tests are Zig code — any <code>comptime</code> available.",
  ["L1_mechanics"])

# === MEMORY ===

c("Memory", "What is the <code>GeneralPurposeAllocator</code>?",
  "A debugging allocator that detects memory leaks, double-frees, and use-after-free. Used during development: <code>var gpa = std.heap.GeneralPurposeAllocator(.{}){}; const allocator = gpa.allocator(); defer _ = gpa.deinit();</code>. Check <code>gpa.deinit()</code> for leaks.",
  ["L1_mechanics"])

c("Memory", "What is the <code>ArenaAllocator</code>?",
  "Bumps a pointer, frees all at once. <code>var arena = std.heap.ArenaAllocator.init(page_allocator); defer arena.deinit();</code>. Cannot free individual allocations — good for short-lived batches (HTTP request processing).",
  ["L1_mechanics"])

c("Memory", "What is <code>errdefer</code>?",
  "Like <code>defer</code> but only executes if the scope exits with an error. <code>errdefer allocator.free(buf);</code>. Perfect for cleanup of partially constructed objects when an error occurs.",
  ["L1_mechanics"])

c("Memory", "What are <code>sentinel-terminated</code> arrays and slices?",
  "<code>[:0]const u8</code> — slice with null terminator, compatible with C strings. <code>[*:0]const u8</code> — pointer to null-terminated array. Zig understands sentinels and checks them in debug mode.",
  ["L1_mechanics"])

# === COMPTIME ===

c("CompileTime", "What can <code>comptime</code> do?",
  "Execute any function at compile time. Generate types: <code>fn Matrix(comptime T: type, comptime rows: usize, comptime cols: usize) type { ... }</code>. Loop unrolling, precomputed lookup tables, code generation. Replaces templates, generics, macros.",
  ["L1_mechanics"])

c("CompileTime", "How do you use <code>comptime var</code>?",
  "<code>comptime var i = 0; inline for (fields) |f| { i += 1; }</code>. Variables at compile time are mutable within the comptime scope. Used for counting, accumulation, and state during metaprogramming.",
  ["L1_mechanics"])

c("CompileTime", "What is <code>@Type</code> and <code>@typeInfo</code>?",
  "<code>@TypeOf(value)</code> returns the type of a value. <code>@typeInfo(T)</code> returns a <code>std.builtin.Type</code> enum describing the type's structure. Combine with comptime to reflect on and generate types programmatically.",
  ["L6_innovation"])

c("CompileTime", "What is <code>@Type</code> using a type info struct?",
  "<code>const T = @Type(.{ .Int = .{ .bits = 32, .signedness = .unsigned } });</code> — constructs types from type descriptors. Enables generating structs, enums, unions at compile time from configuration data.",
  ["L6_innovation"])

# === PATTERNS ===

c("Patterns", "What is the tagged union pattern?",
  "<code>const Value = union(enum) { int: i32, float: f64, string: []const u8 };</code>. Switch to destructure: <code>switch (v) { .int =&gt; |i| ..., else =&gt; ... }</code>. Enforces exhaustive handling at compile time.",
  ["L2_composition"])

c("Patterns", "What is the multi-sequence for loop pattern?",
  "<code>for (arr1, arr2, 0..) |a, b, i| { ... }</code> — iterate multiple sequences simultaneously. Any sequence mismatches in length: panic in debug, UB in release. Powerful for parallel iteration.",
  ["L2_composition"])

c("Patterns", "What is the allocator-passing pattern?",
  "Every function that allocates accepts an <code>std.mem.Allocator</code> parameter. No global allocator. This makes allocations explicit, testable (pass a <code>testing.allocator</code>), and composable (arena vs. GPA decisions at call site).",
  ["L3_design"])

c("Patterns", "What is the builder pattern in <code>build.zig</code>?",
  "Zig's build system uses a method chaining pattern: <code>b.addExecutable(...).addCSourceFile(...).linkLibC().setBuildMode(...)</code>. Each method returns self. Familiar if you've used CMake target properties but in pure Zig.",
  ["L2_composition"])

c("Patterns", "What is the <code>try</code> waterfall pattern?",
  "<code>const a = try step1(); const b = try step2(a); const c = try step3(b); return c;</code>. Clean linear error handling — if any step fails, the error bubbles up. No nesting, no callbacks, just linear try-cascade.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why does my Zig build fail with 'no entry point found'?",
  "Zig programs need a <code>pub fn main() !void { ... }</code> function. Libraries don't need main. Check that your root source file has a public main function.",
  ["L4_diagnosis"])

c("Gotchas", "What happens with <code>undefined</code> values?",
  "In debug mode: <code>0xaa</code> pattern for integers, catches uninitialized reads. In release: compiler may optimize assuming it's never read, leading to UB. Always initialize variables unless you know the next line will set them.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>const</code> on a pointer not prevent mutation?",
  "<code>const p: *i32</code> — the pointer itself is const (can't change what it points to), but the TARGET can be mutated (<code>p.* = 5</code> works). For const target: <code>const p: *const i32</code>. Const on pointer vs const on target are separate.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'cannot assign to constant' error with function parameters?",
  "Function parameters are immutable (<code>const</code>). If you need to modify a parameter, copy it to a <code>var</code>: <code>var local = param; local += 1;</code>. Or pass a pointer: <code>fn increment(p: *i32) { p.* += 1; }</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why do some integer operations cause overflow?",
  "Zig has strict overflow semantics: <code>@addWithOverflow</code>, <code>+%</code> (wrapping add), <code>+|</code> (saturating add). Plain <code>+</code> in debug mode panics on overflow. In release: undefined behavior. Use wrapping/saturating ops when overflow is expected.",
  ["L4_diagnosis"])

c("Gotchas", "What is the zig fmt style and how strict is it?",
  "<code>zig fmt</code> formats all Zig files to a canonical style. Very few options — the community standard is to run <code>zig fmt</code> before commits. No tabs-vs-spaces debates; Zig says 4 spaces.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is Zig's cross-compilation story?",
  "Zig bundles its own standard library and can build for any target from any host: <code>zig build-exe main.zig -target aarch64-macos</code> or <code>x86_64-windows-gnu</code>. No external toolchains needed. Even <code>zig cc</code> serves as a cross-compiling C compiler.",
  ["L6_innovation"])

c("Expert", "What is <code>@call</code> with <code>modifier</code>?",
  "Direct control over calling convention, tail calls, and async frames: <code>@call(.{ .modifier = .always_tail }, foo, .{arg})</code>. Zig guarantees tail call elimination when specified. No 'may tail-call' — it's guaranteed or compile error.",
  ["L6_innovation"])

c("Expert", "What is Zig's async story?",
  "Zig has no built-in async/await — it was removed to simplify the language. For I/O: use blocking I/O with threads, or <code>std.Thread</code>. For event loops: use <code>std.io_uring</code> (Linux io_uring). The philosophy: be explicit about concurrency.",
  ["L5_opinion"])

c("Expert", "How do you do C interop without bindings?",
  "<code>const c = @cImport({ @cInclude(\"header.h\"); @cDefine(\"FLAG\", \"1\"); });</code>. Zig translates C types directly. Use <code>zig translate-c file.h</code> to generate Zig bindings. Call any C library without writing a single binding file.",
  ["L3_design"])

c("Expert", "What is the Zig compiler's role as a C compiler?",
  "Zig ships a full C compiler (<code>zig cc</code>). It can compile any C project with <code>zig cc main.c -o main</code>. Combined with @cImport, Zig can incrementally adopt existing C codebases — recompile C alongside Zig in one step.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
