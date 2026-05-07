#!/usr/bin/env python3
"""LangGraph Zero-to-Hero Anki deck. ~160 cards covering the orchestration runtime for stateful agents."""

import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "LangGraph"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "StateGraph":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-StateGraph-API"),
    "NodesEdges":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Nodes-Edges"),
    "Checkpointer": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Checkpointing"),
    "HumanLoop":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Human-in-the-Loop"),
    "Agents":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Agent-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::09-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ═══ 01 - FUNDAMENTALS ═══════════════════════════════════════════════════════════

c("Fundamentals", "What is LangGraph?",
  "A <b>low-level orchestration framework and runtime</b> for building, managing, and deploying long-running, stateful agents. It models agent workflows as graphs with nodes (computation) and edges (control flow).",
  ["L0_primitives"])

c("Fundamentals", "What distinguishes LangGraph from LangChain?",
  "LangChain = agent framework with abstractions for models, tools, agent loops.<br>LangGraph = orchestration <b>runtime</b> focused on durable execution, streaming, human-in-the-loop, and persistence. LangGraph can be used <i>without</i> LangChain.",
  ["L0_primitives"])

c("Fundamentals", "What are the 3 core components of a LangGraph graph?",
  "1. <b>State</b> — a shared data structure spanning the application snapshot<br>2. <b>Nodes</b> — Python functions that read state, do work, return state updates<br>3. <b>Edges</b> — rules determining which node executes next (fixed or conditional)",
  ["L0_primitives"])

c("Fundamentals", "What programming model inspired LangGraph?",
  "Google's <b>Pregel</b> (message-passing graph computation) and <b>Apache Beam</b>. The public interface draws from <b>NetworkX</b>. Execution proceeds in discrete <b>super-steps</b>.",
  ["L0_primitives"])

c("Fundamentals", "What is a super-step in LangGraph?",
  "A single iteration over graph nodes. Nodes that run in parallel are part of the <b>same</b> super-step. Sequential nodes belong to separate super-steps. A checkpoint is created at each super-step boundary.",
  ["L0_primitives"])

c("Fundamentals", "How does LangGraph handle cyclical graphs (loops)?",
  "LangGraph <b>natively supports cycles</b>. Nodes → edges → nodes can form loops (e.g., an agent loop: call LLM → check tool calls → call tools → call LLM again). The graph terminates when all nodes vote to <b>halt</b>.",
  ["L0_primitives"])

c("Fundamentals", "What is the mental model for a LangGraph agent?",
  "Think of it as a <b>graph of LLM calls</b>: nodes can contain LLM invocations, tool executions, or plain code. Edges define the routing logic. State is the working memory that flows through the graph.",
  ["L0_primitives"])

c("Fundamentals", "How does LangGraph compare to LangChain's LCEL chains?",
  "LCEL chains are <b>DAG-based</b> (no cycles, linear flow). LangGraph supports <b>arbitrary graphs with cycles</b>, enabling agent loops, branching, and parallel execution. LangGraph is the runtime under LangChain agents.",
  ["L0_primitives"])

c("Fundamentals", "What is the relationship between LangGraph's Graph API and Functional API?",
  "Both share the same underlying runtime. <b>Graph API</b> (<code>StateGraph</code>) is declarative — you explicitly define nodes and edges as a graph. <b>Functional API</b> (<code>@entrypoint</code>, <code>@task</code>) lets you use standard Python control flow.",
  ["L0_primitives"])

c("Fundamentals", "What does it mean that LangGraph offers 'durable execution'?",
  "Workflow progress is saved at key points (checkpoints). If interrupted — by failure, timeout, or human-in-the-loop — the graph can <b>resume from where it left off</b>, even days later, without redoing completed work.",
  ["L0_primitives"])

c("Fundamentals", "What is a 'channel' in LangGraph state?",
  "Each key in the graph state is a <b>channel</b> that receives updates from nodes. Channels have associated <b>reducer</b> functions controlling how updates merge into the existing state (e.g., overwrite vs. append).",
  ["L0_primitives"])

c("Fundamentals", "What is the purpose of the <code>compile()</code> method?",
  "It finalizes the graph: validates structure (no orphaned nodes), wires up runtime args (checkpointer, breakpoints, cache), and returns a <code>CompiledGraph</code> ready for <code>invoke()</code> / <code>stream()</code>.",
  ["L0_primitives"])

c("Fundamentals", "What happens if you try to invoke a graph that hasn't been compiled?",
  "It won't work. You <b>MUST</b> call <code>graph = builder.compile()</code> before calling <code>graph.invoke()</code> or <code>graph.stream()</code>. The compile step validates and wires the graph.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>START</code> node?",
  "A special virtual node representing the entry point that sends user input to the graph. Used with <code>add_edge(START, \"node_a\")</code> to specify which node runs first.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>END</code> node?",
  "A special virtual node representing termination. Edges to <code>END</code> tell the runtime that no further nodes should execute from that point. Without an END edge, the graph may run forever.",
  ["L0_primitives"])

c("Fundamentals", "How does LangGraph's node model differ from a simple function pipeline?",
  "Each node receives <b>the full state as input</b> and returns only <b>the keys it wants to update</b> (a partial state update, not the whole state). Reducers control how updates merge into existing state.",
  ["L0_primitives"])

c("Fundamentals", "What are the 5 core benefits LangGraph provides?",
  "1. <b>Durable execution</b> — survive failures and resume<br>2. <b>Human-in-the-loop</b> — pause for approval/editing<br>3. <b>Comprehensive memory</b> — short-term (checkpoints) + long-term (store)<br>4. <b>Debugging via LangSmith</b> — trace execution, visualize<br>5. <b>Production-ready deployment</b> — scalable infrastructure for stateful agents",
  ["L0_primitives"])

c("Fundamentals", "Can LangGraph be used without any LLM at all?",
  "Yes. Nodes can be plain Python functions. LangGraph is a general-purpose <b>stateful workflow orchestrator</b> — you can build any long-running, stateful workflow, not just LLM agents.",
  ["L0_primitives"])

# ═══ 02 - CORE OPERATIONS ═══════════════════════════════════════════════════════

