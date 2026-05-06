import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Phoenix_Elixir"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Patterns"),
    "Workflows":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Workflows"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
    "Internals":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Internals"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === ELIXIR FUNDAMENTALS ===

c("Fundamentals", "What is Elixir?",
  "A dynamic, functional language built on the Erlang VM (BEAM), designed for building scalable and maintainable applications.",
  ["L0_primitives"])

c("Fundamentals", "What is the BEAM?",
  "Bogdan/Björn's Erlang Abstract Machine — the VM that runs Erlang and Elixir code. Provides lightweight processes, fault-tolerance, and soft real-time capabilities.",
  ["L0_primitives"])

c("Fundamentals", "What is an Elixir process?",
  "A lightweight, isolated concurrent unit on the BEAM — NOT an OS process. Each has its own memory and communicates via message passing.",
  ["L0_primitives"])

c("Fundamentals", "How is concurrency handled in Elixir?",
  "Via the Actor model: lightweight BEAM processes that send and receive messages. No shared memory. Supervisors manage process lifecycles.",
  ["L0_primitives"])

c("Fundamentals", "What is immutability in Elixir?",
  "Data cannot be modified in place. Every transformation returns a new copy. This eliminates shared-mutable-state bugs and simplifies concurrency.",
  ["L0_primitives"])

c("Fundamentals", "What is pattern matching in Elixir?",
  "The <code>=</code> operator is a match operator. It destructures data on the left if it can match the right. Failures raise MatchError.",
  ["L0_primitives"])

c("Fundamentals", "What is a tuple in Elixir?",
  "A fixed-size, ordered collection stored contiguously in memory. Written as <code>{:ok, value}</code>. Access with <code>elem/2</code> or pattern matching.",
  ["L0_primitives"])

c("Fundamentals", "What is a list in Elixir?",
  "A linked list of cons cells: <code>[head | tail]</code>. Efficient for prepending (<code>O(1)</code>), not random access (<code>O(n)</code>).",
  ["L0_primitives"])

c("Fundamentals", "What is a map in Elixir?",
  "A key-value store with <code>O(log n)</code> access. Two syntaxes: <code>%{key =&gt; value}</code> for any keys, <code>%{key: value}</code> for atom keys.",
  ["L0_primitives"])

c("Fundamentals", "What is an atom in Elixir?",
  "A constant whose name is its value, like Ruby symbols. Prefixed with <code>:</code>. Commonly used as tags like <code>:ok</code>, <code>:error</code>. Atoms are not garbage collected.",
  ["L0_primitives"])

c("Fundamentals", "What is a keyword list?",
  "A list of two-element tuples with atom first elements. Syntactic sugar: <code>[a: 1, b: 2]</code> is <code>[{:a, 1}, {:b, 2}]</code>. Keys can repeat and order matters.",
  ["L0_primitives"])

c("Fundamentals", "What is the pipe operator <code>|&gt;</code>?",
  "Takes the result of the left expression and passes it as the first argument to the right function. Enables clear data-transformation pipelines.",
  ["L1_mechanics"])

c("Fundamentals", "What is a module in Elixir?",
  "A namespace for functions, defined with <code>defmodule</code>. Can contain public (<code>def</code>) and private (<code>defp</code>) functions.",
  ["L0_primitives"])

c("Fundamentals", "What is a Mix project?",
  "Mix is Elixir's build tool, task runner, and dependency manager. Created via <code>mix new project_name</code>. Generates a standard project skeleton.",
  ["L0_primitives"])

c("Fundamentals", "What is OTP?",
  "Open Telecom Platform — a set of libraries and design principles for building fault-tolerant, distributed systems on the BEAM. Includes GenServer, Supervisor, Application.",
  ["L0_primitives"])

c("Fundamentals", "What is a GenServer?",
  "A generic server behavior — the most common OTP abstraction for maintaining state and handling synchronous/asynchronous calls in a process.",
  ["L0_primitives"])

