import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "RabbitMQ"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "AMQP":         genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-AMQP-Exchanges-Queues"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Messaging-Patterns"),
    "Reliability":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Reliability-DLQ"),
    "Operations":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Operations-Management"),
    "Plugins":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Plugins-Protocols"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ─── 01 Fundamentals ───────────────────────────────────────────────────────

c("Fundamentals",
  "What is RabbitMQ?",
  "An open-source <b>message broker</b> implementing AMQP 0-9-1. Written in Erlang, it accepts, stores, and forwards binary blobs (messages) between producers and consumers via exchanges and queues.",
  ["rabbitmq", "fundamentals", "definition"])

c("Fundamentals",
  "What is a <b>message broker</b>?",
  "Middleware that decouples producers from consumers — producers send messages to the broker, consumers receive them, possibly at a different time. Enables async, resilient, scalable systems.",
  ["rabbitmq", "fundamentals", "broker"])

c("Fundamentals",
  "What is the <b>AMQP 0-9-1</b> protocol?",
  "Advanced Message Queuing Protocol — a wire-level protocol defining how clients and brokers talk. Models: exchange, queue, binding. RabbitMQ's primary protocol (via a plugin for AMQP 1.0).",
  ["rabbitmq", "fundamentals", "amqp"])

c("Fundamentals",
  "What is a <b>producer</b> vs a <b>consumer</b>?",
  "<b>Producer</b>: app that sends messages to an exchange.<br><b>Consumer</b>: app that subscribes to a queue and receives messages. Both connect via channels on a single TCP connection.",
  ["rabbitmq", "fundamentals", "producer", "consumer"])

c("Fundamentals",
  "What is a <b>Virtual Host (vhost)</b> in RabbitMQ?",
  "A logical isolation unit — each vhost has its own exchanges, queues, bindings, users, and permissions. Think of it like a database inside a PostgreSQL server. Default: <code>/</code>.",
  ["rabbitmq", "fundamentals", "vhost"])

c("Fundamentals",
  "What are the three core AMQP primitives?",
  "<b>Exchange</b> — receives messages from producers, routes them.<br><b>Queue</b> — stores messages until consumed.<br><b>Binding</b> — a rule linking an exchange to a queue with a routing key.",
  ["rabbitmq", "fundamentals", "amqp", "exchange", "queue", "binding"])

c("Fundamentals",
  "What is a <b>routing key</b>?",
  "A string the producer specifies on publish. The exchange uses it (with binding keys) to decide which queue(s) receive the message.",
  ["rabbitmq", "fundamentals", "routing-key"])

c("Fundamentals",
  "How does a <b>connection</b> differ from a <b>channel</b>?",
  "<b>Connection</b>: TCP connection to the broker (heavy, TLS overhead).<br><b>Channel</b>: virtual connection multiplexed over one TCP connection (lightweight). Do one operation per channel at a time; use many channels per connection.",
  ["rabbitmq", "fundamentals", "connection", "channel"])

c("Fundamentals",
  "What are <b>message acknowledgments</b> (acks)?",
  "A consumer tells RabbitMQ <i>'I've processed this message, delete it'</i>. Without acks, RabbitMQ redelivers the message when the consumer disconnects. Auto-ack deletes on delivery (unsafe); manual ack is safe.",
  ["rabbitmq", "fundamentals", "ack"])

c("Fundamentals",
  "RabbitMQ vs Kafka — key difference?",
  "<b>RabbitMQ</b>: smart broker, dumb consumer — routing, TTL, DLX built in. Push-based. Lower throughput, more flexible.<br><b>Kafka</b>: dumb broker, smart consumer — append-only log, pull-based. Massive throughput, stream processing, message replay.",
  ["rabbitmq", "fundamentals", "comparison", "kafka"])

c("Fundamentals",
  "RabbitMQ vs NATS — key difference?",
  "<b>NATS</b>: ultra-light, pub-sub focused, at-most-once (JetStream adds persistence). Single-digit-ms latency.<br><b>RabbitMQ</b>: full AMQP routing, exchanges, DLX, TTL, quorum queues. Feature-rich but heavier.",
  ["rabbitmq", "fundamentals", "comparison", "nats"])

c("Fundamentals",
  "RabbitMQ vs SQS/SNS — key difference?",
  "<b>SQS</b>: AWS-managed, no server to run, HTTP-only, at-least-once (FIFO for exactly-once).<br><b>RabbitMQ</b>: self-hosted or managed, AMQP protocol, rich routing, lower latency, more control.",
  ["rabbitmq", "fundamentals", "comparison", "sqs"])

c("Fundamentals",
  "What Erlang/OTP primitives power RabbitMQ?",
  "Lightweight processes, message passing, supervision trees, mnesia (DB). This gives RabbitMQ its fault-tolerance and concurrency model.",
  ["rabbitmq", "fundamentals", "erlang", "otp"])

c("Fundamentals",
  "What is the <b>default exchange</b> (nameless exchange)?",
  "An unnamed direct exchange (<code>''</code>) automatically created by the broker. Every queue is bound to it with the queue name as routing key — allows sending directly to a queue by name.",
  ["rabbitmq", "fundamentals", "default-exchange"])

# ─── 02 AMQP Exchanges & Queues ────────────────────────────────────────────

c("AMQP",
  "Name all built-in <b>exchange types</b> and their routing logic.",
  "<b>Direct</b> — exact match of routing key to binding key.<br><b>Fanout</b> — broadcast to ALL bound queues (ignores routing key).<br><b>Topic</b> — pattern match using <code>*</code> (one word) and <code>#</code> (zero+ words).<br><b>Headers</b> — routes on header attributes, not routing key (deprecated, rarely used).<br><b>Default</b> — unnamed direct, routing key = queue name.",
  ["rabbitmq", "amqp", "exchange-types"])

c("AMQP",
  "How does a <b>direct exchange</b> route?",
  "A queue binds with a binding key <code>K</code>. The exchange delivers to the queue when the message's routing key <b>exactly equals</b> <code>K</code>.",
  ["rabbitmq", "amqp", "direct-exchange"])

c("AMQP",
  "How does a <b>fanout exchange</b> route?",
  "Delivers the message to <b>every queue</b> bound to the exchange — routing key is ignored. Useful for broadcast/pub-sub.",
  ["rabbitmq", "amqp", "fanout-exchange"])

c("AMQP",
  "How does a <b>topic exchange</b> route?<br>Explain <code>*</code> and <code>#</code>.",
  "Binding key is a dot-separated pattern. <code>*</code> matches exactly one word, <code>#</code> matches zero or more words.<br>e.g. <code>order.*.created</code> matches <code>order.us.created</code> and <code>order.eu.created</code> but not <code>order.created</code>.<br><code>order.#</code> matches all order events.",
  ["rabbitmq", "amqp", "topic-exchange", "wildcards"])