c("CoreOps", "What is the main class for building a graph?",
  "<code>StateGraph</code> — parameterized by a user-defined <code>State</code> object. <code>from langgraph.graph import StateGraph</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you create a StateGraph with a TypedDict state?",
  "<pre>from typing_extensions import TypedDict\nfrom langgraph.graph import StateGraph\n\nclass State(TypedDict):\n    messages: list[str]\n\nbuilder = StateGraph(State)</pre>",
  ["L1_mechanics"])

c("CoreOps", "How do you add a node to a graph?",
  "<code>builder.add_node(\"node_name\", node_function)</code> — the function receives state and returns a dict of state updates.",
  ["L1_mechanics"])

c("CoreOps", "How do you add a fixed edge from node A to node B?",
  "<code>builder.add_edge(\"node_a\", \"node_b\")</code> — execution always proceeds from A to B after A completes.",
  ["L1_mechanics"])

c("CoreOps", "How do you add a conditional edge?",
  "<code>builder.add_conditional_edges(\"node_a\", routing_func, {\"option_a\": \"node_b\", \"option_b\": \"node_c\"})</code><br>The routing function receives state and returns a key from the mapping dict.",
  ["L1_mechanics"])

c("CoreOps", "How do you specify which node runs first?",
  "<code>builder.add_edge(START, \"first_node\")</code> — an edge from the virtual START node to your entry node.",
  ["L1_mechanics"])

c("CoreOps", "How do you compile a graph with a checkpointer?",
  "<code>graph = builder.compile(checkpointer=MemorySaver())</code> — enables persistence, interrupts, and time travel.",
  ["L1_mechanics"])

c("CoreOps", "How do you invoke a graph synchronously?",
  "<code>result = graph.invoke(input_state, config={\"configurable\": {\"thread_id\": \"1\"}})</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you invoke a graph asynchronously?",
  "<code>result = await graph.ainvoke(input_state, config=config)</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you stream graph execution?",
  "<code>for chunk in graph.stream(state, stream_mode=\"updates\", config=config):</code><br>Also: <code>graph.astream()</code> for async streaming.",
  ["L1_mechanics"])

c("CoreOps", "What does the <code>stream_mode=\"values\"</code> give you?",
  "The <b>full state</b> after each super-step. Every chunk is the complete current snapshot.",
  ["L1_mechanics"])

c("CoreOps", "What does the <code>stream_mode=\"updates\"</code> give you?",
  "Only the <b>state updates</b> returned by each node after each step. Includes the node name as the key.",
  ["L1_mechanics"])

c("CoreOps", "What does the <code>stream_mode=\"messages\"</code> give you?",
  "LLM tokens streamed token-by-token from any chat model calls inside the graph. Each chunk is <code>(message_chunk, metadata)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you specify the state schema using TypedDict?",
  "<pre>from typing_extensions import TypedDict\n\nclass State(TypedDict):\n    input: str\n    output: str\n    steps: list[str]</pre>",
  ["L1_mechanics"])

c("CoreOps", "How do you define a state with a list that <b>accumulates</b> (appends) across updates?",
  "Use <code>Annotated</code> with <code>operator.add</code>:<br><pre>from typing import Annotated\nfrom typing_extensions import TypedDict\nimport operator\n\nclass State(TypedDict):\n    messages: Annotated[list[str], operator.add]</pre>",
  ["L1_mechanics"])

c("CoreOps", "What is the <code>add_messages</code> reducer and why use it over <code>operator.add</code>?",
  "<code>add_messages</code> is a prebuilt reducer for message lists that handles:<br>• Message deduplication by ID<br>• Overwriting existing messages (not just appending)<br>• Deserialization of dicts into LangChain Message objects",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>add_messages</code> in your state?",
  "<pre>from langgraph.graph.message import add_messages\n\nclass State(TypedDict):\n    messages: Annotated[list[AnyMessage], add_messages]</pre>",
  ["L1_mechanics"])

c("CoreOps", "What is <code>MessagesState</code>?",
  "A prebuilt state (<code>from langgraph.graph import MessagesState</code>) with a single <code>messages</code> key using <code>add_messages</code> reducer. Commonly subclassed to add more fields.",
  ["L1_mechanics"])

# ═══ 03 - STATEGRAPH API ════════════════════════════════════════════════════════

c("StateGraph", "What are the three extra parameters a node function can accept beyond <code>state</code>?",
  "1. <code>config: RunnableConfig</code> — contains <code>thread_id</code>, tags, metadata<br>2. <code>runtime: Runtime</code> — contains context, store, stream_writer<br>3. <code>writer: StreamWriter</code> — for custom streaming in async contexts",
  ["L2_composition"])

c("StateGraph", "How do you set the entry point without using the START node?",
  "<code>builder.set_entry_point(\"my_node\")</code> — explicitly sets which node runs first. Equivalent to <code>add_edge(START, \"my_node\")</code>.",
  ["L2_composition"])

c("StateGraph", "How do you set the finish point?",
  "<code>builder.set_finish_point(\"my_node\")</code> — equivalent to <code>add_edge(\"my_node\", END)</code>.",
  ["L2_composition"])

c("StateGraph", "How does a routing function in <code>add_conditional_edges</code> work without a mapping dict?",
  "The return value of the routing function is used <b>directly as the node name</b> (or list of node names). All those nodes run in parallel in the next super-step.",
  ["L2_composition"])

c("StateGraph", "What does returning a <b>list of node names</b> from a conditional edge routing function do?",
  "All listed nodes execute <b>in parallel</b> during the next super-step. This is how you create parallel branches/fan-out.",
  ["L2_composition"])

c("StateGraph", "What is the <code>Command</code> primitive and what 4 parameters does it accept?",
  "A unified control flow primitive accepting:<br>• <code>update</code> — state updates (like a node return)<br>• <code>goto</code> — navigate to specific node(s)<br>• <code>graph</code> — target a parent graph (<code>Command.PARENT</code>)<br>• <code>resume</code> — value to resume after an interrupt",
  ["L2_composition"])

c("StateGraph", "When should you use <code>Command</code> from a node instead of conditional edges?",
  "When you need to <b>both update state AND route</b> in a single step. Use conditional edges only for routing, <code>Command</code> for combined state-update + routing.",
  ["L2_composition"])

c("StateGraph", "What is the <code>Send</code> API used for?",
  "Dynamic <b>map-reduce / fan-out</b> patterns where the number of downstream nodes isn't known ahead of time. A conditional edge returns <code>[Send(\"node_name\", state), ...]</code> to spawn multiple parallel executions.",
  ["L2_composition"])