c("Fundamentals", "What is a Supervisor in Elixir/OTP?",
  "A process whose only job is to monitor child processes and restart them according to a strategy (<code>:one_for_one</code>, <code>:one_for_all</code>, <code>:rest_for_one</code>).",
  ["L0_primitives"])

c("Fundamentals", "What is IEx?",
  "Elixir's interactive shell — a REPL where you can evaluate expressions, inspect modules, and connect to running BEAM nodes.",
  ["L0_primitives"])

c("Fundamentals", "What is a struct in Elixir?",
  "A typed map with predefined keys and default values. Defined inside a module with <code>defstruct</code>. Enforces compile-time key validation.",
  ["L0_primitives"])

c("Fundamentals", "What is a behaviour in Elixir?",
  "A contract that a module must implement certain callbacks. Defined with <code>@callback</code>, implemented with <code>@behaviour</code>. Used heavily in OTP (GenServer, Supervisor).",
  ["L0_primitives"])

# === ELIXIR MECHANICS ===

c("CoreOps", "How do you define a module in Elixir?",
  "<code>defmodule MyModule do ... end</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you define a public function?",
  "<code>def my_function(arg) do ... end</code> — callable from other modules as <code>MyModule.my_function(val)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a private function?",
  "<code>defp my_private(arg) do ... end</code> — only callable within the same module.",
  ["L1_mechanics"])

c("CoreOps", "How do you pattern match on a function head?",
  "Write multiple <code>def</code> clauses with different patterns. Elixir tries them top-to-bottom and executes the first match. Example: <code>def fib(0), do: 0; def fib(1), do: 1; def fib(n), do: fib(n-1) + fib(n-2)</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you prepend to a list?",
  "<code>[new_head | existing_list]</code> — <code>O(1)</code> operation that creates a new list with the element at the front.",
  ["L1_mechanics"])

c("CoreOps", "How do you access a map key?",
  "<code>map[key]</code> for any key type, or <code>map.key</code> for atom keys. Pattern matching is preferred: <code>%{key: val} = map</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you update a map or struct key?",
  "<code>%{map | key: new_val}</code> — this syntax requires the key to exist. For adding keys use <code>Map.put(map, :key, val)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an anonymous function?",
  "<code>fn x -&gt; x * 2 end</code> for named params, or the capture syntax <code>&amp;(&amp;1 * 2)</code>. Call with dot notation: <code>func.(arg)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the capture operator for functions?",
  "<code>&amp;String.upcase/1</code> creates a function reference. <code>&amp;(&amp;1 + &amp;2)</code> creates shorthand anonymous functions using positional args.",
  ["L1_mechanics"])

c("CoreOps", "How do you iterate over an enumerable?",
  "Use the <code>Enum</code> module: <code>Enum.map(collection, fn x -&gt; x * 2 end)</code>, <code>Enum.each</code>, <code>Enum.filter</code>, <code>Enum.reduce</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle the <code>{:ok, result}</code> and <code>{:error, reason}</code> tuples?",
  "With <code>case</code> or <code>with</code>: <code>case File.read(path) do <br> {:ok, content} -&gt; content<br> {:error, reason} -&gt; reason<br> end</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you raise and rescue errors?",
  "<code>raise \"message\"</code> raises a RuntimeError. <code>try do ... rescue RuntimeError -&gt; ... end</code> catches it. Prefer tagged tuples (<code>{:ok/:error}</code>) over exceptions for control flow.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a new Mix project?",
  "<code>mix new my_project</code> — add <code>--sup</code> to include an OTP supervision tree (Application + Supervisor).",
  ["L1_mechanics"])

c("CoreOps", "How do you add a dependency?",
  "Add <code>{:package_name, \"~&gt; version\"}</code> to <code>deps</code> in <code>mix.exs</code>, then run <code>mix deps.get</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you run tests?",
  "<code>mix test</code> runs all tests. <code>mix test test/file_test.exs:LINE</code> runs a specific test. <code>mix test --trace</code> for verbose output.",
  ["L1_mechanics"])

c("CoreOps", "How do you start IEx with your project?",
  "<code>iex -S mix</code> — starts an interactive shell with your project's modules and dependencies loaded.",
  ["L1_mechanics"])

