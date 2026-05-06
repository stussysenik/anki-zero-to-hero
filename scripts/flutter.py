import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Flutter"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Widgets":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Widgets"),
    "State":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-State-Management"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === FLUTTER FUNDAMENTALS ===

c("Fundamentals", "What is Flutter?",
  "An open-source UI toolkit by Google for building natively compiled applications for mobile, web, and desktop from a single codebase. Uses the Dart language. Renders its own widgets (no OEM widgets) via the Skia/Impeller graphics engine.",
  ["L0_primitives"])

c("Fundamentals", "What is Dart?",
  "The language used by Flutter. Object-oriented, class-based, with sound null safety. Supports both JIT (hot reload during development) and AOT (native compilation for release). Syntax familiar to Java/JavaScript/C# developers.",
  ["L0_primitives"])

c("Fundamentals", "What is a Widget in Flutter?",
  "The fundamental building block of Flutter UI. Everything is a widget: layout, text, buttons, animations, padding, alignment. Immutable — widgets describe their configuration. The framework rebuilds the widget tree when state changes.",
  ["L0_primitives"])

c("Fundamentals", "What is the widget tree?",
  "A hierarchical structure of widgets describing the UI. A <code>MaterialApp</code> at the root, containing <code>Scaffold</code>, containing <code>Column</code>, containing <code>Text</code> and <code>Button</code> widgets. The tree is recreated when state changes and diffed for efficient rendering.",
  ["L0_primitives"])

c("Fundamentals", "What is a StatefulWidget vs StatelessWidget?",
  "StatelessWidget: immutable, no mutable state. Built once from configuration. StatefulWidget: holds mutable <code>State</code> object. <code>setState(() { ... })</code> triggers rebuild. Use StatefulWidget for interactivity, animations, and data that changes over time.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>setState</code>?",
  "Triggers a rebuild of the widget with updated state. <code>setState(() { _counter++; })</code>. Must be called inside the State class. The framework calls <code>build()</code> again. The simplest form of state management — built into Flutter.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>build</code> method?",
  "Every widget has a <code>build(BuildContext context)</code> method that returns a widget subtree. Called: 1) initially, 2) after <code>setState()</code>, 3) when parent rebuilds, 4) when <code>InheritedWidget</code> dependencies change. Should be pure (no side effects).",
  ["L0_primitives"])

c("Fundamentals", "What is Hot Reload?",
  "Inject updated source code into a running Dart VM without restarting or losing state. Preserves app state — you can change UI code and see it instantly. Doesn't work for: global variable init, generic type changes, native code changes.",
  ["L0_primitives"])

c("Fundamentals", "What is the Flutter rendering pipeline?",
  "Widget → Element → RenderObject → Layer → Engine. Widgets describe configuration. Elements are the instantiated tree. RenderObjects handle layout and painting. Layers are composited by the engine (Skia/Impeller). The framework diffs and efficiently updates.",
  ["L0_primitives"])

c("Fundamentals", "What is Material Design in Flutter?",
  "Google's design system implemented as Flutter widgets: <code>MaterialApp</code>, <code>Scaffold</code>, <code>AppBar</code>, <code>FloatingActionButton</code>, <code>Card</code>, <code>BottomNavigationBar</code>. Provide consistent look-and-feel on Android and web. Cupertino widgets for iOS style.",
  ["L0_primitives"])

# === DART & FLUTTER CORE OPS ===

c("CoreOps", "How do you create a new Flutter project?",
  "<code>flutter create my_app</code>. With org: <code>flutter create --org com.mycompany my_app</code>. Creates <code>lib/main.dart</code>, <code>android/</code>, <code>ios/</code>, <code>web/</code>, <code>test/</code>. Run: <code>flutter run</code>.",
  ["L1_mechanics"])