c("AMQP",
  "Give examples of topic exchange patterns matching <code>quick.orange.rabbit</code>.",
  "<code>*.orange.*</code> → match<br><code>*.*.rabbit</code> → match<br><code>lazy.#</code> → no match<br><code>quick.#</code> → match<br><code>#.rabbit</code> → match<br><code>quick.orange.fox.#</code> → no match (subject has only 3 words)",
  ["rabbitmq", "amqp", "topic-exchange", "examples"])

c("AMQP",
  "What is a <b>headers exchange</b>?",
  "Routes based on message <b>headers</b> (not routing key). Binding specifies header key-value pairs with <b>x-match</b>: <code>all</code> (AND) or <code>any</code> (OR). Rarely used; favour topic exchanges.",
  ["rabbitmq", "amqp", "headers-exchange"])

c("AMQP",
  "What are <b>exchange-to-exchange bindings</b>?",
  "Bind one exchange to another, just like binding to a queue. Messages flow E1 → E2 → queues. Enables composing routing topologies (e.g., fanout to two topic exchanges for departmental routing).",
  ["rabbitmq", "amqp", "e2e-binding"])

c("AMQP",
  "What queue arguments control message <b>durability</b> and <b>lifetime</b>?",
  "<code>durable=True</code> — survives broker restart (metadata only; messages need <code>delivery_mode=2</code>).<br><code>exclusive=True</code> — used by one connection, deleted on disconnect.<br><code>auto_delete=True</code> — deleted when last consumer unsubscribes.",
  ["rabbitmq", "amqp", "queue", "durability"])

c("AMQP",
  "What is <code>x-message-ttl</code>?",
  "Queue argument: messages expire after N milliseconds. Expired messages are dropped or routed to a Dead Letter Exchange if configured. Can also set per-message TTL via <code>expiration</code> property.",
  ["rabbitmq", "amqp", "queue", "ttl"])

c("AMQP",
  "What is <code>x-max-length</code> and <code>x-max-length-bytes</code>?",
  "<code>x-max-length</code>: max number of messages in queue. Overflow behaviour controlled by <code>x-overflow</code>.<br><code>x-max-length-bytes</code>: max total bytes of message bodies in queue.<br>When limit hit, oldest messages are dropped-from-head (or reject-publish with overflow=reject-publish).",
  ["rabbitmq", "amqp", "queue", "max-length"])

c("AMQP",
  "What is a <b>Dead Letter Exchange</b> (DLX)? Configure which two arguments.",
  "A queue declares <code>x-dead-letter-exchange</code> (target exchange for dead messages) and optionally <code>x-dead-letter-routing-key</code>. Messages are dead-lettered when: rejected (requeue=false), TTL expires, or queue length limit reached.",
  ["rabbitmq", "amqp", "dlx"])

c("AMQP",
  "What is <code>x-single-active-consumer</code>?",
  "Queue argument: only one consumer at a time is active; others are standby. If the active consumer disconnects, a standby takes over. Enables hot-standby without external coordination.",
  ["rabbitmq", "amqp", "queue", "single-active-consumer"])

c("AMQP",
  "What is <code>x-queue-mode=lazy</code>?",
  "Lazy queue: messages go straight to <b>disk</b> (not memory). Great for long queues where most messages aren't consumed immediately. Reduces RAM usage, increases I/O.",
  ["rabbitmq", "amqp", "queue", "lazy-queue"])

c("AMQP",
  "What is <code>x-overflow</code>?",
  "Controls queue overflow behaviour when max-length/bytes is hit.<br><code>drop-head</code> (default): remove oldest messages.<br><code>reject-publish</code>: reject new publishes with <code>basic.nack</code>.<br><code>reject-publish-dlx</code>: dead-letter rejected messages.",
  ["rabbitmq", "amqp", "queue", "overflow"])

c("AMQP",
  "What is <b>prefetch count</b> (<code>basic_qos</code>)?",
  "Max number of unacknowledged messages a consumer can have at once. <code>channel.basic_qos(prefetch_count=10)</code>. Prevents one consumer from being overloaded; enables fair dispatch.",
  ["rabbitmq", "amqp", "prefetch"])

c("AMQP",
  "List critical <b>message properties</b> (AMQP basic.properties).",
  "<code>delivery_mode</code>: 1=transient, 2=persistent<br><code>content_type</code>: e.g. <code>application/json</code><br><code>content_encoding</code>: e.g. <code>gzip</code><br><code>correlation_id</code>: links request to reply (RPC)<br><code>reply_to</code>: queue name for reply (RPC)<br><code>expiration</code>: per-message TTL ms<br><code>message_id</code>: unique id<br><code>timestamp</code>: epoch<br><code>type</code>: app-level message type<br><code>headers</code>: arbitrary key-value map<br><code>priority</code>: 0-255 (requires x-max-priority on queue)",
  ["rabbitmq", "amqp", "message-properties"])

c("AMQP",
  "What are <b>publisher confirms</b>?<br>How to enable in pika?",
  "The broker asynchronously confirms it has handled a published message (routed to all queues).<br>Enable: <code>channel.confirm_delivery()</code> (pika) / <code>channel.confirm_select()</code> (amqplib). Publisher receives an <code>ack</code> or <code>nack</code> callback. Use for guaranteed delivery.",
  ["rabbitmq", "amqp", "publisher-confirms"])

c("AMQP",
  "What are the <b>mandatory</b> and <b>immediate</b> flags?",
  "<b>mandatory=True</b>: if message can't be routed to any queue, broker returns it to publisher (via <code>basic.return</code>).<br><b>immediate=True</b>: if no consumer ready, return message. (Removed in RabbitMQ 3.0; use TTL+DLX instead.)",
  ["rabbitmq", "amqp", "mandatory", "immediate"])

c("AMQP",
  "What is <b>consumer prefetch</b> (<code>basic_qos</code>) and how does the <code>global</code> flag work?",
  "<code>channel.basic_qos(prefetch_count=N, global=False)</code> — per-consumer limit (default).<br><code>global=True</code> — limit shared across ALL consumers on the channel. Use per-consumer (non-global) for fair dispatch; global is rarely wanted.",
  ["rabbitmq", "amqp", "prefetch", "global"])

c("AMQP",
  "Explain <b>connection recovery</b> and <b>topology recovery</b>.",
  "Client libraries (pika, amqplib) can auto-reconnect on network failure and re-declare exchanges, queues, and bindings. RabbitMQ stream protocol also has built-in reconnect. Configure recovery intervals and retry limits.",
  ["rabbitmq", "amqp", "recovery"])