c("CoreOps", "How do you recompile on file change?",
  "Run <code>iex -S mix</code> then type <code>recompile()</code>. Or use <code>mix compile --watch</code> (requires fswatch).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a default value for a function parameter?",
  "<code>def greet(name \\\\ \"World\")</code> — the <code>\\\\</code> operator provides a default value when the argument is not passed.",
  ["L1_mechanics"])

c("CoreOps", "How do you use guards in a function clause?",
  "<code>def sign(n) when n &gt; 0, do: :positive<br> def sign(n) when n &lt; 0, do: :negative<br> def sign(0), do: :zero</code>",
  ["L1_mechanics"])

c("CoreOps", "What are valid guard clauses?",
  "Only pure, limited expressions: comparisons, type checks (<code>is_integer/1</code>), arithmetic, boolean operators, and a few Kernel functions. Cannot call user-defined functions.",
  ["L1_mechanics"])

c("CoreOps", "How do you send a message to a process?",
  "<code>send(pid, {:hello, \"world\"})</code> — the message goes into the recipient's mailbox. Messages are processed in order via <code>receive</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you receive a message?",
  "<code>receive do<br> {:hello, name} -&gt; IO.puts(\"Hello, #{name}\")<br> after 5000 -&gt; IO.puts(\"Timeout\")<br> end</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you spawn a new process?",
  "<code>spawn(fn -&gt; some_work() end)</code> or <code>spawn(Module, :function, [args])</code>. Returns a PID.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a struct?",
  "<code>defmodule User do<br> defstruct [:name, :email, age: 0]<br> end</code> — creates <code>%User{}</code> with defaults.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the <code>|&gt;</code> pipe operator?",
  "<code>\"hello\" |&gt; String.upcase() |&gt; String.reverse()</code> — the result of each expression becomes the first argument of the next function call.",
  ["L1_mechanics"])

c("CoreOps", "How do you pattern match in a <code>with</code> block?",
  "<code>with {:ok, a} &lt;- step1(), {:ok, b} &lt;- step2(a) do<br> b<br> else<br> {:error, reason} -&gt; reason<br> end</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you inspect a value in IEx?",
  "Type the expression and press Enter. Or use <code>IO.inspect(value, label: \"debug\")</code> to print during execution while returning the value.",
  ["L1_mechanics"])

c("CoreOps", "How do you get help for a module in IEx?",
  "<code>h ModuleName</code> for module docs, <code>h ModuleName.function</code> for function docs and typespecs.",
  ["L1_mechanics"])

# === PHOENIX FUNDAMENTALS ===

c("Fundamentals", "What is Phoenix?",
  "A web framework for Elixir using the MVC pattern. Built on Plug and Cowboy, with real-time support via Phoenix Channels (WebSockets) and LiveView for server-rendered reactive UIs.",
  ["L0_primitives"])

c("Fundamentals", "What is Plug in Phoenix?",
  "A specification for composable modules in web applications. Plugs are functions that receive a connection and return a modified connection. Forms the middleware pipeline of Phoenix.",
  ["L0_primitives"])

c("Fundamentals", "What is Phoenix LiveView?",
  "A library for building rich, real-time user experiences with server-rendered HTML. State lives on the server; UI diffs are pushed over WebSocket. No client-side JS required for interactivity.",
  ["L0_primitives"])

c("Fundamentals", "What is an Ecto schema?",
  "A mapping between Elixir structs and database tables. Part of Ecto (the database library). Defines fields, types, associations, and validations.",
  ["L0_primitives"])

c("Fundamentals", "What is Ecto.Changeset?",
  "A pipeline for filtering, casting, validating, and tracking changes to data before inserting/updating in the database. Central to form handling in Phoenix.",
  ["L0_primitives"])

c("Fundamentals", "What is a Phoenix Channel?",
  "A bidirectional, persistent communication layer over WebSockets (or fallback long-polling). Used for real-time features like chat, notifications, and LiveView.",
  ["L0_primitives"])