c("CoreOps", "What is the basic structure of a Flutter app?",
  "<code>void main() =&gt; runApp(MyApp());<br>class MyApp extends StatelessWidget {<br>  @override Widget build(BuildContext context) {<br>    return MaterialApp(home: Scaffold(body: Text('Hello')));<br>  }<br>}</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you declare variables in Dart?",
  "<code>var x = 42;</code> — type inferred. <code>int x = 42;</code> — explicit type. <code>final x = 42;</code> — runtime constant (set once). <code>const x = 42;</code> — compile-time constant. <code>String? name = null;</code> — nullable (with null safety).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a StatelessWidget?",
  "<code>class MyWidget extends StatelessWidget {<br>  final String title;<br>  const MyWidget({required this.title});<br>  @override Widget build(BuildContext context) {<br>    return Text(title);<br>  }<br>}</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you define a StatefulWidget?",
  "<code>class Counter extends StatefulWidget {<br>  @override State&lt;Counter&gt; createState() =&gt; _CounterState();<br>}<br>class _CounterState extends State&lt;Counter&gt; {<br>  int _count = 0;<br>  @override Widget build(BuildContext context) {<br>    return TextButton(onPressed: () =&gt; setState(() =&gt; _count++), child: Text('$_count'));<br>  }<br>}</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you lay out widgets vertically?",
  "<code>Column(children: [Text('A'), Text('B'), Text('C')])</code>. Properties: <code>mainAxisAlignment</code>, <code>crossAxisAlignment</code>, <code>mainAxisSize</code>. If children overflow, wrap with <code>SingleChildScrollView</code> or use <code>ListView</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you lay out widgets horizontally?",
  "<code>Row(children: [Icon(Icons.star), Text('Favorite')])</code>. Same properties as Column. For wrapping rows, use <code>Wrap</code> instead (auto-wraps to next line).",
  ["L1_mechanics"])

c("CoreOps", "What is <code>Container</code>?",
  "A convenience widget combining: padding, margin, decoration (color, border, shadow), constraints, alignment, and a child. <code>Container(padding: EdgeInsets.all(16), color: Colors.blue, child: Text('Hi'))</code>. Without a child, tries to be as big as possible.",
  ["L1_mechanics"])

c("CoreOps", "How do you add padding around a widget?",
  "<code>Padding(padding: EdgeInsets.all(16.0), child: Text('Padded'))</code>. <code>EdgeInsets.symmetric(horizontal: 16, vertical: 8)</code>. <code>EdgeInsets.only(left: 16, top: 8)</code>. Prefer <code>Padding</code> over <code>Container</code> when only padding is needed.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle user input (TextFormField)?",
  "<code>TextFormField(decoration: InputDecoration(labelText: 'Name'), onChanged: (val) =&gt; ..., validator: (val) =&gt; val.isEmpty ? 'Required' : null)</code>. Wrap in <code>Form</code> with <code>GlobalKey&lt;FormState&gt;</code> for validation on submit.",
  ["L1_mechanics"])

c("CoreOps", "How do you navigate between screens?",
  "<code>Navigator.push(context, MaterialPageRoute(builder: (_) =&gt; NextScreen()))</code>. Go back: <code>Navigator.pop(context)</code>. Push replacement: <code>pushReplacement</code>. Named routes: <code>Navigator.pushNamed(context, '/details')</code> with <code>routes</code> in <code>MaterialApp</code>.",
  ["L1_mechanics"])

# === WIDGETS ===

c("Widgets", "What is <code>Expanded</code> and <code>Flexible</code>?",
  "<code>Expanded</code>: forces child to fill available space in a Row/Column. <code>Expanded(flex: 2, child: ...)</code> — proportional sizing. <code>Flexible</code>: child CAN expand but won't be forced larger than its content. Both need a Row/Column parent.",
  ["L1_mechanics"])

c("Widgets", "What is <code>ListView</code>?",
  "A scrollable list of widgets. <code>ListView(children: [...])</code> — builds all at once. <code>ListView.builder(itemCount: n, itemBuilder: (ctx, i) =&gt; ...)</code> — lazy, builds only visible items. Use builder for long/infinite lists.",
  ["L1_mechanics"])

