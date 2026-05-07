import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Logfire"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "SpansTraces":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Spans-Traces"),
    "Integrations": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Integrations"),
    "Querying":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Querying-Exploring"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === LOGFIRE FUNDAMENTALS ===

c("Fundamentals", "What is Pydantic Logfire?",
  "An observability platform by the Pydantic team. Unifies <b>structured logging</b>, <b>tracing</b>, and <b>metrics</b> for Python (with JS/TS and Rust SDKs too). Built on <b>OpenTelemetry</b> with no vendor lock-in. Provides a cloud dashboard (<code>logfire.pydantic.dev</code>) and supports self-hosting.",
  ["L0_primitives"])

c("Fundamentals", "What are the three pillars of observability?",
  "<b>Logs</b> — timestamped text records of specific events. <b>Metrics</b> — numerical values aggregated over time (latency, error rate, CPU). <b>Traces</b> — end-to-end timelines of requests through multiple services. Logfire provides all three in one platform.",
  ["L0_primitives"])

c("Fundamentals", "How does Logfire relate to OpenTelemetry?",
  "Logfire is <b>built on OpenTelemetry</b>. The Python SDK wraps the OTel Python package. By default it sends to the Logfire cloud, but you can point it to any <b>OTLP-compliant endpoint</b>. Any framework with OTel instrumentation works automatically — no special Logfire integration needed.",
  ["L0_primitives"])

c("Fundamentals", "What is a span in Logfire?",
  "The atomic unit of telemetry. A span has a <b>start time</b>, <b>end time</b>, and <b>duration</b>. It carries attributes (structured key-value data), belongs to a trace, and can have parent-child relationships. Created via <code>with logfire.span(...)</code> or the <code>@logfire.instrument()</code> decorator.",
  ["L0_primitives"])

c("Fundamentals", "What is a trace in Logfire?",
  "A <b>tree of spans</b> sharing the same <code>trace_id</code>. Spans are ordered and nested — like a stack trace showing the full history of a request through your services. A new trace starts when you create a span with no active parent span. Can span multiple services via context propagation.",
  ["L0_primitives"])

c("Fundamentals", "What is a log in Logfire vs a span?",
  "A log is a span with <b>zero duration</b> — start and end times are the same. Created via <code>logfire.info()</code>, <code>.error()</code>, etc. Logs and spans are stored together in the same <code>records</code> table and can be queried with SQL. Logs are children of whatever span is currently active.",
  ["L0_primitives"])

c("Fundamentals", "Why structured logging over <code>print()</code>?",
  "<code>print()</code> is unstructured text — impossible to query, aggregate, or alert on. Structured logging attaches <b>typed attributes</b> (key-value pairs) you can filter with SQL, build dashboards from, and set alerts on. Logfire auto-extracts f-string variables as attributes in Python 3.11+.",
  ["L0_primitives"])

c("Fundamentals", "How does Logfire install and authenticate?",
  "<code>pip install logfire</code>, then <code>logfire auth</code> to authenticate. Credentials are stored in <code>~/.logfire/default.toml</code>. For production, set <code>LOGFIRE_TOKEN</code> environment variable with a write token. Use <code>logfire projects use &lt;name&gt;</code> to select a project.",
  ["L0_primitives"])

c("Fundamentals", "What is the Logfire dashboard?",
  "A web UI at <code>logfire.pydantic.dev</code>. Features: <b>Live View</b> (real-time span/log stream), <b>Explore</b> (SQL querying), <b>Dashboards</b> (charts &amp; metrics), <b>Alerts</b> (Slack/webhook notifications), <b>LLM Panels</b> (AI interaction traces), and <b>Issues</b> (error grouping).",
  ["L0_primitives"])

c("Fundamentals", "How does Logfire compare to Datadog?",
  "Logfire: Python-first, developer-focused, built on OpenTelemetry, simpler setup, no agents to install, natively understands Pydantic/PydanticAI. Datadog: multi-language APM, broader infrastructure monitoring, more enterprise features, proprietary agent, higher cost at scale.",
  ["L0_primitives"])

c("Fundamentals", "How does Logfire compare to Sentry?",
  "Sentry focuses on <b>error tracking and crash reporting</b>. Logfire is a full <b>observability platform</b> — traces, logs, metrics, dashboards, SQL querying. Sentry captures exceptions; Logfire shows you <b>why</b> the exception happened by tracing the entire request flow through database, API, and business logic.",
  ["L0_primitives"])

c("Fundamentals", "What is a Logfire project?",
  "A namespace for organizing telemetry data. All data sent to Logfire must be associated with a project. Projects belong to an <b>Organization</b>. Create via UI (Organization &gt; Projects &gt; New project) or CLI (<code>logfire projects new</code>). Each project has its own write tokens and settings.",
  ["L0_primitives"])