c("AMQP",
  "What are the three consumer acknowledgment modes?",
  "<b>basic.ack</b>: success, remove message.<br><b>basic.nack</b>: fail, optionally requeue (multiple=true for batch).<br><b>basic.reject</b>: fail single message, optionally requeue.<br><b>requeue=False</b> + DLX configured = message goes to dead-letter queue.",
  ["rabbitmq", "amqp", "ack", "nack", "reject"])

# ─── 03 Messaging Patterns ─────────────────────────────────────────────────

c("Patterns",
  "What is the <b>Competing Consumers</b> pattern?",
  "Multiple consumers subscribe to the <b>same queue</b>. RabbitMQ dispatches messages round-robin. Each message is processed by exactly one consumer. Scales horizontally — add more consumers to handle load.",
  ["rabbitmq", "patterns", "competing-consumers"])

c("Patterns",
  "What is the <b>Publish-Subscribe</b> pattern?",
  "Producer sends to a <b>fanout exchange</b>. Each consumer declares its own (auto-delete) queue bound to the exchange. Every consumer gets a copy of every message. Useful for event broadcasting.",
  ["rabbitmq", "patterns", "pub-sub"])

c("Patterns",
  "What is the <b>Routing</b> pattern?",
  "Producer sends to a <b>direct exchange</b> with a routing key. Consumers bind their queues with specific binding keys. Only queues with a matching key receive the message. More selective than fanout.",
  ["rabbitmq", "patterns", "routing"])

c("Patterns",
  "What is the <b>Topic-based routing</b> pattern?",
  "Producer sends to a <b>topic exchange</b>. Consumers bind with wildcard patterns (<code>*</code>, <code>#</code>). e.g., <code>logs.#</code> for all log levels, <code>logs.error.#</code> for errors only. Flexible multi-criteria routing.",
  ["rabbitmq", "patterns", "topic-routing"])

c("Patterns",
  "How does the <b>RPC pattern</b> work in RabbitMQ?<br>Which message properties are used?",
  "Client publishes to <code>rpc_queue</code> with <code>reply_to</code> (callback queue name) and <code>correlation_id</code> (unique request ID). Server consumes, processes, and publishes the result to the <code>reply_to</code> queue with the same <code>correlation_id</code>. Client correlates the response.",
  ["rabbitmq", "patterns", "rpc"])

c("Patterns",
  "What is the <b>Scatter-Gather</b> pattern?",
  "Publisher sends a message. Multiple independent processors (bound to same exchange) each receive a copy, process it, and each sends their result to an aggregator queue. The aggregator waits for all results and combines them.",
  ["rabbitmq", "patterns", "scatter-gather"])

c("Patterns",
  "What is an <b>idempotent consumer</b>?",
  "A consumer designed to safely receive the same message multiple times without side effects. Use a <b>deduplication store</b> (e.g., Redis, DB) keyed by <code>message_id</code> to detect and skip duplicates.",
  ["rabbitmq", "patterns", "idempotent", "dedup"])

c("Patterns",
  "How to implement <b>message deduplication</b> in RabbitMQ?",
  "Set a unique <code>message_id</code> on every message. Consumer checks a dedup store (Redis <code>SETNX</code> with TTL, or DB unique index) before processing. If message_id already seen, skip. Clean up old IDs periodically.",
  ["rabbitmq", "patterns", "dedup"])

c("Patterns",
  "How to implement <b>delayed messages</b> in RabbitMQ? (two approaches)",
  "<b>1. TTL + DLX pattern:</b> Publish to a queue with <code>x-message-ttl</code> and <code>x-dead-letter-exchange</code> set. Message expires → routed to DLX → consumed from target queue.<br><b>2. <code>rabbitmq_delayed_message_exchange</code> plugin:</b> Custom exchange type <code>x-delayed-message</code>. Set <code>x-delay</code> header in ms. Message delivered after delay.",
  ["rabbitmq", "patterns", "delayed-message"])

c("Patterns",
  "What is a <b>priority queue</b>? How to configure?",
  "Declare queue with <code>x-max-priority</code> (0-255). Publish messages with a <code>priority</code> property (higher = first). Messages are dequeued in priority order. Note: priority queues have performance overhead.",
  ["rabbitmq", "patterns", "priority-queue"])

c("Patterns",
  "What is a <b>lazy queue</b>? When to use it?",
  "Queue with <code>x-queue-mode=lazy</code>. Messages go directly to disk, only loaded to memory on demand. Use when: queue may grow very large, consumers are slow, RAM is constrained. Trade-off: higher disk I/O.",
  ["rabbitmq", "patterns", "lazy-queue"])

c("Patterns",
  "What is the <b>Sharded Queue</b> pattern (<code>rabbitmq_sharding</code> plugin)?",
  "Automatically partitions a logical queue across multiple physical queues on different nodes. Producer publishes to the sharded exchange; a sharding function distributes messages. Consumer consumes from all shards. Improves throughput and parallelism.",
  ["rabbitmq", "patterns", "sharded-queue"])

c("Patterns",
  "What is the <b>Consistent Hash Exchange</b> plugin?",
  "Routes messages to queues based on a hash of the routing key (or a specified header). When a queue is added or removed, only the keys that map to that queue are affected — consistent hashing minimises re-routing.",
  ["rabbitmq", "patterns", "consistent-hash"])

c("Patterns",
  "What is a <b>Request-Response over Messaging</b> pattern?",
  "The asynchronous equivalent of HTTP request-response. Requester publishes request with <code>reply_to</code> + <code>correlation_id</code>, subscribes to reply queue. Responder processes and publishes reply. Decouples caller from callee in time and space.",
  ["rabbitmq", "patterns", "request-response"])

c("Patterns",
  "Give a real-world example of <b>topic exchange</b> routing for e-commerce.",
  "Exchange: <code>events</code><br>Binding: <code>order.*.paid</code> → billing queue<br>Binding: <code>order.*.shipped</code> → notification queue<br>Binding: <code>order.#</code> → analytics queue<br>Publish: <code>order.us.paid</code> hits billing + analytics; <code>order.eu.shipped</code> hits notification + analytics.",
  ["rabbitmq", "patterns", "topic-exchange", "ecommerce"])

# ─── 04 Reliability & DLQ ──────────────────────────────────────────────────

c("Reliability",
  "What is a <b>Dead Letter Exchange</b> (DLX) and when does a message become dead-lettered?",
  "A DLX receives messages that are:<br>1. <b>Rejected</b> (<code>basic.reject</code> or <code>basic.nack</code>) with <code>requeue=False</code><br>2. <b>TTL expired</b> (message TTL or queue TTL)<br>3. <b>Queue length exceeded</b> (max-length/bytes + overflow drop-head or reject-publish-dlx)<br>Config: set <code>x-dead-letter-exchange</code> on the source queue.",
  ["rabbitmq", "reliability", "dlx"])