c("StateGraph", "How do you use the Send API for map-reduce?",
  "<pre>from langgraph.types import Send\n\ndef continue_to_jokes(state: OverallState):\n    return [Send(\"generate_joke\", {\"subject\": s})\n            for s in state['subjects']]\n\ngraph.add_conditional_edges(\"node_a\", continue_to_jokes)</pre>",
  ["L2_composition"])

c("StateGraph", "What is the <code>ToolNode</code>?",
  "A prebuilt node (<code>from langgraph.prebuilt import ToolNode</code>) that takes a list of tools and executes tool calls found in the last AI message. Handles the tool-calling loop automatically.",
  ["L2_composition"])

c("StateGraph", "How do you define input and output schemas separate from the internal state?",
  "<pre>class InputState(TypedDict):\n    user_input: str\n\nclass OutputState(TypedDict):\n    answer: str\n\nclass OverallState(InputState, OutputState):\n    internal_data: str\n\nbuilder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)</pre>",
  ["L2_composition"])

c("StateGraph", "How do nodes access private state channels not in the main schema?",
  "Define a private TypedDict schema, and a node can declare it as its return type, writing to those channels. LangGraph discovers the schema and adds those channels to the graph state.",
  ["L2_composition"])

c("StateGraph", "How do you set a recursion limit on graph execution?",
  "Pass <code>config={\"recursion_limit\": 25}</code> to <code>invoke()</code> or <code>stream()</code>. Default is 1000. Raises <code>GraphRecursionError</code> when exceeded.",
  ["L2_composition"])

c("StateGraph", "What is the <code>RemainingSteps</code> managed value?",
  "A special state field (<code>from langgraph.managed import RemainingSteps</code>) that tracks how many steps remain before hitting the recursion limit. Use for graceful degradation inside nodes.",
  ["L2_composition"])

c("StateGraph", "How do you visualize a compiled graph?",
  "<code>graph.get_graph().draw_mermaid_png()</code> — outputs a PNG. Also supports <code>draw_mermaid()</code> for Mermaid text, useful in notebooks.",
  ["L2_composition"])

c("StateGraph", "What is the <code>runtime</code> parameter in node functions?",
  "An injected <code>Runtime</code> object providing access to <code>context</code> (user-defined runtime config), <code>store</code> (long-term memory), <code>stream_writer</code>, <code>config</code>, and <code>control</code> (graceful shutdown).",
  ["L2_composition"])

c("StateGraph", "How do you define runtime context (e.g., user_id, model name)?",
  "<pre>@dataclass\nclass Context:\n    user_id: str\n    model_name: str = \"gpt-4o\"\n\nbuilder = StateGraph(State, context_schema=Context)\ngraph.invoke(inputs, context={\"user_id\": \"42\"})</pre>",
  ["L2_composition"])

c("StateGraph", "What happens when a node has <b>multiple outgoing edges</b>?",
  "All destination nodes execute <b>in parallel</b> as part of the next super-step. This enables fan-out patterns without explicit parallelism code.",
  ["L2_composition"])

# ═══ 04 - NODES & EDGES ═════════════════════════════════════════════════════════

c("NodesEdges", "What are the two ways to add a subgraph to a parent graph?",
  "1. <b>As a node</b>: <code>builder.add_node(\"sub\", compiled_subgraph)</code> — used when parent and subgraph share state keys<br>2. <b>Inside a node function</b>: call <code>subgraph.invoke(...)</code> — used when schemas differ; you transform state manually",
  ["L3_design"])

c("NodesEdges", "When should you add a subgraph as a direct node vs. calling it in a function?",
  "<b>Shared state keys</b> → add as direct node (automatic state pass-through).<br><b>Different schemas</b> → call inside a function (manual transform between parent/subgraph state).<br>Shared keys give cleaner code; different schemas give isolation.",
  ["L3_design"])

c("NodesEdges", "What are the 3 subgraph persistence modes and when to use each?",
  "• <b>Per-invocation</b> (<code>checkpointer=None</code>): default, each call fresh, supports interrupts<br>• <b>Per-thread</b> (<code>checkpointer=True</code>): state accumulates, multi-turn memory<br>• <b>Stateless</b> (<code>checkpointer=False</code>): no checkpointing, no interrupts, plain function call",
  ["L3_design"])

c("NodesEdges", "What state design should you choose: TypedDict, dataclass, or Pydantic BaseModel?",
  "<b>TypedDict</b>: most common, best performance, simple.<br><b>dataclass</b>: when you need default values.<br><b>Pydantic BaseModel</b>: when you need recursive validation (slower, but stricter).<br>Default: start with TypedDict.",
  ["L3_design"])

c("NodesEdges", "When should you use conditional edges vs. putting routing logic in a node?",
  "<b>Conditional edges</b>: route based on state without updating it. Cleaner separation of concerns.<br><b>Node with Command</b>: route AND update state in one step. Use when the routing decision and state change are coupled.",
  ["L3_design"])

c("NodesEdges", "What is the tradeoff between a flat graph and nested subgraphs?",
  "<b>Flat graph</b>: simpler to reason about, all state visible. Good for simple to moderate workflows.<br><b>Subgraphs</b>: encapsulation, independent development, reusable components. Good for multi-agent systems, complex workflows. Adds checkpoint namespace complexity.",
  ["L3_design"])

c("NodesEdges", "How should you decide what goes in state vs. what's passed as node arguments?",
  "<b>State</b>: data that needs to persist across nodes, be checkpointed, or be shared between branches.<br><b>Runtime context</b>: configuration/dependencies (model, user ID, DB connection) — passed via <code>runtime.context</code>, not state.",
  ["L3_design"])

c("NodesEdges", "What is the rule for mixing <code>Command</code> routing and static edges from the same node?",
  "<b>Don't mix them.</b> If <code>node_a</code> returns <code>Command(goto=\"x\")</code> AND you have <code>add_edge(\"node_a\", \"node_b\")</code>, both <code>x</code> and <code>node_b</code> will execute. Use one routing mechanism per node.",
  ["L3_design"])

c("NodesEdges", "How should you structure state for a multi-agent system with independent message histories?",
  "Each agent gets its own subgraph with a <b>private messages channel</b>. The parent graph's state likely has a shared messages channel. Use subgraphs called inside nodes for isolation.",
  ["L3_design"])