c("Fundamentals", "What is a Phoenix Context?",
  "A module that groups related business logic and data access. Acts as a boundary and public API for a feature area (e.g., <code>Accounts</code>, <code>Catalog</code>). Controllers call contexts, not Ecto directly.",
  ["L0_primitives"])

c("Fundamentals", "What is Phoenix PubSub?",
  "A distributed publish-subscribe system for broadcasting messages across nodes and processes. Channels and LiveView both rely on it internally.",
  ["L0_primitives"])

c("Fundamentals", "What is a Phoenix Endpoint?",
  "The entry point for all HTTP requests. Handles the request pipeline, routing, and starts the web server. Defined in <code>lib/my_app_web/endpoint.ex</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is Phoenix Router?",
  "Maps HTTP verbs and paths to controller actions, pipes requests through pipelines (like <code>:browser</code>, <code>:api</code>), and defines LiveView routes.",
  ["L0_primitives"])

c("Fundamentals", "What is a Phoenix Template (HEEx)?",
  "HTML+EEx — Phoenix's HTML-aware template language. Supports embedded Elixir with <code>&lt;%= %&gt;</code> and component-style <code>&lt;.form&gt;</code> function components.",
  ["L0_primitives"])

c("Fundamentals", "What is Phoenix.Component?",
  "A module that defines reusable, stateless or stateful (LiveComponent) UI functions. Uses <code>~H</code> sigil for HEEx templates. Inline assigns via <code>attr</code> and <code>slot</code> macros.",
  ["L0_primitives"])

c("Fundamentals", "What is a Phoenix LiveComponent?",
  "A stateful component managed by a LiveView. Has its own <code>mount</code>, <code>update</code>, and <code>handle_event</code> lifecycle. Can send messages to its parent LiveView.",
  ["L0_primitives"])

c("Fundamentals", "How does LiveView track state changes?",
  "Assigns — a map of state in the socket. When assigns change, LiveView diffs the old and new state and sends minimal HTML patches over WebSocket to the browser.",
  ["L1_mechanics"])

# === PHOENIX MECHANICS ===

c("CoreOps", "How do you generate a new Phoenix project?",
  "<code>mix phx.new my_app</code> — creates the full project skeleton with Ecto, LiveView, Tailwind (optional), and tests.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a new Ecto migration?",
  "<code>mix ecto.gen.migration add_users_table</code> — creates a migration file in <code>priv/repo/migrations/</code>. Fill in the <code>change/0</code> function.",
  ["L1_mechanics"])

c("CoreOps", "How do you run migrations?",
  "<code>mix ecto.migrate</code> runs all pending migrations. <code>mix ecto.rollback</code> reverts the last migration.",
  ["L1_mechanics"])

c("CoreOps", "How do you generate an Ecto context with schema?",
  "<code>mix phx.gen.context Accounts User users name:string email:string:unique</code> — generates schema, migration, context, and tests.",
  ["L1_mechanics"])

c("CoreOps", "How do you generate a LiveView page?",
  "<code>mix phx.gen.live Catalog Product products name:string price:decimal</code> — generates full CRUD LiveView with context, tests, and templates.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a route in Phoenix?",
  "In <code>router.ex</code>: <code>get \"/users\", UserController, :index</code> for standard controllers, <code>live \"/users\", UserLive.Index, :index</code> for LiveViews.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a Phoenix controller action?",
  "<code>def index(conn, _params) do<br> users = Accounts.list_users()<br> render(conn, :index, users: users)<br> end</code> — returns a <code>Plug.Conn</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a changeset validation?",
  "<code>def changeset(user, attrs) do<br> user<br> |&gt; cast(attrs, [:name, :email])<br> |&gt; validate_required([:name, :email])<br> |&gt; unique_constraint(:email)<br> |&gt; validate_format(:email, ~r/@/)<br> end</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you write an Ecto query?",
  "<code>from u in User, where: u.age &gt; 18, select: u.name</code> or the keyword syntax: <code>User |&gt; where([u], u.age &gt; 18) |&gt; select([u], u.name)</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you insert a record with Ecto?",
  "<code>Accounts.create_user(%{name: \"Alice\", email: \"a@b.com\"})</code> — typically calls <code>Repo.insert(changeset)</code> inside the context function.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle a form submission in LiveView?",
  "<code>def handle_event(\"save\", %{\"user\" =&gt; params}, socket) do ... end</code> — receives the form data, validates with changeset, and updates assigns.",
  ["L1_mechanics"])