c("Reliability",
  "How to configure a <b>Dead Letter Queue</b> (DLQ) and its exchange?",
  "<b>1.</b> Declare DLX: <code>exchange_declare('my_dlx', 'direct')</code><br><b>2.</b> Declare DLQ: <code>queue_declare('dead_letters')</code><br><b>3.</b> Bind: <code>queue_bind('dead_letters', 'my_dlx', 'dead')</code><br><b>4.</b> Set on source queue: <code>queue_declare('work', arguments={'x-dead-letter-exchange': 'my_dlx', 'x-dead-letter-routing-key': 'dead'})</code>",
  ["rabbitmq", "reliability", "dlq", "setup"])

c("Reliability",
  "What is a <b>poison message</b> and how to handle it?",
  "A message that always causes the consumer to fail. Without DLX, it loops forever (deliver → fail → requeue → deliver).<br>Fix: consumer <b>nack with requeue=False</b>, DLX routes to DLQ. Monitor DLQ for poison messages. Optionally add retry count header and limit retries before DLQ-ing.",
  ["rabbitmq", "reliability", "poison-message"])

c("Reliability",
  "How to achieve <b>guaranteed delivery</b> in RabbitMQ? (3 pieces)",
  "1. <b>Durable exchange</b> + <b>durable queue</b> (survive broker restart)<br>2. <b>Persistent messages</b> (<code>delivery_mode=2</code>)<br>3. <b>Publisher confirms</b> (broker acks receipt) + <b>mandatory=True</b> (ensure routed)<br>+ <b>Manual consumer acks</b> (only ack after processing)",
  ["rabbitmq", "reliability", "guaranteed-delivery"])

c("Reliability",
  "What is the difference between <b>auto-ack</b> and <b>manual ack</b>?",
  "<b>auto_ack=True</b>: message deleted from queue immediately upon delivery. If consumer crashes, message is <b>lost</b>.<br><b>auto_ack=False</b> (manual): consumer must explicitly <code>basic.ack()</code>. If consumer crashes before ack, message is <b>re-queued</b> and redelivered.<br><b>Always use manual ack in production.</b>",
  ["rabbitmq", "reliability", "ack"])

c("Reliability",
  "What is <b>high availability</b> in RabbitMQ?<br>Classic mirrored queues vs quorum queues.",
  "<b>Classic Mirrored Queues</b>: one master + N mirrors. All writes go through master. Async replication to mirrors. Deprecated since 3.12, removed in 4.0.<br><b>Quorum Queues</b>: Raft-based, leader + followers. Majority-write confirmation. Replaces mirrored queues. <code>x-queue-type=quorum</code>.",
  ["rabbitmq", "reliability", "ha", "mirrored-queues", "quorum-queues"])

c("Reliability",
  "What are <b>quorum queues</b> and how do they work?",
  "Based on the <b>Raft consensus algorithm</b>. A leader is elected; all writes go through the leader and are replicated to a majority of followers before confirming. If a follower becomes unreachable, the leader continues. If the leader fails, a new leader is elected. Provides data safety and consistency.",
  ["rabbitmq", "reliability", "quorum-queues"])

c("Reliability",
  "How to declare a <b>quorum queue</b>? Minimum cluster size?",
  "<code>channel.queue_declare('my_queue', arguments={'x-queue-type': 'quorum'})</code><br>Minimum: 3 RabbitMQ nodes (odd number for Raft majority). Quorum queues are durable by default, ignore exclusive/auto-delete.",
  ["rabbitmq", "reliability", "quorum-queues", "setup"])

c("Reliability",
  "Quorum queues vs Mirrored queues vs Streams — when to use each?",
  "<b>Quorum queues</b>: safe, consistent, Raft-based. Default for new HA queues.<br><b>Mirrored queues</b>: legacy, async replication, removed in 4.0. Avoid for new projects.<br><b>Streams</b>: append-only log, replay, large fan-out, consumer groups, offset tracking. Use for event sourcing, replayable logs.",
  ["rabbitmq", "reliability", "quorum", "mirrored", "streams", "comparison"])

c("Reliability",
  "What is the <b>polling consumer</b> pattern (<code>basic.get</code> vs <code>basic.consume</code>)?",
  "<code>basic.get</code>: pull a single message. Consumer requests one at a time. Inefficient — high overhead, may miss messages if no polling.<br><code>basic.consume</code>: push-based subscription (preferred). Broker pushes messages as they arrive. Lower latency, lower overhead.",
  ["rabbitmq", "reliability", "polling", "get", "consume"])

c("Reliability",
  "What is <b>message TTL</b> vs <b>queue TTL</b>?",
  "<b>Message TTL</b>: set via <code>expiration</code> property on publish (per-message).<br><b>Queue TTL</b>: set via <code>x-message-ttl</code> queue argument. Applies to all messages in that queue.<br>Message TTL overrides queue TTL if both are set.",
  ["rabbitmq", "reliability", "ttl"])

c("Reliability",
  "Can RabbitMQ achieve <b>exactly-once</b> processing?",
  "Not natively. RabbitMQ guarantees <b>at-least-once</b> (message may be redelivered).<br>For exactly-once: consumer must be idempotent, use message deduplication, and manual acks. <b>Streams</b> with deduplication come closer. Kafka + transactions is the gold standard for exactly-once.",
  ["rabbitmq", "reliability", "exactly-once"])

c("Reliability",
  "What are the <b>Federation</b> and <b>Shovel</b> plugins?",
  "<b>Federation</b>: connects exchanges/queues across brokers (upstream → downstream). Messages flow in one direction. Useful for WAN/cross-DC.<br><b>Shovel</b>: moves messages from a source (queue/exchange) to a destination. Lower-level than federation; good for migration or bridging unidirectional traffic.",
  ["rabbitmq", "reliability", "federation", "shovel"])

c("Reliability",
  "What are the <b>three pillars of message durability</b>?",
  "1. <b>Durable Exchange</b> — survives broker restart.<br>2. <b>Durable Queue</b> — survives broker restart.<br>3. <b>Persistent Message</b> — <code>delivery_mode=2</code>, written to disk before confirm.<br>All three required for full durability; missing any one = potential data loss.",
  ["rabbitmq", "reliability", "durability"])

# ─── 05 Operations & Management ────────────────────────────────────────────

c("Operations",
  "How to enable the <b>Management Plugin</b> and what does it provide?",
  "<code>rabbitmq-plugins enable rabbitmq_management</code><br>Provides: Web UI on <code>http://localhost:15672</code> (default user: <code>guest</code>), HTTP management API, CLI tool <code>rabbitmqadmin</code>. Enables monitoring, admin, and inspection.",
  ["rabbitmq", "operations", "management-plugin"])