c("NodesEdges", "What is the recommended way to handle errors within graph nodes?",
  "Wrap error-prone logic in <b>try/except</b> inside the node. Return a state update with error info. Use conditional edges to route to an error-handling node. For node-level retry, use <code>RetryPolicy</code> when adding the node.",
  ["L3_design"])

c("NodesEdges", "How do you add retry policies to a node?",
  "<code>builder.add_node(\"my_node\", func, retry=RetryPolicy(max_attempts=3))</code><br>Configurable: <code>max_attempts</code>, <code>initial_interval</code>, <code>backoff_factor</code>, <code>max_interval</code>.",
  ["L3_design"])

c("NodesEdges", "What is node caching and when should you use it?",
  "Pass <code>cache_policy=CachePolicy(ttl=60)</code> to <code>add_node</code>. Skips re-execution if the node input is identical (by hash) within the TTL. Use for expensive, deterministic computations.",
  ["L3_design"])

c("NodesEdges", "How can a subgraph node navigate back to a parent graph node?",
  "Return <code>Command(update=..., goto=\"parent_node\", graph=Command.PARENT)</code> from inside the subgraph node. Useful for multi-agent handoffs.",
  ["L3_design"])

c("NodesEdges", "What does the <code>interrupt_before</code> compile option do?",
  "Sets <b>static breakpoints</b> before specified nodes: <code>graph.compile(interrupt_before=[\"approval_node\"])</code>. The graph pauses before executing those nodes. Resume with <code>graph.invoke(None, config)</code>.",
  ["L3_design"])

c("NodesEdges", "What is the difference between <code>interrupt_before</code> and <code>interrupt_after</code>?",
  "<code>interrupt_before</code>: pauses <b>before</b> the node runs (state from previous step).<br><code>interrupt_after</code>: pauses <b>after</b> the node runs (includes node's updates).<br>Both are static breakpoints; for dynamic pauses use <code>interrupt()</code>.",
  ["L3_design"])

c("NodesEdges", "How does parallel execution work when multiple nodes have the same source?",
  "All destination nodes receive the state and execute <b>concurrently</b> in the same super-step. Their outputs are collected and <b>reduced</b> together (using each key's reducer) before the next super-step.",
  ["L3_design"])

c("NodesEdges", "What is the 'routing function' signature for <code>add_conditional_edges</code>?",
  "<code>def router(state: State) -> str | list[str] | Sequence[Send]:</code><br>Returns a node name, list of node names (parallel), or Send objects (dynamic map-reduce).",
  ["L3_design"])

c("NodesEdges", "What is a conditional entry point?",
  "Instead of <code>add_edge(START, \"node\")</code>, use <code>add_conditional_edges(START, router, mapping)</code> to choose the first node dynamically based on input state.",
  ["L3_design"])

# ═══ 05 - CHECKPOINTING ════════════════════════════════════════════════════════

c("Checkpointer", "What is a checkpoint in LangGraph?",
  "A <b>snapshot of the full graph state</b> saved at each super-step boundary. Represented as a <code>StateSnapshot</code> with values, next nodes, metadata, and config.",
  ["L1_mechanics"])

c("Checkpointer", "What is a thread in LangGraph persistence?",
  "A unique ID (<code>thread_id</code>) that identifies a sequence of runs. All checkpoints for a given execution history are stored under the same thread. Like a 'conversation ID'.",
  ["L1_mechanics"])

c("Checkpointer", "How do you specify a thread_id when invoking a graph?",
  "<pre>config = {\"configurable\": {\"thread_id\": \"user-123\"}}\ngraph.invoke(input_state, config=config)</pre>",
  ["L1_mechanics"])

c("Checkpointer", "What are the three durability modes for checkpointing?",
  "• <code>\"exit\"</code>: saves only on exit (fastest, no mid-run recovery)<br>• <code>\"async\"</code>: saves asynchronously during execution<br>• <code>\"sync\"</code>: saves synchronously before each step (most durable, some overhead)",
  ["L1_mechanics"])

c("Checkpointer", "How do you specify a durability mode?",
  "<code>graph.stream(state, stream_mode=\"updates\", durability=\"sync\")</code> — passed as a parameter to any execution method.",
  ["L1_mechanics"])

c("Checkpointer", "What does <code>graph.get_state(config)</code> return?",
  "The <b>latest</b> <code>StateSnapshot</code> for the given thread. Contains <code>values</code>, <code>next</code> (nodes to execute), <code>metadata</code>, <code>created_at</code>, <code>parent_config</code>, and <code>tasks</code>.",
  ["L1_mechanics"])

c("Checkpointer", "How do you get the full execution history of a thread?",
  "<code>list(graph.get_state_history(config))</code><br>Returns a list of <code>StateSnapshot</code> objects in reverse chronological order (newest first).",
  ["L1_mechanics"])

c("Checkpointer", "How do you retrieve a specific checkpoint by ID?",
  "<pre>config = {\"configurable\": {\"thread_id\": \"1\", \"checkpoint_id\": \"some-uuid\"}}\nsnapshot = graph.get_state(config)</pre>",
  ["L1_mechanics"])

c("Checkpointer", "What is time travel replay?",
  "Invoke the graph with a past <code>checkpoint_id</code> to re-execute nodes from that point. Nodes before the checkpoint are skipped; nodes after it re-execute (including LLM calls and interrupts).",
  ["L1_mechanics"])

c("Checkpointer", "How do you manually update graph state at a specific checkpoint?",
  "<code>graph.update_state(config, {\"key\": \"new_value\"})</code><br>Creates a <b>new</b> checkpoint with the update. Optionally specify <code>as_node</code> to control which node executes next.",
  ["L1_mechanics"])

c("Checkpointer", "What are 'pending writes' in checkpointing?",
  "When a node in a parallel super-step fails, the <b>successful nodes' outputs are already saved</b> as pending writes. On resume, those nodes are NOT re-executed — only the failed one retries.",
  ["L1_mechanics"])

c("Checkpointer", "What is <code>MemorySaver</code> and when should you use it?",
  "<code>from langgraph.checkpoint.memory import MemorySaver</code><br>An <b>in-memory</b> checkpointer for development and testing. Not persistent across restarts. Good for prototyping; use <code>SqliteSaver</code> or <code>PostgresSaver</code> in production.",
  ["L1_mechanics"])