c("CoreOps", "How do you send an event from client to LiveView?",
  "<code>phx-click=\"my_event\"</code> (no JS) or <code>JS.push(\"my_event\", value: %{key: val})</code> for programmatic pushes with optional payload.",
  ["L1_mechanics"])

c("CoreOps", "How do you broadcast a message via PubSub in Phoenix?",
  "<code>Phoenix.PubSub.broadcast(MyApp.PubSub, \"users:1\", {:user_updated, user})</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you subscribe to a PubSub topic in a LiveView?",
  "In <code>mount/3</code> or <code>handle_params/3</code>: <code>if connected?(socket), do: Phoenix.PubSub.subscribe(MyApp.PubSub, \"topic\")</code> — then handle with <code>handle_info/2</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a Phoenix Channel?",
  "<code>mix phx.gen.channel Room</code> — generates channel module with <code>join/3</code>, <code>handle_in/3</code>, <code>handle_out/3</code> callbacks.",
  ["L1_mechanics"])

c("CoreOps", "How do you start Phoenix server?",
  "<code>mix phx.server</code> or <code>iex -S mix phx.server</code> to run with an interactive shell.",
  ["L1_mechanics"])

c("CoreOps", "How do you configure the database in Phoenix?",
  "In <code>config/dev.exs</code> (or <code>config/runtime.exs</code>): configure <code>config :my_app, MyApp.Repo, database: \"my_app_dev\", ...</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you add a custom Plug?",
  "Define a module with <code>init/1</code> and <code>call/2</code>: <code>def call(conn, _opts), do: Conn.put_resp_header(conn, \"x-custom\", \"val\")</code>. Add to the pipeline in <code>router.ex</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a LiveView module?",
  "<code>use MyAppWeb, :live_view</code> — then define <code>mount/3</code>, <code>render/1</code>, and event handlers (<code>handle_event</code>, <code>handle_info</code>, <code>handle_params</code>).",
  ["L1_mechanics"])

# === ELIXIR PATTERNS ===

c("Patterns", "What is the Supervisor restart strategy <code>:one_for_one</code>?",
  "When a child crashes, only that child is restarted. Others continue unaffected. Best for independent processes.",
  ["L2_composition"])

c("Patterns", "What is the Supervisor restart strategy <code>:one_for_all</code>?",
  "When a child crashes, ALL children are terminated and restarted in order. Use when children depend on each other and must stay in sync.",
  ["L2_composition"])

c("Patterns", "What is the Supervisor restart strategy <code>:rest_for_one</code>?",
  "When a child crashes, that child and all children started AFTER it are terminated and restarted. Useful for ordered dependencies (DB connection pool before repository).",
  ["L2_composition"])

c("Patterns", "What is the let-it-crash philosophy?",
  "Don't defensively code for every error — instead let processes crash and let supervisors restart them from a clean state. Focus recovery logic in supervisors, not business code.",
  ["L3_design"])

c("Patterns", "How should you handle error states in Elixir functions?",
  "Return <code>{:ok, result}</code> or <code>{:error, reason}</code> tuples (not exceptions). This makes error handling explicit and composable via <code>with</code>, <code>case</code>.",
  ["L2_composition"])

c("Patterns", "What is the registry pattern in Ecto contexts?",
  "Context modules act as the public API. Controllers/dead views should never call <code>MyApp.Repo</code> directly — always go through the context. This provides a clear boundary and single place for authorization.",
  ["L3_design"])

c("Patterns", "What is the umbrella project pattern in Elixir?",
  "An umbrella project (<code>mix new app --umbrella</code>) contains multiple Mix sub-projects in <code>apps/</code>. Useful for separating bounded contexts, reducing compile times, and independently versioning components.",
  ["L3_design"])