c("Operations",
  "Key endpoints of the <b>Management HTTP API</b>.",
  "<code>GET /api/overview</code> — cluster-wide stats<br><code>GET /api/vhosts</code> — list vhosts<br><code>GET /api/vhosts/{name}</code> — vhost details<br><code>GET /api/exchanges/{vhost}</code> — exchanges<br><code>GET /api/queues/{vhost}</code> — queues<br><code>GET /api/bindings/{vhost}</code> — bindings<br><code>GET /api/connections</code> — connections<br><code>GET /api/channels</code> — channels<br>Auth: Basic, user:pass.",
  ["rabbitmq", "operations", "http-api"])

c("Operations",
  "How to create a queue binding via the <b>Management HTTP API</b>?",
  "<code>POST /api/bindings/{vhost}/e/{exchange}/q/{queue}</code><br>Body: <code>{\"routing_key\": \"my_key\", \"arguments\": {}}</code><br>Content-Type: application/json<br>Auth: Basic auth with admin user.",
  ["rabbitmq", "operations", "http-api", "binding"])

c("Operations",
  "What CLI tools come with RabbitMQ?",
  "<code>rabbitmqctl</code> — manage nodes, users, vhosts, policies, queues, cluster<br><code>rabbitmq-plugins</code> — enable/disable/list plugins<br><code>rabbitmq-diagnostics</code> — health checks, status, environment info<br><code>rabbitmqadmin</code> — HTTP-API-based CLI (requires management plugin)<br><code>rabbitmq-queues</code> — quorum queue and stream management",
  ["rabbitmq", "operations", "cli-tools"])

c("Operations",
  "How to create a <b>user</b> and grant permissions via <code>rabbitmqctl</code>?",
  "<code>rabbitmqctl add_user myuser mypassword</code><br><code>rabbitmqctl set_permissions -p / myuser \".*\" \".*\" \".*\"</code><br>Permissions: configure (exchanges/queues), write (publish), read (consume) — each a regex matching resource names.",
  ["rabbitmq", "operations", "users", "permissions"])

c("Operations",
  "How to set a <b>policy</b> in RabbitMQ? When to use policies vs queue arguments?",
  "<code>rabbitmqctl set_policy DLX \"^work\\.\" '{\"dead-letter-exchange\":\"my_dlx\"}' --priority 1 --apply-to queues</code><br><b>Policies</b>: dynamically updateable, apply to multiple queues by regex pattern, override queue arguments. Prefer policies for operational settings that may change.<br><b>Queue arguments</b>: set at declaration, immutable without re-creating the queue.",
  ["rabbitmq", "operations", "policies"])

c("Operations",
  "How to <b>cluster</b> RabbitMQ nodes?",
  "1. Stop the joining node: <code>rabbitmqctl stop_app</code><br>2. Join cluster: <code>rabbitmqctl join_cluster rabbit@node1</code><br>3. Start: <code>rabbitmqctl start_app</code><br>Nodes share vhosts, exchanges, users across cluster. Queues live on one node (or are replicated via quorum queues).<br>Check: <code>rabbitmqctl cluster_status</code>",
  ["rabbitmq", "operations", "clustering"])

c("Operations",
  "What is the <b>Erlang cookie</b> and why is it important?",
  "A shared secret (file <code>~/.erlang.cookie</code> or <code>/var/lib/rabbitmq/.erlang.cookie</code>) that RabbitMQ nodes use to authenticate to each other. All nodes in a cluster MUST have the same cookie value.",
  ["rabbitmq", "operations", "erlang-cookie"])

c("Operations",
  "How to <b>monitor RabbitMQ with Prometheus + Grafana</b>?",
  "Enable: <code>rabbitmq-plugins enable rabbitmq_prometheus</code><br>Metrics exposed at <code>GET /metrics</code> (Prometheus format). Includes queue depths, message rates, connection/channel counts, memory, disk, node stats.<br>Import official Grafana dashboard (ID 10991) or build custom dashboards.",
  ["rabbitmq", "operations", "prometheus", "grafana"])

c("Operations",
  "What key metrics to monitor in RabbitMQ?",
  "<b>Queue depth</b> (messages ready/unacked) — backlog indicator<br><b>Publish/deliver/ack rates</b> — throughput<br><b>Consumer count</b> — are consumers connected?<br><b>Memory usage</b> — high watermark alarm<br><b>Disk free space</b> — disk alarm threshold<br><b>Connection/channel count</b> — connection leaks<br><b>Unroutable message rate</b> — dropped messages<br><b>GC runs</b> — Erlang VM health",
  ["rabbitmq", "operations", "metrics", "monitoring"])

c("Operations",
  "What is <b>memory alarm</b> and <b>disk alarm</b>?",
  "RabbitMQ blocks publishers (flow control) when:<br><b>Memory</b> exceeds <code>vm_memory_high_watermark</code> (default 0.4 = 40% of RAM)<br><b>Free disk</b> drops below <code>disk_free_limit</code> (default 50MB).<br>Unblocks when below threshold. Prevents broker crash from resource exhaustion.",
  ["rabbitmq", "operations", "flow-control", "alarms"])

c("Operations",
  "How to <b>backup and restore</b> RabbitMQ?",
  "<b>Export definitions:</b> <code>rabbitmqctl export_definitions backup.json</code> (vhosts, users, policies, exchanges, queues, bindings — no messages).<br><b>Import:</b> <code>rabbitmqctl import_definitions backup.json</code><br>For message-level backup, use Federation/Shovel to replicate to a backup broker, or filesystem-level backup (stop node first).",
  ["rabbitmq", "operations", "backup", "restore"])

c("Operations",
  "How to <b>upgrade RabbitMQ</b> with minimal downtime?",
  "1. Use a cluster (≥3 nodes).<br>2. Upgrade one node at a time: drain (stop publishing to it), upgrade, restart, rejoin.<br>3. For major versions, check release notes — blue-green or rolling upgrade supported.<br>4. Quorum queues survive node restarts (Raft); classic queues may need mirroring during upgrade.",
  ["rabbitmq", "operations", "upgrade"])

# ─── 06 Plugins & Protocols ────────────────────────────────────────────────

c("Plugins",
  "What is the <b>RabbitMQ Streams</b> plugin?",
  "An append-only log (similar to Kafka) — immutable, replayable, partitioned. Supports consumer groups with offset tracking, super-streams (partitioned across nodes), server-side filtering, and deduplication. Use for event sourcing, audit logs, high fan-out.",
  ["rabbitmq", "plugins", "streams"])

c("Plugins",
  "What are <b>consumer groups</b> in RabbitMQ Streams?",
  "Multiple consumers in the same group share the stream — each message is delivered to one consumer in the group (like competing consumers). Offset tracking per consumer; consumers can restart from last committed offset.",
  ["rabbitmq", "plugins", "streams", "consumer-groups"])