c("Checkpointer", "What is <code>SqliteSaver</code> and how do you use it?",
  "<pre>import sqlite3\nfrom langgraph.checkpoint.sqlite import SqliteSaver\n\ncheckpointer = SqliteSaver(sqlite3.connect(\"checkpoints.db\"))\ngraph = builder.compile(checkpointer=checkpointer)</pre>",
  ["L1_mechanics"])

c("Checkpointer", "What is the store (long-term memory) in LangGraph?",
  "A key-value store (<code>InMemoryStore</code> / <code>PostgresStore</code>) for information that persists <b>across threads</b>. Unlike checkpoints (per-thread), the store is <b>global</b>, typically namespaced by user ID.",
  ["L1_mechanics"])

c("Checkpointer", "How do you use the store in a node?",
  "<pre>def my_node(state: State, runtime: Runtime[Context]):\n    user_id = runtime.context.user_id\n    namespace = (user_id, \"memories\")\n    # write\n    await runtime.store.aput(namespace, \"mem_1\", {\"key\": \"val\"})\n    # read/search\n    memories = await runtime.store.asearch(namespace, query=\"...\")</pre>",
  ["L1_mechanics"])

c("Checkpointer", "What does a <code>StateSnapshot</code> contain?",
  "<code>values</code> (state dict), <code>next</code> (next nodes), <code>config</code> (thread/checkpoint IDs), <code>metadata</code> (source, writes, step), <code>created_at</code>, <code>parent_config</code>, <code>tasks</code>.",
  ["L1_mechanics"])

# ═══ 06 - HUMAN-IN-THE-LOOP ═════════════════════════════════════════════════════

c("HumanLoop", "What function pauses graph execution and waits for external input?",
  "<code>interrupt()</code> — <code>from langgraph.types import interrupt</code>. Accepts any JSON-serializable value as payload. The graph saves state and waits indefinitely.",
  ["L2_composition"])

c("HumanLoop", "How do you resume a graph after an interrupt?",
  "<code>graph.invoke(Command(resume=value), config=config)</code><br>The resume value becomes the return value of the <code>interrupt()</code> call inside the paused node.",
  ["L2_composition"])

c("HumanLoop", "What three things do you need for interrupt() to work?",
  "1. A <b>checkpointer</b> (to persist state)<br>2. A <b>thread_id</b> in config (to know which state to resume)<br>3. The <code>interrupt()</code> call inside a node",
  ["L2_composition"])

c("HumanLoop", "What is the cardinal rule about wrapping <code>interrupt()</code> in try/except?",
  "<b>DO NOT</b> wrap <code>interrupt()</code> in a bare <code>try/except Exception</code>. The interrupt works by raising a special exception — catching it prevents the pause. Catching specific exception types is safe.",
  ["L2_composition"])

c("HumanLoop", "What is the rule about the order of multiple <code>interrupt()</code> calls in a node?",
  "The order of interrupt calls <b>must be consistent</b> across executions. Resume values are matched <b>index-based</b>. Don't conditionally skip interrupts or loop based on non-deterministic data.",
  ["L2_composition"])

c("HumanLoop", "What happens when a node with an interrupt is resumed?",
  "The <b>entire node re-executes from the beginning</b> — not from the interrupt line. Code before the interrupt runs again. This is why pre-interrupt side effects must be idempotent.",
  ["L2_composition"])

c("HumanLoop", "How do you build an approval gate pattern?",
  "<pre>def approval_node(state: State) -> Command[Literal[\"proceed\", \"cancel\"]]:\n    is_approved = interrupt(\"Approve?\")\n    if is_approved:\n        return Command(goto=\"proceed\")\n    return Command(goto=\"cancel\")</pre>",
  ["L2_composition"])

c("HumanLoop", "How do you implement review-and-edit of generated content?",
  "<pre>def review_node(state: State):\n    edited = interrupt({\n        \"instruction\": \"Review this\",\n        \"content\": state[\"draft\"]\n    })\n    return {\"draft\": edited}</pre>",
  ["L2_composition"])

c("HumanLoop", "How do you validate human input with a re-prompt loop?",
  "<pre>def get_input_node(state: State):\n    prompt = \"Enter your age:\"\n    while True:\n        answer = interrupt(prompt)\n        if isinstance(answer, int) and answer > 0:\n            break\n        prompt = f\"'{answer}' invalid. Enter a number.\"\n    return {\"age\": answer}</pre>",
  ["L2_composition"])

c("HumanLoop", "How do you place an interrupt inside a tool function?",
  "Define the tool with <code>@tool</code> and call <code>interrupt()</code> inside it just like in a node. The tool pauses when called. Resume the graph, and the tool's interrupt returns the resume value.",
  ["L2_composition"])

c("HumanLoop", "What happens when parallel branches both hit interrupt()?",
  "Both interrupts are collected and returned. To resume, pass a <b>dict mapping interrupt IDs to resume values</b>:<br><code>Command(resume={id1: \"answer1\", id2: \"answer2\"})</code>",
  ["L2_composition"])

c("HumanLoop", "How do you access the interrupt payload when streaming with v2?",
  "Check <code>chunk[\"interrupts\"]</code> on <code>values</code> stream parts. With <code>invoke(version=\"v2\")</code>, access <code>result.interrupts</code> on the returned <code>GraphOutput</code> object.",
  ["L2_composition"])

c("HumanLoop", "What are static breakpoints vs. dynamic interrupts?",
  "<b>Static breakpoints</b> (<code>interrupt_before</code> / <code>interrupt_after</code>): pause at fixed node boundaries, set at compile or runtime.<br><b>Dynamic interrupts</b> (<code>interrupt()</code>): pause at any line inside a node, conditional on logic.",
  ["L2_composition"])

c("HumanLoop", "What is <code>GraphOutput</code> in the v2 API?",
  "The return type of <code>graph.invoke(version=\"v2\")</code>. Has <code>.value</code> (the state/output) and <code>.interrupts</code> (tuple of Interrupt objects if any occurred). Replaces the old <code>result[\"__interrupt__\"]</code>.",
  ["L2_composition"])

c("HumanLoop", "How do you resume a graph after an error/interrupt with the same thread?",
  "For interrupts: <code>graph.invoke(Command(resume=value), config)</code><br>For errors: <code>graph.invoke(None, config)</code> — resumes from last successful checkpoint.",
  ["L2_composition"])