c("Patterns", "What is the GenServer <code>handle_call</code> vs <code>handle_cast</code> pattern?",
  "<code>handle_call</code>: synchronous, caller waits for reply. <code>handle_cast</code>: asynchronous, caller continues immediately. Use <code>call</code> for reads/queries, <code>cast</code> for fire-and-forget updates.",
  ["L2_composition"])

c("Patterns", "What is the Ecto multi pattern?",
  "<code>Ecto.Multi</code> chains operations into a transaction: <code>Multi.new() |&gt; Multi.insert(:user, changeset) |&gt; Multi.insert(:profile, profile_cs) |&gt; Repo.transaction()</code>. All-or-nothing semantics.",
  ["L2_composition"])

c("Patterns", "What is the LiveView assign pattern?",
  "Use <code>assign(socket, :key, value)</code> to set state. For multiple: <code>assign(socket, key1: \"val1\", key2: \"val2\")</code>. Every assign change triggers a re-render diff against the previous render.",
  ["L2_composition"])

c("Patterns", "What is the Phoenix HEEx component pattern?",
  "Function components: define a function that takes <code>assigns</code> and returns <code>~H\"\"\"...\"\"\"</code>. Declare slots and attributes with <code>attr</code> and <code>slot</code>. Call as <code>&lt;.component_name attr=\"val\"&gt;</code>.",
  ["L2_composition"])

c("Patterns", "What is the GenServer client-API pattern?",
  "Create thin wrapper functions in the GenServer module: <code>def start_link(args), do: GenServer.start_link(__MODULE__, args)</code>. This hides the PID from callers and provides a clean interface.",
  ["L2_composition"])

c("Patterns", "How do you share Ecto queries across contexts?",
  "Use composable Ecto query functions that return <code>Ecto.Queryable.t()</code>: <code>def active(query), do: from q in query, where: q.active == true</code>. Compose with pipes: <code>User |&gt; active() |&gt; by_role(:admin)</code>",
  ["L2_composition"])

# === ELIXIR DIAGNOSIS ===

c("Gotchas", "Why does <code>length(list)</code> become slow on large lists?",
  "Lists are linked lists. <code>length/1</code> traverses the entire list (<code>O(n)</code>). For frequent length checks, consider using a map with a counter or a tuple with metadata.",
  ["L4_diagnosis"])

c("Gotchas", "What happens if you create too many atoms at runtime?",
  "The BEAM atom table has a hard limit (default ~1M) and atoms are NOT garbage collected. Creating atoms from user input (<code>String.to_atom</code>) can crash the VM. Use <code>String.to_existing_atom/1</code> instead.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>Ecto.put_assoc</code> delete existing records?",
  "<code>put_assoc</code> replaces the entire association. To add to an existing association, use <code>Ecto.build_assoc</code> or manipulate the assoc list manually. Use <code>cast_assoc</code> for nested forms.",
  ["L4_diagnosis"])

c("Gotchas", "Why does LiveView sometimes not re-render?",
  "LiveView diffs assigns by identity. If you mutate a nested structure in-place instead of creating a new copy, LiveView won't detect the change. Always return new maps/lists from updates.",
  ["L4_diagnosis"])

c("Gotchas", "What causes <code>GenServer timeout</code> errors?",
  "The default timeout is 5000ms. If <code>handle_call</code> takes longer, the caller crashes. Restructure long work using <code>handle_cast</code> + <code>GenServer.reply/2</code>, or use <code>Task.async</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>IO.inspect</code> return a value?",
  "<code>IO.inspect/2</code> prints the value AND returns it — perfect for pipe debugging: <code>data |&gt; IO.inspect(label: \"before\") |&gt; transform() |&gt; IO.inspect(label: \"after\")</code>",
  ["L4_diagnosis"])