# === CORE OPERATIONS ===

c("CoreOps", "What does <code>logfire.configure()</code> do?",
  "Initializes the Logfire SDK. Must be called <b>once at startup</b> before any logging. Key parameters: <code>token</code> (write token), <code>service_name</code>, <code>service_version</code>, <code>environment</code>, <code>send_to_logfire</code> (bool), <code>console</code> (ConsoleOptions), <code>sampling</code>, <code>scrubbing</code>, <code>inspect_arguments</code> (default True in 3.11+).",
  ["L1_mechanics"])

c("CoreOps", "How do you set service name and version?",
  "<code>logfire.configure(service_name='my-api', service_version='1.2.3')</code>. These become <b>resource attributes</b> attached to every span/log from this process. Useful for distinguishing services in traces and filtering in the dashboard. Often combined with <code>environment='production'</code>.",
  ["L1_mechanics"])

c("CoreOps", "How does <code>logfire.info()</code> work?",
  "<code>logfire.info('template {key}', key=value)</code>. Creates a log (zero-duration span) at <b>info</b> level. The first argument is a <code>str.format</code> template — becomes <code>span_name</code>. Keyword arguments become structured <b>attributes</b>. In Python 3.11+ with f-strings, attributes are auto-extracted.",
  ["L1_mechanics"])

c("CoreOps", "What log levels does Logfire support?",
  "Seven levels: <code>trace</code>, <code>debug</code>, <code>info</code>, <code>notice</code>, <code>warn</code> (alias <code>warning</code>), <code>error</code>, <code>fatal</code>. Each has a corresponding method: <code>logfire.trace()</code>, <code>logfire.debug()</code>, etc. Spans default to <code>info</code> level. <code>logfire.log('info', 'msg')</code> for dynamic levels.",
  ["L1_mechanics"])

c("CoreOps", "How do you log an exception with a traceback?",
  "<code>logfire.exception('Something went wrong')</code>. Equivalent to <code>logfire.error(..., _exc_info=True)</code>. Automatically records the currently handled exception's traceback. For a specific exception: <code>logfire.error('msg', _exc_info=my_exception)</code>. Underscore-prefixed kwargs have special meaning.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a span with <code>logfire.span()</code>?",
  "<code>with logfire.span('operation {param}', param=val) as span:</code>. Context manager that creates a span with duration. Arguments become attributes (no underscore prefix). Returns a <code>LogfireSpan</code> object with <code>.set_attribute()</code>, <code>.record_exception()</code>, <code>.set_level()</code>, and <code>.message</code>.",
  ["L1_mechanics"])

c("CoreOps", "What is <code>span_name</code> and why should it be low-cardinality?",
  "The <code>span_name</code> column identifies what kind of operation this is (e.g., <code>'Hello {name}'</code>). It should <b>not vary per request</b> — otherwise you get millions of unique values, making filtering slow. Use attributes for dynamic data. The <code>message</code> column shows the formatted string.",
  ["L1_mechanics"])

c("CoreOps", "What does <code>@logfire.instrument()</code> do?",
  "Decorator that wraps a function in a span. <b>Must be applied first</b> (below other decorators). By default extracts function arguments as span attributes. <code>instrument(extract_args=False)</code> to disable. <code>instrument('Applying {x=}')</code> for custom template. <code>record_return=True</code> to capture return value.",
  ["L1_mechanics"])

c("CoreOps", "How do you set the minimum log level?",
  "<code>logfire.configure(min_level='info')</code>. Skips spans/logs below this level (span level must be set explicitly with <code>_level</code>). For console-only filtering: <code>logfire.configure(console=logfire.ConsoleOptions(min_log_level='debug'))</code>. The console defaults to <code>info</code> minimum.",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>logfire.log()</code> for dynamic levels?",
  "<code>logfire.log('error', 'Something broke', **attrs)</code>. First arg is the level name as string. Equivalent to the level-specific methods but lets you choose the level at runtime. Useful when the level is determined programmatically.",
  ["L1_mechanics"])

c("CoreOps", "What is <code>logfire.force_flush()</code> and when should you use it?",
  "Flushes all pending telemetry data to the backend. Critical for <b>serverless environments</b> (AWS Lambda, Cloud Functions) where the process may be frozen after handling a request. Call before the handler returns to ensure no data is lost. Also available: <code>logfire.shutdown()</code> for graceful cleanup.",
  ["L1_mechanics"])

c("CoreOps", "How do you configure console output formatting?",
  "<code>logfire.configure(console=logfire.ConsoleOptions(...))</code>. Options: <code>min_log_level</code>, <code>verbose</code> (show attributes), <code>include_timestamps</code>, <code>include_tags</code>, <code>span_style</code> (indentation format), <code>show_project_link</code> (show dashboard URL on first log).",
  ["L1_mechanics"])