c("HumanLoop", "Why should side effects before <code>interrupt()</code> be idempotent?",
  "Because the node <b>re-executes from the start</b> on resume. Non-idempotent operations (DB inserts, API calls with side effects) would happen twice. Place side effects <b>after</b> the interrupt, or in a separate node.",
  ["L2_composition"])

# ═══ 07 - AGENT PATTERNS ═══════════════════════════════════════════════════════

c("Agents", "What is the classic ReAct / tool-calling agent loop in LangGraph?",
  "<pre>START -> agent (LLM call) -> conditional_edge:\n  if tool_calls: -> tools (ToolNode) -> agent\n  else: -> END</pre>The agent calls the LLM, checks for tool calls, executes tools, loops back.",
  ["L2_composition"])

c("Agents", "What does <code>ToolNode</code> do with the tool calls in an AI message?",
  "It extracts <code>tool_calls</code> from the last <code>AIMessage</code>, executes each tool, and returns a list of <code>ToolMessage</code> results. Use it with <code>add_messages</code> reducer for automatic appending.",
  ["L2_composition"])

c("Agents", "How do you build a RAG (Retrieval-Augmented Generation) graph?",
  "1. <b>Retrieve node</b>: query vector store, put docs in state<br>2. <b>Generate node</b>: LLM with retrieved docs as context<br>3. Optionally: <b>Grade/Filter node</b> before generation, <b>Rewrite query</b> node if retrieval is poor",
  ["L2_composition"])

c("Agents", "What is a 'router' node pattern?",
  "A node that analyzes the input and <b>routes to different downstream subgraphs</b> based on intent/domain. E.g., route 'billing question' → billing subagent, 'tech support' → tech subagent.",
  ["L2_composition"])

c("Agents", "How do you implement parallel tool calls in an agent graph?",
  "When the LLM returns multiple tool calls in one message, <code>ToolNode</code> executes them concurrently. Map-reduce with <code>Send</code> is another approach for parallel independent processing.",
  ["L2_composition"])

c("Agents", "What is a supervisor agent pattern?",
  "A 'supervisor' node (often an LLM) decides which <b>specialist subagent</b> to route to next. Each specialist is a compiled subgraph. The supervisor loops until the task is complete.",
  ["L2_composition"])

c("Agents", "How do you implement a multi-agent handoff?",
  "Subagent A returns <code>Command(goto=\"subagent_b\", graph=Command.PARENT)</code> to transfer control to another subagent in the parent graph. Both need to be added as nodes to the parent.",
  ["L2_composition"])

c("Agents", "How does the <code>create_agent</code> helper in LangChain relate to LangGraph?",
  "<code>from langchain.agents import create_agent</code><br>It produces a compiled LangGraph graph under the hood. A convenience wrapper that sets up the standard tool-calling loop with the Graph API. Fully interoperable with raw LangGraph.",
  ["L2_composition"])

c("Agents", "What is the <code>Command</code> parameter <code>graph=Command.PARENT</code> for?",
  "Navigates from a <b>subgraph node</b> to a node in the <b>parent graph</b>. Essential for multi-agent handoffs where execution needs to bubble up.",
  ["L2_composition"])

c("Agents", "How do you build a streaming human-in-the-loop agent?",
  "Use <code>graph.astream()</code> with <code>stream_mode=[\"messages\", \"updates\"]</code>, <code>subgraphs=True</code>, <code>version=\"v2\"</code>. Check for <code>chunk[\"type\"] == \"updates\"</code> with <code>__interrupt__</code> to detect pauses, then resume with <code>Command(resume=...)</code>.",
  ["L2_composition"])

c("Agents", "What is the pattern for an agent that reflects on and critiques its own output?",
  "A loop: <code>generate → critique → conditional_edge</code> (if critique finds issues → regenerate; else → END). The critique node is an LLM call with instructions to evaluate the generated content.",
  ["L2_composition"])

c("Agents", "How do you implement an agent with 'plan and execute' pattern?",
  "1. <b>Planner node</b>: LLM generates a list of steps<br>2. <b>Executor loop</b>: for each step, execute (possibly with tools), update state<br>3. <b>Replanner node</b>: LLM evaluates progress, adjusts remaining steps if needed",
  ["L2_composition"])

c("Agents", "What is the difference between using subgraphs for multi-agent vs. flat conditional routing?",
  "<b>Subgraphs</b>: agent isolation, independent state, reusable, can be developed by different teams.<br><b>Flat routing</b>: simpler, all state shared, better for single-team projects with simpler coordination needs.",
  ["L2_composition"])

c("Agents", "How do you pass streaming LLM tokens through a tool-calling agent?",
  "Use <code>stream_mode=\"messages\"</code>. Even when the LLM is called with <code>.invoke()</code> (not <code>.stream()</code>), LangGraph intercepts and streams tokens. Filter by <code>metadata[\"langgraph_node\"]</code> to isolate specific LLM calls.",
  ["L2_composition"])

c("Agents", "What is a <code>StreamWriter</code> in LangGraph?",
  "Access via <code>get_stream_writer()</code> (sync) or as a <code>writer</code> parameter (async). Emits arbitrary key-value data as <code>custom</code> stream events. Use for progress updates, intermediate results, or streaming non-LangChain LLMs.",
  ["L2_composition"])

c("Agents", "How do you stream from a non-LangChain LLM in LangGraph?",
  "Use <code>stream_mode=\"custom\"</code> with <code>get_stream_writer()</code>. Inside the node, iterate over your custom LLM's streaming API and call <code>writer({\"chunk\": token})</code> for each token.",
  ["L2_composition"])

# ═══ 08 - GOTCHAS ══════════════════════════════════════════════════════════════

c("Gotchas", "Why do you get 'Node not found' errors at compile time?",
  "An edge references a node name that doesn't exist. Check <b>typos</b> in node names, or that the node was actually added before referencing it. Default node names use the <b>function name</b> if no name was given.",
  ["L4_diagnosis"])