c("Widgets", "What is <code>Stack</code>?",
  "Layers widgets on top of each other. <code>Stack(children: [Image(...), Positioned(bottom: 8, child: Text('Overlay'))])</code>. First child is at the bottom. Use <code>Positioned</code> or <code>Align</code> for positioning children within the stack.",
  ["L1_mechanics"])

c("Widgets", "What is <code>MediaQuery</code>?",
  "Access device/screen information: <code>MediaQuery.of(context).size.width</code>, <code>.size.height</code>, <code>.padding.top</code> (safe area), <code>.textScaleFactor</code>. Use for responsive layouts. <code>MediaQuery.of(context).platformBrightness</code> for dark/light mode check.",
  ["L1_mechanics"])

c("Widgets", "What is <code>LayoutBuilder</code>?",
  "Builds widget based on parent constraints: <code>LayoutBuilder(builder: (context, constraints) { if (constraints.maxWidth &gt; 600) return wideLayout; return narrowLayout; })</code>. The true responsive pattern — responds to any width, not just breakpoints.",
  ["L1_mechanics"])

# === STATE MANAGEMENT ===

c("State", "What is <code>InheritedWidget</code>?",
  "A widget that provides data down the tree efficiently. Descendants call <code>context.dependOnInheritedWidgetOfExactType&lt;T&gt;()</code> to subscribe. Rebuilds only when data changes. The foundation of Provider, Theme, MediaQuery. Rarely used directly.",
  ["L3_design"])

c("State", "What is the Provider package?",
  "A wrapper around InheritedWidget for state management. <code>ChangeNotifierProvider(create: (_) =&gt; Counter(), child: MyApp())</code>. Downstream: <code>context.watch&lt;Counter&gt;().count</code> (subscribes), <code>context.read&lt;Counter&gt;().increment()</code> (doesn't rebuild).",
  ["L2_composition"])

c("State", "What is Riverpod?",
  "A compile-safe, testable state management library (Provider v2). <code>final counterProvider = StateProvider((ref) =&gt; 0);</code>. Read: <code>ref.watch(counterProvider)</code>. No BuildContext needed. Providers are global (compile-time safe). Supports async, auto-dispose, families.",
  ["L3_design"])

c("State", "What is Bloc/Cubit?",
  "Business Logic Component pattern. <code>class CounterCubit extends Cubit&lt;int&gt; { CounterCubit() : super(0); void increment() =&gt; emit(state + 1); }</code>. UI: <code>BlocBuilder&lt;CounterCubit, int&gt;(builder: (ctx, count) =&gt; Text('$count'))</code>. Events in, states out.",
  ["L3_design"])

# === PATTERNS ===

c("Patterns", "What is the widget composition over inheritance pattern?",
  "Flutter has no visual inheritance. Compose small widgets: <code>Padding(child: Center(child: Text('Hello')))</code>. Build complex UIs by nesting simple widgets. Each widget does one layout thing. Avoid monster widgets.",
  ["L2_composition"])

c("Patterns", "What is the <code>const</code> constructor pattern?",
  "Mark constructors <code>const</code> where possible: <code>const Padding(padding: EdgeInsets.all(8))</code>. Flutter reuses the same instance across rebuilds — zero allocation. Use <code>const</code> wherever the widget tree is static. Significant performance boost.",
  ["L2_composition"])

c("Patterns", "What is the async UI pattern (FutureBuilder/StreamBuilder)?",
  "<code>FutureBuilder(future: fetchData(), builder: (ctx, snapshot) { if (snapshot.hasData) return ...; if (snapshot.hasError) return ...; return CircularProgressIndicator(); })</code>. <code>StreamBuilder</code> for real-time data (Firebase, WebSocket).",
  ["L2_composition"])