# === SPANS & TRACES ===

c("SpansTraces", "How do nested spans work?",
  "Any span or log created inside <code>with logfire.span(...):</code> becomes a <b>child</b> of that span. This creates a tree structure visible in the Live View (expandable blue boxes). The <code>parent_span_id</code> of the child equals the <code>span_id</code> of the parent. All share the same <code>trace_id</code>.",
  ["L2_composition"])

c("SpansTraces", "How do you add attributes to a span after creation?",
  "<code>with logfire.span('operation') as span:</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;result = compute()</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;span.set_attribute('result', result)</code><br>Use <code>.set_attributes({k1: v1, k2: v2})</code> for multiple. Attributes appear in the UI details panel and are queryable via SQL. Must be set before the span ends.",
  ["L2_composition"])

c("SpansTraces", "How do you change a span's message or level mid-span?",
  "<code>span.message = f'Calculated: {result}'</code> — updates the formatted message. <code>span.set_level('error')</code> — changes the log level (e.g., downgrade to error on failure). Both must be called <b>before the <code>with</code> block exits</b>. Useful for setting error level only when a problem is detected.",
  ["L2_composition"])

c("SpansTraces", "How do you record a handled exception inside a span?",
  "<code>with logfire.span('operation') as span:</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;try: ...</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;except ValueError as e:</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;span.record_exception(e)</code><br>Records the traceback without re-raising. Unhandled exceptions are auto-recorded and set the span level to <code>error</code>.",
  ["L2_composition"])

c("SpansTraces", "How does <code>@logfire.instrument()</code> work with function arguments?",
  "By default (<code>extract_args=True</code>), all function arguments are added as span attributes. Use <code>extract_args=['x', 'y']</code> to include only specific args. <code>extract_args=False</code> to log none (useful for large objects). <b>Must be the innermost decorator</b> — apply below <code>@app.route()</code> etc. Source code must be accessible.",
  ["L2_composition"])

c("SpansTraces", "How do you start a new trace from within an existing trace?",
  "Use <code>@logfire.instrument(new_trace=True)</code> or <code>logfire.span('...', _links=[(ctx, attrs)])</code>. Creates a new trace with a span link to the current context. Also: <code>with logfire.attach_context({}):</code> clears the current context so any spans inside start a fresh trace. Useful for background tasks.",
  ["L2_composition"])

c("SpansTraces", "How do f-strings work with Logfire in Python 3.11+?",
  "<code>logfire.info(f'Hello {name}')</code> auto-extracts <code>name</code> as an attribute and sets <code>span_name</code> to <code>'Hello {name}'</code>. Enabled by default in 3.11+ via <code>inspect_arguments</code>. Disable with <code>logfire.configure(inspect_arguments=False)</code>. Values are evaluated twice — avoid expensive/side-effect functions inside f-strings.",
  ["L2_composition"])

c("SpansTraces", "What happens when a span exits due to an unhandled exception?",
  "The exception's traceback is automatically recorded (visible in the UI's 'Exception Traceback' tab). The span's level is set to <code>error</code>. If the span has children, they remain in the trace. Use <code>span.record_exception(e)</code> for caught exceptions you want to record without re-raising.",
  ["L2_composition"])

c("SpansTraces", "How do you set span kind and span links?",
  "<code>logfire.span('op', _span_kind=SpanKind.CLIENT, _links=[(span_context, {'key': 'val'})])</code>. <code>_span_kind</code>: <code>INTERNAL</code>, <code>SERVER</code>, <code>CLIENT</code>, <code>PRODUCER</code>, <code>CONSUMER</code> (from OpenTelemetry spec). <code>_links</code> connect spans in different traces, useful for async workflows.",
  ["L2_composition"])

c("SpansTraces", "How do you instrument async functions with Logfire?",
  "Everything works the same as sync: <code>with logfire.span('op'): await do_stuff()</code> and <code>@logfire.instrument()</code> on <code>async def</code>. Async context is preserved. For generators, you need <code>instrument(allow_generator=True)</code> — without it, you get a warning to read the generators guide.",
  ["L2_composition"])

c("SpansTraces", "What is <code>_span_name</code> and when should you use it?",
  "Pass <code>_span_name='Greeting'</code> to <code>logfire.info('Hello {name}', name='World', _span_name='Greeting')</code> to set the span name independently from the message template. Span name becomes <code>'Greeting'</code>, message becomes <code>'Hello World'</code>. Useful for grouping related logs under a canonical name.",
  ["L2_composition"])

c("SpansTraces", "How does context propagation work across services?",
  "Logfire uses W3C TraceContext and Baggage headers for distributed tracing. When Service A makes an HTTP call to Service B, trace context is automatically forwarded. Both services' spans appear in the same trace. Requires both services to be instrumented. Handled automatically by <code>instrument_httpx()</code>, <code>instrument_requests()</code>.",
  ["L2_composition"])