c("Gotchas", "What causes an <code>GraphRecursionError</code>?",
  "The graph exceeded the <b>recursion limit</b> (default 1000). Usually means an infinite loop — check that your conditional edge logic eventually routes to <code>END</code>. Increase limit with <code>config={\"recursion_limit\": N}</code> if truly needed.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my state being <b>overwritten</b> instead of accumulated?",
  "You forgot to annotate the state key with a <b>reducer</b> (like <code>Annotated[list, operator.add]</code>). Without a reducer, each node update <b>replaces</b> the entire value for that key.",
  ["L4_diagnosis"])

c("Gotchas", "Why do messages seem to disappear or get duplicated?",
  "If using <code>operator.add</code> reducer for messages: manual state updates append instead of overwriting, causing duplicates. Use <code>add_messages</code> which handles message IDs properly.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my graph hang / never finish?",
  "Most likely: a node has no path to <code>END</code>, or a conditional edge always routes to a node that routes back (infinite loop without exit condition). Every branch of every conditional edge must eventually reach <code>END</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my compiled graph fail with 'invalid edge' errors?",
  "Common causes:<br>• Edge referencing a node that was never added<br>• Typo in node name string<br>• Using <code>add_edge</code> from the same node with a node that also returns <code>Command</code> routing (both paths execute)<br>• Not using <code>START</code> / <code>END</code> correctly",
  ["L4_diagnosis"])

c("Gotchas", "Why is <code>stream_mode=\"updates\"</code> returning the same update twice?",
  "You may have both a <b>static edge</b> and a <b>Command-based route</b> from the same node — both paths execute. Also check that you're not mixing <code>add_edge</code> with <code>add_conditional_edges</code> from the same source node.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my async graph behave differently from sync in Python &lt; 3.11?",
  "Python &lt; 3.11 doesn't support <code>context</code> param for asyncio tasks. You MUST:<br>• Pass <code>config</code> explicitly to LLM <code>ainvoke()</code> calls<br>• Can't use <code>get_stream_writer()</code> — pass <code>writer</code> as a parameter instead",
  ["L4_diagnosis"])

c("Gotchas", "Why does resume after interrupt put the wrong value in my variable?",
  "Resume values are matched <b>by index</b> to interrupt calls. If you added/removed/reordered <code>interrupt()</code> calls, or skipped one conditionally, the indices won't match. Keep interrupt order consistent.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my state get corrupted after a subgraph runs?",
  "The subgraph might be writing to a shared state key <b>without a reducer</b> defined in the parent. When both parent and subgraph write to the same key, both must agree on the reducer. Define reducers on parent state keys.",
  ["L4_diagnosis"])

c("Gotchas", "Why doesn't checkpointing work with my custom state objects?",
  "Checkpoint serialization requires JSON-serializable values. Custom objects, functions, or non-serializable types will fail. Use <code>JsonPlusSerializer(pickle_fallback=True)</code> for pickle support, or keep state simple.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>get_state()</code> return stale data?",
  "You might be looking at a checkpoint <b>before</b> the latest super-step completed. Check <code>snapshot.next</code> — if empty <code>()</code>, the graph is finished. If non-empty, there's a pending step. Use <code>get_state_history()</code> to find the right checkpoint.",
  ["L4_diagnosis"])

c("Gotchas", "Why do my parallel branches produce inconsistent results?",
  "Parallel nodes <b>cannot see each other's state updates</b> within the same super-step. Each operates on the state from the <b>previous super-step</b>. Use reducers to merge outputs, or make them sequential if order matters.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>interrupt()</code> not pause the graph?",
  "Likely missing a <b>checkpointer</b>. <code>interrupt()</code> requires persistence to save state. Compile with <code>checkpointer=MemorySaver()</code> or equivalent. Also check you didn't wrap it in a bare <code>try/except</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why can't I pass <code>Command(update=...)</code> as input for a follow-up message?",
  "<code>Command</code> resumes from the latest checkpoint, not from <code>START</code>. For multi-turn conversations, pass a <b>plain dict</b>: <code>graph.invoke({\"messages\": [new_msg]}, config)</code>. Only use <code>Command(resume=...)</code> for interrupts.",
  ["L4_diagnosis"])

c("Gotchas", "What happens if my <code>add_conditional_edges</code> routing function returns a node name not in the mapping?",
  "If no mapping dict is provided, the return value is used directly as the node name (must exist). If a mapping dict is provided, unknown keys are <b>ignored</b> — the graph may halt without reaching <code>END</code>. Always handle all cases.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my graph run with <code>interrupt()</code> but the resume value returns <code>None</code>?",
  "You called <code>Command(resume=True)</code> which resolves to Python's <code>True</code>, but your node logic may expect a different type. Or you passed <code>Command()</code> without a <code>resume=</code> argument. Check that the resume value matches what the node expects.",
  ["L4_diagnosis"])

# ═══ 09 - EXPERT ═══════════════════════════════════════════════════════════════

c("Expert", "How does LangGraph compare to CrewAI for multi-agent systems?",
  "CrewAI: higher-level, opinionated, role-based agents with built-in task delegation. Good for structured team workflows.<br>LangGraph: lower-level, unopinionated graph runtime. More flexible, more control, but requires building the orchestration yourself.",
  ["L5_opinion"])

c("Expert", "How does LangGraph compare to AutoGen?",
  "AutoGen (Microsoft): conversation-driven, agent chat patterns, code generation focus.<br>LangGraph: graph-driven, general-purpose stateful orchestration, finer-grained control over flow. Both support multi-agent; LangGraph offers more customization.",
  ["L5_opinion"])

c("Expert", "When should you NOT use LangGraph?",
  "• Simple single-call LLM workflows — use LangChain LCEL or direct API calls<br>• Stateless request/response — overkill<br>• You need a prebuilt agent with zero configuration — use <code>create_agent</code> or CrewAI<br>• Trivial sequential chains that never need loops or state",
  ["L5_opinion"])

c("Expert", "LangGraph Cloud vs. self-hosted deployment — what are the tradeoffs?",
  "<b>Cloud</b> (<b>LangSmith Deployment</b>): managed checkpointing, auto-scaling, Studio debugging, monitoring, semantic search. Less ops.<br><b>Self-hosted</b>: full control, lower per-request cost at scale, but you manage Postgres, Redis, scaling, monitoring. Use PostgresSaver + custom API server.",
  ["L5_opinion"])

c("Expert", "What is the LangGraph Platform / Agent Server?",
  "A managed deployment target that handles checkpointing, streaming, and state management automatically. You deploy graph definitions; the platform runs them as scalable, stateful HTTP+SSE APIs. No need to wire persistence manually.",
  ["L5_opinion"])