c("Plugins",
  "What are <b>super-streams</b>?",
  "A logical stream partitioned across multiple physical streams on different nodes, with a hash-based routing. Like Kafka topics with partitions. Enables horizontal scaling and higher throughput in RabbitMQ Streams.",
  ["rabbitmq", "plugins", "streams", "super-streams"])

c("Plugins",
  "What is the <b><code>rabbitmq_delayed_message_exchange</code></b> plugin?",
  "Adds exchange type <code>x-delayed-message</code>. Publish with header <code>x-delay</code> (ms). Message is held internally, then routed after the delay. Simpler than TTL+DLX for scheduled/delayed delivery.",
  ["rabbitmq", "plugins", "delayed-message"])

c("Plugins",
  "What is the <b><code>rabbitmq_consistent_hash_exchange</code></b> plugin?",
  "Exchange type <code>x-consistent-hash</code>. Routes messages to queues based on a hash of the routing key (or message header). Adding/removing queues minimally redistributes messages — consistent hashing.",
  ["rabbitmq", "plugins", "consistent-hash-exchange"])

c("Plugins",
  "What is the <b><code>rabbitmq_sharding</code></b> plugin?",
  "Automatically shards a logical queue across multiple physical queues. Producer publishes to <code>x-modulus-hash</code> exchange; consumer automatically consumes from all shards. Improves throughput by parallelising queue operations.",
  ["rabbitmq", "plugins", "sharding"])

c("Plugins",
  "What is the <b><code>rabbitmq_message_timestamp</code></b> plugin?",
  "Automatically adds a <code>timestamp</code> header (epoch ms) when a message is published. Enables consumers to know when a message was published without the producer setting the timestamp manually.",
  ["rabbitmq", "plugins", "message-timestamp"])

c("Plugins",
  "What is the <b><code>rabbitmq_top</code></b> plugin?",
  "Provides <code>rabbitmq-top</code>-like functionality: identifies top processes by memory usage, reductions, or message rates. Helps find which queues/exchanges/connections are consuming the most resources.",
  ["rabbitmq", "plugins", "top"])

c("Plugins",
  "What is the <b><code>rabbitmq_tracing</code></b> plugin?",
  "Captures every message passing through a vhost (or specific routing patterns). Writes traces to a log file. Invaluable for debugging routing issues. High overhead — disable in production after debugging.",
  ["rabbitmq", "plugins", "tracing"])

c("Plugins",
  "What <b>MQTT protocol</b> support does RabbitMQ have?",
  "Enable: <code>rabbitmq-plugins enable rabbitmq_mqtt</code>. Listens on port 1883 (or 8883 for MQTT over TLS). Maps MQTT topics to AMQP topic exchanges. Great for IoT devices with low bandwidth. Supports QoS 0, 1, 2.",
  ["rabbitmq", "plugins", "mqtt"])

c("Plugins",
  "What is <b>STOMP</b> protocol support in RabbitMQ?",
  "Enable: <code>rabbitmq-plugins enable rabbitmq_stomp</code>. STOMP (Simple Text Oriented Messaging Protocol) is a text-based protocol popular with Ruby, Python, and web clients. Maps STOMP destinations to AMQP exchanges/queues.",
  ["rabbitmq", "plugins", "stomp"])

c("Plugins",
  "What is <b>AMQP 1.0</b> support in RabbitMQ?",
  "Enable: <code>rabbitmq-plugins enable rabbitmq_amqp1_0</code>. AMQP 1.0 is an OASIS/ISO standard (different from 0-9-1). Adds links, sessions, and container model. Enables interoperability with Azure Service Bus, ActiveMQ, etc.",
  ["rabbitmq", "plugins", "amqp-1.0"])

c("Plugins",
  "How does <b>OAuth 2.0 and JWT authentication</b> work in RabbitMQ?",
  "Enable <code>rabbitmq_auth_backend_oauth2</code>. Configure an OAuth2 provider (Keycloak, Auth0, etc.). Clients authenticate with JWT tokens. RabbitMQ validates the token signature and extracts identity/scope. Scopes map to vhost permissions.",
  ["rabbitmq", "plugins", "oauth2", "jwt"])

c("Plugins",
  "How does <b>LDAP authentication</b> work in RabbitMQ?",
  "Enable: <code>rabbitmq_auth_backend_ldap</code>. Configures an LDAP server (Active Directory, OpenLDAP) for user authentication and authorisation. RabbitMQ checks user credentials and groups against LDAP. Combine with internal auth as fallback.",
  ["rabbitmq", "plugins", "ldap"])

c("Plugins",
  "What is the <b><code>rabbitmq_peer_discovery_k8s</code></b> plugin?",
  "Enables RabbitMQ nodes running in Kubernetes to discover each other automatically via the Kubernetes API. Uses pod labels/annotations to form a cluster. Replaces manual <code>join_cluster</code> commands.",
  ["rabbitmq", "plugins", "kubernetes", "peer-discovery"])

c("Plugins",
  "What is the <b><code>rabbitmq_prometheus</code></b> plugin?",
  "Exposes RabbitMQ metrics in Prometheus text format at <code>GET /metrics</code>. Replaces the legacy <code>rabbitmq_prometheus</code> and <code>rabbitmq_management_agent</code> for metrics. Used with Prometheus + Grafana for monitoring dashboards.",
  ["rabbitmq", "plugins", "prometheus"])

# ─── 07 Gotchas ────────────────────────────────────────────────────────────

c("Gotchas",
  "What happens when a message is <b>unroutable</b>? How to prevent silent loss?",
  "By default, RabbitMQ <b>silently drops</b> unroutable messages. Prevention:<br>1. <b><code>mandatory=True</code></b> — broker returns unroutable messages to publisher via <code>basic.return</code>.<br>2. <b>Alternate Exchange</b> — configure exchange with <code>alternate-exchange</code> argument; unroutable messages go there instead.<br>Always use one of these in production.",
  ["rabbitmq", "gotchas", "unroutable"])

c("Gotchas",
  "What is the <b>alternate exchange</b> pattern?",
  "When declaring an exchange, set argument <code>alternate-exchange=my_ae</code>. Any message that can't be routed to any queue is instead routed to <code>my_ae</code>. Catch-all safety net for unroutable messages.",
  ["rabbitmq", "gotchas", "alternate-exchange"])

c("Gotchas",
  "Why is <b>high consumer prefetch</b> dangerous?",
  "A consumer with <code>prefetch_count=1000</code> grabs 1000 messages. If it's slow, those messages sit unacknowledged while other fast consumers are idle. <b>Uneven load distribution</b>. Set prefetch to 10-50 for fair dispatch. Even lower (1) for strict round-robin.",
  ["rabbitmq", "gotchas", "prefetch"])