c("SpansTraces", "How do you add tags to spans and logs?",
  "<code>logfire.info('msg', _tags=['payment', 'critical'])</code>. Tags appear in the UI and are filterable. Use <code>logfire.with_tags('env:prod')</code> for a context manager that adds tags to all spans/logs within. Tags in console output require <code>ConsoleOptions(include_tags=True)</code>.",
  ["L2_composition"])

# === INTEGRATIONS ===

c("Integrations", "How do you instrument a FastAPI app?",
  "<code>logfire.instrument_fastapi(app)</code> (or <code>app</code> can be omitted for auto-detection). Automatically creates spans for each request with method, path, status code, duration. Captures request attributes and headers. Must call <b>after</b> <code>logfire.configure()</code>. Also instruments the ASGI middleware.",
  ["L4_integrations"])

c("Integrations", "How do you instrument SQLAlchemy?",
  "<code>logfire.instrument_sqlalchemy(engine)</code>. Creates child spans for every SQL query showing the statement and duration. Pass the engine or session factory. Works with both sync and async SQLAlchemy. Automatically visible as children of the request span in FastAPI/Django.",
  ["L4_integrations"])

c("Integrations", "How do you instrument HTTPX?",
  "<code>logfire.instrument_httpx()</code> — call once after <code>configure()</code>. Automatically creates spans for all outgoing HTTPX requests with URL, method, status code, duration. Also propagates trace context headers for distributed tracing. Works with both sync (<code>httpx.Client</code>) and async (<code>httpx.AsyncClient</code>).",
  ["L4_integrations"])

c("Integrations", "How do you instrument Django?",
  "<code>logfire.instrument_django()</code>. Automatically traces each request through Django middleware. Creates spans with HTTP method, path, status, and duration. Captures request details. Must be called after <code>logfire.configure()</code>. Also available: <code>instrument_wsgi()</code> for generic WSGI apps.",
  ["L4_integrations"])

c("Integrations", "How do you instrument Flask?",
  "<code>logfire.instrument_flask(app)</code> or <code>logfire.instrument_flask()</code> for auto-detection. Traces each request with route, method, status, duration. Works through WSGI instrumentation. Combine with <code>instrument_sqlalchemy()</code> for database query visibility within request spans.",
  ["L4_integrations"])

c("Integrations", "How do you instrument Pydantic AI?",
  "<code>logfire.instrument_pydantic_ai()</code>. Traces LLM calls, tool usage, and agent runs with Pydantic AI. Creates structured spans for each interaction. Use <code>include_content=False</code> to exclude prompt/completion content for privacy. Natively integrates with Logfire's LLM Panels for visualizing AI interactions.",
  ["L4_integrations"])

c("Integrations", "How do you instrument OpenAI and Anthropic?",
  "<code>logfire.instrument_openai()</code> and <code>logfire.instrument_anthropic()</code>. Auto-trace LLM API calls including token usage, model name, duration. Works with the official client libraries. Also available: <code>instrument_google_genai()</code>, <code>instrument_litellm()</code>, <code>instrument_dspy()</code>.",
  ["L4_integrations"])

c("Integrations", "How do you instrument Celery?",
  "<code>logfire.instrument_celery()</code>. Automatically traces task execution: when a task is published, received, and completed. Links the producer span to the consumer span via distributed context propagation. Shows task name, arguments, queue, and duration.",
  ["L4_integrations"])

c("Integrations", "How do you enable system metrics?",
  "<code>logfire.instrument_system_metrics()</code>. Auto-collects CPU usage, memory, disk I/O, and network metrics. Sends to dashboards. For custom metrics, use <code>logfire.metric_counter()</code>, <code>.metric_histogram()</code>, <code>.metric_gauge()</code>, <code>.metric_up_down_counter()</code>.",
  ["L4_integrations"])

c("Integrations", "How do you instrument <code>print()</code> statements and stdlib logging?",
  "<code>logfire.instrument_print()</code> — captures <code>print()</code> calls as Logfire info logs. In Python 3.11+ with <code>inspect_arguments</code> enabled, f-string variables are auto-extracted as attributes.<br><code>logfire.instrument_logging()</code> — redirects Python stdlib <code>logging</code> module output to Logfire.",
  ["L4_integrations"])

c("Integrations", "How do you instrument Psycopg and asyncpg?",
  "<code>logfire.instrument_psycopg()</code> — traces PostgreSQL queries via psycopg (sync and async). <code>logfire.instrument_asyncpg()</code> — for the asyncpg driver. Both create child spans with SQL statements, parameters, and duration. Similar: <code>instrument_mysql()</code>, <code>instrument_sqlite3()</code>, <code>instrument_redis()</code>, <code>instrument_pymongo()</code>.",
  ["L4_integrations"])

