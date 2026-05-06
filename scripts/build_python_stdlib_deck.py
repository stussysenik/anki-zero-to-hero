import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)

model = genanki.Model(
    R(), "Python Stdlib Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}\n<hr id=answer>\n{{Back}}"}],
    css=""".card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px;
                text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; }
           .front { font-weight: bold; margin-top: 60px; }
           .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
           code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244;
                       padding: 2px 6px; border-radius: 4px; font-size: 18px; }
           hr { border-color: #45475a; }"""
)

decks = {
    "Fundamentals":   genanki.Deck(R(), "Python Stdlib::Zero2Hero::01-Fundamentals"),
    "DataStructures": genanki.Deck(R(), "Python Stdlib::Zero2Hero::02-Data-Structures"),
    "TextRegex":      genanki.Deck(R(), "Python Stdlib::Zero2Hero::03-Text-and-Regex"),
    "IterFunctions":  genanki.Deck(R(), "Python Stdlib::Zero2Hero::04-Iteration-Functions"),
    "IO":             genanki.Deck(R(), "Python Stdlib::Zero2Hero::05-IO-and-Filesystem"),
    "Serialization":  genanki.Deck(R(), "Python Stdlib::Zero2Hero::06-Serialization"),
    "DateTime":       genanki.Deck(R(), "Python Stdlib::Zero2Hero::07-Date-and-Time"),
    "Concurrency":    genanki.Deck(R(), "Python Stdlib::Zero2Hero::08-Concurrency"),
    "Networking":     genanki.Deck(R(), "Python Stdlib::Zero2Hero::09-Networking"),
    "DataModeling":   genanki.Deck(R(), "Python Stdlib::Zero2Hero::10-Data-Modeling"),
    "TestingDebug":   genanki.Deck(R(), "Python Stdlib::Zero2Hero::11-Testing-Debugging"),
    "Security":       genanki.Deck(R(), "Python Stdlib::Zero2Hero::12-Security-Crypto"),
    "Expert":         genanki.Deck(R(), "Python Stdlib::Zero2Hero::13-Expert-Patterns"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# =====================================================================
# SUBDECK 01 — FUNDAMENTALS
# =====================================================================

c("Fundamentals", "What is the Python standard library?",
  "A collection of modules distributed with every Python install — no pip needed. Covers files, networking, data structures, concurrency, testing, and more.",
  ["L0_primitives"])

c("Fundamentals", "How do you import a module from the standard library?",
  "<code>import module_name</code> — e.g. <code>import collections</code>. Access items as <code>collections.Counter</code>.",
  ["L0_primitives"])

c("Fundamentals", "How do you import a specific name from a module?",
  "<code>from module import Name</code> — e.g. <code>from collections import Counter</code>. Direct access, no module prefix needed.",
  ["L0_primitives"])

c("Fundamentals", "What does <code>dir(module)</code> return?",
  "A sorted list of all names (attributes, functions, classes) defined in that module. Useful for exploration.",
  ["L0_primitives"])

c("Fundamentals", "What does <code>help(obj)</code> do?",
  "Prints docstring and signature info for any object, function, class, or module directly in the REPL.",
  ["L0_primitives"])

c("Fundamentals", 'What is the difference between a "built-in" and a "standard library" module?',
  "Built-ins: always available without import (<code>len</code>, <code>print</code>, <code>range</code>). Stdlib modules need <code>import</code> but ship with Python.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>__name__</code> variable?",
  "The module's name as a string. Set to <code>'__main__'</code> when run directly. Used for script guards: <code>if __name__ == '__main__': main()</code>.",
  ["L0_primitives"])

c("Fundamentals", "What does <code>sys.path</code> contain?",
  "A list of directory paths where Python searches for modules during <code>import</code>. Starts with script's dir, then <code>PYTHONPATH</code>, then stdlib and site-packages.",
  ["L0_primitives"])

c("Fundamentals", "What are <code>*args</code> and <code>**kwargs</code>?",
  "<code>*args</code>: captures extra positional arguments as a tuple. <code>**kwargs</code>: captures extra keyword arguments as a dict. Convention names — the <code>*</code> and <code>**</code> are what matter.",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between <code>is</code> and <code>==</code>?",
  "<code>is</code>: object identity (same memory address). <code>==</code>: value equality (calls <code>__eq__</code>). <code>a is None</code> is the idiomatic None check.",
  ["L0_primitives"])

c("Fundamentals", "What is a generator?",
  "A function that uses <code>yield</code> instead of <code>return</code>. Returns an iterator that lazily produces values one at a time — memory efficient for large sequences.",
  ["L0_primitives"])

c("Fundamentals", "What is a list comprehension?",
  "<code>[expr for item in iterable if condition]</code> — creates a new list by evaluating expr for each item passing the optional filter.",
  ["L0_primitives"])

c("Fundamentals", "What is a context manager and how do you use one?",
  "An object with <code>__enter__</code> and <code>__exit__</code>. Used with <code>with obj as var:</code>. Guarantees cleanup (file close, lock release) even if exceptions occur.",
  ["L0_primitives"])

c("Fundamentals", "What is the GIL (Global Interpreter Lock)?",
  "A mutex preventing multiple native threads from executing Python bytecode simultaneously. Limits CPU-bound threading but doesn't block I/O threads or multiprocessing.",
  ["L0_primitives"])

c("Fundamentals", "How do you check the Python version at runtime?",
  "<code>import sys; sys.version_info</code> — named tuple like <code>(3, 11, 5, 'final', 0)</code>. Compare: <code>sys.version_info >= (3, 8)</code>.",
  ["L1_mechanics"])

c("Fundamentals", "How do you time a block of code?",
  "<code>time.perf_counter()</code> before and after — monotonic, high-res. For microbenchmarks: <code>python -m timeit -s 'setup' 'stmt'</code>.",
  ["L1_mechanics"])

c("Fundamentals", 'How do you create a "main" function pattern?',
  "<code>def main(): ...</code> with <code>if __name__ == '__main__': main()</code> at the bottom. Prevents code from running on import.",
  ["L1_mechanics"])

c("Fundamentals", "How do you pass command-line arguments?",
  "<code>import sys; sys.argv</code> — <code>sys.argv[0]</code> is script name, <code>sys.argv[1:]</code> are args. For proper parsing use <code>argparse</code>.",
  ["L1_mechanics"])

c("Fundamentals", "What are <code>sys.stdin</code>/<code>sys.stdout</code>/<code>sys.stderr</code>?",
  "File-like objects for standard I/O streams. Iterate <code>for line in sys.stdin:</code> for efficient line-by-line reading.",
  ["L1_mechanics"])

c("Fundamentals", "How do you get the size of an object in memory?",
  "<code>sys.getsizeof(obj)</code> — size in bytes, shallow (doesn't count referenced objects). For deep size use third-party <code>pympler</code>.",
  ["L1_mechanics"])

c("Fundamentals", "How do you exit a script with a specific exit code?",
  "<code>sys.exit(code)</code> — raises <code>SystemExit</code>. <code>0</code> = success, non-zero = error. Can pass a string message.",
  ["L1_mechanics"])

c("Fundamentals", "What does <code>enumerate()</code> do and what's its optional second argument?",
  "<code>enumerate(iterable, start=0)</code> yields <code>(index, item)</code> tuples. Use <code>start=1</code> for 1-based counting.",
  ["L1_mechanics"])

c("Fundamentals", "How do you create a sorted copy vs sort in place?",
  "<code>sorted(iterable, key=..., reverse=False)</code> returns new list. <code>list.sort(key=..., reverse=False)</code> sorts in place, returns <code>None</code>.",
  ["L1_mechanics"])

c("Fundamentals", "What is the <code>key</code> parameter in <code>sorted()</code>?",
  "A function applied to each element before comparison (Schwartzian transform). <code>sorted(words, key=len)</code> sorts by length; <code>key=lambda x: x[1]</code> by second element.",
  ["L1_mechanics"])

c("Fundamentals", "How do you lazily process a large file, filtering and transforming?",
  "Generator expression: <code>(line.upper() for line in open('f') if 'ERROR' in line)</code>. Never loads full file; yields on demand.",
  ["L2_composition"])

c("Fundamentals", "How do you profile a script for bottlenecks?",
  "<code>python -m cProfile -s cumulative script.py</code> — function call counts and timings sorted by cumulative time. Use <code>pstats</code> for deeper analysis.",
  ["L2_composition"])

c("Fundamentals", "How do you run a module as a script from the command line?",
  "<code>python -m module_name args</code> — e.g. <code>python -m http.server 8000</code>, <code>python -m json.tool data.json</code>. Runs <code>__main__.py</code> inside the module.",
  ["L2_composition"])

c("Fundamentals", "Why should you use <code>sys.exit()</code> instead of <code>os._exit()</code>?",
  "<code>sys.exit()</code> raises <code>SystemExit</code> (catchable), runs cleanup handlers, flushes buffers. <code>os._exit()</code> kills immediately — no cleanup, no <code>finally</code>.",
  ["L3_design"])

c("Fundamentals", "Why are mutable default arguments dangerous?",
  "<code>def f(lst=[])</code> creates the list ONCE at definition. All calls share the same list. Fix: <code>def f(lst=None): if lst is None: lst = []</code>.",
  ["L3_design"])

c("Fundamentals", "What is EAFP vs LBYL coding style?",
  "EAFP: try-and-catch (Pythonic). LBYL: check-then-do. Python prefers EAFP: <code>try: d['k'] except KeyError: ...</code> over <code>if 'k' in d: ...</code>.",
  ["L3_design"])

c("Fundamentals", "You got <code>ModuleNotFoundError</code>. What are common causes?",
  "1) Module not installed. 2) Typo. 3) Wrong venv active. 4) Script name shadows stdlib. 5) <code>sys.path</code> missing the directory.",
  ["L4_diagnosis"])

c("Fundamentals", "Why does iterating a file twice print nothing the second time?",
  "File iterator exhausted after first loop — pointer at EOF. Call <code>file.seek(0)</code> to reset, or use <code>with</code> + reopen. Better: store lines in list for multiple iterations.",
  ["L4_diagnosis"])

c("Fundamentals", "You wrote <code>print('hello', file=myfile)</code> but nothing appears. Why?",
  "Forgot <code>flush()</code> or <code>close()</code>. <code>print</code> buffers output. Use context managers or <code>print(..., flush=True)</code>.",
  ["L4_diagnosis"])

c("Fundamentals", "Should you use <code>from module import *</code>?",
  "No. Pollutes namespace with unknown names, makes code unreadable, can silently shadow built-ins. Explicit imports only.",
  ["L5_opinion"])

c("Fundamentals", "When should you use a generator expression vs list comprehension?",
  "Generator when: iterate once, no indexing needed, large data (memory). List when: need indexing, multiple iterations, result is small.",
  ["L5_opinion"])

c("Fundamentals", "Should you use <code>os.system()</code> or <code>subprocess.run()</code>?",
  "<code>subprocess.run()</code> always. <code>os.system()</code> spawns a shell (security risk), can't capture output. Use <code>subprocess.run(cmd, capture_output=True, text=True)</code>.",
  ["L5_opinion"])

# =====================================================================
# SUBDECK 02 — DATA STRUCTURES
# =====================================================================

c("DataStructures", "What is <code>collections.Counter</code>?",
  "A dict subclass for counting hashable objects. <code>Counter('abracadabra')</code> → <code>Counter({'a':5,'b':2,'r':2,'c':1,'d':1})</code>. Missing keys return 0 instead of KeyError.",
  ["L0_primitives"])

c("DataStructures", "What is <code>collections.defaultdict</code>?",
  "Dict subclass calling a factory for missing keys. <code>defaultdict(list)</code> — accessing <code>d['new']</code> auto-creates an empty list.",
  ["L0_primitives"])

c("DataStructures", "What is <code>collections.deque</code>?",
  "Double-ended queue, O(1) appends/pops both ends. <code>deque([1,2,3])</code>. Supports <code>maxlen</code> for bounded history.",
  ["L0_primitives"])

c("DataStructures", "What is <code>collections.namedtuple</code>?",
  "Factory for tuple subclasses with named fields. <code>Point = namedtuple('Point', ['x','y']); p = Point(10, 20); p.x</code>. Immutable, memory-efficient.",
  ["L0_primitives"])

c("DataStructures", "What is <code>collections.OrderedDict</code>?",
  "Dict that remembers insertion order. Since 3.7, regular dict is also ordered. Still needed for <code>move_to_end()</code> and order-sensitive equality.",
  ["L0_primitives"])

c("DataStructures", "What is <code>collections.ChainMap</code>?",
  "Groups multiple dicts into one view. Searches in order; writes/deletes only affect first dict. Perfect for layered configs (defaults &lt; env &lt; CLI args).",
  ["L0_primitives"])

c("DataStructures", "What is the <code>heapq</code> module?",
  "Min-heap operations on a regular list. All ops O(log n) except <code>heapify</code> O(n). <code>heap[0]</code> is always the smallest element.",
  ["L0_primitives"])

c("DataStructures", "What is the <code>bisect</code> module?",
  "Binary search in sorted lists. O(log n) search, O(n) insert. <code>bisect_left</code> / <code>bisect_right</code> return insertion points.",
  ["L0_primitives"])

c("DataStructures", "What does the <code>array</code> module provide?",
  "Homogeneous C-typed arrays in contiguous memory. <code>array('i', [1,2,3])</code> for signed ints. More memory-efficient than lists for numeric data.",
  ["L0_primitives"])

c("DataStructures", "What is the <code>queue</code> module?",
  "Thread-safe queues: <code>Queue</code> (FIFO), <code>LifoQueue</code>, <code>PriorityQueue</code>. <code>put</code>/<code>get</code> with optional blocking and timeout.",
  ["L0_primitives"])

c("DataStructures", "How do you get the N most common elements from a Counter?",
  "<code>c.most_common(n)</code> — returns <code>(element, count)</code> tuples descending. O(n log k) for fixed n. Without n, returns all sorted.",
  ["L1_mechanics"])

c("DataStructures", "How do you create a defaultdict for grouping items?",
  "<code>groups = defaultdict(list); groups[key].append(value)</code>. No need to check if key exists — factory handles it.",
  ["L1_mechanics"])

c("DataStructures", "How do you create a deque with a maximum size?",
  "<code>deque(maxlen=5)</code> — when full, append drops from opposite end. Perfect for sliding windows.",
  ["L1_mechanics"])

c("DataStructures", "How do you rotate a deque?",
  "<code>d.rotate(n)</code> — positive = right, negative = left. O(k) where k is rotation amount.",
  ["L1_mechanics"])

c("DataStructures", "How do you push/pop from both ends of a deque?",
  "Right: <code>append()</code>/<code>pop()</code>. Left: <code>appendleft()</code>/<code>popleft()</code>. All O(1).",
  ["L1_mechanics"])

c("DataStructures", "How do you convert a namedtuple to a dict?",
  "<code>p._asdict()</code> — returns <code>dict</code> (OrderedDict pre-3.8). <code>_replace(**kwargs)</code> returns new instance with specified fields changed.",
  ["L1_mechanics"])

c("DataStructures", "How do you add/subtract from a Counter?",
  "<code>c.update(iterable)</code> — adds counts. <code>c.subtract(iterable)</code> — subtracts (can go negative). <code>+</code>/<code>-</code> operators create new Counters (drop non-positive).",
  ["L1_mechanics"])

c("DataStructures", "How do you push and pop from a heap?",
  "<code>heapq.heappush(heap, item)</code> — push O(log n). <code>heapq.heappop(heap)</code> — pop smallest O(log n). <code>heap[0]</code> is minimum without popping.",
  ["L1_mechanics"])

c("DataStructures", "How do you convert a list into a heap in-place?",
  "<code>heapq.heapify(mylist)</code> — O(n) rearranges into heap order. More efficient than repeated <code>heappush</code>.",
  ["L1_mechanics"])

c("DataStructures", "How do you find the N largest/smallest in an iterable?",
  "<code>heapq.nlargest(n, iterable, key=...)</code> and <code>nsmallest</code>. More efficient than sorting when n &lt;&lt; len(iterable).",
  ["L1_mechanics"])

c("DataStructures", "How do you use bisect to find insertion points?",
  "<code>bisect_left(a, x)</code> — index before equal values. <code>bisect_right(a, x)</code> — after equal values. Both O(log n).",
  ["L1_mechanics"])

c("DataStructures", "How do you insert into a sorted list?",
  "<code>bisect.insort(a, x)</code> — finds spot O(log n), insertion is O(n) due to list shift.",
  ["L1_mechanics"])

c("DataStructures", "How do you move a key to front/back in OrderedDict?",
  "<code>od.move_to_end(key, last=True)</code> — to end. <code>last=False</code> — to beginning. Main reason to use OrderedDict in 3.7+.",
  ["L1_mechanics"])

c("DataStructures", "How do you implement a sliding window maximum?",
  "Use <code>deque</code> storing indices of decreasing values. Pop right while smaller, pop left if outside window. <code>nums[d[0]]</code> is current max. O(n).",
  ["L2_composition"])

c("DataStructures", "How do you implement a max-heap using heapq?",
  "Negate values: <code>heappush(heap, -value)</code> / <code>-heappop(heap)</code>. For objects: <code>(-priority, item)</code> tuples. Or wrap class with reversed <code>__lt__</code>.",
  ["L2_composition"])

c("DataStructures", "How do you find top K frequent elements? (CodeSignal pattern)",
  "<code>counts = Counter(arr); return [x for x, _ in counts.most_common(k)]</code>. O(n log k) — efficient for small k vs full sort.",
  ["L2_composition"])

c("DataStructures", "How do you merge two sorted iterables lazily?",
  "<code>heapq.merge(*iterables)</code> — yields sorted union without consuming all at once. O(n) total comparisons. Inputs must be pre-sorted.",
  ["L2_composition"])

c("DataStructures", "How do you implement a priority queue with FIFO tie-breaking?",
  "Store <code>(priority, counter, item)</code> where <code>counter = next(itertools.count())</code>. Python compares tuples element-wise — ties broken by insertion order.",
  ["L2_composition"])

c("DataStructures", "When should you use <code>deque</code> instead of <code>list</code>?",
  "When you need O(1) appends/pops from BOTH ends. <code>list.insert(0, x)</code> is O(n) shift. <code>deque.appendleft(x)</code> is O(1). Also for bounded history with <code>maxlen</code>.",
  ["L3_design"])

c("DataStructures", "When should you use <code>array</code> instead of <code>list</code>?",
  "Large homogeneous numeric data. C arrays use much less memory, faster numeric ops. No mixed types. Type code must match.",
  ["L3_design"])

c("DataStructures", "When should you NOT use <code>defaultdict</code>?",
  "When side effects on read matter — accessing missing key creates an entry. When you need to distinguish 'missing' from 'present but empty'. Use <code>dict.get()</code> instead.",
  ["L3_design"])

c("DataStructures", "Why use <code>heappushpop</code> instead of push then pop?",
  "<code>heappushpop(heap, item)</code> does one O(log n) sift vs two. Efficient for fixed-size top-K: push new, pop smallest in one op.",
  ["L3_design"])

c("DataStructures", "Why does <code>Counter('aa') - Counter('a')</code> give <code>Counter({'a':1})</code> but <code>c.subtract('a')</code> gives <code>Counter({'a':0})</code>?",
  "<code>-</code> operator drops zero/negative counts. <code>subtract()</code> keeps them. Different semantics — arithmetic ops produce clean (positive, non-zero) results.",
  ["L4_diagnosis"])

c("DataStructures", "Why does modifying <code>heap[i]</code> directly break the heap?",
  "Heap invariant only holds through <code>heapq</code> functions. Direct mutation breaks the tree structure. Always use <code>heappush</code>/<code>heappop</code>/<code>heapify</code>.",
  ["L4_diagnosis"])

c("DataStructures", "Why does <code>bisect_left([1,2,3], 4)</code> return 3?",
  "Returns INSERTION point, not found/not-found. 4 would insert at index 3 (end). Check <code>i &lt; len(a) and a[i] == x</code> to determine existence.",
  ["L4_diagnosis"])

c("DataStructures", "Why does <code>groupby</code> not group unsorted data?",
  "<code>groupby</code> groups CONSECUTIVE equal elements. <code>[1,2,1,2]</code> → 4 groups, not 2. Sort first, or use <code>defaultdict(list)</code> for unsorted grouping.",
  ["L4_diagnosis"])

c("DataStructures", "Why is <code>deque[i]</code> slow?",
  "Random access is O(n), not O(1). Deque is a linked-list-of-blocks — designed for ends-only. Use <code>list</code> for random access.",
  ["L4_diagnosis"])

c("DataStructures", "Why does <code>PriorityQueue</code> crash with uncomparable items?",
  "Uses <code>(priority, item)</code> tuples. Same priority? Python compares items — crashes on uncomparable types (dicts). Fix: <code>(priority, counter, item)</code>.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 03 — TEXT and REGEX
# =====================================================================

c("TextRegex", "What is the <code>re</code> module?",
  "Python's regex engine. <code>search</code>, <code>match</code>, <code>findall</code>, <code>finditer</code>, <code>sub</code>, <code>split</code>, <code>compile</code>. Perl-style syntax.",
  ["L0_primitives"])

c("TextRegex", "What is the difference between <code>re.search</code> and <code>re.match</code>?",
  "<code>re.match</code>: only at string START. <code>re.search</code>: ANYWHERE. Almost always use <code>search</code> unless you specifically want start-anchoring.",
  ["L0_primitives"])

c("TextRegex", "What does <code>re.compile()</code> do?",
  "Compiles a regex into a reusable pattern object. <code>pat = re.compile(r'\\d+'); pat.findall(text)</code>. Faster for repeated use — parsed once.",
  ["L0_primitives"])

c("TextRegex", "How do you find all matches of a pattern?",
  "<code>re.findall(pattern, string)</code> — list of strings (or tuples if groups). <code>re.finditer</code> — iterator of match objects (memory efficient).",
  ["L1_mechanics"])

c("TextRegex", "How do you replace text using regex?",
  "<code>re.sub(pattern, replacement, string, count=0)</code>. Can use backreferences like <code>\\1</code>, <code>\\g&lt;name&gt;</code>. <code>re.subn</code> returns (new_string, count).",
  ["L1_mechanics"])

c("TextRegex", "How do you split a string by a regex pattern?",
  "<code>re.split(pattern, string, maxsplit=0)</code>. Capturing groups include delimiters in the result. Unlike <code>str.split</code>, delimiter is any regex.",
  ["L1_mechanics"])

c("TextRegex", "What are capturing groups and how do you access them?",
  "<code>()</code> captures sub-matches. <code>m = re.search(r'(\\d+)-(\\d+)', '123-456'); m.group(0)</code>=<code>'123-456'</code>, <code>m.group(1)</code>=<code>'123'</code>, <code>m.group(2)</code>=<code>'456'</code>.",
  ["L1_mechanics"])

c("TextRegex", "What are named groups in regex?",
  "<code>(?P&lt;name&gt;pattern)</code> — named capture. Access: <code>m.group('name')</code>, <code>m.groupdict()</code>. Use <code>\\g&lt;name&gt;</code> in replacements.",
  ["L1_mechanics"])

c("TextRegex", "What are lookahead and lookbehind assertions?",
  "Lookahead: <code>(?=...)</code> positive, <code>(?!...)</code> negative — check what FOLLOWS. Lookbehind: <code>(?&lt;=...)</code>, <code>(?&lt;!...)</code> — check what PRECEDES. Don't consume characters.",
  ["L1_mechanics"])

c("TextRegex", "What are the common regex flags?",
  "<code>re.IGNORECASE</code>/<code>re.I</code>, <code>re.MULTILINE</code>/<code>re.M</code> (^$ match lines), <code>re.DOTALL</code>/<code>re.S</code> (. matches newline), <code>re.VERBOSE</code>/<code>re.X</code> (comments, whitespace).",
  ["L1_mechanics"])

c("TextRegex", "When should you use a raw string <code>r'...'</code> for regex?",
  "ALWAYS. Without <code>r</code>: <code>\\b</code> becomes ASCII backspace, <code>\\d</code> gets escaped. <code>r'\\bword\\b'</code> ensures backslashes reach the regex engine intact.",
  ["L1_mechanics"])

c("TextRegex", "How do you escape special regex chars in user input?",
  "<code>re.escape(raw_string)</code> — backslash-escapes all non-alphanumeric characters. Essential when building patterns from untrusted/dynamic input.",
  ["L1_mechanics"])

c("TextRegex", "How do you check if a full string matches a pattern?",
  "<code>bool(re.fullmatch(pattern, string))</code>. Unlike <code>search</code>, requires the ENTIRE string to match. <code>fullmatch('\\d+', '42')</code> = True; <code>fullmatch('\\d+', '42a')</code> = False.",
  ["L1_mechanics"])

c("TextRegex", "What does <code>textwrap.dedent()</code> do?",
  "Removes common leading whitespace from every line, like docstring formatting. <code>textwrap.fill(text, width=70)</code> wraps to width. <code>shorten(text, width=50)</code> truncates with <code>[...]</code>.",
  ["L1_mechanics"])

c("TextRegex", "How do you find fuzzy string matches?",
  "<code>difflib.SequenceMatcher(None, a, b).ratio()</code> — similarity 0.0–1.0. <code>difflib.get_close_matches(word, possibilities, n=3)</code> — best matches.",
  ["L1_mechanics"])

c("TextRegex", "How do you extract all words that appear more than once in text?",
  "<code>words = re.findall(r'\\w+', text.lower()); from collections import Counter; [w for w, c in Counter(words).items() if c &gt; 1]</code>.",
  ["L2_composition"])

c("TextRegex", "How do you validate an email address using stdlib?",
  "Don't write a regex — just check <code>'@' in addr</code> and send verification. For sanity: <code>re.fullmatch(r'[^@]+@[^@]+\\.[^@]+', addr)</code>. Full RFC-compliant regex is impractically long.",
  ["L2_composition"])

c("TextRegex", "Why does <code>re.match(r'cat', 'The cat')</code> return <code>None</code>?",
  "<code>match</code> only checks position 0. <code>'The cat'</code> starts with <code>'T'</code>. Use <code>re.search</code> for matches anywhere.",
  ["L4_diagnosis"])

c("TextRegex", "Why does <code>re.sub(r'[.*]', '', text)</code> remove more than just brackets?",
  "<code>[.*]</code> is a character class matching <code>.</code> and <code>*</code>. To match literal brackets, escape: <code>r'\\[.*?\\]'</code>.",
  ["L4_diagnosis"])

c("TextRegex", "Why does <code>re.findall(r'(ab)+', 'abab')</code> return <code>['ab']</code>?",
  "With capturing groups, <code>findall</code> returns the LAST capture per match. Use non-capturing <code>(?:ab)+</code> or <code>finditer</code> + <code>m.group(0)</code>.",
  ["L4_diagnosis"])

c("TextRegex", "Should you use regex or string methods for simple operations?",
  "String methods (<code>.startswith</code>, <code>.replace</code>, <code>.split</code>, <code>in</code>) are faster, clearer, less error-prone. Only regex for patterns with actual variability.",
  ["L5_opinion"])

c("TextRegex", "When should you compile a regex vs use module-level functions?",
  "Compile when repeating in a loop. Module functions cache ~512 recent patterns, so one-offs don't benefit. Explicit <code>re.compile</code> makes intent clearer.",
  ["L5_opinion"])

# =====================================================================
# SUBDECK 04 — ITERATION and FUNCTIONS
# =====================================================================

c("IterFunctions", "What does <code>itertools.chain()</code> do?",
  "<code>chain('AB', 'CD')</code> → A,B,C,D. Chains iterables sequentially. <code>chain.from_iterable(iter_of_iters)</code> flattens one level.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.product()</code> do?",
  "Cartesian product. <code>product('AB', '12')</code> → <code>('A','1'),('A','2'),('B','1'),('B','2')</code>. <code>repeat=N</code>: product with itself N times.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.permutations()</code> do?",
  "All orderings of r elements. <code>permutations('ABC', 2)</code> → AB, AC, BA, BC, CA, CB. Order matters, no repeats. n!/(n-r)! results.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.combinations()</code> do?",
  "All subsets of r elements, lexicographic order. <code>combinations('ABC', 2)</code> → <code>('A','B'),('A','C'),('B','C')</code>. Order doesn't matter, no repeats.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.combinations_with_replacement()</code> do?",
  "Like combinations but elements CAN repeat. <code>combinations_with_replacement('AB', 2)</code> → <code>('A','A'),('A','B'),('B','B')</code>.",
  ["L1_mechanics"])

c("IterFunctions", "How does <code>itertools.groupby()</code> work?",
  "Returns <code>(key, group_iterator)</code>. Iterable MUST be sorted by key. Each group yields consecutive equal elements. Consume each group before advancing.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.islice()</code> do?",
  "Lazy slicing: <code>islice(iter, stop)</code> or <code>islice(iter, start, stop, step)</code>. No negative indices. Works on infinite iterators.",
  ["L1_mechanics"])

c("IterFunctions", "What do <code>dropwhile</code> and <code>takewhile</code> do?",
  "<code>dropwhile(pred, iter)</code>: skip while True, then yield ALL rest. <code>takewhile(pred, iter)</code>: yield while True, stop permanently on first False.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.zip_longest()</code> do?",
  "Like <code>zip()</code> but uses ALL elements. Fills missing with <code>fillvalue</code>. <code>zip_longest('AB', '123', fillvalue='-')</code> → <code>('A','1'),('B','2'),('-','3')</code>.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.starmap()</code> do?",
  "Like <code>map</code> but unpacks args. <code>starmap(pow, [(2,5), (3,2)])</code> → 32, 9. Equivalent to <code>map(lambda args: func(*args), iterable)</code> but faster.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.pairwise()</code> do? (Python 3.10+)",
  "<code>pairwise('ABCDE')</code> → <code>('A','B'),('B','C'),('C','D'),('D','E')</code>. Like <code>zip(iter, iter[1:])</code>. Great for consecutive diffs.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>itertools.accumulate()</code> do?",
  "Running accumulate. <code>accumulate([1,2,3,4])</code> → 1,3,6,10 (cumulative sum). <code>func=operator.mul</code> for product. <code>initial=N</code> prepends N (3.8+).",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>functools.reduce()</code> do?",
  "Left-fold: <code>reduce(operator.mul, [1,2,3,4])</code> = <code>((1*2)*3)*4</code> = 24. <code>initializer</code> is placed BEFORE the sequence.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>functools.partial()</code> do?",
  "Freezes some args of a function. <code>partial(int, base=2)</code> creates a binary-int parser. Frozen args go first; call-time args after.",
  ["L1_mechanics"])

c("IterFunctions", "How do you use <code>functools.lru_cache</code>?",
  "<code>@lru_cache(maxsize=128)</code> above a function. Memoizes by args, thread-safe. <code>maxsize=None</code> = unbounded. <code>f.cache_clear()</code> to invalidate, <code>f.cache_info()</code> for stats.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>functools.cached_property</code> do? (Python 3.8+)",
  "Compute-once descriptor. <code>@cached_property</code> on a method — computed on first access, stored in instance <code>__dict__</code>. NOT thread-safe on first access.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>functools.wraps()</code> do?",
  "Copies <code>__name__</code>, <code>__doc__</code>, <code>__module__</code>, <code>__dict__</code> from wrapped to wrapper. Essential for decorators so tracebacks/<code>help()</code> show the right name.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>functools.singledispatch</code> do?",
  "Dispatches on type of FIRST argument. Register with <code>@func.register(Type)</code>. Type-based polymorphism without class methods.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>operator.itemgetter</code> do?",
  "Callable that fetches by index/key. <code>itemgetter(1)</code> ≈ <code>lambda x: x[1]</code>. <code>itemgetter(1,0)</code> returns <code>(x[1], x[0])</code>. C-coded, faster than lambda.",
  ["L1_mechanics"])

c("IterFunctions", "What does <code>operator.attrgetter</code> do?",
  "Callable that fetches attributes. <code>attrgetter('name')</code>. Supports dotted: <code>attrgetter('a.b.c')</code>. C-coded, faster than lambda.",
  ["L1_mechanics"])

c("IterFunctions", "How do you generate all dice roll combinations? (CodeSignal)",
  "<code>list(itertools.product(range(1,7), repeat=n_dice))</code>. For unordered: <code>combinations_with_replacement</code>.",
  ["L2_composition"])

c("IterFunctions", "How do you memoize a recursive function?",
  "<code>from functools import lru_cache; @lru_cache(maxsize=None); def fib(n): return n if n &lt; 2 else fib(n-1) + fib(n-2)</code>. Cache auto-manages results.",
  ["L2_composition"])

c("IterFunctions", "How do you flatten a list of lists?",
  "<code>list(itertools.chain.from_iterable(list_of_lists))</code> — O(n). NEVER <code>sum(lists, [])</code> — O(n²) string-concatenation-style behavior.",
  ["L2_composition"])

c("IterFunctions", "How do you group dicts by a key?",
  "<code>groups = defaultdict(list); for d in dicts: groups[d['key']].append(d)</code>. Or <code>groupby(sorted(dicts, key=lambda d: d['k']), lambda d: d['k'])</code>.",
  ["L2_composition"])

c("IterFunctions", "Why use <code>operator.itemgetter</code> over lambda for <code>sorted()</code>?",
  "Faster (C-coded, no Python bytecode). Cleaner for multi-key: <code>sorted(data, key=itemgetter(1, 0))</code>. Also clearer intent.",
  ["L3_design"])

c("IterFunctions", "When should you use <code>reduce</code> vs a loop?",
  "Reduce for simple two-arg folds where it reads naturally (product, union). Loop for complex logic, intermediate state, or early exit. Readability first.",
  ["L3_design"])

c("IterFunctions", "Why does <code>lru_cache</code> fail on a list argument?",
  "Lists are mutable → unhashable (can't be dict keys). Use <code>tuple(arg)</code> or accept only hashable types.",
  ["L4_diagnosis"])

c("IterFunctions", "Why does <code>itertools.tee</code> consume extra memory?",
  "Stores consumed items not yet consumed by ALL tee'd iterators. If one runs far ahead, backlog grows. For large data, <code>list()</code> and slice copies often better.",
  ["L4_diagnosis"])

c("IterFunctions", "Why is <code>reduce(lambda a,b: a+b, strings)</code> horribly slow?",
  "Each <code>a+b</code> creates new intermediate string — O(n²). Use <code>''.join(strings)</code>. Similarly, <code>sum(lists, [])</code> is O(n²) — use <code>chain.from_iterable</code>.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 05 — IO and FILESYSTEM
# =====================================================================

c("IO", "How do you safely open and close a file?",
  "<code>with open('file.txt', 'r') as f: data = f.read()</code>. <code>with</code> guarantees close even on exception.",
  ["L1_mechanics"])

c("IO", "What file modes does <code>open()</code> support?",
  "<code>'r'</code> read, <code>'w'</code> write+truncate, <code>'a'</code> append, <code>'x'</code> exclusive create, <code>'r+'</code> read/write. Add <code>'b'</code> for binary, <code>'t'</code> for text.",
  ["L1_mechanics"])

c("IO", "How do you read a file line by line?",
  "<code>with open('file.txt') as f: for line in f: process(line.rstrip('\\n'))</code>. File object IS an iterator — memory efficient.",
  ["L1_mechanics"])

c("IO", "How do you get the current working directory?",
  "<code>os.getcwd()</code> or <code>Path.cwd()</code> (pathlib). Prefer <code>pathlib</code> for all new code — OOP, cross-platform.",
  ["L1_mechanics"])

c("IO", "How do you list files in a directory?",
  "<code>Path('.').iterdir()</code> — iterator of Path objects. <code>Path('.').glob('*.py')</code> — pattern matching. Older: <code>os.listdir(path)</code> returns names only.",
  ["L1_mechanics"])

c("IO", "How do you check if a path exists / is file / is dir?",
  "<code>Path('x').exists()</code>, <code>.is_file()</code>, <code>.is_dir()</code>. Older: <code>os.path.exists()</code>/<code>isfile()</code>/<code>isdir()</code>.",
  ["L1_mechanics"])

c("IO", "How do you join path components portably?",
  "<code>Path('a') / 'b' / 'c'</code> → <code>Path('a/b/c')</code> (Unix) or <code>Path('a\\b\\c')</code> (Windows). Never use <code>+ '/' +</code>.",
  ["L1_mechanics"])

c("IO", "How do you get path parts (stem, suffix, parent)?",
  "<code>p = Path('/a/b/c.txt'); p.name='c.txt'; p.stem='c'; p.suffix='.txt'; p.parent=Path('/a/b'); p.parts=('/', 'a', 'b', 'c.txt')</code>.",
  ["L1_mechanics"])

c("IO", "How do you create a temporary file that auto-deletes?",
  "<code>with tempfile.NamedTemporaryFile() as f: f.write(data); f.flush()</code>. Deleted when context exits. <code>delete=False</code> to keep.",
  ["L1_mechanics"])

c("IO", "How do you copy/move/delete files?",
  "<code>shutil.copy(src, dst)</code> — copy content+perms. <code>shutil.move(src, dst)</code> — rename or copy+delete. <code>Path('x').unlink()</code> — delete file.",
  ["L1_mechanics"])

c("IO", "How do you create a directory (and parents)?",
  "<code>Path('a/b/c').mkdir(parents=True, exist_ok=True)</code>. <code>parents=True</code> = <code>mkdir -p</code>.",
  ["L1_mechanics"])

c("IO", "What are <code>io.StringIO</code> and <code>io.BytesIO</code>?",
  "In-memory file-like objects. <code>StringIO</code> for text, <code>BytesIO</code> for bytes. For testing file-operating code, or composing output without disk.",
  ["L1_mechanics"])

c("IO", "How do you read an entire file into a string or bytes?",
  "<code>Path('f.txt').read_text()</code> for str. <code>Path('f.bin').read_bytes()</code> for bytes. Or <code>with open('f') as f: data = f.read()</code>.",
  ["L1_mechanics"])

c("IO", "How do you walk a directory tree recursively?",
  "<code>Path('.').rglob('*.py')</code> — recursive glob. <code>os.walk('.')</code> — <code>(dirpath, dirnames, filenames)</code> tuples. Prefer <code>rglob</code>.",
  ["L1_mechanics"])

c("IO", "How do you atomically write a file?",
  "<code>with tempfile.NamedTemporaryFile(dir=target_dir, delete=False) as tf: tf.write(data); os.replace(tf.name, final_path)</code>. Atomic on same filesystem.",
  ["L2_composition"])

c("IO", "How do you process all <code>.log</code> files in a directory tree line-by-line?",
  "<code>for path in Path('.').rglob('*.log'): for line in path.open(): process(line)</code>. Lazy — one line in memory at a time.",
  ["L2_composition"])

c("IO", "Why use <code>pathlib</code> over <code>os.path</code>?",
  "OOP: paths are objects with methods. <code>p / 'sub' / 'file'</code> vs <code>os.path.join(p, 'sub', 'file')</code>. Cross-platform, readable, modern. All new code should use pathlib.",
  ["L3_design"])

c("IO", "Why use <code>tempfile</code> instead of writing to <code>/tmp</code> manually?",
  "Safe name generation (no races), auto-cleanup, platform-appropriate location. Manual <code>/tmp/myfile</code> is a security and portability risk.",
  ["L3_design"])

c("IO", "Why does writing to a file not appear until program exits?",
  "Buffering. Call <code>f.flush()</code> or open with <code>buffering=1</code> (line-buffered). Context managers auto-flush+close on exit.",
  ["L4_diagnosis"])

c("IO", "Why does <code>os.listdir</code> return bare filenames?",
  "Returns names relative to listed dir. For full paths: <code>os.path.join(dir, name)</code> or use <code>Path(dir).iterdir()</code> which returns full Path objects.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 06 — SERIALIZATION
# =====================================================================

c("Serialization", "How do you parse JSON from a string?",
  "<code>json.loads(json_string)</code> — returns dict/list/str/int/float/bool/None. Raises <code>json.JSONDecodeError</code> (subclass of <code>ValueError</code>) with <code>.pos</code>, <code>.lineno</code>, <code>.colno</code>.",
  ["L1_mechanics"])

c("Serialization", "How do you serialize a Python dict to JSON string?",
  "<code>json.dumps(data, indent=2, ensure_ascii=False)</code>. <code>indent</code> pretty-prints. <code>ensure_ascii=False</code> preserves non-ASCII. <code>default=str</code> handles non-serializable types.",
  ["L1_mechanics"])

c("Serialization", "How do you handle datetime with <code>json.dumps</code>?",
  "Datetime not natively JSON-serializable. Use <code>default=lambda o: o.isoformat() if isinstance(o, datetime) else o</code> or subclass <code>json.JSONEncoder</code>.",
  ["L1_mechanics"])

c("Serialization", "How do you read/write JSON from/to files?",
  "<code>with open('data.json') as f: data = json.load(f)</code>. <code>json.dump(data, open('out.json', 'w'))</code>. Same as <code>loads</code>/<code>dumps</code> but with file objects.",
  ["L1_mechanics"])

c("Serialization", "How do you read CSV as list of dicts?",
  "<code>with open('data.csv', newline='') as f: rows = list(csv.DictReader(f))</code>. Each row is a dict keyed by header. <code>csv.reader</code> returns list rows.",
  ["L1_mechanics"])

c("Serialization", "How do you write CSV from list of dicts?",
  "<code>with open('out.csv','w',newline='') as f: writer = csv.DictWriter(f, fieldnames=keys); writer.writeheader(); writer.writerows(rows)</code>. MUST <code>newline=''</code> on open.",
  ["L1_mechanics"])

c("Serialization", "What does <code>pickle</code> do and when NOT to use it?",
  "Serializes arbitrary Python objects. NEVER unpickle untrusted data — can execute arbitrary code. Use <code>json</code> for data interchange; <code>pickle</code> only for internal persistence.",
  ["L1_mechanics"])

c("Serialization", "How do you pack/unpack binary data with <code>struct</code>?",
  "<code>struct.pack('>i4s', 42, b'ABCD')</code> → bytes. <code>struct.unpack('>i4s', packed)</code> → tuple. <code>></code>=big-endian, <code><</code>=little, <code>i</code>=int, <code>f</code>=float.",
  ["L1_mechanics"])

c("Serialization", "How do you base64 encode/decode?",
  "<code>base64.b64encode(data)</code> — bytes→bytes. <code>b64decode(encoded)</code>. For URLs: <code>urlsafe_b64encode</code> uses <code>-</code> and <code>_</code> instead of <code>+</code>/<code>/</code>.",
  ["L1_mechanics"])

c("Serialization", "How do you pretty-print JSON from command line?",
  "<code>python -m json.tool data.json</code> — reads JSON, pretty-prints to stdout. Also validates: if it succeeds, JSON is valid.",
  ["L2_composition"])

c("Serialization", "How do you add custom JSON serialization for a class?",
  "<code>json.dumps(obj, default=lambda o: {'__type__': o.__class__.__name__, **o.__dict__})</code>. For round-trip: pair with <code>object_hook</code> in <code>loads</code>.",
  ["L2_composition"])

c("Serialization", "Why use <code>json</code> over <code>pickle</code> for data storage?",
  "JSON: human-readable, cross-language, SAFE. Pickle: Python-only, unreadable, code-exec risk. JSON for interchange; pickle only for internal caching.",
  ["L3_design"])

c("Serialization", "Why does <code>json.dumps(float('nan'))</code> produce <code>NaN</code>?",
  "<code>NaN</code>/<code>Infinity</code> are NOT valid JSON. Python allows them by default (<code>allow_nan=True</code>). Set <code>allow_nan=False</code> to raise <code>ValueError</code>.",
  ["L4_diagnosis"])

c("Serialization", "Why does <code>csv.reader</code> produce extra blank lines on Windows?",
  "Missing <code>newline=''</code> on <code>open()</code>. CSV module handles its own newlines; default text-mode translation adds extra <code>\\r</code>.",
  ["L4_diagnosis"])

c("Serialization", "Why does <code>base64.b64encode</code> return <code>bytes</code> not <code>str</code>?",
  "Base64 transforms binary → binary. Call <code>.decode('ascii')</code> for string. <code>b64decode</code> expects <code>bytes</code> — pass <code>s.encode('ascii')</code> if you have a str.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 07 — DATE and TIME
# =====================================================================

c("DateTime", "How do you get the current date and time?",
  "<code>datetime.datetime.now(datetime.timezone.utc)</code> — UTC aware. <code>.now()</code> is local naive (bad for storage). <code>date.today()</code> for date only.",
  ["L1_mechanics"])

c("DateTime", "How do you parse a date string?",
  "<code>datetime.strptime('2024-01-15', '%Y-%m-%d')</code>. For ISO: <code>datetime.fromisoformat('2024-01-15T10:30:00')</code> (3.7+). Third-party <code>dateutil</code> for fuzzy parsing.",
  ["L1_mechanics"])

c("DateTime", "How do you format a datetime as a string?",
  "<code>dt.strftime('%Y-%m-%d %H:%M:%S')</code> or <code>dt.isoformat()</code>. Codes: <code>%Y</code>=year, <code>%m</code>=month, <code>%d</code>=day, <code>%H</code>=24h, <code>%M</code>=min, <code>%S</code>=sec.",
  ["L1_mechanics"])

c("DateTime", "How do you compute a time difference?",
  "Subtract: <code>diff = dt2 - dt1</code> → <code>timedelta</code>. <code>diff.days</code>, <code>diff.seconds</code>, <code>diff.total_seconds()</code>.",
  ["L1_mechanics"])

c("DateTime", "How do you add/subtract time from a datetime?",
  "<code>dt + datetime.timedelta(days=7, hours=2)</code>. Internally only <code>days</code>, <code>seconds</code>, <code>microseconds</code>. <code>timedelta(weeks=1)</code> = <code>days=7</code>.",
  ["L1_mechanics"])

c("DateTime", "What is naive vs aware datetime?",
  "Naive: no <code>tzinfo</code>. Aware: has <code>tzinfo</code>. NEVER mix them — Python raises <code>TypeError</code> or silently does wrong thing in comparison/arithmetic.",
  ["L1_mechanics"])

c("DateTime", "How do you make a naive datetime timezone-aware?",
  "<code>dt.replace(tzinfo=timezone.utc)</code> — assumes naive was UTC. For local: <code>zoneinfo.ZoneInfo('America/New_York')</code> (3.9+). Pre-3.9: third-party <code>pytz</code>.",
  ["L1_mechanics"])

c("DateTime", "How do you convert a datetime between timezones?",
  "<code>dt.astimezone(target_tz)</code> — returns new datetime in target zone. Works only on aware datetimes. Use <code>zoneinfo.ZoneInfo</code> for IANA names.",
  ["L1_mechanics"])

c("DateTime", "How do you get a Unix timestamp?",
  "<code>dt.timestamp()</code> — float seconds since epoch. For aware dt, converts to UTC first. <code>datetime.fromtimestamp(ts, tz=timezone.utc)</code> to go back.",
  ["L1_mechanics"])

c("DateTime", "How do you measure elapsed time correctly?",
  "<code>time.perf_counter()</code> for short intervals (monotonic, highest-res). <code>time.monotonic()</code> for long-running. NEVER <code>time.time()</code> — can jump backward (NTP, DST).",
  ["L1_mechanics"])

c("DateTime", "How do you pause execution (sleep)?",
  "<code>time.sleep(seconds)</code> — blocks calling thread (float ok, e.g. 0.5). For async: <code>await asyncio.sleep(seconds)</code>.",
  ["L1_mechanics"])

c("DateTime", "How do you get first/last day of current month?",
  "<code>import calendar; first = today.replace(day=1); _, days = calendar.monthrange(year, month); last = first + timedelta(days=days-1)</code>. <code>monthrange</code> returns (weekday_of_1st, days_in_month).",
  ["L2_composition"])

c("DateTime", "How do you iterate over a date range?",
  "<code>current = start; while current &lt;= end: yield current; current += timedelta(days=1)</code>. Use a generator. For complex recurrence: <code>dateutil.rrule</code> (third-party).",
  ["L2_composition"])

c("DateTime", 'Why does <code>datetime.now()</code> give wrong results in production?',
  "Naive (no TZ) — uses system local time, varies by server, ambiguous during DST. Always use <code>now(timezone.utc)</code> for storage, convert local for display only.",
  ["L4_diagnosis"])

c("DateTime", "Why does <code>timedelta(months=1)</code> raise <code>TypeError</code>?",
  "<code>timedelta</code> only supports <code>days</code>, <code>seconds</code>, <code>microseconds</code>. Months have variable lengths. Use <code>dateutil.relativedelta</code> (third-party) or <code>calendar.monthrange</code>.",
  ["L4_diagnosis"])

c("DateTime", "Why is <code>time.time()</code> bad for elapsed time?",
  "System clock can jump backward (NTP correction, DST). Use <code>time.perf_counter()</code> (short intervals) or <code>time.monotonic()</code> (long-running).",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 08 — CONCURRENCY
# =====================================================================

c("Concurrency", "What is the difference between threading and multiprocessing?",
  "Threading: shared memory, GIL-limited (one thread at time executes Python). Good for I/O. Multiprocessing: separate memory, bypasses GIL, uses multiple cores. Good for CPU-bound. IPC overhead.",
  ["L1_mechanics"])

c("Concurrency", "How do you run a function in a thread using <code>concurrent.futures</code>?",
  "<code>with ThreadPoolExecutor(max_workers=5) as e: future = e.submit(func, arg); result = future.result(timeout=10)</code>. Returns <code>Future</code>.",
  ["L1_mechanics"])

c("Concurrency", "How do you parallel-map a function over an iterable?",
  "<code>with ThreadPoolExecutor() as e: results = list(e.map(func, iterable))</code>. Preserves order, returns iterator. For CPU: <code>ProcessPoolExecutor</code>.",
  ["L1_mechanics"])

c("Concurrency", "How do you use a <code>Lock</code> to protect shared state?",
  "<code>lock = threading.Lock(); with lock: shared_data[key] = value</code>. <code>with</code> acquires/releases; exceptions unlock safely. <code>RLock</code> allows reentrant locking by same thread.",
  ["L1_mechanics"])

c("Concurrency", "What does <code>asyncio.run()</code> do?",
  "Entry point for asyncio. Creates event loop, runs coroutine, closes loop. <code>asyncio.run(main())</code> called from sync code — can't nest inside another running loop.",
  ["L1_mechanics"])

c("Concurrency", "How do you define and run an async function?",
  "<code>async def get_data(): return await fetch()</code>. <code>await</code> suspends execution, yields to event loop. Only callable from other <code>async def</code> or via <code>asyncio.run()</code>.",
  ["L1_mechanics"])

c("Concurrency", "How do you run multiple coroutines concurrently?",
  "<code>results = await asyncio.gather(coro1(), coro2(), coro3())</code> — returns list in submission order. <code>asyncio.as_completed()</code> yields as each finishes.",
  ["L1_mechanics"])

c("Concurrency", "How do you set a timeout for an async operation?",
  "<code>await asyncio.wait_for(coro, timeout=5.0)</code> — raises <code>asyncio.TimeoutError</code>. Wraps ANY awaitable. Python 3.11+: <code>async with asyncio.timeout(N):</code> context manager.",
  ["L1_mechanics"])

c("Concurrency", "How do you share data between processes?",
  "<code>multiprocessing.Queue</code> (thread-safe queue), <code>Pipe</code> (bidirectional), <code>Value</code>/<code>Array</code> (shared memory). All use pickle for Python objects.",
  ["L1_mechanics"])

c("Concurrency", "How do you create an async context manager?",
  "Define <code>__aenter__</code> and <code>__aexit__</code> (both async). Consume: <code>async with obj: ...</code>. Use <code>contextlib.asynccontextmanager</code> decorator to create from generators.",
  ["L1_mechanics"])

c("Concurrency", "How do you create an async iterator?",
  "Define <code>__aiter__</code> (can be async) and <code>__anext__</code> (async, raises <code>StopAsyncIteration</code>). Consume: <code>async for item in iterable:</code>.",
  ["L1_mechanics"])

c("Concurrency", "How do you run a blocking function without blocking the event loop?",
  "<code>result = await asyncio.to_thread(blocking_func, arg)</code> (Python 3.9+). Runs in default <code>ThreadPoolExecutor</code>. Pre-3.9: <code>loop.run_in_executor(None, f, arg)</code>.",
  ["L2_composition"])

c("Concurrency", "How do you implement producer-consumer with asyncio?",
  "<code>q = asyncio.Queue(); await q.put(item)</code> (producer); <code>item = await q.get()</code> (consumer); <code>q.task_done()</code>. Queue handles backpressure.",
  ["L2_composition"])

c("Concurrency", "How do you download multiple URLs concurrently with stdlib?",
  "Stdlib has NO async HTTP client. Use <code>ThreadPoolExecutor</code> + <code>urllib.request.urlopen</code> for parallel downloads. For true async: <code>aiohttp</code> or <code>httpx</code>.",
  ["L2_composition"])

c("Concurrency", "When to use asyncio vs threading vs multiprocessing?",
  "asyncio: I/O-bound, many concurrent connections (servers, scrapers). Threading: I/O-bound, non-async libs (file I/O, legacy DB). Multiprocessing: CPU-bound (data processing, ML inference).",
  ["L3_design"])

c("Concurrency", "Why is shared state between processes expensive?",
  "Separate memory spaces → data must be pickled (serialized) for IPC. Pickling is CPU-intensive and a bottleneck. Design for data parallelism — independent work per process.",
  ["L3_design"])

c("Concurrency", "Why does multithreaded CPU-bound code not run faster?",
  "The GIL prevents multiple threads from executing Python simultaneously. CPU threads take turns — single-thread performance at best. Use <code>ProcessPoolExecutor</code> or C extensions that release the GIL.",
  ["L4_diagnosis"])

c("Concurrency", "Why does <code>asyncio.run()</code> inside Jupyter crash?",
  "Jupyter already has a running event loop. Use <code>await</code> directly in cells, or <code>nest_asyncio</code> to allow nesting. Scripts: <code>asyncio.run()</code> is the only entry point.",
  ["L4_diagnosis"])

c("Concurrency", "Why does <code>ThreadPoolExecutor</code> hang on exit?",
  "No context manager — <code>with</code> calls <code>shutdown(wait=True)</code>. Without it, executor waits for running futures. Always use <code>with ThreadPoolExecutor() as e:</code>.",
  ["L4_diagnosis"])

c("Concurrency", "Why does <code>as_completed</code> return futures in weird order?",
  "Yields as futures COMPLETE, not as submitted. For ordered results, use <code>executor.map()</code>. <code>as_completed</code> is for processing results ASAP as each finishes.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 09 — NETWORKING
# =====================================================================

c("Networking", "How do you make an HTTP GET request using stdlib?",
  "<code>from urllib.request import urlopen; with urlopen('https://example.com') as resp: data = resp.read()</code>. Returns bytes. Always <code>with</code> and set <code>timeout=N</code>.",
  ["L1_mechanics"])

c("Networking", "How do you make an HTTP POST with JSON using stdlib?",
  "<code>req = Request(url, data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'}, method='POST'); with urlopen(req) as resp: data = resp.read()</code>. Must encode to bytes.",
  ["L1_mechanics"])

c("Networking", "How do you handle HTTP errors with <code>urllib</code>?",
  "Catch <code>urllib.error.HTTPError</code> first — has <code>.code</code>, <code>.reason</code>, and <code>.read()</code> for body. Then <code>URLError</code> for connection failures. <code>HTTPError</code> is subclass of <code>URLError</code>.",
  ["L1_mechanics"])

c("Networking", "How do you URL-encode query parameters?",
  "<code>urllib.parse.urlencode({'q':'hello world','page':2})</code> → <code>'q=hello+world&amp;page=2'</code>. For list values: <code>urlencode({'k':[1,2]}, doseq=True)</code> → <code>'k=1&amp;k=2'</code>.",
  ["L1_mechanics"])

c("Networking", "How do you parse a URL into components?",
  "<code>urlparse('https://user@ex.com:8080/path?q=1#frag')</code> returns <code>ParseResult</code> named tuple: <code>.scheme</code>, <code>.netloc</code>, <code>.path</code>, <code>.params</code>, <code>.query</code>, <code>.fragment</code>.",
  ["L1_mechanics"])

c("Networking", "How do you percent-encode/decode URL components?",
  "<code>urllib.parse.quote('hello world')</code> → <code>'hello%20world'</code>. <code>quote_plus</code>: spaces as <code>+</code>. <code>unquote</code>/<code>unquote_plus</code> decode.",
  ["L1_mechanics"])

c("Networking", "How do you resolve a relative URL?",
  "<code>urllib.parse.urljoin('https://example.com/path/', '../other')</code> → <code>'https://example.com/other'</code>. Handles <code>..</code>, absolute, scheme-relative.",
  ["L1_mechanics"])

c("Networking", "How do you create a TCP client socket?",
  "<code>s = socket.create_connection(('host', 80), timeout=5.0)</code>. High-level — handles DNS resolution, tries all addresses. Returns connected socket.",
  ["L1_mechanics"])

c("Networking", "How do you send and receive on a socket?",
  "<code>s.sendall(data_bytes)</code> — guarantees ALL sent (loops internally). <code>data = s.recv(4096)</code> — UP TO 4096 bytes. Loop <code>recv</code> until <code>b''</code> for full read.",
  ["L1_mechanics"])

c("Networking", "How do you start a simple HTTP server?",
  "<code>python -m http.server 8000</code> — serves CWD at <code>localhost:8000</code>. NOT for production. Specify dir (3.7+): <code>--directory /path</code>. Single-threaded.",
  ["L1_mechanics"])

c("Networking", "How do you send an email using stdlib?",
  "<code>from email.message import EmailMessage; msg = EmailMessage(); msg.set_content('Hello'); with smtplib.SMTP('host', 587) as s: s.starttls(); s.login(u,p); s.send_message(msg)</code>. Use <code>EmailMessage</code> (3.6+) not MIMEText.",
  ["L1_mechanics"])

c("Networking", "How do you create an SSL context for secure connections?",
  "<code>ssl.create_default_context()</code> — system CAs, TLS defaults. <code>ctx.wrap_socket(sock, server_hostname='host')</code> to upgrade. <code>ctx.load_cert_chain('cert.pem', 'key.pem')</code> for client certs.",
  ["L1_mechanics"])

c("Networking", "How do you build a URL with query parameters safely?",
  "<code>parts = urlparse(url); parts._replace(query=urlencode({'q':q,'p':p})).geturl()</code>. Never concatenate strings — use parse/unparse cycle.",
  ["L2_composition"])

c("Networking", "How do you implement a simple TCP echo server?",
  "<code>with socket.create_server(('', 9999)) as srv: while True: conn, _ = srv.accept(); with conn: while data := conn.recv(1024): conn.sendall(data)</code>. Single-threaded. Add <code>threading</code> for concurrency.",
  ["L2_composition"])

c("Networking", "How do you download a large file with progress?",
  "<code>with urlopen(url) as resp: with open('out','wb') as f: for chunk in iter(lambda: resp.read(8192), b''): f.write(chunk)</code>. Uses <code>iter</code> with sentinel to read chunks.",
  ["L2_composition"])

c("Networking", "Why use <code>requests</code> instead of <code>urllib</code>?",
  "Session pooling, auto JSON, better auth, simpler API, connection reuse. <code>urllib</code> is the stdlib fallback. Interviews: know <code>urllib</code> basics; production: <code>requests</code>/<code>httpx</code>.",
  ["L3_design"])

c("Networking", "Why use <code>sendall</code> instead of <code>send</code>?",
  "<code>send(data)</code> returns bytes actually sent — may be less than len(data). <code>sendall(data)</code> loops until all sent, raising on error. Always use <code>sendall</code>.",
  ["L3_design"])

c("Networking", "Why do I get <code>SSLCertVerificationError</code> with <code>urlopen</code>?",
  "Python verifies SSL with system CA bundle. Causes: expired cert, self-signed, missing intermediate, wrong time. macOS: run <code>Install Certificates.command</code> from Python folder.",
  ["L4_diagnosis"])

c("Networking", "Why does my socket <code>bind</code> fail with 'Address already in use'?",
  "Port in TIME_WAIT from previous run. Set <code>s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)</code> BEFORE <code>bind()</code>.",
  ["L4_diagnosis"])

c("Networking", "Why does <code>socket.recv(1024)</code> return fewer than 1024 bytes?",
  "<code>recv(N)</code> returns UP TO N bytes — whatever the OS buffer has ready. Loop until expected amount received or <code>recv</code> returns <code>b''</code> (peer closed).",
  ["L4_diagnosis"])

c("Networking", "Why does <code>http.server</code> serve the wrong directory?",
  "<code>SimpleHTTPRequestHandler</code> serves from <code>os.getcwd()</code>, not script dir. Use <code>--directory /path</code> (3.7+) or <code>os.chdir()</code>. Also: directory traversal CVE — fixed in 3.8+.",
  ["L4_diagnosis"])

c("Networking", "Should you use <code>http.client</code> directly?",
  "Almost never. Low-level: manual connections, header parsing, chunked encoding. Use <code>urllib</code> if stdlib-only; <code>requests</code>/<code>httpx</code> for real apps.",
  ["L5_opinion"])

# =====================================================================
# SUBDECK 10 — DATA MODELING
# =====================================================================

c("DataModeling", "What is <code>dataclasses.dataclass</code>?",
  "Decorator auto-generating <code>__init__</code>, <code>__repr__</code>, <code>__eq__</code>, and optionally <code>__hash__</code> from type annotations. <code>@dataclass class Point: x: int; y: int</code>.",
  ["L0_primitives"])

c("DataModeling", "What is the <code>typing</code> module?",
  "Type hint primitives: <code>List</code>, <code>Dict</code>, <code>Optional</code>, <code>Union</code>, <code>Literal</code>, <code>TypedDict</code>, <code>Protocol</code>, <code>Final</code>, <code>TypeAlias</code>. Runtime impact minimal — used by type checkers (mypy, pyright).",
  ["L0_primitives"])

c("DataModeling", "What is <code>Enum</code>?",
  "Symbolic names bound to unique values. <code>class Color(Enum): RED=1; GREEN=2</code>. Singletons, comparable by identity, iterable. <code>IntEnum</code>/<code>StrEnum</code> for int/str subclasses.",
  ["L0_primitives"])

c("DataModeling", "What is the <code>abc</code> module?",
  "Abstract Base Classes. <code>class Shape(ABC): @abstractmethod def area(self): ...</code>. Can't instantiate. Subclasses must implement <code>@abstractmethod</code>s. Used with <code>isinstance</code> for structural conformance.",
  ["L0_primitives"])

c("DataModeling", "How do you make a dataclass immutable?",
  "<code>@dataclass(frozen=True)</code> — instances become read-only. Hashable if all fields are hashable. <code>field(init=False)</code> for computed attributes excluded from <code>__init__</code>.",
  ["L1_mechanics"])

c("DataModeling", "How do you exclude a field from <code>__init__</code> or <code>__repr__</code>?",
  "<code>field(init=False)</code>: not in <code>__init__</code>. <code>field(repr=False)</code>: not in <code>__repr__</code>. <code>field(compare=False)</code>: excluded from <code>__eq__</code>/<code>__hash__</code>. <code>field(default_factory=list)</code>: mutable default.",
  ["L1_mechanics"])

c("DataModeling", "How do you validate a dataclass after init?",
  "<code>def __post_init__(self): if self.x &lt; 0: raise ValueError(...)</code>. Called automatically after <code>__init__</code>. Validate fields, compute derived values, enforce invariants.",
  ["L1_mechanics"])

c("DataModeling", "What is <code>typing.Optional[X]</code>?",
  "<code>Union[X, None]</code>. <code>Optional[str]</code> = <code>str | None</code>. Does NOT make the arg optional — use default value for that: <code>def f(x: Optional[str] = None)</code>.",
  ["L1_mechanics"])

c("DataModeling", "What is <code>typing.Literal</code>?",
  "Restrict to specific values. <code>def set_mode(mode: Literal['r','w','a']): ...</code>. Type checker flags non-literal args. Runtime: no effect.",
  ["L1_mechanics"])

c("DataModeling", "What is <code>typing.TypedDict</code>?",
  "Dict with typed keys. <code>class Movie(TypedDict): name: str; year: int</code>. Type checker validates. Runtime: just a <code>dict</code>. Ideal for JSON structures.",
  ["L1_mechanics"])

c("DataModeling", "What is <code>typing.Protocol</code>?",
  "Structural subtyping (static duck typing). <code>class Drawable(Protocol): def draw(self) -> None: ...</code>. Any class with <code>draw</code> method satisfies it without inheriting.",
  ["L1_mechanics"])

c("DataModeling", "What is <code>typing.Annotated</code>?",
  "<code>Annotated[T, metadata]</code> — adds metadata to type hint. <code>Annotated[int, ValueRange(0,100)]</code>. Metadata accessible at runtime via <code>get_type_hints(include_extras=True)</code>. Used by Pydantic/FastAPI.",
  ["L1_mechanics"])

c("DataModeling", "How do you define an abstract base class?",
  "<code>from abc import ABC, abstractmethod; class Base(ABC): @abstractmethod def doit(self): ...</code>. Subclasses MUST override <code>doit</code>. <code>...</code> (Ellipsis) is the idiomatic body.",
  ["L1_mechanics"])

c("DataModeling", "How do you auto-assign enum values?",
  "<code>class Color(Enum): RED = auto(); GREEN = auto()</code>. Values are implementation detail — don't rely on exact numbers. Use when values don't matter semantically.",
  ["L1_mechanics"])

c("DataModeling", "How do you register all subclasses automatically? (plugin pattern)",
  "<code>class Plugin: _registry = {}; def __init_subclass__(cls, **kw): super().__init_subclass__(**kw); Plugin._registry[cls.__name__] = cls</code>. Each subclass auto-registers on definition.",
  ["L2_composition"])

c("DataModeling", "How do you convert a dataclass to dict/tuple?",
  "<code>dataclasses.asdict(instance)</code> — recursive dict. <code>dataclasses.astuple(instance)</code> — recursive tuple. Useful for JSON serialization of nested dataclasses.",
  ["L2_composition"])

c("DataModeling", "How do you make a read-only cached computed property?",
  "<code>@cached_property def full_name(self): return f'{self.first} {self.last}'</code>. Computed once, stored in <code>__dict__</code>. Like <code>@property</code> + manual cache. Python 3.8+.",
  ["L2_composition"])

c("DataModeling", "When should you use <code>Protocol</code> vs <code>ABC</code>?",
  "<code>Protocol</code>: structural (duck typing) — any type with right methods works. <code>ABC</code>: nominal (must inherit). Protocol for callbacks/interfaces consumed by your code; ABC for frameworks controlling the hierarchy.",
  ["L3_design"])

c("DataModeling", "dataclass vs namedtuple vs TypedDict — when to use each?",
  "dataclass: mutable, methods, complex logic, post_init validation. namedtuple: immutable, lightweight, unpackable, backward-compat. TypedDict: typed dicts for JSON APIs, zero class-instance overhead.",
  ["L3_design"])

c("DataModeling", "Why use <code>Enum</code> instead of string constants?",
  "Singletons (<code>Color.RED is Color.RED</code>), prevents typos, supports iteration/membership/autocomplete. Strings silently accept wrong values. Enums are self-documenting.",
  ["L3_design"])

c("DataModeling", "Why does my dataclass with <code>mylist: list = []</code> share data?",
  "Mutable default — <code>[]</code> created ONCE at class definition, shared by all instances. Dataclass catches this early: raises <code>ValueError</code>. Fix: <code>field(default_factory=list)</code>.",
  ["L4_diagnosis"])

c("DataModeling", "Why does <code>isinstance(42, int | str)</code> raise <code>TypeError</code> in older Python?",
  "<code>int | str</code> union syntax is 3.10+. Pre-3.10: <code>isinstance(42, (int, str))</code> (tuple) or <code>Union[int, str]</code>. The <code>|</code> syntax doesn't work at runtime for <code>isinstance</code> pre-3.10.",
  ["L4_diagnosis"])

c("DataModeling", "Why does <code>Enum</code> member comparison return <code>False</code> for equal values?",
  "Enum compares by IDENTITY, not value. <code>Color.RED != Color.GREEN</code> even if both have value 1. <code>IntEnum</code> allows value comparison but weakens type safety.",
  ["L4_diagnosis"])

c("DataModeling", "Should you use <code>dataclass</code> or Pydantic <code>BaseModel</code>?",
  "Dataclass: stdlib, lightweight, internal data holders. Pydantic: full validation, serialization, JSON Schema, runtime type coercion. Use Pydantic at system boundaries (APIs, configs); dataclass internally.",
  ["L5_opinion"])

# =====================================================================
# SUBDECK 11 — TESTING and DEBUGGING
# =====================================================================

c("TestingDebug", "How do you write a basic unit test?",
  "<code>import unittest; class TestX(unittest.TestCase): def test_foo(self): self.assertEqual(result, expected)</code>. Run: <code>python -m unittest test_module.py</code>.",
  ["L1_mechanics"])

c("TestingDebug", "What are the most common <code>unittest</code> assertion methods?",
  "<code>assertEqual(a,b)</code>, <code>assertTrue(x)</code>, <code>assertFalse(x)</code>, <code>assertIs(a,b)</code>, <code>assertIsNone(x)</code>, <code>assertIn(a,b)</code>, <code>assertRaises(Exc, f)</code>, <code>assertAlmostEqual(a,b)</code> (floats).",
  ["L1_mechanics"])

c("TestingDebug", "How do you test that an exception is raised?",
  "<code>with self.assertRaises(ValueError): func(arg)</code>. Also: <code>self.assertRaises(ValueError, func, arg)</code>. Verifies exact exception type.",
  ["L1_mechanics"])

c("TestingDebug", "How do you skip a test conditionally?",
  "<code>@unittest.skip('reason')</code>, <code>@unittest.skipIf(condition, 'reason')</code>, <code>@unittest.skipUnless(condition, 'reason')</code>. <code>@expectedFailure</code> marks expected-to-fail tests.",
  ["L1_mechanics"])

c("TestingDebug", "What are <code>setUp</code> and <code>tearDown</code>?",
  "<code>setUp(self)</code>: before EACH test. <code>tearDown(self)</code>: after EACH test (even on failure). <code>setUpClass</code>/<code>tearDownClass</code>: once per test class.",
  ["L1_mechanics"])

c("TestingDebug", "How do you start the Python debugger interactively?",
  "<code>breakpoint()</code> (Python 3.7+). Drops into <code>pdb</code>. Commands: <code>n</code>=next, <code>s</code>=step into, <code>c</code>=continue, <code>p expr</code>=print, <code>l</code>=list code, <code>q</code>=quit.",
  ["L1_mechanics"])

c("TestingDebug", "How do you print a formatted exception traceback?",
  "<code>traceback.print_exc()</code> — prints to stderr. <code>traceback.format_exc()</code> — returns string. Useful in <code>except</code> blocks for logging.",
  ["L1_mechanics"])

c("TestingDebug", "How do you set up basic logging?",
  "<code>import logging; logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')</code>. Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.",
  ["L1_mechanics"])

c("TestingDebug", "How do you log to a file?",
  "<code>logging.basicConfig(filename='app.log', level=logging.INFO)</code>. Or: <code>handler = logging.FileHandler('app.log'); logging.getLogger().addHandler(handler)</code>.",
  ["L1_mechanics"])

c("TestingDebug", "How do you mock a function in a test?",
  "<code>from unittest.mock import patch; with patch('module.func', return_value=42): result = tested_function()</code>. Replaces <code>func</code> with <code>MagicMock</code> in the <code>with</code> block.",
  ["L2_composition"])

c("TestingDebug", "How do you assert mock was called with specific args?",
  "<code>mock.assert_called_once_with(arg1, arg2)</code>. <code>mock.assert_called_with(arg)</code> checks LAST call. <code>mock.call_args_list</code> for complex call histories.",
  ["L2_composition"])

c("TestingDebug", "How do you write doctests?",
  "<code>def add(a,b): '''&gt;&gt;&gt; add(2,3) 5''' return a+b</code>. Run: <code>python -m doctest module.py -v</code>. Doubles as docs and tests. Good for simple functions.",
  ["L2_composition"])

c("TestingDebug", "Why use <code>logging</code> instead of <code>print</code>?",
  "Severity levels (filterable), multiple outputs (file+console+syslog), auto timestamps/module names, configurable without code changes. <code>print</code> has none of these.",
  ["L3_design"])

c("TestingDebug", "Why does <code>assertEqual(1, True)</code> pass?",
  "<code>bool</code> is a subclass of <code>int</code> — <code>1 == True</code>. Use <code>assertIs(1, True)</code> for identity check. Surprising but consistent with Python's type hierarchy.",
  ["L4_diagnosis"])

c("TestingDebug", "Why is <code>patch</code> not working? Still calls real function.",
  "<code>patch</code> replaces the name WHERE LOOKED UP. If your module does <code>from other import func</code>, patch the IMPORTING module: <code>patch('your_module.func')</code>, not the source.",
  ["L4_diagnosis"])

c("TestingDebug", "Why does <code>basicConfig()</code> have no effect on second call?",
  "Configures root logger ONCE only. Subsequent calls silently ignored. Create named logger: <code>logger = logging.getLogger(__name__)</code> — inherits root's config but can have own handlers.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 12 — SECURITY and CRYPTO
# =====================================================================

c("Security", "How do you compute a SHA-256 hash?",
  "<code>hashlib.sha256(data).hexdigest()</code> — 64-char hex str. <code>.digest()</code> for raw bytes. Incremental: <code>h = sha256(); h.update(chunk); h.hexdigest()</code>.",
  ["L1_mechanics"])

c("Security", "How do you hash a password securely?",
  "NEVER <code>sha256</code>/<code>md5</code> directly. Use <code>hashlib.pbkdf2_hmac('sha256', password, salt, 100_000)</code>. Production: <code>bcrypt</code>, <code>scrypt</code>, <code>argon2</code> (memory-hard, auto salt).",
  ["L1_mechanics"])

c("Security", "How do you compare two secrets safely?",
  "<code>hmac.compare_digest(a, b)</code> — constant-time. For ANY secrets (API keys, tokens, signatures). Regular <code>==</code> short-circuits — attacker can time it byte-by-byte.",
  ["L1_mechanics"])

c("Security", "How do you create an HMAC?",
  "<code>hmac.HMAC(key, msg, hashlib.sha256).hexdigest()</code>. Key must be <code>bytes</code>. Verify: regenerate and compare with <code>compare_digest</code>. Used for webhooks, API signing.",
  ["L1_mechanics"])

c("Security", "How do you generate cryptographically secure random numbers?",
  "<code>secrets.token_hex(16)</code> — 32-char hex. <code>secrets.token_urlsafe(16)</code> — URL-safe. <code>secrets.choice(seq)</code> — secure choice. NEVER <code>random</code> for security (predictable Mersenne Twister).",
  ["L1_mechanics"])

c("Security", "What is the difference between <code>random</code> and <code>secrets</code>?",
  "<code>random</code>: fast, deterministic, reproducible (games/sims). <code>secrets</code>: OS CSPRNG, non-deterministic (passwords, tokens, keys). Use <code>secrets</code> for anything security-related.",
  ["L1_mechanics"])

c("Security", "How do you generate a cryptographically random integer?",
  "<code>secrets.randbelow(n)</code> — <code>[0, n)</code>. <code>secrets.randbits(k)</code> — k random bits. <code>random.SystemRandom()</code> wraps <code>os.urandom</code> with <code>random</code> API (older alternative).",
  ["L1_mechanics"])

c("Security", "How do you verify a signed webhook payload?",
  "<code>expected = hmac.HMAC(key, body, hashlib.sha256).hexdigest(); valid = compare_digest(expected, request.headers['X-Signature'])</code>. HMAC-SHA256 the raw body, constant-time compare.",
  ["L2_composition"])

c("Security", "How do you hash a large file without loading into memory?",
  "<code>h = sha256(); for chunk in iter(lambda: f.read(65536), b''): h.update(chunk); return h.hexdigest()</code>. 64KB chunks, O(1) memory, works on files of any size.",
  ["L2_composition"])

c("Security", "Why is <code>md5</code> still in the stdlib if it's cryptographically broken?",
  "Backward compat + non-security uses: checksums (file integrity vs accidental corruption), hash tables, fingerprinting. Use <code>hashlib.md5(usedforsecurity=False)</code> in 3.9+ to make intent clear.",
  ["L3_design"])

c("Security", "Why does <code>md5(b'data').hexdigest()</code> work but <code>md5().hexdigest()</code> gives empty hash?",
  "Passing data to constructor = create + update. <code>md5(b'data')</code> hashes 'data' immediately; <code>md5()</code> creates empty. Incremental: create empty, <code>.update(chunk)</code>.",
  ["L4_diagnosis"])

c("Security", "Why does <code>b64decode</code> raise <code>binascii.Error</code> not <code>ValueError</code>?",
  "Historical — wraps C-level <code>binascii</code> module. Catch <code>Exception</code> broadly or import <code>binascii</code> and catch <code>binascii.Error</code> specifically.",
  ["L4_diagnosis"])

# =====================================================================
# SUBDECK 13 — EXPERT PATTERNS
# =====================================================================

c("Expert", "How do you create a context manager from a generator?",
  "<code>@contextlib.contextmanager; def my_ctx(): setup(); try: yield resource; finally: teardown()</code>. Before <code>yield</code> = <code>__enter__</code>; after (in finally) = <code>__exit__</code>.",
  ["L1_mechanics"])

c("Expert", "What is <code>contextlib.suppress()</code>?",
  "<code>with suppress(FileNotFoundError): os.remove(path)</code>. Silently ignores specified exceptions. Cleaner than <code>try: except: pass</code>. Don't suppress broadly — hides bugs.",
  ["L1_mechanics"])

c("Expert", "What is <code>contextlib.ExitStack</code>?",
  "Dynamic stack of context managers — enter dynamically, exit in reverse order. <code>with ExitStack() as s: files = [s.enter_context(open(f)) for f in filenames]</code>. Perfect for variable number of resources.",
  ["L1_mechanics"])

c("Expert", "What is <code>contextlib.nullcontext</code>?",
  "No-op context manager. <code>with nullcontext(): ...</code>. For conditional contexts: <code>cm = open(f) if f else nullcontext(); with cm as r: ...</code>.",
  ["L1_mechanics"])

c("Expert", "What is <code>weakref.ref</code> and <code>WeakValueDictionary</code>?",
  "Weak references that don't prevent GC. <code>ref = weakref.ref(obj); obj = ref()</code> returns <code>None</code> if GC'd. <code>WeakValueDictionary</code>: values auto-remove when GC'd. For caches, registries, observers.",
  ["L1_mechanics"])

c("Expert", "What do descriptors <code>__get__</code>/<code>__set__</code>/<code>__delete__</code> do?",
  "Control attribute access. <code>__get__(self, instance, owner)</code> on read, <code>__set__(self, instance, value)</code> on write, <code>__delete__</code> on <code>del</code>. <code>@property</code>, <code>@staticmethod</code> are built on descriptors.",
  ["L1_mechanics"])

c("Expert", "What is <code>__slots__</code>?",
  "Class attribute fixing allowed instance attributes, preventing <code>__dict__</code>. <code>__slots__ = ('x','y')</code>. Saves ~50%+ memory per instance, faster attr access. No arbitrary attribute assignment.",
  ["L1_mechanics"])

c("Expert", "What is <code>__init_subclass__</code>?",
  "Classmethod called when class is subclassed. <code>class Base: def __init_subclass__(cls, **kw): ...</code>. Auto-registration, config validation, enforcing constraints — without metaclasses.",
  ["L1_mechanics"])

c("Expert", "What is <code>__set_name__</code> on a descriptor?",
  "Called when descriptor is assigned to a class attribute. <code>def __set_name__(self, owner, name): self.name = name</code>. Gives descriptor its attribute name — no manual passing. Python 3.6+.",
  ["L1_mechanics"])

c("Expert", "What does <code>sys.settrace</code> do?",
  "Sets a trace function called for every Python line executed. Basis of debuggers (<code>pdb</code>), profilers (<code>cProfile</code>), coverage tools. Very slow — not for production.",
  ["L1_mechanics"])

c("Expert", "What is the <code>gc</code> module?",
  "Controls cyclic garbage collector. <code>gc.collect()</code> — force collection. <code>gc.get_objects()</code> — all tracked objects. <code>gc.set_debug(gc.DEBUG_LEAK)</code> — leak debugging. Not normally needed.",
  ["L1_mechanics"])

c("Expert", "How do you write a decorator that takes arguments?",
  "Decorator factory (3 layers): <code>def retry(times): def decorator(func): @wraps(func) def wrapper(*a,**k): ... return wrapper; return decorator</code>. Factory → decorator → wrapper. Always use <code>@wraps</code>.",
  ["L2_composition"])

c("Expert", "How do you write a class decorator?",
  "<code>def add_foo(cls): cls.foo = 42; return cls; @add_foo class MyClass: ...</code>. Receives and returns the class. Can add methods, modify attrs, register.",
  ["L2_composition"])

c("Expert", "How do you implement a thread-safe singleton?",
  "<code>class Singleton: _inst = None; _lock = threading.Lock(); def __new__(cls): if cls._inst is None: with cls._lock: if cls._inst is None: cls._inst = super().__new__(cls); return cls._inst</code>. Double-checked locking.",
  ["L2_composition"])

c("Expert", "How do you implement <code>__copy__</code> and <code>__deepcopy__</code>?",
  "<code>__copy__(self)</code>: return new instance with same attrs. <code>__deepcopy__(self, memo)</code>: use <code>memo</code> dict to handle cycles, deep copy each attr. Used by <code>copy.copy()</code>/<code>copy.deepcopy()</code>.",
  ["L2_composition"])

c("Expert", "How do you use <code>WeakSet</code> for observer patterns?",
  "Store observers in <code>WeakSet()</code>. Auto-removed when GC'd — no explicit unregister. Prevents memory leaks from dangling observer references.",
  ["L2_composition"])

c("Expert", "When should you use <code>__slots__</code>?",
  "Use: millions of instances (data records). Avoid: need <code>__dict__</code> for dynamic attrs, multiple inheritance (complex layout), inheriting from <code>__dict__</code> class (adds dict anyway).",
  ["L3_design"])

c("Expert", "Why use <code>ExitStack</code> over nested <code>with</code> blocks?",
  "Dynamic number of context managers, conditional entering, and programmatic management. <code>ExitStack</code> guarantees LIFO cleanup. Nested <code>with</code> blocks require known count at write-time.",
  ["L3_design"])

c("Expert", "When should you use a metaclass vs <code>__init_subclass__</code>?",
  "<code>__init_subclass__</code>: 90% of use cases — simpler, no metaclass conflict. Metaclass: when you need to modify class CREATION (<code>__new__</code>), not just react to it. Prefer <code>__init_subclass__</code>.",
  ["L3_design"])

c("Expert", "How do you write a metatype?",
  "<code>class Meta(type): def __new__(meta, name, bases, ns): return super().__new__(meta, name, bases, ns); def __init__(cls, name, bases, ns): ...</code>. <code>__new__</code> creates the class; <code>__init__</code> initializes it. Use: <code>class Foo(metaclass=Meta): ...</code>.",
  ["L6_innovation"])

c("Expert", "What does <code>typing.get_type_hints</code> do that <code>__annotations__</code> doesn't?",
  "Resolves forward references (string annotations), evaluates <code>from __future__ import annotations</code>, and handles <code>Annotated</code> metadata. <code>__annotations__</code> is raw dict — use <code>get_type_hints(obj)</code> for runtime inspection.",
  ["L6_innovation"])

c("Expert", "How do you implement an LRU cache manually using <code>OrderedDict</code>?",
  "<code>class LRU(OrderedDict): def __init__(self, maxsize): ...; def __getitem__(self, k): self.move_to_end(k); return super().__getitem__(k); def __setitem__(self, k, v): super().__setitem__(k, v); if len(self) &gt; self.maxsize: self.popitem(last=False)</code>.",
  ["L6_innovation"])

c("Expert", "How do you build a coroutine-based scheduler (like <code>asyncio</code>) manually?",
  "Use <code>collections.deque</code> as a task queue. Each task is a generator/coroutine. Loop: pop task, send <code>None</code> via <code>.send()</code>, catch <code>StopIteration</code>. If task yields a future, re-queue. This is how <code>asyncio</code> and <code>curio</code> work at the core.",
  ["L6_innovation"])

c("Expert", "How do you use <code>importlib</code> to dynamically import a module by name?",
  "<code>import importlib; mod = importlib.import_module('package.module')</code>. For reload: <code>importlib.reload(mod)</code>. Use for plugin systems, hot-reloading, or config-driven imports.",
  ["L6_innovation"])

c("Expert", "How do you inspect a function's signature at runtime?",
  "<code>from inspect import signature; sig = signature(func); sig.parameters</code> — OrderedDict of <code>Parameter</code> objects (<code>.name</code>, <code>.kind</code>, <code>.default</code>, <code>.annotation</code>). <code>sig.bind(*a, **kw)</code> validates args.",
  ["L6_innovation"])

# =====================================================================
# BUILD and WRITE
# =====================================================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = "Python_Stdlib_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")

# VERIFICATION (run this block after build):
# import zipfile, sqlite3, json
# FILENAME = "Python_Stdlib_Zero_to_Hero.apkg"
# with zipfile.ZipFile(FILENAME) as z: z.extract("collection.anki2", "/tmp/")
# db = sqlite3.connect("/tmp/collection.anki2")
# n, c = db.execute("SELECT count(*) FROM notes").fetchone()[0], db.execute("SELECT count(*) FROM cards").fetchone()[0]
# decks_data = json.loads(db.execute("SELECT decks FROM col").fetchone()[0])
# print(f"Notes: {n}, Cards: {c}")
# for v in decks_data.values():
#     if v["name"] != "Default": print(f"  {v['name']}")
# assert n == c == len(C), f"Mismatch: {n} notes, {c} cards, {len(C)} defined"