c("Gotchas",
  "What causes <b>connection leaks</b> and <b>channel leaks</b>?",
  "Not closing connections/channels on app shutdown or on error. Each connection is a TCP socket (OS limits); each channel uses Erlang resources. Use <code>try/finally</code> or context managers. Monitor with <code>rabbitmqctl list_connections</code> / <code>list_channels</code>.",
  ["rabbitmq", "gotchas", "leaks"])

c("Gotchas",
  "Why does <b>auto-ack lose messages</b>?",
  "With <code>auto_ack=True</code>, the broker deletes the message the moment it delivers it. If the consumer crashes before processing, the message is <b>gone forever</b>. Always use manual acknowledgments (<code>auto_ack=False</code>) in production.",
  ["rabbitmq", "gotchas", "auto-ack"])

c("Gotchas",
  "Why does <b>requeue cause infinite loops</b> with poison messages?",
  "If a consumer <code>nack(requeue=True)</code> a poison message, RabbitMQ puts it back at the queue head and immediately redelivers it. The consumer fails again → nack → requeue → infinite loop, starving other messages.<br>Fix: <b>nack with requeue=False + DLX</b> to dead-letter the poison.",
  ["rabbitmq", "gotchas", "requeue-loop"])

c("Gotchas",
  "Why is <b>message ordering NOT guaranteed</b> with multiple consumers?",
  "Multiple consumers on one queue receive messages in a round-robin fashion. If consumer A processes msg-1 slowly and consumer B processes msg-2 quickly, B may finish before A → out-of-order processing.<br>For ordering: use <b>one consumer per queue</b> or use single-active-consumer.",
  ["rabbitmq", "gotchas", "ordering"])

c("Gotchas",
  "What is <b>split-brain</b> in classic mirrored queues?",
  "When a network partition separates cluster nodes, each partition may think it's the master and elect a new master. Two masters = conflicting writes = data divergence and loss. Quorum queues use Raft leader election to avoid split-brain.",
  ["rabbitmq", "gotchas", "split-brain"])

c("Gotchas",
  "How does <b>network partition handling</b> work in RabbitMQ?",
  "Detection modes: <code>ignore</code>, <code>pause_minority</code>, <code>pause_if_all_down</code>, <code>autoheal</code>.<br><code>pause_minority</code> (default): nodes in minority partition pause themselves (no publishers/consumers). Prevents split-brain. Majority partition continues.<br><code>autoheal</code>: when partition heals, the winning partition's state is kept; others restart and rejoin.",
  ["rabbitmq", "gotchas", "partition"])

c("Gotchas",
  "What is the <b>lazy queue startup time</b> problem?",
  "Lazy queues (<code>x-queue-mode=lazy</code>) write all messages to disk. On node restart, the queue must rebuild its on-disk index before serving consumers. For queues with millions of messages, this can take <b>minutes</b>. Use quorum queues or streams for large persistent workloads instead.",
  ["rabbitmq", "gotchas", "lazy-queue-startup"])

c("Gotchas",
  "What are the <b>disk requirements</b> for quorum queues?",
  "Quorum queues use Raft — every write is fsynced to disk on a majority of nodes. This requires <b>low-latency SSDs</b>. Spinning disks cause massive performance degradation. Plan for replication factor × message volume disk.",
  ["rabbitmq", "gotchas", "quorum-queue-disk"])

c("Gotchas",
  "What causes <b>high connection churn</b> to crash RabbitMQ?",
  "Opening and closing TCP connections rapidly (e.g., one connection per message). Each connection triggers Erlang network driver setup and teardown. Use <b>long-lived connections + many channels</b>. Connection pooling is essential — never open a new connection per publish/consume.",
  ["rabbitmq", "gotchas", "connection-churn"])

c("Gotchas",
  "What are the <b>large message</b> limits in RabbitMQ?",
  "RabbitMQ recommends messages <b>under 128MB</b> (practical limit ~512MB before Erlang VM issues). Large messages cause memory pressure, GC pauses, and I/O storms. For large payloads: store the data in S3/object storage and pass a URL/ID in the message.",
  ["rabbitmq", "gotchas", "large-messages"])

c("Gotchas",
  "What <b>client library timeouts</b> cause issues?",
  "Default heartbeat timeout is 60s. If consumer processing takes longer with no network activity, the broker closes the connection. Set <code>heartbeat</code> higher (e.g., 600s) or send heartbeats during long processing. Connection timeout, socket timeout, and operation timeout should all be configured.",
  ["rabbitmq", "gotchas", "timeouts"])

c("Gotchas",
  "Why do <b>federation links fail</b>?",
  "Federation uses AMQP connections between upstream and downstream. Common failures: network partition, SSL cert expiry, credential changes, upstream queue deleted. Monitor federation link status and set up alerts.<br><code>rabbitmqctl federation_status</code>",
  ["rabbitmq", "gotchas", "federation-failures"])

# ─── 08 Expert ─────────────────────────────────────────────────────────────

c("Expert",
  "RabbitMQ vs Kafka — decision framework. When to choose which?",
  "<b>Choose RabbitMQ when:</b><br>- Complex routing (topic, headers, DLX, TTL)<br>- Low latency per-message delivery<br>- Flexible consumer topologies<br>- Smaller message volumes (millions/day)<br><b>Choose Kafka when:</b><br>- Massive throughput (millions/sec)<br>- Message replay and time-travel<br>- Stream processing (Kafka Streams, Flink)<br>- Append-only immutable log required<br>- Long-term persistent storage of all messages",
  ["rabbitmq", "expert", "kafka-vs-rabbitmq"])

c("Expert",
  "Should <b>quorum queues be the default</b> for new queues? Why?",
  "<b>Yes.</b> Quorum queues provide Raft-based consensus, data safety, and automatic leader election. Classic queues are deprecated and will be removed in RabbitMQ 4.0. New projects should default to quorum queues unless they specifically need features not in quorum queues (e.g., message priorities).",
  ["rabbitmq", "expert", "quorum-queues-default"])

c("Expert",
  "What is the <b>classic queues deprecation path</b>?",
  "RabbitMQ 3.12: classic mirrored queues deprecated (warning on use).<br>RabbitMQ 4.0: classic mirrored queues removed. Plain classic queues remain but considered legacy.<br>Migration: re-declare classic queues as quorum queues, migrate messages, switch consumers.",
  ["rabbitmq", "expert", "classic-deprecation"])

c("Expert",
  "When to use <b>RabbitMQ Streams</b> instead of queues?",
  "Use Streams when:<br>- Messages need to be <b>replayed</b> (consumer can start from any offset)<br>- <b>High fan-out</b> (many consumers reading same data independently)<br>- <b>Event sourcing</b> — immutable event log<br>- <b>Consumer groups</b> with offset tracking<br>- Messages should be persisted for long periods and not deleted on consumption<br>Use Queues when: one-time delivery, complex routing, TTL, DLX.",
  ["rabbitmq", "expert", "streams-vs-queues"])