c("Integrations", "How do you instrument AWS Lambda?",
  "<code>logfire.instrument_aws_lambda()</code>. Optimized for serverless — creates a span for each invocation. Important: call <code>logfire.force_flush()</code> before returning to ensure all data is sent before the Lambda freezes. Use with environment variable <code>LOGFIRE_TOKEN</code> for authentication.",
  ["L4_integrations"])

c("Integrations", "How do you instrument Pydantic validation?",
  "<code>logfire.instrument_pydantic()</code>. Traces <b>Pydantic model validation</b> — shows which models are validated, duration, and any validation errors. Use <code>PydanticPlugin(record='all')</code> to trace all validations, or configure <code>include</code>/<code>exclude</code> to filter specific models.",
  ["L4_integrations"])

# === QUERYING & EXPLORING ===

c("Querying", "What is the Live View in Logfire?",
  "A <b>real-time stream</b> of spans and logs from your application. Shows nested spans as expandable trees. Click any span to see its attributes, duration, children, and exception traceback in the details panel. Filter with SQL: <code>span_name = 'Hello {name}'</code>. Supports auto-refresh.",
  ["L5_querying"])

c("Querying", "How do you query Logfire data with SQL?",
  "Use the <b>Explore</b> view or the SQL filter at the top of Live View. The main table is <code>records</code>. Key columns: <code>span_name</code>, <code>message</code>, <code>kind</code> (span/log), <code>level</code>, <code>start_timestamp</code>, <code>end_timestamp</code>, <code>trace_id</code>, <code>span_id</code>, <code>parent_span_id</code>, <code>attributes</code> (JSONB). Filter attributes with <code>attributes-&gt;&gt;'key' = 'value'</code>.",
  ["L5_querying"])

c("Querying", "How are attributes stored and queried in Logfire?",
  "Stored as <b>JSONB</b> in the <code>attributes</code> column of the <code>records</code> table. Use <code>attributes-&gt;&gt;'key'</code> to extract text values in SQL. Supports JSON operators: <code>attributes-&gt;'nested'-&gt;&gt;'field'</code>, <code>attributes ? 'key'</code> (key exists). All keyword arguments to <code>logfire.info()</code> / <code>.span()</code> become attributes.",
  ["L5_querying"])

c("Querying", "What is the difference between <code>span_name</code> and <code>message</code>?",
  "<code>span_name</code> is the <b>template</b> (e.g., <code>'Hello {name}'</code>) — low-cardinality, indexed. <code>message</code> is the <b>formatted output</b> (e.g., <code>'Hello Alice'</code>) — high-cardinality. Always filter on <code>span_name</code> for efficiency. Use <code>span_name = 'Hello {name}' AND attributes-&gt;&gt;'name' = 'Alice'</code> rather than <code>message = 'Hello Alice'</code>.",
  ["L5_querying"])

c("Querying", "How do you create dashboards in Logfire?",
  "Use the <b>Dashboards</b> page. Write <b>SQL queries</b> to populate charts. Supports line charts, bar charts, tables, single-stat, and heatmaps. Pre-built dashboards for <b>Web Server Metrics</b> and <b>System Metrics</b>. Alerts can be configured on any dashboard metric with thresholds and notification channels (Slack, webhook).",
  ["L5_querying"])

c("Querying", "How do you set up Slack alerts in Logfire?",
  "1) Navigate to <b>Alerts</b> page. 2) Create an alert with a <b>SQL-based condition</b> (e.g., <code>error_rate &gt; 5%</code>). 3) Set a threshold and evaluation window. 4) Add a Slack notification channel with webhook URL. Alerts fire when the condition is met. Also supports <b>webhook</b> alerts and <b>service-down detection</b>.",
  ["L5_querying"])

c("Querying", "What are LLM Panels in Logfire?",
  "A specialized view for <b>AI/LLM interaction traces</b>. Shows the full conversation: prompts, completions, tool calls, token usage, cost estimates, and latency. Works automatically when using <code>instrument_pydantic_ai()</code>, <code>instrument_openai()</code>, etc. Helps debug agent behavior and optimize token costs.",
  ["L5_querying"])

c("Querying", "What are Issues in Logfire?",
  "An <b>error grouping</b> feature. Similar to Sentry's issues — groups related exceptions together. Shows frequency, affected traces, and stack traces. Use to track error trends over time. Create alerts on issue frequency changes. Issues are auto-created from spans with <code>error</code>/<code>fatal</code> level and tracebacks.",
  ["L5_querying"])