c("Expert", "How do you implement a custom checkpointer?",
  "Implement the <code>BaseCheckpointSaver</code> interface: <code>get_tuple</code>, <code>put</code>, <code>put_writes</code>, <code>list</code>, <code>delete_thread</code> (and async versions). Use <code>SerializerProtocol</code> for your serialization format.",
  ["L6_innovation"])

c("Expert", "How do you encrypt checkpoint data?",
  "<pre>from langgraph.checkpoint.serde.encrypted import EncryptedSerializer\nfrom langgraph.checkpoint.postgres import PostgresSaver\n\nserde = EncryptedSerializer.from_pycryptodome_aes()\n# reads LANGGRAPH_AES_KEY env var\ncheckpointer = PostgresSaver.from_conn_string(..., serde=serde)</pre>",
  ["L6_innovation"])

c("Expert", "What is LangGraph Studio and what can you do with it?",
  "A visual IDE for building and debugging LangGraph agents. Features: graph visualization, step-through debugging, state inspection at each checkpoint, interrupt handling, real-time streaming, and one-click deployment to LangSmith.",
  ["L6_innovation"])

c("Expert", "How do you write a custom tool that integrates with LangGraph's state?",
  "Use <code>@tool</code> + <code>Command</code> return. The tool can update graph state (<code>update=...</code>) and route (<code>goto=...</code>) directly:<br><pre>@tool\ndef lookup_customer(name: str) -> Command:\n    data = db.query(name)\n    return Command(update={\"customer\": data}, goto=\"process_customer\")</pre>",
  ["L6_innovation"])

c("Expert", "What is the middleware pattern in LangGraph?",
  "LangChain agents support <b>middleware</b> that wraps or intercepts tool calls. Examples: <code>ToolCallLimitMiddleware</code> (limit parallel calls), custom middleware for logging, rate limiting, or transforming tool inputs/outputs before execution.",
  ["L6_innovation"])

c("Expert", "How do you implement a <code>DeltaChannel</code> for storage optimization?",
  "For append-heavy channels (long message histories), use <code>DeltaChannel</code> (requires <code>langgraph>=1.2</code>). Stores only <b>incremental deltas</b> instead of the full accumulated value. Tradeoff: smaller storage, but recomputation on read.",
  ["L6_innovation"])

c("Expert", "How do you use <code>entrypoint.final</code> to decouple return value from saved state?",
  "<pre>@entrypoint(checkpointer=checkpointer)\ndef workflow(n: int, *, previous: Any = None) -> entrypoint.final[int, int]:\n    previous = previous or 0\n    return entrypoint.final(value=previous, save=2 * n)\n# Returns the previous value to caller, saves 2*n as next 'previous'</pre>",
  ["L6_innovation"])

c("Expert", "What is graceful shutdown in LangGraph?",
  "Pass <code>control=RunControl()</code> to <code>invoke()</code>. Call <code>control.request_drain()</code> from a signal handler to stop after the current super-step completes. Catches <code>GraphDrained</code> exception; checkpoint is saved, resumable.",
  ["L6_innovation"])

c("Expert", "How do you implement a SIGTERM handler for graceful graph drain?",
  "<pre>import signal\nfrom langgraph.runtime import RunControl\nfrom langgraph.errors import GraphDrained\n\ncontrol = RunControl()\nsignal.signal(signal.SIGTERM, lambda *_: control.request_drain(\"sigterm\"))\ntry:\n    result = graph.invoke(inputs, config, control=control)\nexcept GraphDrained as e:\n    log.info(\"drained: %s\", e.reason)</pre>",
  ["L6_innovation"])

c("Expert", "What is the Functional API's <code>@task</code> decorator and when is it needed?",
  "Wraps side-effecting or non-deterministic operations so results are <b>saved to checkpoints</b>. On resume, tasks return cached results instead of re-executing. Critical for human-in-the-loop determinism. Used within <code>@entrypoint</code> functions.",
  ["L6_innovation"])

c("Expert", "How do <code>@entrypoint</code> and <code>@task</code> differ from StateGraph?",
  "<b>@entrypoint/@task</b>: imperative, use Python control flow (if/for), state is implicit in function scopes. Tasks are the unit of checkpointing.<br><b>StateGraph</b>: declarative, explicit graph topology, explicit state schema with reducers. Both share the same runtime.",
  ["L6_innovation"])

c("Expert", "How do you implement semantic search over long-term memory in the store?",
  "<pre>store = InMemoryStore(\n    index={\n        \"embed\": init_embeddings(\"openai:text-embedding-3-small\"),\n        \"dims\": 1536,\n        \"fields\": [\"content\", \"$\"]\n    }\n)\nmemories = store.search(namespace, query=\"user's preference about X\")</pre>",
  ["L6_innovation"])

c("Expert", "Why does LangGraph exist as a separate product from LangChain?",
  "LangChain handles agent <b>abstractions</b> (models, tools, prompts). LangGraph handles agent <b>infrastructure</b> (orchestration, persistence, streaming). Separating them lets LangGraph serve non-LangChain users and lets LangChain focus on integrations. Deep Agents SDK builds on LangGraph for higher-level features.",
  ["L5_opinion"])

c("Expert", "How do you extend LangGraph with custom stream modes?",
  "Use <code>get_stream_writer()</code> for <code>custom</code> mode. LangGraph currently supports fixed modes (<code>values</code>, <code>updates</code>, <code>messages</code>, <code>custom</code>, <code>checkpoints</code>, <code>tasks</code>, <code>debug</code>). Custom data goes through <code>custom</code> mode with your own keys.",
  ["L6_innovation"])

c("Expert", "What are the key differences between LangGraph's v1 and v2 streaming API?",
  "<b>v1</b>: output format changes based on options (single mode → raw dict, multiple → tuples, subgraphs → namespaced tuples).<br><b>v2</b>: always a <code>StreamPart</code> dict with <code>type</code>, <code>ns</code>, <code>data</code>. <code>invoke()</code> returns <code>GraphOutput</code> with <code>.value</code> and <code>.interrupts</code>. Type-safe, consistent.",
  ["L6_innovation"])

# ═══ BUILD ═══════════════════════════════════════════════════════════════════════

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