c("Gotchas", "What is the classic Phoenix 'DBConnection' pool exhaustion error?",
  "The default Ecto pool size is 10. Long-running queries or forgotten connections can exhaust the pool. Check for missing <code>Repo.transaction</code> closures, or increase <code>pool_size</code> in config.",
  ["L4_diagnosis"])

c("Gotchas", "Why does LiveView mount twice in development?",
  "The LiveView socket disconnects-reconnects on page load in dev (to test reconnection logic). The first mount may have <code>connected?(socket) == false</code>. Handle this case for initial dead-render vs live mount.",
  ["L4_diagnosis"])

c("Gotchas", "What causes <code>** (FunctionClauseError)</code> in Elixir?",
  "No function clause matches the given arguments. Common when pattern matching on the wrong shape of data. Check all function clauses handle the input shape, or add a catch-all clause.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my Ecto changeset not valid despite passing validation?",
  "Check that you called <code>cast/3</code> before validations — uncased fields are silently ignored. Also verify the field names in <code>cast</code> match the schema exactly.",
  ["L4_diagnosis"])

# === ELIXIR EXPERT ===

c("Expert", "When should you use named processes vs. anonymous processes?",
  "Named processes: singleton resources (e.g., a GenServer managing global state). Anonymous: most processes should be anonymous and registered with a Registry or DynamicSupervisor. Named processes fight each other on restart; use with caution.",
  ["L3_design"])

c("Expert", "What is the difference between <code>Registry</code>, <code>ETS</code>, and <code>:pg</code>?",
  "Registry: local process registry (one per node). ETS: in-memory key-value store for any Erlang term (not just PIDs). <code>:pg</code>: distributed process groups across nodes. Use Registry for local lookups, ETS for shared data, <code>:pg</code> for cluster-wide discovery.",
  ["L5_opinion"])

c("Expert", "When should you use a Task vs a GenServer?",
  "Task: one-off or fire-and-forget async work (<code>Task.async</code>, <code>Task.start</code>). GenServer: long-lived, stateful processes. Use Task for 80% of cases; GenServer when you need state + message handling.",
  ["L5_opinion"])

c("Expert", "What is the <code>DynamicSupervisor</code> use case?",
  "When you need to start and stop children at runtime (e.g., a process per user session or per uploaded file). Static Supervisor requires children listed upfront. DynamicSupervisor uses <code>start_child/2</code>.",
  ["L3_design"])

c("Expert", "How do you handle Phoenix controller vs LiveView choice for a new feature?",
  "LiveView: interactive, real-time, stateful pages (forms, dashboards, chat). Controller: simple read-only pages, APIs, redirects, file downloads, static content. Controller for when you don't need the socket.",
  ["L5_opinion"])

c("Expert", "What is <code>Process.flag(:trap_exit, true)</code>?",
  "Converts child exit signals into messages instead of killing the process. Required for Supervisors (to intercept child exits) and for graceful shutdown logic.",
  ["L3_design"])

c("Expert", "When should you bypass Ecto changesets?",
  "Only for bulk operations where validation overhead is unacceptable. Use <code>Repo.insert_all</code> for raw inserts. But you lose constraints, validations, timestamps, and associations — use sparingly.",
  ["L5_opinion"])

c("Expert", "What is LiveView's <code>push_patch</code> vs <code>push_navigate</code>?",
  "<code>push_patch</code>: updates current LiveView URL and params without remounting (reuses the same process). <code>push_navigate</code>: starts a new LiveView process at the new URL. Patch for same LV, navigate for different LV.",
  ["L3_design"])

c("Expert", "How do you handle long-running operations in LiveView without blocking?",
  "Use <code>Task.async</code> in <code>handle_event</code>: <code>Task.async(fn -&gt; heavy_work() end) |&gt; then(&amp;send(self(), {:work_done, &amp;1}))</code>. Keep the LiveView responsive by offloading.",
  ["L3_design"])

c("Expert", "What is telemetry in Phoenix/Elixir?",
  "A library for dispatching and consuming metrics and instrumentation events. Phoenix, Ecto, and Plug emit telemetry events. You attach handlers to collect metrics (with <code>:telemetry</code>, <code>Phoenix.LiveDashboard</code>).",
  ["L3_design"])