c("Patterns", "What is the ValueNotifier + ValueListenableBuilder pattern?",
  "Lightweight reactive primitive: <code>final notifier = ValueNotifier(0); notifier.value = 1;</code>. Listen: <code>ValueListenableBuilder(valueListenable: notifier, builder: (ctx, val, _) =&gt; Text('$val'))</code>. Simpler than full state management for simple cases.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why does my widget not rebuild after <code>setState</code>?",
  "Common reasons: 1) <code>setState</code> called on wrong State object. 2) The value mutated in-place (list/map) but reference didn't change — Flutter compares by identity. 3) The build method returns the same widget instance (const widgets may not rebuild). Create new instances.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>context</code> not work in <code>initState</code>?",
  "<code>initState</code> runs before the widget is inserted in the tree. <code>context</code> is not yet available. Use <code>didChangeDependencies</code> or <code>WidgetsBinding.instance.addPostFrameCallback((_) =&gt; ...)</code> for post-build operations.",
  ["L4_diagnosis"])

c("Gotchas", "What causes 'A RenderFlex overflowed'?",
  "Content exceeds the available space in a Row or Column. Solutions: wrap with <code>Expanded</code>/<code>Flexible</code>, use <code>SingleChildScrollView</code>, reduce font size, or switch to <code>ListView</code>. Check in debug mode — the overflow indicator is yellow/black stripes.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>setState</code> called in <code>build</code> cause infinite loop?",
  "<code>build()</code> triggers <code>setState()</code> which triggers <code>build()</code> again — infinite recursion. Never call <code>setState</code> inside <code>build</code>. Move state changes to event handlers, <code>initState</code>, or lifecycle methods.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my keys important for lists?",
  "When reordering, adding, or removing list items, Flutter matches elements to widgets by key. Without unique keys, state (scroll position, animation, focus) jumps to wrong items. Use <code>ValueKey(item.id)</code> or <code>UniqueKey()</code>. Especially critical for StatefulWidgets in lists.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'null check operator used on a null value' error?",
  "<code>!</code> on a nullable expression that is null at runtime. Always check for null: <code>if (value != null) { ... }</code> or <code>value?.method()</code>. The <code>!</code> operator is a promise to the compiler — it panics at runtime if wrong.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is the Flutter rendering engine?",
  "Skia (legacy) and Impeller (new, iOS/Android). Impeller precompiles shaders at build time (no runtime stutter). It's a purpose-built rendering engine for Flutter replacing Skia. AOT-compiled shaders eliminate 'jank' from shader compilation.",
  ["L6_innovation"])

c("Expert", "What is the Flutter Engine and Platform Channels?",
  "Platform Channels bridge Dart and native code (Kotlin/Swift): <code>MethodChannel('channel_name').invokeMethod('method', args)</code>. Native side receives the call, returns result. Used for platform APIs not exposed by Flutter (camera, sensors, payments).",
  ["L6_innovation"])

c("Expert", "What is Flutter Web and its rendering modes?",
  "Two modes: HTML (DOM-based, better compatibility) and CanvasKit (Skia compiled to WebAssembly, pixel-perfect). <code>flutter build web --web-renderer canvaskit</code>. Service workers for PWA. Not all plugins support web — check compatibility.",
  ["L3_design"])

c("Expert", "What are CustomPaint and Canvas?",
  "Low-level drawing API: <code>CustomPaint(painter: MyPainter())</code>. <code>class MyPainter extends CustomPainter { void paint(Canvas canvas, Size size) { canvas.drawCircle(...); } }</code>. Full access to Skia/Impeller canvas drawing primitives. For custom charts, animations, visualizations.",
  ["L6_innovation"])

c("Expert", "How do you create animations in Flutter?",
  "Implicit: <code>AnimatedContainer(duration: ..., color: newColor)</code> — Flutter handles the in-between. Explicit: <code>AnimationController</code> + <code>Tween</code> + <code>AnimatedBuilder</code> — full control over timing, curves, and values. Prefer implicit for simple transitions.",
  ["L3_design"])

c("Expert", "When should you choose Flutter vs React Native?",
  "Flutter: pixel-perfect custom UI, high performance, 2D game-like interfaces, consistent look across platforms, Dart ecosystem. React Native: leverage web React skills, native look-and-feel, larger package ecosystem, JS/TS stack. Flutter for brand-driven UI; RN for platform-native feel.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