c("Querying", "How do you find slow database queries or HTTP calls?",
  "In Explore, query <code>SELECT * FROM records WHERE kind = 'span' AND span_name LIKE 'SELECT%' ORDER BY (end_timestamp - start_timestamp) DESC LIMIT 20</code>. Or filter in Live View: <code>span_name LIKE '%query%' AND (end_timestamp - start_timestamp) &gt; '1 second'</code>. Dashboard: create a latency histogram chart.",
  ["L5_querying"])

c("Querying", "What is <code>logfire.url_from_eval()</code>?",
  "Returns the <b>Logfire dashboard URL</b> for the current trace/span. Useful for logging it alongside exceptions or including it in error responses. Format: <code>logfire.url_from_eval()</code> returns the Live View URL filtered to the current trace. Use inside <code>with logfire.span(...):</code>.",
  ["L5_querying"])

c("Querying", "How do Saved Searches work?",
  "Save a <b>SQL query + filter combination</b> with a name. Accessible from the sidebar. Share with team members in the same project. Useful for common investigation patterns: 'slow requests', 'payment errors', 'failed logins'. Can be used as the basis for dashboard panels.",
  ["L5_querying"])

c("Querying", "How does Logfire integrate as an MCP server?",
  "Logfire can act as an <b>MCP (Model Context Protocol) server</b>. This allows AI coding assistants (Claude Code, Cursor, Open Code) to query your Logfire data directly — they can write SQL against your traces to investigate bugs, check metrics, and analyze performance without leaving the editor.",
  ["L5_querying"])

# === GOTCHAS ===

c("Gotchas", "Why are my spans not appearing in the dashboard?",
  "Common causes: (1) <code>logfire.configure()</code> not called or called <b>after</b> instrumentation. (2) Invalid/missing <b>write token</b> — check <code>LOGFIRE_TOKEN</code> env var. (3) <b>Sampling</b> discarding traces — check <code>configure(sampling=...)</code>. (4) <code>min_level</code> filtering — debug/trace spans are below default info. (5) <code>send_to_logfire=False</code> set.",
  ["L4_diagnosis"])

c("Gotchas", "Why is the <code>@logfire.instrument</code> decorator not capturing my function arguments?",
  "Likely issues: (1) Decorator is not the <b>innermost</b> — other decorators may change the function signature. <b>Always apply <code>@logfire.instrument()</code> first</b> (below others). (2) Source code is not accessible (e.g., <code>.pyc</code> only deployment — <code>inspect_arguments</code> needs source code). (3) <code>extract_args=False</code> is set.",
  ["L4_diagnosis"])

c("Gotchas", "What is the performance overhead of Logfire?",
  "Minimal in most cases. Spans add <b>nanosecond-level</b> overhead for timing. <b>f-string inspection</b> has a one-time cost of parsing each source file. <b>Tail sampling</b> keeps spans in memory — large traces with many spans may consume RAM. <b>Scrubbing</b> adds overhead to each log. Disable features you don't need via <code>configure()</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my f-strings showing literal text instead of template+attributes?",
  "<code>logfire.info(f'Hello {name}')</code> requires <code>inspect_arguments=True</code> (default in 3.11+). It fails if: (1) source code unavailable (<code>.pyc</code> deployment). (2) First argument is not a literal f-string (<code>msg = f'...'; logfire.info(msg)</code> won't work). (3) You get a warning and the f-string is used as literal — resulting in high-cardinality span names. Disable with <code>configure(inspect_arguments=False)</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my database queries or HTTP URLs not being scrubbed?",
  "Logfire <b>intentionally</b> does not scrub <code>http.url</code> and <code>db.statement</code> attributes. URLs like <code>/users/123/authenticate</code> are considered safe. <b>Security tip:</b> don't put sensitive data in URLs or raw SQL strings. Use request bodies/headers for secrets, and <b>parameterized queries</b> for SQL. Scrubbing is also disabled for LLM message attributes.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my background task spans missing their parent?",
  "When a trace's root span ends and doesn't meet <b>tail sampling criteria</b>, the entire trace is discarded. Background tasks starting after the root span ends will still be exported, but their parent is gone. <b>Fix:</b> use <code>with logfire.attach_context({}):</code> to start a new trace for background work.",
  ["L4_diagnosis"])

c("Gotchas", "How does Pydantic plugin interact with Logfire?",
  "<code>instrument_pydantic()</code> can generate many spans for heavy validation workloads. Use <code>PydanticPlugin(record='failure')</code> to only record validation failures (default), or <code>record='all'</code> for every validation. Use <code>include</code>/<code>exclude</code> to filter specific models and avoid noise.",
  ["L4_diagnosis"])

c("Gotchas", "What happens when <code>inspect_arguments</code> fails silently?",
  "You get a <b>warning</b> (check console output). The f-string value becomes a high-cardinality span name (e.g., <code>'Hello Alice'</code> instead of <code>'Hello {name}'</code>), and no <code>name</code> attribute is extracted. The information isn't completely lost, but filtering/querying becomes harder. Disable inspection if this is a problem.",
  ["L4_diagnosis"])