# === ELIXIR INTERNALS ===

c("Internals", "How does the BEAM scheduler work?",
  "One scheduler per CPU core (by default). Each scheduler has a run queue of processes. Preemptive scheduling — a process runs for ~2000 reductions (~1ms) then yields. No single process can block the VM.",
  ["L6_innovation"])

c("Internals", "What is an Erlang term? How does memory layout work on the BEAM?",
  "Every value is a word-size (8 bytes on 64-bit) tagged value. Lists are tagged cons cells (2 words each). Tuples have a header + elements. Maps are hash tries. Understanding layout helps optimize memory.",
  ["L6_innovation"])

c("Internals", "How does LiveView's diffing engine work?",
  "After each state change, LiveView re-renders the template and compares with the previous render (HTML token stream diff). Only changed parts are sent over WebSocket as minimal HTML/attribute patches.",
  ["L6_innovation"])

c("Internals", "What is a NIF (Native Implemented Function)?",
  "A C function compiled as a shared library and loaded into the BEAM. Used for performance-critical code or wrapping C libraries. Minimal overhead but crashes the VM on failure (use dirty NIFs for long work).",
  ["L6_innovation"])

c("Internals", "What is a Port in Erlang/Elixir?",
  "A mechanism to communicate with external OS processes via stdin/stdout. Safer than NIFs — if the external process crashes, the BEAM survives. Used by <code>Port.open</code>, or wrappers like <code>Porcelain</code>, <code>ErlPort</code>.",
  ["L6_innovation"])

c("Internals", "How do you extend the Phoenix router with custom route macros?",
  "Use <code>Phoenix.Router.scope</code> and define custom macros that delegate to <code>get/3</code>, <code>post/3</code>, etc. Example: creating <code>resources</code>-like macros for custom admin routes with authorization middleware.",
  ["L6_innovation"])

c("Internals", "How do you write a custom Ecto type?",
  "Implement <code>Ecto.Type</code> behaviour: <code>type/0</code>, <code>cast/1</code>, <code>load/1</code>, <code>dump/1</code>. Use in schema: <code>field :price, MyApp.Types.Money</code>. Enables custom serialization/validation at the DB layer.",
  ["L6_innovation"])

c("Internals", "What is BEAM code loading and hot code swapping?",
  "Modules can be reloaded at runtime without restarting the VM. Old code keeps running until it calls a new-version function (fully qualified call). Phoenix uses this for zero-downtime deploys via release upgrades.",
  ["L6_innovation"])

c("Internals", "How does Phoenix Channels handle backpressure?",
  "Process mailbox monitoring: each channel process monitors its mailbox size. If the client can't consume messages fast enough, the channel drops or throttles messages rather than letting the mailbox grow unbounded.",
  ["L6_innovation"])

# === PHOENIX PATTERNS ===

c("Patterns", "What is the clean architecture approach for Phoenix contexts?",
  "Contexts should not know about Phoenix/HTTP concerns. They call Ecto, return result tuples or data. This lets you test contexts in isolation and reuse them across channels, controllers, and mix tasks.",
  ["L3_design"])

c("Patterns", "What is the decorated assigns pattern in LiveView?",
  "Instead of passing raw Ecto structs to the template, precompute display values in assigns: <code>assign(socket, :formatted_price, Money.to_string(product.price))</code>. Keeps templates logic-free.",
  ["L2_composition"])

c("Patterns", "What is the live_session abstraction?",
  "<code>live_session :default, on_mount: [{MyAppWeb.UserAuth, :ensure_authenticated}]</code> — wraps groups of LiveView routes with shared lifecycle hooks (auth checks, assigns setup).",
  ["L2_composition"])

c("Patterns", "What is the handle_info pattern for PubSub in LiveView?",
  "<code>def handle_info({:new_message, msg}, socket) do<br> {:noreply, assign(socket, messages: [msg | socket.assigns.messages])}<br> end</code> — reactive updates without page refresh.",
  ["L2_composition"])

# Build & write
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