c("Expert",
  "How to use RabbitMQ for <b>event sourcing</b>?",
  "Use <b>RabbitMQ Streams</b> (or a durable queue with manual deletion). All domain events are published to a stream as an append-only, immutable log. Projections (read models) consume from the stream, tracking offset. Streams support replay from any offset for rebuilding projections.",
  ["rabbitmq", "expert", "event-sourcing"])

c("Expert",
  "How to run RabbitMQ in <b>Kubernetes</b>?",
  "Use <b>StatefulSet</b> with persistent volumes for each pod. Enable the <code>rabbitmq_peer_discovery_k8s</code> plugin for auto-clustering. Use a headless service for pod DNS. Set <code>RABBITMQ_USE_LONGNAME=true</code>. Mount the Erlang cookie as a secret. Use quorum queues for data safety across pod restarts.",
  ["rabbitmq", "expert", "kubernetes"])

c("Expert",
  "What is the <b>cluster sizing</b> recommendation for RabbitMQ?",
  "Use an <b>odd number of nodes</b> (3, 5, 7) for Raft quorum operations. 3 nodes is the minimum for production; tolerates 1 failure. 5 nodes tolerates 2 failures. More than 7 nodes adds latency for quorum consensus without proportional benefit. Consider Streams for higher throughput scenarios.",
  ["rabbitmq", "expert", "cluster-sizing"])

c("Expert",
  "How to balance <b>quorum queue leader distribution</b>?",
  "Quorum queue leaders handle all writes. If all leaders land on one node, it becomes a hotspot.<br>Use <code>rabbitmq-queues rebalance quorum</code> to redistribute leaders evenly across nodes. Set up automatic rebalancing with <code>queue_master_locator</code> policy: choose <code>min-masters</code> (least loaded) or <code>client-local</code> (co-locate with publisher).",
  ["rabbitmq", "expert", "quorum-leader-balancing"])

c("Expert",
  "Self-hosted RabbitMQ vs managed services (CloudAMQP, AWS MQ) — when to use which?",
  "<b>Self-hosted</b> (Kubernetes or VMs): full control, custom plugins, lower cost at scale, no vendor lock-in. Requires operational expertise.<br><b>Managed</b>: no ops burden, automated patching, built-in monitoring, support SLA. Ideal for teams without RabbitMQ expertise or when ops cost exceeds service cost.<br>Hybrid: managed for production, self-hosted for dev/staging.",
  ["rabbitmq", "expert", "self-hosted-vs-managed"])

c("Expert",
  "What is <b>AWS MQ</b> and its limitations?",
  "AWS-managed RabbitMQ (and ActiveMQ). Supports AMQP, MQTT, STOMP. Limitations: single-instance or cluster of 3 (no 5+), limited plugin support, delayed message plugin not available, no federation/shovel to external brokers, slower to get new RabbitMQ versions. Good for simple workloads; for advanced, self-host or CloudAMQP.",
  ["rabbitmq", "expert", "aws-mq"])

c("Expert",
  "What is <b>queue federation</b> for WAN deployments?",
  "The <code>rabbitmq_federation</code> plugin connects queues across distant brokers (different DCs). Upstream messages are consumed and replicated downstream. Provides eventual consistency, WAN-tolerant (withstands latency). Use Federation for cross-DC deployments where full clustering (low-latency LAN) isn't possible.",
  ["rabbitmq", "expert", "wan", "federation"])

c("Expert",
  "What is the <b>management API</b> throttling and how to avoid it?",
  "Frequent polling of <code>/api/queues</code> or <code>/api/overview</code> can overload the management plugin. Use <b>Prometheus metrics</b> for high-frequency monitoring instead. Rate-limit API calls; use <code>disable_stats</code> or <code>rates_mode=none</code> on specific queues to reduce overhead.",
  ["rabbitmq", "expert", "management-api-throttle"])

c("Expert",
  "What are <b>custom exchange types</b> and how to write one?",
  "Implement an Erlang behaviour (<code>rabbit_exchange_type</code>). Must implement callbacks: <code>description/0</code>, <code>serialise_events/0</code>, <code>route/2</code> (message routing logic), <code>validate/1</code>, <code>create/2</code>, <code>delete/3</code>, <code>policy_changed/3</code>, <code>add_binding/3</code>, <code>remove_bindings/3</code>. Compile as a plugin. Then use via <code>exchange_declare</code>.",
  ["rabbitmq", "expert", "custom-exchange"])

c("Expert",
  "What is <b>Raft consensus</b> in the context of quorum queues?",
  "Raft is a distributed consensus algorithm. In a quorum queue cluster:<br>1. One node is the <b>leader</b> (all writes go through it).<br>2. Others are <b>followers</b> (replicate the log).<br>3. A write is committed only when a <b>majority</b> (quorum) of nodes have written it to disk.<br>4. If the leader fails, followers hold an election to choose a new leader.<br>This ensures data consistency even with node failures.",
  ["rabbitmq", "expert", "raft"])

c("Expert",
  "How does <b>stream deduplication</b> work in RabbitMQ Streams?",
  "Publishers include a <b>publisher ID</b> and per-publisher <b>sequence number</b> on each message. The broker tracks the last sequence per publisher. If a message arrives with a sequence ≤ last committed sequence, it's discarded. Provides <b>exactly-once publish semantics</b> at the protocol level.",
  ["rabbitmq", "expert", "stream-dedup"])

c("Expert",
  "How to design a <b>dead letter strategy</b> for production?",
  "1. All work queues → DLX to a central DLQ.<br>2. Monitor DLQ depth (alert if > 0).<br>3. Add <b>retry count</b> header; only DLQ after N retries.<br>4. Use <b>delay</b> between retries (retry TTL queue → back to work queue).<br>5. Have an inspection tool to view, fix, and re-publish DLQ messages.<br>6. Never silently discard messages — at least log them.",
  ["rabbitmq", "expert", "dead-letter-strategy"])

c("Expert",
  "Explain <b>publisher confirms + mandatory</b> for guaranteed delivery.",
  "<b>Publisher confirms</b>: broker sends <code>basic.ack</code> (routed to all queues) or <code>basic.nack</code> for each published message. Publisher must buffer unconfirmed messages for retry.<br><b>Mandatory=True</b>: if message can't be routed to any queue, broker sends <code>basic.return</code> instead of ack.<br>Together: guarantees message is either routed and confirmed, or returned to publisher — no silent loss.",
  ["rabbitmq", "expert", "publisher-confirms-mandatory"])

# ─── Build and export ──────────────────────────────────────────────────────

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