c("Gotchas", "Why is tail sampling using so much memory?",
  "Tail sampling keeps <b>all spans of a trace in memory</b> until the trace ends. High memory usage occurs with: (1) large number of spans per trace, (2) spans with large attributes, (3) high duration thresholds. Mitigation: add <b>head sampling</b> to discard some traces early, reduce attribute sizes, or lower the duration threshold.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my <code>debug()</code> and <code>trace()</code> logs not appearing in console?",
  "The console defaults to <code>min_log_level='info'</code>. Use <code>logfire.configure(console=logfire.ConsoleOptions(min_log_level='debug'))</code> to see them. Note: <code>min_level</code> on <code>configure()</code> controls which spans are sent to the backend; console filtering is separate.",
  ["L4_diagnosis"])

c("Gotchas", "How do you test Logfire instrumentation?",
  "Use <code>logfire.configure(send_to_logfire=False, console=logfire.ConsoleOptions(verbose=True))</code> in tests to see spans locally without sending to the cloud. Logfire also provides a <b>pytest integration</b> via <code>logfire.instrument_pytest()</code> and testing utilities in <code>logfire.testing</code> to capture and assert on spans.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "When should you use Logfire vs raw OpenTelemetry?",
  "Use <b>Logfire</b> when: you want batteries-included observability with minimal boilerplate, you're in the Pydantic ecosystem, you want auto-scrubbing, f-string magic, and a managed dashboard. Use <b>raw OTel</b> when: you need full control over the pipeline, you're sending to a different backend, or Logfire's abstractions don't fit your use case.",
  ["L4_opinion"])

c("Expert", "Logfire vs Grafana — when to use which?",
  "Logfire is a <b>turnkey observability platform</b> with hosted backend, auto-instrumentation, and built-in SQL querying. Grafana is a <b>visualization layer</b> that needs a separate backend (Prometheus, Loki, Tempo). Logfire requires less setup; Grafana is more flexible and self-hosted-friendly. They can complement each other.",
  ["L4_opinion"])

c("Expert", "What makes Logfire well-suited for Python-heavy teams?",
  "First-class Python SDK with f-string magic, Pydantic integration, and idiomatic context managers. Auto-instrumentation for the entire Python web stack (FastAPI, Django, Flask, SQLAlchemy, Celery). Built by the Pydantic team — deeply understands Python type systems, validation, and async patterns. JS/TS and Rust SDKs also available.",
  ["L4_opinion"])

c("Expert", "Self-hosted vs cloud Logfire — what are the trade-offs?",
  "<b>Cloud</b>: zero ops, auto-updates, 10M free spans/month, SOC2/HIPAA compliance, EU data region available. <b>Self-hosted</b>: full data sovereignty, required for some compliance regimes, enterprise plan, needs infrastructure management. Both support the same SDK and features. Self-hosted available via enterprise licensing.",
  ["L4_opinion"])

c("Expert", "Structured logging vs traditional logging — why does it matter?",
  "Traditional logging produces <b>unstructured text</b> — you grep to find things. Structured logging produces <b>typed key-value pairs</b> — you query, aggregate, alert, and dashboard. With Logfire, attributes become searchable/filterable via SQL. Structured logging enables: automated alerts on specific attribute values, latency histograms per endpoint, error rate dashboards by status code.",
  ["L4_opinion"])

c("Expert", "How do you create a Counter metric in Logfire?",
  "<code>counter = logfire.metric_counter('exceptions', unit='1', description='Count of exceptions')</code>. Then <code>counter.add(1)</code> to increment. Counters are <b>monotonically increasing</b>. Use for: request counts, error counts, items processed. For values that go up and down, use <code>metric_up_down_counter()</code>.",
  ["L4_innovation"])

c("Expert", "How do you create a Histogram metric in Logfire?",
  "<code>hist = logfire.metric_histogram('request_duration', unit='ms', description='Duration of HTTP requests')</code>. Then <code>hist.record(duration_ms)</code>. Histograms track <b>distributions</b> — you can query p50/p95/p99 latencies. Use for: request duration, payload sizes, queue depths.",
  ["L4_innovation"])

c("Expert", "How do you create a Gauge metric in Logfire?",
  "<code>gauge = logfire.metric_gauge('temperature', unit='C', description='Current temperature')</code>. Then <code>gauge.set(value)</code>. Gauges represent <b>current value at a point in time</b> — not cumulative. Use for: current memory usage, active connections, temperature sensors.",
  ["L4_innovation"])

c("Expert", "What are callback-based metrics and how do they work?",
  "Callback metrics (observable metrics) call your function every 60 seconds to collect readings. <code>logfire.metric_gauge_callback('temp', callbacks=[get_temp])</code>. Your callback receives <code>CallbackOptions</code> and yields <code>Observation(value, attributes)</code>. Use when you can't instrument the source directly (e.g., reading from <code>/proc</code> or a hardware sensor).",
  ["L4_innovation"])

c("Expert", "How does Logfire's scrubbing work and how can you customize it?",
  "Default patterns scrub keys matching: <code>password</code>, <code>secret</code>, <code>api_key</code>, <code>token</code>, <code>credential</code>, <code>cookie</code>, <code>session</code>, <code>jwt</code>, <code>ssn</code>, <code>csrf</code>, etc. Add custom patterns: <code>ScrubbingOptions(extra_patterns=['my_pattern'])</code>. Use a <b>callback</b> function to selectively <b>un-scrub</b> known-safe values. Disable entirely: <code>configure(scrubbing=False)</code>.",
  ["L4_innovation"])

c("Expert", "What sampling strategies does Logfire support?",
  "<b>Head sampling</b>: random percentage via <code>SamplingOptions(head=0.5)</code> or custom OTel <code>Sampler</code>. <b>Tail sampling</b>: <code>SamplingOptions.level_or_duration()</code> keeps traces with errors or duration &gt; 5s. <b>Combined</b>: <code>level_or_duration(head=0.1)</code> keeps 10% plus notable traces. <b>Background rate</b>: <code>level_or_duration(background_rate=0.3)</code> retains 30% of non-notable traces. Custom tail: pass a function to <code>tail</code>.",
  ["L4_innovation"])

c("Expert", "How does Logfire handle PII and sensitive data redaction?",
  "Automatic <b>regex-based scrubbing</b> of attribute keys and values on the client side, before data leaves your process. Default patterns cover passwords, secrets, tokens, API keys. Scrubbing is applied to <b>all</b> attributes recursively. <b>Exceptions</b>: <code>http.url</code>, <code>db.statement</code>, and LLM message attributes are not scrubbed. Customize via <code>ScrubbingOptions</code>.",
  ["L4_innovation"])

c("Expert", "How do you integrate Logfire with an existing OpenTelemetry pipeline?",
  "Logfire's SDK wraps the OTel Python SDK. You can: (1) Point Logfire to a <b>custom OTLP collector</b> via <code>configure(base_url='http://collector:4318')</code>. (2) Use Logfire instrumentation alongside raw OTel spans — they coexist in the same trace. (3) Use the OpenTelemetry Collector for advanced scrubbing, tail sampling, or exporting to multiple backends.",
  ["L4_innovation"])

c("Expert", "How do you suppress spans and scopes programmatically?",
  "<code>logfire.suppress_scopes('sqlalchemy')</code> — prevents spans from specific instrumentation libraries. Use <code>logfire.suppress_instrumentation</code> context manager to temporarily disable all instrumentation. <code>logfire.no_auto_trace()</code> decorator marks functions that should not be auto-instrumented.",
  ["L4_innovation"])

c("Expert", "How do you use Logfire with multiple configurations?",
  "For different environments (dev/staging/prod): use environment variables like <code>LOGFIRE_TOKEN</code>, <code>LOGFIRE_SERVICE_NAME</code>, <code>LOGFIRE_ENVIRONMENT</code>. Create a shared config module: <code>logfire.configure(service_name=..., service_version=..., environment=os.getenv('ENV'))</code>. Use <code>send_to_logfire=False</code> in tests. CLI: <code>logfire projects use</code> to switch projects per directory.",
  ["L4_innovation"])

c("Expert", "What are Managed Variables in Logfire?",
  "A <b>feature flag / remote config</b> system. Define variables in the Logfire UI, then access them in code: <code>logfire.var('feature_enabled', False)</code>. Variables update in real-time with zero redeploy. Supports <b>A/B testing</b>, <b>targeting</b> (by user, region, etc.), and <b>OFREP</b> protocol. Polling interval configurable via <code>VariablesOptions</code>.",
  ["L4_innovation"])

c("Expert", "How does Logfire's MCP server integration work with AI coding assistants?",
  "Logfire exposes an <b>MCP (Model Context Protocol)</b> endpoint. AI assistants like Claude Code can query your Logfire data directly — they write SQL to investigate traces, check error rates, analyze latency, and monitor production. Setup: enable the MCP integration in Logfire settings, then configure your IDE's MCP client.",
  ["L4_innovation"])

c("Expert", "What are Evaluations in Logfire?",
  "Logfire <b>Evals</b> lets you create datasets from production traces and run evaluations against them. Monitor LLM quality over time: groundedness, relevance, toxicity. Catch regressions in AI behavior. Two modes: <b>Dataset experiments</b> (offline) and <b>Live monitoring</b> (continuous evaluation of production traces).",
  ["L4_innovation"])

# === ASSEMBLE & EXPORT ===

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
