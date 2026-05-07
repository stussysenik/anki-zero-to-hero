import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Redis"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "DataTypes":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Data-Types"),
    "Commands":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Commands"),
    "Persistence":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Persistence-Reliability"),
    "PubSub":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-PubSub-Streams"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Advanced-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ============================================================
# 01 — Fundamentals (L0 Primitives)
# ============================================================

c("Fundamentals",
  "What is Redis?",
  "Redis (REmote DIctionary Server) is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It stores all data in RAM for sub-millisecond latency and supports strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, and streams.",
  ["fundamentals", "L0"])

c("Fundamentals",
  "How does Redis handle concurrency?",
  "Redis is <b>single-threaded</b> (main event loop) — it processes one command at a time using an I/O multiplexing mechanism (epoll/kqueue). This eliminates race conditions on in-memory data structures. Threads are used only for I/O (since Redis 6) and certain module operations (e.g. BGSAVE fork).",
  ["fundamentals", "L0", "concurrency"])

c("Fundamentals",
  "What is the key-value model in Redis?",
  "Redis is a key-value store where every key maps to a value of a specific data type. Keys are binary-safe strings up to 512 MB. Values can be strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, or streams. The key is the lookup handle; the value type determines the operations available.",
  ["fundamentals", "L0", "key-value"])

c("Fundamentals",
  "What are the two main persistence mechanisms in Redis?",
  "<b>RDB (Redis Database)</b>: Point-in-time snapshots of the dataset at specified intervals, written as a compact binary file.<br><b>AOF (Append-Only File)</b>: Logs every write operation received by the server, replayable on restart. Can be used together; Redis 4+ supports <b>mixed mode</b> (RDB + AOF tail).",
  ["fundamentals", "L0", "persistence"])

c("Fundamentals",
  "What are the primary use cases for Redis?",
  "1. <b>Cache</b> — sub-millisecond reads, TTL-based expiry<br>2. <b>Session store</b> — centralized, shared session data<br>3. <b>Message broker</b> — Pub/Sub and Streams<br>4. <b>Rate limiter</b> — atomic INCR with windowing<br>5. <b>Leaderboard</b> — Sorted Sets with O(log N) ranking<br>6. <b>Job queue</b> — Lists or Streams with consumer groups<br>7. <b>Distributed lock</b> — SET NX PX<br>8. <b>Real-time analytics</b> — HyperLogLog, bitmaps",
  ["fundamentals", "L0", "use-cases"])

c("Fundamentals",
  "How does Redis compare to Memcached?",
  "<b>Redis</b>: Rich data types (strings, hashes, lists, sets, sorted sets, streams), persistence (RDB/AOF), replication, clustering, Lua scripting, pub/sub, transactions, TTL per key, maxmemory eviction policies.<br><b>Memcached</b>: Strings only, no persistence, no replication (native), multi-threaded, simpler design, slightly lower per-core memory overhead.",
  ["fundamentals", "L0", "comparison"])

c("Fundamentals",
  "How does Redis compare to MongoDB/PostgreSQL?",
  "Redis is <b>in-memory first</b> — all data lives in RAM (persistence is secondary). MongoDB/PostgreSQL are <b>disk-first</b> — data lives on disk with memory as cache. Redis is single-threaded, optimized for simple operations at extreme throughput (~100k ops/s). MongoDB/PostgreSQL support complex queries, joins, transactions, and schemas. Use Redis for caching and real-time; use MongoDB/PostgreSQL for durable, query-heavy workloads.",
  ["fundamentals", "L0", "comparison"])

c("Fundamentals",
  "What is the RESP protocol?",
  "RESP (REdis Serialization Protocol) is the wire protocol used between Redis clients and servers. It uses human-readable prefixes:<br><code>+</code> Simple String<br><code>-</code> Error<br><code>:</code> Integer<br><code>$</code> Bulk String<br><code>*</code> Array<br>Example: <code>*3\\r\\n$3\\r\\nSET\\r\\n$3\\r\\nkey\\r\\n$5\\r\\nvalue\\r\\n</code>",
  ["fundamentals", "L0", "protocol"])

c("Fundamentals",
  "What is the Redis Modules system?",
  "Redis Modules allow extending Redis with new data types and commands using the C API. Modules are loaded at startup via <code>--loadmodule</code> or the <code>MODULE LOAD</code> command. Popular modules: RediSearch (full-text), RedisJSON (JSON docs), RedisTimeSeries, RedisBloom, RedisGraph, RedisGears, RedisAI.",
  ["fundamentals", "L0", "modules"])

c("Fundamentals",
  "What are Redis OSS, Redis Stack, Valkey, and KeyDB?",
  "<b>Redis OSS</b>: The open-source core (BSD-licensed, pre-7.4).<br><b>Redis Stack</b>: Redis OSS + bundled modules (Search, JSON, Timeseries, Bloom, Graph).<br><b>Valkey</b>: A Linux Foundation fork of Redis 7.2.4, BSD-licensed, community-governed replacement after the license change.<br><b>KeyDB</b>: A multi-threaded fork of Redis, focused on higher throughput on multi-core machines.",
  ["fundamentals", "L0", "ecosystem"])

c("Fundamentals",
  "What does 'in-memory' really mean for Redis and what are the implications?",
  "All data is stored in RAM for sub-millisecond access. Implications:<br><b>Pro</b>: Extremely fast reads/writes, predictable latency.<br><b>Con</b>: Dataset size limited by available RAM. Data can be lost on crash if persistence is disabled (default). Persistence (RDB/AOF) mitigates but adds latency and CPU overhead. Eviction policies manage memory pressure via <code>maxmemory</code>.",
  ["fundamentals", "L0", "in-memory"])

c("Fundamentals",
  "What is Redis' default port and how is it configured?",
  "Default port: <b>6379</b> (from MERZ on a phone keypad — the name of an Italian showgirl). Configured via <code>redis.conf</code> with <code>port 6379</code> or command-line <code>--port</code>. TLS-enabled Redis typically uses port <b>6380</b>. Cluster bus uses port <b>16379</b> (data port + 10000).",
  ["fundamentals", "L0", "configuration"])

c("Fundamentals",
  "What are the Redis configuration options for security?",
  "<code>requirepass</code> — Set a password for AUTH<br><code>rename-command</code> — Disable or rename dangerous commands (e.g. <code>CONFIG</code>, <code>FLUSHALL</code>)<br><code>bind</code> — Restrict network interfaces<br><code>protected-mode</code> — Reject non-local connections without password<br><code>tls-port</code> / <code>tls-cert-file</code> — Enable TLS encryption<br><code>aclfile</code> — Use ACL rules (Redis 6+)",
  ["fundamentals", "L0", "security"])

c("Fundamentals",
  "What is Redis Sentinel?",
  "Redis Sentinel is a distributed system for monitoring Redis instances, performing automatic failover, and providing service discovery. It requires at least 3 Sentinel nodes for quorum. Sentinel does <b>not</b> shard data — it provides high availability for a single primary-replica setup.",
  ["fundamentals", "L0", "sentinel"])

c("Fundamentals",
  "What is Redis Cluster?",
  "Redis Cluster provides <b>horizontal scaling</b> by sharding data across 16384 hash slots distributed among nodes. Each node holds a subset of slots. Clients use <code>CRC16(key) % 16384</code> to route commands. Cluster provides automatic failover via replicas. Requires at least 3 primary nodes. Supports cross-slot operations only if keys hash to the same slot (hash tags <code>{key}</code>).",
  ["fundamentals", "L0", "cluster"])

# ============================================================
# 02 — Data Types
# ============================================================

# Strings
c("DataTypes",
  "What are Redis Strings and what operations do they support?",
  "Strings are the most basic Redis type — binary-safe up to 512 MB. Key operations:<br><code>SET key value [EX sec|PX ms|NX|XX]</code> — Set with optional TTL<br><code>GET key</code> — Retrieve value<br><code>SETNX key value</code> — Set only if key doesn't exist<br><code>SETEX key seconds value</code> — Set with TTL<br><code>INCR key</code> / <code>DECR key</code> — Atomic increment/decrement by 1<br><code>INCRBY key N</code> / <code>INCRBYFLOAT key N</code> — Atomic increment/decrement by N<br><code>APPEND key value</code> — Append to existing string<br><code>GETRANGE key start end</code> — Substring<br><code>SETRANGE key offset value</code> — Overwrite at position<br><code>MGET k1 k2 ...</code> / <code>MSET k1 v1 k2 v2 ...</code> — Batch operations<br><code>STRLEN key</code> — String length",
  ["data-types", "L1", "strings"])

c("DataTypes",
  "How does INCR work in Redis and why is it atomic?",
  "<code>INCR key</code> reads the integer value, increments by 1, and writes it back — all within a single command execution. Because Redis is single-threaded, no other command can interleave between the read and write. This makes INCR (and DECR, INCRBY, INCRBYFLOAT) safe for distributed counters without locks.",
  ["data-types", "L1", "strings", "atomic"])

c("DataTypes",
  "What is SETNX and how is it used for locking?",
  "<code>SETNX key value</code> — Sets the key to value <b>only if the key does not already exist</b>. Returns 1 if set, 0 if key already existed. Used as a primitive for distributed locking. Now often replaced by <code>SET key value NX PX 30000</code> which combines SETNX + TTL in one atomic operation for lock expiry.",
  ["data-types", "L1", "strings", "locking"])

c("DataTypes",
  "What is GETSET and what is its modern replacement?",
  "<code>GETSET key value</code> atomically sets a key to a new value and returns the old value. Deprecated in Redis 6.2.0, removed in 7.0.0. Modern replacement: <code>SET key value GET</code> which performs the same atomic get-and-set. Use <code>SET key value GET EX 300</code> to combine with TTL.",
  ["data-types", "L1", "strings"])

# Hashes
c("DataTypes",
  "What are Redis Hashes and when should you use them?",
  "Hashes map field-value pairs under a single key — like a dictionary within a key. Ideal for representing objects (user profiles, configuration). Key commands:<br><code>HSET key field value [field value ...]</code> — Set one or more fields<br><code>HGET key field</code> — Get a field's value<br><code>HMSET</code> / <code>HMGET key field [field ...]</code> — Batch set/get (HMSET deprecated in 4.0, use HSET)<br><code>HGETALL key</code> — Get all fields and values (O(N), caution on large hashes)<br><code>HDEL key field [field ...]</code> — Delete fields<br><code>HEXISTS key field</code> — Check if field exists<br><code>HINCRBY key field N</code> — Increment numeric field<br><code>HKEYS</code> / <code>HVALS</code> — Get all field names or values<br><code>HLEN key</code> — Number of fields",
  ["data-types", "L1", "hashes"])

c("DataTypes",
  "What is the memory encoding optimization for small Hashes?",
  "Small hashes (<= 512 fields, each field/value <= 64 bytes in Redis 7.0+) are stored as a <b>listpack</b> (previously ziplist) — a contiguous memory block instead of a hash table. This saves memory by eliminating pointer overhead. When the hash grows beyond these thresholds, it is transcoded to a regular hash table.",
  ["data-types", "L1", "hashes", "encoding"])

# Lists
c("DataTypes",
  "What are Redis Lists and what are their key commands?",
  "Lists are doubly-linked lists of strings, ordered by insertion. Key commands:<br><code>LPUSH key v1 v2 ...</code> — Prepend (left-push) one or more<br><code>RPUSH key v1 v2 ...</code> — Append (right-push) one or more<br><code>LPOP key</code> / <code>RPOP key [count]</code> — Remove from left/right, count supported in 6.2+<br><code>LRANGE key start stop</code> — Range query (0 -1 = all)<br><code>LLEN key</code> — List length<br><code>LINDEX key index</code> — Element at position<br><code>LINSERT key BEFORE|AFTER pivot value</code> — Insert relative to element<br><code>LREM key count value</code> — Remove N occurrences<br><code>LTRIM key start stop</code> — Trim to range<br><code>BLPOP key [key ...] timeout</code> / <code>BRPOP ...</code> — Blocking pop (0 = infinite)",
  ["data-types", "L1", "lists"])

c("DataTypes",
  "How do blocking list commands (BLPOP/BRPOP) work?",
  "<code>BLPOP key1 key2 ... timeout</code> blocks the connection until a value can be popped from the head of one of the given lists, or until the timeout expires. If multiple keys are specified, they are checked in order. If timeout is 0, it blocks indefinitely. This is the basis of simple blocking job queues (producer RPUSH, consumer BLPOP). Multiple blocking clients are served in FIFO order when data arrives.",
  ["data-types", "L1", "lists", "blocking"])

c("DataTypes",
  "What is the internal encoding of Redis Lists?",
  "Lists use <b>quicklist</b> — a doubly-linked list of <b>listpack</b> nodes. Each listpack node holds multiple elements (default ~8 KB per node). This balances: fast head/tail access (linked list property) with memory efficiency and cache locality (listpack property). Prior to quicklist (Redis 3.2), lists used either ziplist or linkedlist.",
  ["data-types", "L1", "lists", "encoding"])

# Sets
c("DataTypes",
  "What are Redis Sets and what are their key commands?",
  "Sets are unordered collections of unique strings. Key commands:<br><code>SADD key member [member ...]</code> — Add members<br><code>SREM key member [member ...]</code> — Remove members<br><code>SMEMBERS key</code> — Get all members (O(N), avoid on large sets)<br><code>SISMEMBER key member</code> — Check membership (O(1))<br><code>SCARD key</code> — Cardinality (count)<br><code>SINTER key1 key2 ...</code> — Intersection<br><code>SUNION key1 key2 ...</code> — Union<br><code>SDIFF key1 key2 ...</code> — Difference (members in key1 not in others)<br><code>SRANDMEMBER key [N]</code> — Random member(s)<br><code>SPOP key [N]</code> — Remove and return random member(s)<br><code>SMOVE source dest member</code> — Move between sets atomically",
  ["data-types", "L1", "sets"])

c("DataTypes",
  "What is a common use case for Redis Set operations (SINTER, SUNION, SDIFF)?",
  "<b>SINTER</b>: Shared interests / mutual friends between user sets.<br><b>SUNION</b>: All unique visitors across multiple days, combine tags.<br><b>SDIFF</b>: Users who visited yesterday but not today (churn).<br><b>SUNIONSTORE</b> / <b>SINTERSTORE</b> / <b>SDIFFSTORE</b>: Store the result in a destination set to avoid recomputation. All are O(N*M) where N is smallest set and M is number of sets.",
  ["data-types", "L1", "sets"])

c("DataTypes",
  "What is the difference between SRANDMEMBER and SPOP?",
  "<code>SRANDMEMBER key [N]</code> returns random member(s) <b>without removing</b> them from the set. With negative N, may return duplicates (sampling with replacement).<br><code>SPOP key [N]</code> returns and <b>removes</b> random member(s). Atomic remove-and-return. Useful for random work queues, selecting a random item to process, or building a non-repeating shuffle.",
  ["data-types", "L1", "sets"])

# Sorted Sets
c("DataTypes",
  "What are Redis Sorted Sets and what are their key commands?",
  "Sorted Sets (ZSets) are sets where each member has a <b>score</b> (double) that determines ordering. Members are unique; scores may repeat (ordered lexicographically on tie). Key commands:<br><code>ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [... ]</code> — Add with score<br><code>ZRANGE key min max [BYSCORE|BYLEX] [REV] [WITHSCORES]</code> — Range by rank, score, or lex<br><code>ZREVRANGE key start stop [WITHSCORES]</code> — Reverse range (deprecated in 6.2, use ZRANGE ... REV)<br><code>ZRANGEBYSCORE key min max</code> — By score range<br><code>ZREM key member [...]</code> — Remove members<br><code>ZCARD key</code> — Cardinality<br><code>ZCOUNT key min max</code> — Count by score range<br><code>ZRANK key member</code> / <code>ZREVRANK key member</code> — 0-based rank<br><code>ZSCORE key member</code> — Get score<br><code>ZINCRBY key INCR member</code> — Increment score<br><code>ZPOPMIN</code> / <code>ZPOPMAX key [count]</code> — Pop lowest/highest scored<br><code>ZINTERSTORE</code> / <code>ZUNIONSTORE</code> — Intersection/union with score aggregation",
  ["data-types", "L1", "sorted-sets"])

c("DataTypes",
  "How are Sorted Sets used for leaderboards?",
  "Store <code>ZADD leaderboard score player_id</code> for each player. Use <code>ZREVRANGE leaderboard 0 9 WITHSCORES</code> for top 10. Use <code>ZRANK leaderboard player_id</code> for a player's position. Use <code>ZINCRBY leaderboard 10 player_id</code> to add score. Use <code>ZSCORE leaderboard player_id</code> to check exact score. All operations are O(log(N)).",
  ["data-types", "L1", "sorted-sets", "leaderboard"])

c("DataTypes",
  "What is the internal encoding of Sorted Sets?",
  "Sorted Sets use a <b>skiplist + hash table</b> combination. The skiplist provides O(log N) range queries and rank lookups. The hash table provides O(1) score lookup by member. Small sorted sets (<= 128 elements) use <b>listpack</b> encoding for memory efficiency and are transcoded to skiplist on growth.",
  ["data-types", "L1", "sorted-sets", "encoding"])

c("DataTypes",
  "What are ZPOPMIN and ZPOPMAX used for?",
  "<code>ZPOPMIN key [count]</code> removes and returns the member(s) with the <b>lowest score(s)</b>. <code>ZPOPMAX key [count]</code> removes and returns the member(s) with the <b>highest score(s)</b>. These are atomic pop operations, useful for priority queues — BZPOPMIN/BZPOPMAX add blocking versions for consumer-producer patterns.",
  ["data-types", "L1", "sorted-sets", "priority-queue"])

# Bitmaps
c("DataTypes",
  "What are Redis Bitmaps and what commands operate on them?",
  "Bitmaps are not a separate type — they operate on Strings as bit arrays. Each string can hold up to 2^32 bits (~512 MB). Commands:<br><code>SETBIT key offset value</code> — Set bit at offset (0 or 1)<br><code>GETBIT key offset</code> — Get bit at offset<br><code>BITCOUNT key [start end]</code> — Count set bits (population count)<br><code>BITOP AND|OR|XOR|NOT dest key1 key2 [...]</code> — Bitwise operations between strings<br><code>BITPOS key bit [start end]</code> — Position of first 0 or 1<br><code>BITFIELD key GET|SET|INCRBY type offset [OVERFLOW]</code> — Treat string as array of integers",
  ["data-types", "L1", "bitmaps"])

c("DataTypes",
  "What are common use cases for Redis Bitmaps?",
  "1. <b>User online tracking</b>: <code>SETBIT online:2024-01-01 user_id 1</code> — 1 bit per user per day<br>2. <b>A/B testing flags</b>: <code>SETBIT experiment:A user_id 1</code><br>3. <b>Bloom filters</b> (manual): Multiple hash SETBITs + GETBIT checks<br>4. <b>Attendance tracking</b>: Monthly attendance with 1 bit per day<br>5. <b>Feature flags</b>: Per-user feature toggles with O(1) lookup<br>6. <b>Bit-level counters</b>: BITFIELD for small integer arrays (e.g. game inventory)",
  ["data-types", "L1", "bitmaps"])

# HyperLogLog
c("DataTypes",
  "What is Redis HyperLogLog and what are its commands?",
  "HyperLogLog (HLL) is a probabilistic data structure for counting <b>unique elements</b> (cardinality estimation). It uses ~12 KB of memory per key regardless of the number of elements, with a standard error of ~0.81%. Commands:<br><code>PFADD key element [element ...]</code> — Add elements<br><code>PFCOUNT key [key ...]</code> — Estimated cardinality<br><code>PFMERGE dest key1 key2 [...]</code> — Merge multiple HLLs into one",
  ["data-types", "L1", "hyperloglog"])

c("DataTypes",
  "When should you use HyperLogLog vs a Set for counting unique items?",
  "Use <b>HLL</b> when approximate counts are acceptable and memory is a concern (e.g., counting unique daily visitors over years — <code>PFADD daily:2024-01-01 user_id</code>). HLL uses fixed 12 KB vs set which grows linearly with items.<br>Use <b>Set</b> when exact counts are required and you need to retrieve actual members (<code>SISMEMBER</code>). HLL cannot answer 'is this element present?' — it only estimates count.",
  ["data-types", "L1", "hyperloglog"])

# Geospatial
c("DataTypes",
  "What are Redis Geospatial indexes and their commands?",
  "Geospatial indexes store longitude/latitude coordinates (WGS84) in Sorted Sets. Commands:<br><code>GEOADD key lon lat member [lon lat member ...]</code> — Add locations<br><code>GEODIST key m1 m2 [m|km|ft|mi]</code> — Distance between members<br><code>GEORADIUS key lon lat radius unit [WITHDIST] [WITHCOORD] [ASC|DESC] [COUNT N]</code> — Members within radius (deprecated, use GEOSEARCH)<br><code>GEORADIUSBYMEMBER key member radius unit</code> — Radius from existing member<br><code>GEOHASH key member [member ...]</code> — Geohash string<br><code>GEOPOS key member [member ...]</code> — Longitude/latitude<br><code>GEOSEARCH key [FROMMEMBER m|FROMLONLAT lon lat] [BYRADIUS r|BYBOX w h] unit</code> — Generic search (6.2+)",
  ["data-types", "L1", "geospatial"])

c("DataTypes",
  "What is the underlying data structure for Geospatial indexes?",
  "Geospatial indexes are stored as <b>Sorted Sets</b>. Each member's score is the <b>Geohash</b> (a 52-bit integer encoding of lat/lon via Z-order curve interleaving). GEOADD is essentially ZADD with a geohash-encoded score. This means all Sorted Set operations (ZRANGE, ZREM, etc.) work on geo keys, and geospatial queries are range queries on the geohash score.",
  ["data-types", "L1", "geospatial", "encoding"])

# Streams
c("DataTypes",
  "What are Redis Streams and what are their key commands?",
  "Streams are an append-only log data structure (introduced in Redis 5.0) for message queuing and event sourcing. Each entry has a unique ID (milliseconds-sequencenumber) and a set of field-value pairs. Key commands:<br><code>XADD key [NOMKSTREAM] [MAXLEN|MINID] ID field value [...]</code> — Add entry<br><code>XREAD [COUNT N] [BLOCK ms] STREAMS key [...] ID [...]</code> — Read from streams<br><code>XREADGROUP GROUP group consumer [COUNT N] [BLOCK ms] STREAMS key [key ...] ID [ID ...]</code> — Read as consumer group<br><code>XRANGE key start end [COUNT N]</code> — Range by ID<br><code>XREVRANGE key end start [COUNT N]</code> — Reverse range<br><code>XLEN key</code> — Stream length<br><code>XDEL key id [id ...]</code> — Delete entries<br><code>XTRIM key MAXLEN|MINID [=~] threshold</code> — Trim stream<br><code>XACK key group id [id ...]</code> — Acknowledge message<br><code>XGROUP CREATE|DESTROY|CREATECONSUMER|DELCONSUMER|SETID</code> — Consumer group management<br><code>XCLAIM</code> / <code>XINFO</code> / <code>XPENDING</code> — Advanced group ops",
  ["data-types", "L1", "streams"])

c("DataTypes",
  "How do Stream Consumer Groups work?",
  "Consumer groups allow multiple consumers to read from the same stream cooperatively — each message is delivered to exactly one consumer in the group. Key concepts:<br>1. <code>XGROUP CREATE stream group $|0 MKSTREAM</code> — Create group<br>2. Consumers read with <code>XREADGROUP</code> — each gets unique messages<br>3. Messages enter <b>pending entries list (PEL)</b> until <code>XACK</code> is sent<br>4. <code>XCLAIM</code> allows one consumer to take over unacknowledged messages from another (failure recovery)<br>5. <code>XPENDING</code> inspects pending messages<br>This provides <b>at-least-once delivery</b> semantics.",
  ["data-types", "L1", "streams", "consumer-groups"])

c("DataTypes",
  "What is the format of Stream entry IDs?",
  "Stream IDs are in the format <code>millisecondsTime-sequenceNumber</code> (e.g. <code>1518951480106-0</code>). The time part is the Redis server's local time in milliseconds. The sequence number is for ordering entries within the same millisecond. The special ID <code>*</code> tells Redis to auto-generate the ID. The minimum valid ID is <code>0-1</code>. Use <code>$</code> in XREAD to get only new entries.",
  ["data-types", "L1", "streams"])

c("DataTypes",
  "What is XTRIM and how does approximate trimming work?",
  "<code>XTRIM key MAXLEN ~ 1000</code> trims the stream to approximately 1000 entries. The <code>~</code> flag makes trimming <b>approximate</b> (more efficient — removes whole macro nodes) vs exact trimming (removes entry by entry). <code>MINID</code> trims entries older than a given ID. Use XADD with <code>MAXLEN ~ N</code> to cap stream size on every write, preventing unbounded growth.",
  ["data-types", "L1", "streams"])

# ============================================================
# 03 — Commands (Key Management & Administration)
# ============================================================

c("Commands",
  "What are the key TTL/expiry commands in Redis?",
  "<code>EXPIRE key seconds [NX|XX|GT|LT]</code> — Set TTL in seconds<br><code>PEXPIRE key ms [NX|XX|GT|LT]</code> — Set TTL in milliseconds<br><code>EXPIREAT key unix-time-sec [NX|XX|GT|LT]</code> — Expire at Unix timestamp (sec)<br><code>PEXPIREAT key unix-time-ms [NX|XX|GT|LT]</code> — Expire at Unix timestamp (ms)<br><code>TTL key</code> — Remaining seconds (-1 no expiry, -2 key doesn't exist)<br><code>PTTL key</code> — Remaining milliseconds<br><code>PERSIST key</code> — Remove expiry, make key persistent<br>Flag options: <code>NX</code> — Set only if no expiry; <code>XX</code> — Set only if has expiry; <code>GT</code> — Set only if new TTL > current; <code>LT</code> — Set only if new TTL < current",
  ["commands", "L1", "ttl"])

c("Commands",
  "What is the difference between DEL and UNLINK?",
  "<code>DEL key [key ...]</code> synchronously deletes keys — blocks the event loop until all memory is freed. Can cause latency spikes with large keys (big lists, sets, hashes).<br><code>UNLINK key [key ...]</code> (Redis 4+) asynchronously deletes keys — marks them as deleted immediately (key disappears from namespace), but defers memory reclamation to a background thread. Use UNLINK for large keys to avoid blocking.",
  ["commands", "L1", "key-management"])

c("Commands",
  "What is EXISTS and how does it work with multiple keys?",
  "<code>EXISTS key [key ...]</code> returns the number of keys that exist. Example: <code>EXISTS k1 k2 k3</code> might return 2 if only k1 and k3 exist. Introduced in Redis 3.0.3; before that it returned 1/0 for a single key. Use to test key presence without fetching the value.",
  ["commands", "L1", "key-management"])

c("Commands",
  "What is the SCAN command and how does it differ from KEYS?",
  "<code>KEYS pattern</code> blocks the server while scanning the entire keyspace — <b>never use in production</b> on large databases.<br><code>SCAN cursor [MATCH pattern] [COUNT N] [TYPE type]</code> iterates using a cursor, returning a batch of keys each call. Non-blocking, safe for production. Use 0 as initial cursor; repeat until cursor returns 0. Family: <code>SSCAN</code> (sets), <code>HSCAN</code> (hashes), <code>ZSCAN</code> (sorted sets).<br>SCAN may return duplicates (keys added/removed during iteration) — client must deduplicate.",
  ["commands", "L1", "scan"])

c("Commands",
  "How does the SCAN cursor work and what guarantees does it provide?",
  "SCAN uses a cursor-based iteration over the hash table backing the keyspace. Each call returns a new cursor and a batch of keys. The cursor is opaque (not an index). SCAN may return 0 keys on some calls (if all keys in the scanned slot disappeared). It may return the same key multiple times (if rehashing). <b>COUNT</b> is a hint, not a hard limit — Redis may return more or fewer keys. SCAN guarantees that keys present for the entire iteration are returned at least once.",
  ["commands", "L1", "scan"])

c("Commands",
  "What is the INFO command and what are its sections?",
  "<code>INFO [section]</code> returns comprehensive server statistics and information. Key sections:<br><code>server</code> — Redis version, OS, uptime, mode<br><code>clients</code> — Connected clients, blocked clients<br><code>memory</code> — used_memory, RSS, fragmentation ratio, maxmemory<br><code>persistence</code> — RDB status, AOF status<br><code>stats</code> — Total connections, commands processed, keyspace hits/misses, evictions<br><code>replication</code> — Role (master/replica), connected replicas, replication offset<br><code>cpu</code> — CPU usage<br><code>commandstats</code> — Per-command call counts and CPU<br><code>cluster</code> — Cluster status<br><code>keyspace</code> — Keys per database, keys with expiry<br>Default (no section) returns all sections.",
  ["commands", "L1", "info"])

c("Commands",
  "What is CONFIG GET / SET / REWRITE?",
  "<code>CONFIG GET pattern</code> — Read runtime configuration parameters matching glob pattern (e.g. <code>CONFIG GET *maxmemory*</code>).<br><code>CONFIG SET parameter value</code> — Change configuration at runtime without restart (not all params are changeable at runtime).<br><code>CONFIG REWRITE</code> — Persist the current runtime configuration to <code>redis.conf</code>, preserving comments and structure. Essential after runtime CONFIG SET changes.",
  ["commands", "L1", "config"])

c("Commands",
  "What are the CLIENT commands for connection management?",
  "<code>CLIENT LIST [TYPE normal|master|replica|pubsub]</code> — List connected clients with details (id, addr, fd, name, age, idle, flags, db, cmd).<br><code>CLIENT GETNAME</code> / <code>CLIENT SETNAME name</code> — Get/set client connection name.<br><code>CLIENT KILL ip:port|ID id|TYPE type|ADDR ip:port|USER user|SKIPME yes/no</code> — Terminate client connection(s).<br><code>CLIENT PAUSE timeout [WRITE|ALL]</code> — Pause command processing for timeout ms (used during failover).<br><code>CLIENT NO-EVICT on|off</code> — Protect client from eviction under maxmemory.",
  ["commands", "L1", "client"])

c("Commands",
  "What is the MONITOR command and why should it be used carefully?",
  "<code>MONITOR</code> streams every command processed by the Redis server to the client — a real-time debugging tool. <b>Dangers</b>: (1) MONITOR itself increases memory usage (buffers output), (2) it adds latency to every command, (3) on high-throughput instances it can reduce throughput by ~50%, (4) sensitive data may be exposed. Never run MONITOR continuously in production.",
  ["commands", "L1", "monitor"])

c("Commands",
  "What is the SLOWLOG and how is it configured?",
  "<code>SLOWLOG</code> records commands that exceed a configurable execution time threshold. Commands:<br><code>SLOWLOG GET [N]</code> — Retrieve N most recent slow entries<br><code>SLOWLOG LEN</code> — Number of entries<br><code>SLOWLOG RESET</code> — Clear log<br>Config:<br><code>slowlog-log-slower-than 10000</code> — Microseconds threshold (0 = log all, -1 = disable)<br><code>slowlog-max-len 128</code> — Max entries (FIFO circular buffer)<br>Each entry: ID, timestamp, duration (μs), command array, client IP:port, client name.",
  ["commands", "L1", "slowlog"])

c("Commands",
  "What are the MEMORY related commands in Redis?",
  "<code>MEMORY USAGE key [SAMPLES N]</code> — Memory in bytes used by a key and its value (sampling for nested types).<br><code>MEMORY STATS</code> — Detailed memory breakdown (allocator stats, RSS, overhead, startup, dataset).<br><code>MEMORY DOCTOR</code> — Analyze memory usage and suggest optimizations (fragmentation, peak memory, replication backlog, client buffers).<br><code>MEMORY PURGE</code> — Ask the allocator (jemalloc) to release dirty pages back to the OS (requires jemalloc 4+).<br><code>MEMORY MALLOC-STATS</code> — Internal allocator statistics.",
  ["commands", "L1", "memory"])

c("Commands",
  "What are the LATENCY commands for diagnosing performance issues?",
  "<code>LATENCY DOCTOR</code> — Analyzes latency events and provides a human-readable report with recommendations.<br><code>LATENCY HISTOGRAM [command ...]</code> — Latency distribution histogram for specific commands or all (percentiles, microsecond buckets).<br><code>LATENCY GRAPH event</code> — ASCII-art graph of latency spikes for a specific event (command, fast-command, fork, aof-write, etc.).<br><code>LATENCY LATEST</code> — Latest latency events. <code>LATENCY RESET [event ...]</code> — Reset latency data.",
  ["commands", "L1", "latency"])

c("Commands",
  "What are COMMAND INFO, COMMAND COUNT, and COMMAND GETKEYS?",
  "<code>COMMAND</code> (Redis 2.8+) returns all commands in array form.<br><code>COMMAND INFO cmd1 cmd2 ...</code> — Returns info about specific commands (arity, flags, key positions, ACL categories).<br><code>COMMAND COUNT</code> — Total number of commands available on the server (including module commands).<br><code>COMMAND GETKEYS cmd arg1 arg2 ...</code> — Extracts the key names from a full command (useful for cluster routing).<br><code>COMMAND LIST [FILTERBY MODULE mod|ACLCAT cat|PATTERN pat]</code> — List command names (Redis 7+).",
  ["commands", "L1", "command"])

c("Commands",
  "What is the TYPE command and what does OBJECT ENCODING reveal?",
  "<code>TYPE key</code> returns the data type: <code>string</code>, <code>hash</code>, <code>list</code>, <code>set</code>, <code>zset</code>, <code>stream</code>, <code>none</code> (if key doesn't exist).<br><code>OBJECT ENCODING key</code> returns the internal encoding: <code>embstr</code> (embedded string), <code>raw</code> (raw string), <code>int</code>, <code>ziplist</code>, <code>listpack</code>, <code>quicklist</code>, <code>hashtable</code>, <code>skiplist</code>, <code>intset</code>.<br><code>OBJECT REFCOUNT key</code> — Reference count (for shared integers).<br><code>OBJECT IDLETIME key</code> — Seconds since last access.<br><code>OBJECT FREQ key</code> — Logarithmic access frequency counter (for LFU eviction).",
  ["commands", "L1", "type", "encoding"])

c("Commands",
  "What is RENAME vs RENAMENX and what is COPY?",
  "<code>RENAME key newkey</code> — Renames a key. If newkey already exists, <b>it is overwritten</b> (deleted first). O(1).<br><code>RENAMENX key newkey</code> — Renames a key <b>only if newkey does not exist</b>. Returns 0 if newkey exists (no overwrite).<br><code>COPY source dest [DB dest-db] [REPLACE]</code> — Copies the value of source to dest. By default returns 0 if dest exists; <code>REPLACE</code> flag overwrites. <code>DB</code> flag copies to a different database number (0-15).",
  ["commands", "L1", "key-management"])

c("Commands",
  "What is DUMP and RESTORE and when are they used?",
  "<code>DUMP key</code> returns a serialized, version-specific, opaque binary representation of the key's value (RDB format, no TTL info).<br><code>RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME sec] [FREQ freq]</code> reconstructs a key from DUMP output. Use for:<br>1. Migrating keys between instances (with MIGRATE)<br>2. Backup/restore of individual keys<br>3. Key migration across Redis versions (note: older versions can't read newer format)",
  ["commands", "L1", "key-management"])

c("Commands",
  "What is MOVE and what are Redis databases?",
  "<code>MOVE key db</code> moves a key to a different Redis database (numbered 0-15). Returns 1 if moved, 0 if key doesn't exist or already exists in target DB.<br>Redis databases are isolated namespaces within the same server instance — <code>SELECT 0</code> switches context. Databases share the same persistence, config, and maxmemory. <b>Not recommended for production</b> — use separate Redis instances or key prefixes instead. Redis Cluster only supports database 0.",
  ["commands", "L1", "key-management"])

c("Commands",
  "What is DEBUG OBJECT and DEBUG SLEEP?",
  "<code>DEBUG OBJECT key</code> returns low-level info: encoding, serialized length, LRU idle time, refcount.<br><code>DEBUG SLEEP seconds</code> makes the Redis server sleep (blocking) for testing timeout behavior.<br><code>DEBUG SET-ACTIVE-EXPIRE on|off</code> — Toggle active expiry loop.<br><code>DEBUG RELOAD</code> — Save RDB, flush DB, and reload from RDB.<br>DEBUG commands are dangerous — use only in development/debugging environments.",
  ["commands", "L1", "debug"])

# ============================================================
# 04 — Persistence & Reliability
# ============================================================

c("Persistence",
  "What is RDB persistence and how does SAVE differ from BGSAVE?",
  "<b>RDB</b> writes a point-in-time snapshot of the dataset to a compact binary <code>dump.rdb</code> file.<br><code>SAVE</code> — Synchronously creates the snapshot, <b>blocking</b> all other clients until complete. Not for production use.<br><code>BGSAVE</code> — Forks a child process; the child writes the RDB while the parent continues serving clients. Uses OS copy-on-write (COW). If a BGSAVE is already running, returns error (use <code>BGSAVE SCHEDULE</code> to queue).",
  ["persistence", "L2", "rdb"])

c("Persistence",
  "How does fork() and Copy-on-Write affect Redis RDB persistence?",
  "BGSAVE calls <code>fork()</code> to create a child process. The OS uses <b>Copy-on-Write (COW)</b>: parent and child share the same memory pages. When the parent modifies a page, the OS copies it for the parent; the child keeps the original. Memory overhead = pages modified during BGSAVE. If the parent writes to many keys during BGSAVE, COW overhead can double memory usage in the worst case. Ensure <code>overcommit_memory=1</code> (Linux) to allow fork when memory is tight.",
  ["persistence", "L2", "rdb", "fork"])

c("Persistence",
  "What is AOF persistence and what are the fsync policies?",
  "<b>AOF (Append-Only File)</b> logs every write operation to a file, replayable on restart. Three fsync policies (configured via <code>appendfsync</code>):<br><code>always</code> — fsync after every write. Safest (minimal data loss), slowest (~30% of Redis throughput).<br><code>everysec</code> — fsync once per second (background thread). Good balance — at most 1 second of data loss. Default and recommended.<br><code>no</code> — Let the OS decide when to fsync. Fastest, but data loss depends on OS buffer flush timing (up to ~30 seconds on Linux).",
  ["persistence", "L2", "aof"])

c("Persistence",
  "What is AOF rewrite and why is it needed?",
  "AOF grows unbounded as every write is appended. <b>AOF rewrite</b> creates a compact version of the AOF by reading the current dataset and writing the minimal set of commands to recreate it. Triggered by:<br><code>BGREWRITEAOF</code> — Manual trigger<br><code>auto-aof-rewrite-percentage 100</code> — Trigger when AOF grows 100% since last rewrite<br><code>auto-aof-rewrite-min-size 64mb</code> — Minimum AOF size to trigger<br>The rewrite is done by a child process (like BGSAVE) — non-blocking. The parent buffers new writes during rewrite and appends them when done.",
  ["persistence", "L2", "aof"])

c("Persistence",
  "What is mixed persistence mode (aof-use-rdb-preamble)?",
  "Introduced in Redis 4.0, <b>mixed mode</b> (<code>aof-use-rdb-preamble yes</code>) writes the AOF file as: <b>RDB snapshot + AOF tail</b>. The RDB portion is compact and fast to load (bulk load). The AOF tail contains operations since the last rewrite. Benefits: faster restarts (RDB portion loads quickly) + durability of AOF (tail replays recent ops). Enabled by default in Redis 5+.",
  ["persistence", "L2", "aof", "rdb"])

c("Persistence",
  "How do you choose between RDB, AOF, both, or no persistence?",
  "<b>RDB only</b>: Compact backups, fast restarts, but can lose minutes of data between snapshots. Good for cache use cases or periodic backups.<br><b>AOF only (everysec)</b>: More durable (max 1 sec loss), but file can grow large and restarts slower. Good for queued/messaging data.<br><b>RDB + AOF (mixed mode)</b>: Best of both — fast restarts via RDB portion + durability via AOF tail. Recommended for most production cases.<br><b>No persistence</b>: Maximum performance, all data lost on restart. Use for pure caching with data regeneratable from source of truth.",
  ["persistence", "L2", "tradeoffs"])

c("Persistence",
  "What are the RDB configuration parameters for automatic snapshots?",
  "Configured via <code>save</code> directives in <code>redis.conf</code>:<br><code>save 3600 1</code> — Save if at least 1 key changed in 3600 seconds<br><code>save 300 100</code> — Save if at least 100 keys changed in 300 seconds<br><code>save 60 10000</code> — Save if at least 10000 keys changed in 60 seconds<br>Set <code>save \"\"</code> to disable automatic snapshots. You can have multiple save directives; BGSAVE is triggered if ANY condition is met. Use <code>stop-writes-on-bgsave-error yes</code> to block writes if BGSAVE fails.",
  ["persistence", "L2", "rdb"])

c("Persistence",
  "How do you perform data recovery in Redis?",
  "1. Stop Redis server<br>2. Locate <code>dump.rdb</code> and/or <code>appendonly.aof</code> in the working directory (<code>dir</code> in config)<br>3. If AOF is enabled, Redis prefers the AOF file on restart<br>4. If AOF is corrupted, run <code>redis-check-aof --fix appendonly.aof</code><br>5. If RDB is corrupted, run <code>redis-check-rdb dump.rdb</code><br>6. Copy backup files to the data directory<br>7. Start Redis<br>For disaster recovery: regularly copy RDB/AOF files to a separate storage (S3, NFS, rsync) — Redis does NOT have built-in backup shipping.",
  ["persistence", "L2", "recovery"])

c("Persistence",
  "What is Redis replication and how does it work?",
  "Replication copies data from a <b>primary</b> (master) to one or more <b>replicas</b> (slaves). Process:<br>1. Replica connects, sends <code>PSYNC ? -1</code> (full sync request)<br>2. Primary forks a child to create an RDB snapshot in the background<br>3. Primary buffers all new writes in the <b>replication backlog</b><br>4. Primary sends the RDB to the replica, which loads it<br>5. Primary streams buffered writes, then enters live streaming<br>On reconnection, replicas try <b>partial resync</b> using replication offset and backlog — avoiding full resync if backlog has the missing data.",
  ["persistence", "L2", "replication"])

c("Persistence",
  "What is the replication backlog and why does its size matter?",
  "The <b>replication backlog</b> is a circular buffer (FIFO) on the primary that stores recent write commands. When a replica reconnects, the primary checks if the replica's offset is still in the backlog. If yes: <b>partial resync</b> (fast, only sends missing data). If no: <b>full resync</b> (slow, fork + RDB + transfer).<br>Configure via <code>repl-backlog-size 64mb</code> (default 1 MB, increase for high-write environments). The backlog is allocated once at startup. Size = <code>(reconnect time in seconds) * (write ops per second) * (avg command size) * 2</code> (safety margin).",
  ["persistence", "L2", "replication"])

c("Persistence",
  "What is replica lag and how do you monitor it?",
  "Replica lag is the delay between a write on the primary and its application on the replica. Monitor via <code>INFO replication</code>: subtract replica <code>offset</code> from primary <code>master_repl_offset</code>. High lag causes:<br>1. Slow network between primary and replica<br>2. Replica CPU/memory overload (can't process replication stream fast enough)<br>3. Heavy commands on replica (blocking ops)<br>4. Undersized <code>repl-backlog-size</code><br>Mitigations: expand backlog, use <code>repl-diskless-sync</code>, add more replicas, tune network.",
  ["persistence", "L2", "replication"])

c("Persistence",
  "What are Redis backup best practices?",
  "1. <b>Automate RDB backups</b>: Periodically copy dump.rdb to external storage (S3, NFS, rsync + cron)<br>2. <b>Never backup during BGSAVE/AOF rewrite</b>: Copy the RDB file only after BGSAVE completes<br>3. <b>Backup AOF as well</b>: Higher granularity recovery<br>4. <b>Test restoration regularly</b>: A backup that hasn't been tested is not a backup<br>5. <b>Use mixed mode</b> (<code>aof-use-rdb-preamble yes</code>) for easier backup + restore<br>6. <b>Keep multiple generations</b>: Not just the latest — protection against corrupted backups<br>7. <b>Monitor BGSAVE/AOF rewrite failures</b>: Set <code>stop-writes-on-bgsave-error yes</code>",
  ["persistence", "L2", "backup"])

c("Persistence",
  "What is persistence-less replication (diskless replication)?",
  "<code>repl-diskless-sync yes</code> (Redis 2.8.18+): Instead of writing an RDB to disk then sending it, the primary streams the RDB directly to replicas over the network — no intermediate disk I/O. <code>repl-diskless-sync-delay 5</code> waits 5 seconds for more replicas to request sync, then sends once (batched transfer).<br>Benefits: faster sync when disk is slow, avoids disk I/O spike. Drawback: if sync fails, must restart from scratch (no saved RDB).",
  ["persistence", "L2", "replication"])

# ============================================================
# 05 — Pub/Sub & Streams
# ============================================================

c("PubSub",
  "How does Redis Pub/Sub work?",
  "Redis Pub/Sub implements a message-passing system where publishers send messages to <b>channels</b> and subscribers receive them. Commands:<br><code>PUBLISH channel message</code> — Send a message to a channel (returns number of subscribers that received it)<br><code>SUBSCRIBE channel [channel ...]</code> — Subscribe to channels (blocking — client enters pubsub mode)<br><code>UNSUBSCRIBE [channel ...]</code> — Unsubscribe from channels<br><code>PSUBSCRIBE pattern [pattern ...]</code> — Subscribe to channels matching glob pattern (e.g. <code>news.*</code>)<br><code>PUNSUBSCRIBE [pattern ...]</code> — Unsubscribe from patterns<br><code>PUBSUB CHANNELS [pattern]</code> — List active channels<br><code>PUBSUB NUMSUB [channel ...]</code> — Subscriber count per channel<br><code>PUBSUB NUMPAT</code> — Number of pattern subscriptions",
  ["pubsub", "L2", "pubsub"])

c("PubSub",
  "What are the limitations of Redis Pub/Sub?",
  "1. <b>Fire-and-forget</b>: Messages are not persisted — if a subscriber is offline, it misses all messages. No message replay.<br>2. <b>No acknowledgment</b>: Publisher has no confirmation that subscribers received/processed the message.<br>3. <b>No delivery guarantees</b>: If a subscriber disconnects mid-message, the message is lost.<br>4. <b>Synchronous fan-out</b>: PUBLISH iterates all subscribers synchronously; a slow subscriber can delay others.<br>5. <b>No message ordering across channels</b>: Only within a single channel.<br>6. <b>Subscribers can't publish</b>: While in SUBSCRIBE mode, the client can only receive messages — not issue other commands (except UNSUBSCRIBE/PING/QUIT).",
  ["pubsub", "L2", "pubsub", "limitations"])

c("PubSub",
  "What is PSUBSCRIBE and how do glob patterns work?",
  "<code>PSUBSCRIBE news.*</code> subscribes to all channels matching the glob pattern <code>news.*</code> (e.g. <code>news.sports</code>, <code>news.weather</code>). Supported glob patterns:<br><code>?</code> — Matches exactly one character<br><code>*</code> — Matches zero or more characters<br><code>[...]</code> — Character class (e.g. <code>[abc]</code> or <code>[a-z]</code>)<br><code>\\</code> — Escape character<br>Pattern subscriptions are checked in addition to exact channel subscriptions — a message may be delivered multiple times to the same client (once per matching pattern + once for exact subscription).",
  ["pubsub", "L2", "pubsub"])

c("PubSub",
  "What is the difference between Pub/Sub and Streams for messaging?",
  "<b>Pub/Sub</b>: Fire-and-forget, no persistence, no replay, no consumer groups. Best for real-time notifications where message loss is acceptable (chat rooms, live scores, WebSocket fan-out).<br><b>Streams</b>: Persistent message log, consumer groups with acknowledgments, message replay via ID range, at-least-once delivery. Best for reliable message queuing, event sourcing, and when messages must not be lost (order processing, email delivery, audit logs).",
  ["pubsub", "L2", "streams", "comparison"])

c("PubSub",
  "How do you use Streams for event sourcing?",
  "Treat each Stream as an event log for an aggregate. Append every state-changing event with <code>XADD events:* user_id field value ...</code>. Consumers read with XREAD/XREADGROUP to rebuild state. Use <code>XADD events:user:42 * action signup email user@example.com</code>. Benefits: immutable append-only log, replayable, temporal queries with XRANGE, crash recovery by replaying from last checkpoint. Combine with consumer groups for parallel processing by event type.",
  ["pubsub", "L2", "streams", "event-sourcing"])

c("PubSub",
  "What is the pending entries list (PEL) in Streams?",
  "When a consumer reads a message via <code>XREADGROUP</code>, the message is added to that consumer's <b>pending entries list (PEL)</b>. It stays there until the consumer sends <code>XACK group id</code>. Inspect with:<br><code>XPENDING stream group [START end count] [consumer]</code> — Pending summary or detail<br><code>XCLAIM stream group consumer min-idle-time id [id ...] [IDLE ms] [TIME ms-unix-time] [RETRYCOUNT count] [FORCE] [JUSTID]</code> — Transfer ownership of pending messages to another consumer (recovery after consumer failure).<br>The PEL is the key to <b>at-least-once delivery</b> — unacknowledged messages are redeliverable.",
  ["pubsub", "L2", "streams", "pending"])

c("PubSub",
  "What is XCLAIM and how does it handle consumer failure?",
  "<code>XCLAIM</code> transfers ownership of pending messages from one consumer to another within the same consumer group. Typical recovery pattern:<br>1. Monitor consumers (heartbeats or process health)<br>2. If consumer X is dead, inspect its pending messages: <code>XPENDING stream group - + 100 X</code><br>3. Claim messages idle > threshold: <code>XCLAIM stream group Y 60000 id1 id2</code> (claim for consumer Y, idle > 60s)<br>4. Consumer Y processes and ACKs the claimed messages<br>Use <code>RETRYCOUNT</code> to track redelivery attempts and implement a dead-letter queue pattern.",
  ["pubsub", "L2", "streams", "consumer-groups"])

c("PubSub",
  "How do you use blocking XREAD for real-time stream processing?",
  "<code>XREAD BLOCK 0 STREAMS mystream $</code> blocks indefinitely until a new message arrives, then returns it. Pattern:<br>1. Start with <code>$</code> (only new messages)<br>2. On response, process the message<br>3. Record the last ID returned<br>4. Call XREAD again with <code>BLOCK 0</code> and the last ID<br>This creates a persistent, blocking consumer. For multiple consumers reading independently (fan-out), each consumer tracks its own cursor. For cooperative consumption, use consumer groups (XREADGROUP) instead.",
  ["pubsub", "L2", "streams", "blocking"])

c("PubSub",
  "What is XGROUP CREATECONSUMER and SETID used for?",
  "<code>XGROUP CREATECONSUMER stream group consumer</code> — Explicitly create a consumer within a group (consumers are auto-created on first XREADGROUP, but explicit creation allows pre-configuration).<br><code>XGROUP SETID stream group id|$</code> — Change the last-delivered-ID of a consumer group. Use <code>$</code> to start consuming from the newest message (ignores history), or <code>0</code> to consume from the beginning (replay all). Used for:<br>1. Resetting group position for replay<br>2. Skipping a range of messages<br>3. Bootstrapping a new group that should start from a specific point",
  ["pubsub", "L2", "streams", "consumer-groups"])

c("PubSub",
  "What can XINFO tell you about a Stream?",
  "<code>XINFO STREAM stream [FULL [COUNT N]]</code> — Stream overview: length, radix tree keys/nodes, last-generated ID, first/last entry, list of groups.<br><code>XINFO GROUPS stream</code> — For each consumer group: name, consumers count, pending count, last-delivered ID, entries read.<br><code>XINFO CONSUMERS stream group</code> — For each consumer: name, pending count, idle time (ms since last interaction).<br>Use XINFO for monitoring stream health, detecting stalled consumers (high idle time), and debugging consumer group behavior.",
  ["pubsub", "L2", "streams", "monitoring"])

# ============================================================
# 06 — Advanced Patterns (L3 Design)
# ============================================================

c("Patterns",
  "What is the Cache-Aside pattern?",
  "Application reads from cache first; on cache miss, reads from DB and populates cache. Writes go to DB first, then invalidate/update cache. Flow:<br>1. <code>GET key</code> → hit? return.<br>2. Miss → query DB → <code>SET key value EX 3600</code> → return.<br>3. Update: DB write → <code>DEL key</code> (invalidate) or <code>SET key new_value</code> (update).<br>Most common pattern. Application is responsible for cache population. Risk: cache stampede on miss (mitigated with locking/probabilistic recomputation).",
  ["patterns", "L3", "caching"])

c("Patterns",
  "What is the Read-Through caching pattern?",
  "Cache sits between application and database — the cache itself loads data from DB on miss (application only talks to cache). In Redis, implemented via <b>RedisGears</b> or custom proxy layers (e.g. Envoy, NGINX). Read path: <code>GET key</code> → miss? → cache fetches from DB → caches → returns. Application code is simpler (never queries DB directly), but cache logic is more complex and tightly coupled to the data model.",
  ["patterns", "L3", "caching"])

c("Patterns",
  "What is the Write-Through vs Write-Behind pattern?",
  "<b>Write-Through</b>: Application writes to cache; cache synchronously writes to DB before returning. Data is always consistent, but write latency = cache latency + DB latency.<br><b>Write-Behind (Write-Back)</b>: Application writes to cache; cache acknowledges immediately; cache <b>asynchronously</b> flushes writes to DB later. Faster writes, but risk of data loss if cache crashes before flush. Use RedisGears or custom writer threads to implement write-behind in Redis.",
  ["patterns", "L3", "caching"])

c("Patterns",
  "What is cache stampede and how do you prevent it?",
  "Cache stampede: many concurrent requests for the same expired key hit the database simultaneously, overwhelming it. Prevention strategies:<br>1. <b>Locking</b>: On miss, acquire a distributed lock (<code>SET lock:key 1 NX PX 5000</code>), only one request computes, others wait/retry<br>2. <b>Probabilistic early recomputation (PER)</b>: Before TTL expiry, with probability P = delta/TTL, recompute early. Spreads recomputation across the expiry window.<br>3. <b>External recomputation</b>: Background job refreshes cache before expiry — no request-triggered recomputation at all.<br>4. <b>TTL jitter</b>: Add random offset to TTLs so keys don't expire simultaneously.",
  ["patterns", "L3", "caching", "stampede"])

c("Patterns",
  "What is the Redlock algorithm for distributed locking?",
  "Redlock (proposed by Redis/Salvatore Sanfilippo) acquires a lock across N independent Redis instances:<br>1. Get current time T1<br>2. Try <code>SET lock:resource random_value NX PX TTL</code> on all N instances sequentially<br>3. Count how many instances granted the lock; compute elapsed time<br>4. If lock acquired on majority (N/2+1) AND elapsed < TTL: success<br>5. If fail: unlock on all instances (including those where lock wasn't acquired)<br>6. Unlock with Lua script: check <code>GET lock:resource == random_value</code> before DEL (safety — only holder can release)<br><b>Fencing tokens</b>: Monotonically increasing token from lock service included in every write to prevent split-brain.",
  ["patterns", "L3", "locking", "redlock"])

c("Patterns",
  "How do you implement a sliding window rate limiter with Redis?",
  "Use a Sorted Set where each request is a member with the current timestamp as score:<br><code>ZADD ratelimit:user123 NX timestamp timestamp</code> (NX prevents duplicate exact timestamps)<br><code>ZREMRANGEBYSCORE ratelimit:user123 0 (now - window)</code> (remove expired entries)<br><code>ZCARD ratelimit:user123</code> (count remaining = requests in window)<br>If count > limit, reject request.<br>For high-throughput, use a <b>Lua script</b> to combine all three operations atomically and avoid multiple round-trips.",
  ["patterns", "L3", "rate-limiting"])

c("Patterns",
  "How do you implement a token bucket rate limiter with Redis?",
  "Token bucket: bucket has max capacity, tokens refill at a constant rate.<br>Lua script approach:<br>1. <code>GET tokens:user123</code> (current token count) + <code>GET ts:user123</code> (last refill time)<br>2. Calculate tokens to add: <code>(now - last_refill) * refill_rate</code><br>3. <code>tokens = min(capacity, tokens + added)</code><br>4. If <code>tokens >= 1</code>: decrement, update last refill time, allow request<br>5. Else: deny<br><b>Lua script ensures atomicity</b> — no race condition between GET, calculation, and SET.",
  ["patterns", "L3", "rate-limiting"])

c("Patterns",
  "How do you implement a fixed window rate limiter with Redis?",
  "Simplest rate limiter: count requests in a fixed time window using a counter with TTL.<br><code>INCR ratelimit:user123:minute:42</code> (key includes window identifier)<br>On first increment: <code>EXPIRE ratelimit:user123:minute:42 60</code> (set TTL if new)<br>If count > limit: reject.<br><b>Edge problem</b>: Burst at window boundary — a user could make 2*limit requests in seconds by crossing the boundary. Sliding window (sorted set) or sliding window counter (current + previous window weighted by overlap) mitigate this.",
  ["patterns", "L3", "rate-limiting"])

c("Patterns",
  "How do you build a job queue with Redis?",
  "Three approaches:<br>1. <b>List-based (simple)</b>: Producer <code>RPUSH queue:jobs job_data</code>. Consumer <code>BLPOP queue:jobs 0</code> (blocking). No retries, no acknowledgments.<br>2. <b>List with reliable queue pattern</b>: <code>BRPOPLPUSH queue:jobs queue:processing 0</code> — atomically move job to processing queue. On complete: <code>LREM queue:processing 1 job</code>. On failure: move back. Enables retry.<br>3. <b>Streams with consumer groups (robust)</b>: <code>XADD queue:jobs * data json</code>. Consumer group with multiple workers. <code>XACK</code> on completion. <code>XCLAIM</code> for failed jobs. Supports at-least-once delivery, retries, and dead-letter queues.<br>Bull/BullMQ libraries implement pattern 3 on Redis with rich features (delays, priorities, rate limiting, job events).",
  ["patterns", "L3", "job-queue"])

c("Patterns",
  "How do you implement a distributed counter with Redis?",
  "Use atomic increment operations on String keys:<br><code>INCR pageviews:article:42</code> — Atomic by 1<br><code>INCRBY daily:signups 1</code> — Atomic by N<br><code>HINCRBY userstats:123 login_count 1</code> — Atomic field increment in hash<br>For time-series counters (hourly/daily):<br><code>INCRBY visits:2024-01-15 1</code><br><code>EXPIRE visits:2024-01-15 259200</code> (expire after 3 days)<br>For approximate unique counts: <code>PFADD daily:visitors user_id</code> (HyperLogLog, 12 KB, ~0.81% error).",
  ["patterns", "L3", "distributed-counter"])

c("Patterns",
  "What is a Bloom Filter and how is it used with Redis?",
  "A Bloom filter is a probabilistic data structure that tests set membership: <b>definitely not present</b> or <b>possibly present</b> (no false negatives, configurable false positive rate). In Redis via <b>RedisBloom</b> module:<br><code>BF.RESERVE filter 0.01 1000000</code> — Create filter (1% error, 1M capacity)<br><code>BF.ADD filter item</code> — Add item<br><code>BF.EXISTS filter item</code> — Check (returns 0 = definitely absent, 1 = possibly present)<br>Use cases: prevent cache penetration (check bloom before DB query), username availability, fraud detection (known bad actors), web crawler (avoid re-crawling URLs).",
  ["patterns", "L3", "bloom-filter"])

c("Patterns",
  "How does RedisJSON work and what are its key commands?",
  "<b>RedisJSON</b> (module in Redis Stack) stores, updates, and queries JSON documents. Key commands:<br><code>JSON.SET key $ '{\"name\":\"Alice\",\"age\":30}'</code> — Set JSON at path<br><code>JSON.GET key [path]</code> — Get JSON or specific path<br><code>JSON.DEL key path</code> — Delete value at path<br><code>JSON.ARRAPPEND key $.items value</code> — Append to array<br><code>JSON.ARRINSERT key $.items 0 value</code> — Insert at index<br><code>JSON.NUMINCRBY key $.views 1</code> — Increment number<br><code>JSON.TYPE key path</code> — Type of value at path<br><code>JSON.STRLEN</code> / <code>JSON.ARRLEN</code> / <code>JSON.OBJLEN</code> — Length queries<br><code>JSON.MGET key [key ...] path</code> — Multi-key get<br>Useful for configuration, user profiles, content management — document model in Redis.",
  ["patterns", "L3", "json", "modules"])

c("Patterns",
  "How does RediSearch enable full-text search and indexing?",
  "<b>RediSearch</b> (module) provides secondary indexing, full-text search, and aggregations. Key commands:<br><code>FT.CREATE idx ON HASH PREFIX 1 doc: SCHEMA title TEXT WEIGHT 5.0 body TEXT description TEXT</code> — Create index on hash keys<br><code>FT.SEARCH idx \"hello world\"</code> — Full-text search with BM25 scoring<br><code>FT.AGGREGATE idx \"*\" GROUPBY 1 @category REDUCE COUNT 0 AS count</code> — Aggregation pipeline (GROUPBY, SORTBY, APPLY, FILTER, LIMIT)<br><code>FT.SUGADD autocomplete \"hello world\" 1</code> — Add suggestion for autocomplete<br><code>FT.SUGGET autocomplete \"hel\"</code> — Get suggestions<br>Supports: prefix matching, fuzzy matching, geo-filtering, numeric filters, tag filters, highlight, summarization.",
  ["patterns", "L3", "redisearch", "modules"])

c("Patterns",
  "What is RedisTimeSeries and how does it work?",
  "<b>RedisTimeSeries</b> module stores time-series data efficiently with built-in aggregation, downsampling, and retention policies. Key commands:<br><code>TS.CREATE sensor:temp:42 RETENTION 86400000 LABELS sensor_id 42 unit celsius</code> — Create series with retention (ms) and labels<br><code>TS.ADD sensor:temp:42 * 23.5</code> — Add sample (timestamp or * for auto)<br><code>TS.MADD k1 t1 v1 k2 t2 v2 ...</code> — Multi-add (single atomic operation)<br><code>TS.RANGE sensor:temp:42 from to [AGGREGATION avg 60000]</code> — Range query with optional downsampling<br><code>TS.MRANGE from to FILTER unit=celsius AGGREGATION avg 3600000</code> — Multi-series range with label filter<br><code>TS.CREATERULE src dest AGGREGATION avg 60000</code> — Auto-compaction rule (downsample src into dest)<br>Use for IoT sensor data, stock prices, monitoring metrics, API latency tracking.",
  ["patterns", "L3", "timeseries", "modules"])

c("Patterns",
  "How can Redis be used as a Vector Database for AI/ML?",
  "Redis can store and search vector embeddings for semantic search, recommendation, and RAG (Retrieval-Augmented Generation). Via <b>RedisVL</b> or RediSearch's vector similarity:<br><code>FT.CREATE docs_idx ON HASH PREFIX 1 doc: SCHEMA text TEXT embedding VECTOR HNSW 6 DIM 768 TYPE FLOAT32 DISTANCE_METRIC COSINE</code><br><code>HSET doc:1 text \"...\" embedding <byte_blob></code><br><code>FT.SEARCH docs_idx \"*=>[KNN 10 @embedding $query_vec]\" PARAMS 2 query_vec <blob> SORTBY score DESC</code> — K-nearest neighbors search<br>Supports: HNSW index, COSINE/L2/IP distance, hybrid queries (text + vector), up to billions of vectors. Redis Stack bundles this — single DB for cache + vectors + JSON + search.",
  ["patterns", "L3", "vector-db", "ai"])

c("Patterns",
  "How do you implement a session store with Redis?",
  "Store session data as a Hash keyed by session ID:<br><code>HSET session:abc123 user_id 42 username alice role admin last_access 1715123400</code><br><code>EXPIRE session:abc123 1800</code> (auto-expire after 30 min idle)<br>On each request:<br>1. <code>HGETALL session:abc123</code> (load session)<br>2. <code>HSET session:abc123 last_access now</code> + <code>EXPIRE session:abc123 1800</code> (extend TTL)<br>For <b>shared session store</b>: all app servers point to the same Redis instance — no sticky sessions needed. For <b>sticky session store</b>: each app server has its own Redis, session ID is hashed to route to the right server. Shared is simpler; sticky reduces Redis load.",
  ["patterns", "L3", "session-store"])

c("Patterns",
  "How do you implement priority queues with Sorted Sets?",
  "Use Sorted Sets where score represents priority:<br><code>ZADD priority:queue priority job_id</code> (lower score = higher priority, or negate score)<br><code>ZPOPMIN priority:queue</code> — Dequeue highest priority job (lowest score)<br><code>ZPOPMAX priority:queue</code> — Dequeue lowest priority job<br>For priority + FIFO (same priority = FIFO order): encode timestamp in the score's fractional part:<br><code>ZADD queue priority+timestamp/1e13 job_id</code><br><code>BZPOPMIN queue 0</code> — Blocking version for consumer-producer pattern. Use <code>ZRANGE</code>/<code>ZRANK</code> to inspect queue without dequeuing. Supports delayed jobs: <code>ZADD queue future_timestamp job_id</code> (only ZPOPMIN when score <= now).",
  ["patterns", "L3", "priority-queue"])

c("Patterns",
  "What is the pattern for preventing cache penetration with Redis?",
  "Cache penetration: requests for keys that don't exist in cache OR database (e.g., attack querying random non-existent product IDs). Every request hits the DB unnecessarily. Mitigations:<br>1. <b>Cache null values</b>: <code>SET nonexistent:id -1 EX 60</code> — Cache an empty marker with a short TTL<br>2. <b>Bloom Filter</b>: Pre-filter using <code>BF.EXISTS</code> — if item definitely doesn't exist in DB, reject immediately without querying DB<br>3. <b>Input validation</b>: Reject obviously invalid request patterns before cache/DB lookup<br>4. <b>Rate limiting per key pattern</b>: Throttle requests for suspicious key patterns",
  ["patterns", "L3", "caching", "cache-penetration"])

# ============================================================
# 07 — Gotchas (L4 Diagnosis)
# ============================================================

c("Gotchas",
  "Why is KEYS * dangerous in production?",
  "<code>KEYS pattern</code> performs a full scan of the entire keyspace and blocks the Redis event loop until complete. On a database with millions of keys, this can take <b>seconds to minutes</b> — during which <b>all other commands are blocked</b>. This causes application timeouts, cascading failures, and potentially a full outage.<br>Always use <code>SCAN cursor [MATCH pattern] [COUNT N]</code> instead — it iterates in small batches without blocking.",
  ["gotchas", "L4", "keys"])

c("Gotchas",
  "What are O(N) commands and why should you be careful with them?",
  "Commands with O(N) complexity run in the main event loop and <b>block all other commands</b> until complete. Dangerous on large collections:<br><code>KEYS</code>, <code>SMEMBERS</code>, <code>HGETALL</code>, <code>LRANGE 0 -1</code>, <code>ZRANGE 0 -1</code>, <code>SORT</code>, <code>SUNION</code>/<code>SINTER</code>/<code>SDIFF</code> on large sets, <code>FLUSHDB</code>/<code>FLUSHALL</code> (sync version).<br>Mitigations: Use <code>SCAN</code> family, paginate <code>LRANGE</code>/<code>ZRANGE</code>, use <code>UNLINK</code> instead of <code>DEL</code>, use <code>SSCAN</code>/<code>HSCAN</code>/<code>ZSCAN</code>, or use ASYNC versions (<code>FLUSHDB ASYNC</code>).",
  ["gotchas", "L4", "complexity"])

c("Gotchas",
  "What are the maxmemory eviction policies and when do you use each?",
  "When <code>maxmemory</code> is reached, Redis evicts keys based on policy:<br><b>noeviction</b> (default): Returns error on writes — safest, use when data must not be lost.<br><b>allkeys-lru</b>: Evict least recently used keys (all keys). Best for power-law access patterns (cache).<br><b>volatile-lru</b>: Evict LRU among keys with TTL. Use when some keys are persistent and some expire.<br><b>allkeys-lfu</b>: Evict least frequently used (Redis 4+). Better for some access patterns than LRU.<br><b>volatile-lfu</b>: LFU among keys with TTL.<br><b>allkeys-random</b>: Random eviction. Simpler, lower CPU.<br><b>volatile-random</b>: Random among keys with TTL.<br><b>volatile-ttl</b>: Evict keys with shortest TTL first. Use for cache with varying TTLs.",
  ["gotchas", "L4", "eviction"])

c("Gotchas",
  "What is memory fragmentation in Redis and how do you detect it?",
  "Memory fragmentation = <code>used_memory_rss / used_memory</code> (ratio from INFO memory). Ratio > 1.5 is concerning. Causes:<br>1. Allocator (jemalloc) doesn't return memory to OS<br>2. Many small allocations/deallocations leave gaps<br>3. Fork operations (BGSAVE) leave unreleased pages<br>Detection: <code>INFO memory</code> → <code>mem_fragmentation_ratio</code><br>Mitigation: <code>activedefrag yes</code> (Redis 4+ active defragmentation), restart Redis, use <code>MEMORY PURGE</code> (jemalloc), use <code>CONFIG SET activedefrag yes</code> at runtime. Active defrag uses CPU but doesn't block.",
  ["gotchas", "L4", "memory"])

c("Gotchas",
  "Why does BGSAVE/BGREWRITEAOF fork() sometimes fail?",
  "fork() copies the parent process's page table. If the Redis process is large (e.g. 20 GB), fork() needs the OS to reserve enough virtual memory for the copy — even with COW, the page table copy itself needs memory. Linux <code>overcommit_memory</code> setting controls this:<br><code>sysctl vm.overcommit_memory=1</code> — Always overcommit (recommended for Redis)<br><code>/proc/sys/vm/overcommit_memory=0</code> — Heuristic (may reject fork when memory is tight)<br><code>/proc/sys/vm/overcommit_memory=2</code> — Never overcommit (fork likely fails)<br>Failure mode: <code>Can't save in background: fork: Cannot allocate memory</code> — Redis stops accepting writes if <code>stop-writes-on-bgsave-error yes</code>.",
  ["gotchas", "L4", "fork", "persistence"])

c("Gotchas",
  "What are Redis Cluster hash slots and why 16384?",
  "Redis Cluster divides the keyspace into <b>16384 hash slots</b>. Each key is assigned to a slot via <code>CRC16(key) % 16384</code>. Each node owns a subset of slots. Why 16384:<br>1. Small enough to fit the full bit array in a compact heartbeat message (2 KB = 16384 bits)<br>2. Large enough for reasonable distribution across nodes<br>3. 16K is sufficient for most clusters (16384 slots / 1000 nodes = ~16 slots per node minimum)<br>Use <b>hash tags</b> <code>{user:123}</code> to force related keys to the same slot: <code>CRC16(\"user:123\") % 16384</code>.",
  ["gotchas", "L4", "cluster"])

c("Gotchas",
  "What is cluster resharding?",
  "Resharding moves hash slots between Redis Cluster nodes when adding/removing nodes or rebalancing. Process:<br>1. <code>CLUSTER SETSLOT slot MIGRATING source_node_id</code> — Mark slot as migrating on source<br>2. <code>CLUSTER SETSLOT slot IMPORTING target_node_id</code> — Mark slot as importing on target<br>3. <code>MIGRATE host port key|"" dest-db timeout [COPY] [REPLACE] [KEYS key [key...]]</code> — Move keys<br>4. <code>CLUSTER SETSLOT slot NODE target_node_id</code> — Finalize on both nodes<br>Use <code>redis-cli --cluster reshard</code> to automate. During resharding, the cluster is operational — clients receive MOVED/ASK redirects. ASK is a one-time redirect for queries during migration.",
  ["gotchas", "L4", "cluster"])

c("Gotchas",
  "What is split-brain in Redis Sentinel and how is it prevented?",
  "Split-brain: Network partition causes two Sentinels to elect different primaries, leading to divergent writes. Prevention:<br>1. <b>Quorum</b>: <code>sentinel monitor master ip port quorum</code> — Majority must agree on failure<br>2. <b>min-replicas-to-write</b>: <code>min-replicas-to-write 1</code> — Primary refuses writes if fewer than N replicas are connected<br>3. <b>min-replicas-max-lag</b>: <code>min-replicas-max-lag 10</code> — Replicas must be within N seconds of replication lag<br>4. <b>Odd number of Sentinels</b>: 3 or 5 Sentinels (never 2 or 4 — no majority without partition)<br>5. <b>Distribute Sentinels across availability zones</b>: Network partition shouldn't isolate all to one side.",
  ["gotchas", "L4", "sentinel"])

c("Gotchas",
  "What are the dangers of Lua scripting in Redis?",
  "Lua scripts execute <b>atomically</b> — no other command runs while the script is executing. Dangers:<br>1. <b>Long-running scripts block the entire server</b>: Use <code>SCRIPT KILL</code> to stop a script that hasn't written yet; if it has written, only <code>SHUTDOWN NOSAVE</code> can stop it<br>2. <b>No yielding</b>: Scripts can't yield/pause — no I/O, no blocking commands (BLPOP, etc.) inside scripts<br>3. <b>Replication</b>: Scripts replicate as EVAL/EVALSHA — or as the resulting write commands (if using Redis Functions with <code>no-writes</code> flag or random replication)<br>4. <b>Randomness and time</b>: <code>redis.call('TIME')</code> and <code>math.random()</code> must be deterministic across replicas — use <code>redis.replicate_commands()</code> for script-level write replication<br>5. <b>EVALSHA</b>: Script cache can be flushed — always handle NOSCRIPT error and fallback to EVAL",
  ["gotchas", "L4", "lua"])

c("Gotchas",
  "What is the difference between pipelines and transactions (MULTI/EXEC)?",
  "<b>Pipeline</b>: Client sends multiple commands without waiting for replies — reduces network round-trips. Commands execute independently as they arrive. No atomicity — other clients' commands can interleave.<br><b>Transaction (MULTI/EXEC)</b>: Commands between <code>MULTI</code> and <code>EXEC</code> are queued and executed atomically (no other commands interleave). But: no rollback on failure — if one command fails, others still execute. Use <code>WATCH</code> for optimistic locking: <code>WATCH key</code> → <code>MULTI</code> → commands → <code>EXEC</code> fails (returns nil) if watched key was modified before EXEC.<br>Pipelines are for performance; transactions are for atomicity.",
  ["gotchas", "L4", "transactions"])

c("Gotchas",
  "Why should you never run MONITOR in production?",
  "<code>MONITOR</code> streams every command to the client — this adds significant overhead: (1) every command is duplicated to the monitor buffer, (2) output buffer can grow unbounded, (3) throughput can drop by ~50% on high-traffic instances, (4) sensitive data (passwords, tokens, PII) in commands may be exposed, (5) MONITOR itself is a command that competes for event loop time. Use <code>SLOWLOG</code> for performance debugging, <code>CLIENT LIST</code> for connection analysis, or sampling/filtering proxy layers.",
  ["gotchas", "L4", "monitor"])

c("Gotchas",
  "What are the dangers of TCP backlog issues with Redis?",
  "If new connections arrive faster than Redis can accept() them, the TCP listen backlog fills up. Clients get connection refused or timeout. Causes: (1) too many clients connecting simultaneously, (2) slow accept loop due to high CPU load, (3) Docker/Kubernetes port mapping overhead, (4) <code>tcp-backlog 511</code> too small. Mitigation: increase <code>tcp-backlog</code> (max <code>/proc/sys/net/core/somaxconn</code>), increase <code>net.core.somaxconn</code> sysctl, use connection pooling (reuse connections), monitor <code>rejected_connections</code> in INFO stats.",
  ["gotchas", "L4", "networking"])

c("Gotchas",
  "How do slowlog entries from Lua scripts behave?",
  "Lua scripts are measured as a single command in SLOWLOG — the duration is the entire script execution time, and the command is <code>EVAL script snippet numkeys</code> (or <code>EVALSHA sha</code>). This means: (1) a script with many commands that individually would be fast appears as a single slow entry, (2) you can't see which line/operation in the script was slow, (3) the script body in the slowlog may be truncated (<code>slowlog-max-len</code> caps string length). Use <code>redis.log()</code> inside Lua scripts with <code>SCRIPT DEBUG</code> for fine-grained profiling.",
  ["gotchas", "L4", "lua", "slowlog"])

c("Gotchas",
  "What is the danger of using WATCH without a retry loop?",
  "<code>WATCH key1 key2</code> marks keys for optimistic locking. Inside a MULTI/EXEC block, if any watched key is modified by another client, EXEC returns nil (aborted). The client <b>must retry</b> the entire WATCH→MULTI→EXEC cycle. Without retry: transaction silently fails — no data changed, but the client thinks it succeeded. Correct pattern:<br><code>while True: WATCH key; val = GET key; val = val + 1; MULTI; SET key val; if EXEC: break</code><br>Complexity increases with more read-modify-write operations and higher contention (more retries = more CPU).",
  ["gotchas", "L4", "transactions"])

c("Gotchas",
  "How does maxmemory sampling accuracy affect LRU/LFU eviction?",
  "Redis doesn't maintain a global LRU/LFU list (would be too expensive). Instead, when eviction is needed, it <b>samples</b> N random keys (<code>maxmemory-samples 5</code>, default) and evicts the best candidate among the sample. Higher samples → more accurate eviction (closer to true LRU/LFU) but higher CPU cost. Redis 3.0+ uses an <b>approximated LRU algorithm</b> with sampling, achieving near-true-LRU behavior with small samples. LFU (Redis 4+) uses a logarithmic frequency counter per object (8-bit Morris counter) for sampling-based eviction.<br>Set <code>maxmemory-samples 10</code> for better accuracy if CPU allows.",
  ["gotchas", "L4", "eviction"])

# ============================================================
# Additional DataType / Command / PubSub cards
# ============================================================

c("DataTypes",
  "What is LMOVE and BLMOVE used for?",
  "<code>LMOVE source dest LEFT|RIGHT LEFT|RIGHT</code> atomically pops from one list and pushes to another — both sides configurable. Example: <code>LMOVE queue processing LEFT RIGHT</code> pops from left of 'queue' and pushes to right of 'processing'. Use cases: reliable job queue (move job to processing queue atomically), shuffling items between lists.<br><code>BLMOVE source dest from to timeout</code> is the blocking version (Redis 6.2+). Replaces <code>BRPOPLPUSH</code> (deprecated). Unlike RPOPLPUSH which only supports RIGHT→LEFT, LMOVE supports all four direction combinations.",
  ["data-types", "L1", "lists"])

c("DataTypes",
  "What are ZMSCORE, ZDIFF, ZINTER, ZUNION commands introduced in Redis 6.2?",
  "<code>ZMSCORE key member [member ...]</code> — Get scores of multiple members in one call (replaces N× ZSCORE round-trips).<br><code>ZDIFF numkeys key [key ...] [WITHSCORES]</code> — Set difference on sorted sets (members in first key not in others).<br><code>ZINTER numkeys key [key ...] [WEIGHTS w [w ...]] [AGGREGATE SUM|MIN|MAX] [WITHSCORES]</code> — Sorted set intersection (replaces ZINTERSTORE).<br><code>ZUNION numkeys key [key ...] [WEIGHTS w [w ...]] [AGGREGATE SUM|MIN|MAX] [WITHSCORES]</code> — Sorted set union (replaces ZUNIONSTORE).<br>ZINTER/ZUNION return results directly (no temporary key) — unlike ZINTERSTORE/ZUNIONSTORE which require a destination key.",
  ["data-types", "L1", "sorted-sets"])

c("DataTypes",
  "What is SMISMEMBER and when is it useful?",
  "<code>SMISMEMBER key member [member ...]</code> (Redis 6.2+) checks multiple members for set membership in one call. Returns array of 1/0 for each member — replaces N× SISMEMBER round-trips. Example: <code>SMISMEMBER blacklisted:ips 1.2.3.4 5.6.7.8 9.10.11.12</code> → [1, 0, 0]. Reduces network overhead for batch membership checks. O(N) where N = number of members checked.",
  ["data-types", "L1", "sets"])

c("Commands",
  "What is the MIGRATE command and how does it work?",
  "<code>MIGRATE host port key|"" dest-db timeout [COPY] [REPLACE] [AUTH password] [AUTH2 username password] [KEYS key [key ...]]</code> atomically transfers keys between Redis instances. Internally: DUMP on source → RESTORE on target → DEL on source (if not COPY). The source blocks (timeout) until the target confirms restore — atomicity guarantee: if target fails, keys stay on source. Use <code>COPY</code> to keep keys on source (for cloning). Use <code>REPLACE</code> to overwrite existing keys on target. Cluster-safe with <code>KEYS</code> option. Primary tool for cluster resharding and live data migration.",
  ["commands", "L1", "migration"])

c("PubSub",
  "What is XAUTOCLAIM and how does it simplify consumer failure recovery?",
  "<code>XAUTOCLAIM stream group consumer min-idle-time start-id [COUNT N] [JUSTID]</code> (Redis 6.2+) automatically finds and claims pending messages that have been idle longer than the threshold, assigning them to the given consumer. Replaces the manual XCLAIM + XPENDING loop. Returns array of claimed message IDs + new start ID for the next call (cursor-based iteration). Use in a loop to continuously claim stale messages from failed consumers. Much simpler failure recovery than manual PEL inspection + XCLAIM.",
  ["pubsub", "L2", "streams", "consumer-groups"])

c("PubSub",
  "How does Redis Streams compare to Apache Kafka?",
  "<b>Redis Streams</b>: In-memory, append-only log, consumer groups with at-least-once semantics, simple deployment (single binary), lower operational overhead, excellent for moderate throughput messaging and real-time event sourcing. No built-in message retention by time (XTRIM by length).<br><b>Apache Kafka</b>: Disk-backed, partitioned topic log, designed for extreme throughput (millions msg/s), durable storage with configurable retention (time + size), stronger ordering guarantees per partition, ecosystem (Kafka Connect, KSQL, Schema Registry). Higher operational complexity (ZooKeeper/ KRaft, dedicated cluster).<br>When Redis: moderate scale, low latency, simpler ops, already using Redis. When Kafka: massive scale, long-term durable event storage, replay from past years, strict ordering.",
  ["pubsub", "L2", "streams", "comparison"])

c("PubSub",
  "How does Redis Streams compare to RabbitMQ for message queuing?",
  "<b>Redis Streams</b>: Append-only log, consumer groups, at-least-once, message replay via ID range. No exchange/routing topology. Messages are in a single stream — use multiple streams for routing.<br><b>RabbitMQ</b>: AMQP broker with exchanges, queues, bindings — flexible routing (fanout, direct, topic, headers). Strong delivery guarantees (publisher confirm, consumer ack). Dead-letter exchanges, TTL per message, priority queues. Erlang/OTP-based, battle-tested.<br>When Redis: simpler, low-latency, using Redis already, append-only event model sufficient. When RabbitMQ: complex routing patterns, need per-message TTL, priority, dead-letter funneling, or AMQP protocol compliance.",
  ["pubsub", "L2", "streams", "comparison"])

c("Patterns",
  "What is RedisBloom's Cuckoo Filter and when to use it instead of Bloom Filter?",
  "<b>Cuckoo Filter</b> (RedisBloom) is a probabilistic set-membership structure supporting <b>deletion</b> (unlike standard Bloom). Commands:<br><code>CF.RESERVE filter capacity [BUCKETSIZE b] [MAXITERATIONS m] [EXPANSION e]</code><br><code>CF.ADD filter item</code> — Add item<br><code>CF.DEL filter item</code> — Delete item<br><code>CF.EXISTS filter item</code> — Check membership<br><code>CF.COUNT filter item</code> — Count occurrences (approximate, with insertions count)<br>Use Cuckoo over Bloom when: items need to be removed (user sessions, active connections), or when count capability is needed. Cuckoo filters use ~10% more memory than Bloom filters for equivalent FPR but add delete support.",
  ["patterns", "L3", "bloom-filter", "modules"])

c("Patterns",
  "What is RedisBloom's Count-Min Sketch and what is it used for?",
  "<b>Count-Min Sketch</b> (CMS) estimates the frequency of items in a data stream with sub-linear memory. Commands:<br><code>CMS.INITBYDIM key width depth</code> — Create with dimensions<br><code>CMS.INCRBY key item increment [item increment ...]</code> — Increment counts<br><code>CMS.QUERY key item [item ...]</code> — Estimated frequency (overcounts, never undercounts)<br><code>CMS.MERGE dest numkeys source [source ...] [WEIGHTS w [w ...]]</code> — Merge sketches<br>Use cases: heavy hitter detection, top-K frequency analysis, network traffic monitoring, word frequency in streaming text. Guaranteed: estimate >= true count. Error = ε × total count with probability 1-δ (configurable via width/depth).",
  ["patterns", "L3", "count-min-sketch", "modules"])

c("Patterns",
  "What is RedisBloom's Top-K data structure?",
  "<b>Top-K</b> (RedisBloom) maintains a list of the K most frequent items in a stream. Commands:<br><code>TOPK.RESERVE key topk [width depth decay]</code> — Create Top-K list<br><code>TOPK.ADD key item [item ...]</code> — Add items to the stream<br><code>TOPK.LIST key</code> — Return current top-K items (with counts, if WITHCOUNT)<br><code>TOPK.QUERY key item [item ...]</code> — Check if items are in top-K<br><code>TOPK.COUNT key item [item ...]</code> — Estimated count of items<br><code>TOPK.INCRBY key item increment</code> — Weighted increment<br>Uses HeavyKeeper algorithm — combines count-min sketch with probabilistic eviction. Decay parameter controls how quickly old entries fade (for sliding-window top-K). Use for: trending topics, popular products, top referrers.",
  ["patterns", "L3", "top-k", "modules"])

c("Gotchas",
  "What is the lazy-free mechanism and how does it reduce latency?",
  "Lazy-free (Redis 4+) defers memory reclamation of deleted objects to a background thread instead of doing it inline during command execution. Operations supporting lazy-free:<br><code>UNLINK key</code> — Async delete (instead of DEL)<br><code>FLUSHDB ASYNC</code> / <code>FLUSHALL ASYNC</code> — Async flush<br>Config options for automatic lazy-free:<br><code>lazyfree-lazy-eviction yes</code> — Async on eviction<br><code>lazyfree-lazy-expire yes</code> — Async on key expiry<br><code>lazyfree-lazy-server-del yes</code> — Async when server-side DEL needed (rename, side effects)<br><code>replica-lazy-flush yes</code> — Async flush on replica during full resync<br>The key disappears from namespace immediately (atomic), but memory is released incrementally by background threads. Dramatically reduces latency spikes from deleting large keys.",
  ["gotchas", "L4", "latency", "memory"])

c("Gotchas",
  "What is slave-to-master promotion and what are the risks during failover?",
  "When Sentinel promotes a replica to primary, the sequence is:<br>1. Sentinel detects primary failure (subjective → objective via quorum)<br>2. Sentinel elects a leader Sentinel to perform failover<br>3. Leader selects 'best' replica (highest replication offset, then lowest runid)<br>4. <code>REPLICAOF NO ONE</code> on selected replica → becomes new primary<br>5. Other replicas reconfigure to replicate from new primary<br>Risks:<br>• <b>Data loss</b>: Writes on old primary not yet replicated are lost (async replication)<br>• <b>Split-brain with old primary</b>: If old primary was isolated (not dead), both 'primaries' accept writes. Clients reading from old primary see stale data. Mitigated by <code>min-replicas-to-write</code> on the primary.<br>• <b>Replication offset mismatch</b>: If no replica was fully sync'd, partial data loss unavoidable.",
  ["gotchas", "L4", "sentinel", "replication"])

# ============================================================
# 08 — Expert (L5 Opinion + L6 Innovation)
# ============================================================

c("Expert",
  "When should you choose Redis Cluster vs Sentinel?",
  "<b>Redis Cluster</b>: Use when you need <b>horizontal scaling</b> (dataset > single node RAM) and automatic sharding. Provides data partitioning across nodes. Operational complexity is higher (resharding, slot migration, multi-key constraint). Requires client-side cluster support.<br><b>Redis Sentinel</b>: Use when dataset fits in a single node but you need <b>high availability</b> (automatic failover). No sharding — all data on one primary. Simpler operations, any Redis client works. Suitable for most small-to-medium workloads.<br>Can combine: Sentinel-managed replicas for each Cluster node (but adds complexity).<br>Rule of thumb: < 25 GB dataset = Sentinel; > 25 GB = Cluster.",
  ["expert", "L5", "cluster", "sentinel"])

c("Expert",
  "When should you use Redis vs Memcached for caching?",
  "Choose <b>Memcached</b> when:<br>• You only need simple string caching (no data types)<br>• Multi-threaded scaling on multi-core servers matters<br>• Memory fragmentation overhead is critical (Memcached's slab allocator can be more predictable)<br>• You never need persistence, replication, or data modeling<br>Choose <b>Redis</b> when:<br>• You need rich data types (hashes for objects, sorted sets for ranking, etc.)<br>• You need TTL-per-key, eviction policies, or persistence<br>• You need replication, cluster, sentinel, or streaming<br>• You might need more than caching later (message broker, session store, queue)<br>In practice, Redis is the default choice for most new projects.",
  ["expert", "L5", "caching", "comparison"])

c("Expert",
  "Can Redis be used as a primary database?",
  "Yes, under specific constraints. Redis as primary DB requires:<br>1. <b>Persistence enabled</b>: Both RDB (every 5 min) and AOF (everysec), or mixed mode<br>2. <b>Dataset fits in RAM</b>: Plan for growth; cluster for datasets beyond single node<br>3. <b>Data loss tolerance defined</b>: max 1 sec loss with AOF everysec — acceptable for many use cases<br>4. <b>No complex queries</b>: Redis has no JOINs, GROUP BY, or ad-hoc queries — data model must be designed for Redis access patterns<br>5. <b>Backup and recovery process tested</b>: Regular RDB/AOF backup + restore drills<br>6. <b>Indexing via RediSearch/FT.CREATE</b>: For secondary index and full-text search needs<br>Suitable for: leaderboards, session stores, shopping carts, real-time analytics, feature flags, rate limiters.",
  ["expert", "L5", "primary-database"])

c("Expert",
  "What is Valkey and how does it compare to Redis OSS?",
  "<b>Valkey</b> is an open-source (BSD-3-Clause), community-driven fork of Redis 7.2.4, created by the Linux Foundation in March 2024 after Redis Ltd. changed its license from BSD to dual RSALv2/SSPLv1 (source-available). Key points:<br>• Fully compatible with Redis OSS 7.2 clients and data<br>• Maintained by original Redis contributors (including many core developers)<br>• BSD licensed — no restrictions on cloud providers offering it as a service<br>• Active development with new features independent of Redis<br>• Supported by AWS, Google Cloud, Oracle, Ericsson, Snap<br><b>When to choose</b>: If you need BSD/OSS licensing for compliance, or want community governance. Redis OSS (pre-7.4) remains BSD; Redis 7.4+ uses new license.",
  ["expert", "L5", "valkey", "ecosystem"])

c("Expert",
  "What is Redis Stack and when should you use it vs standalone modules?",
  "<b>Redis Stack</b> bundles Redis OSS with: RediSearch, RedisJSON, RedisTimeSeries, RedisBloom, and RedisGraph — pre-tested compatible versions. Use Redis Stack when:<br>• You need multiple module capabilities (search + JSON + timeseries)<br>• You want simpler deployment (one Docker image, one package)<br>• You want guaranteed module compatibility (versions tested together)<br>Use <b>standalone modules</b> when:<br>• You need only one module (reduce attack surface and memory)<br>• You need a specific module version not bundled<br>• You're on a custom Redis build or fork (Valkey, KeyDB)<br>Redis Stack is the easiest path to a full-featured Redis — Docker: <code>redis/redis-stack</code>.",
  ["expert", "L5", "redis-stack", "modules"])

c("Expert",
  "What are the considerations for Redis on Kubernetes?",
  "1. <b>StatefulSet</b>: Use for stable network identity and persistent storage (RDB/AOF on PersistentVolume)<br>2. <b>Pod anti-affinity</b>: Spread Redis pods across nodes for HA<br>3. <b>Resource limits/requests</b>: Set memory limits carefully (<code>maxmemory</code> must be < pod limit — reserve for fork() overhead and system)<br>4. <b>Sentinel or Cluster</b>: Run Sentinel (3 pods) for HA or Cluster for sharding. Use Redis Operator (e.g., Spotahome, OT-CONTAINER-KIT) to automate<br>5. <b>Health probes</b>: <code>redis-cli PING</code> for liveness/readiness<br>6. <b>Graceful shutdown</b>: <code>redis-cli SHUTDOWN NOSAVE|SAVE</code> in preStop hook<br>7. <b>Persistence</b>: Use fast storage class (SSD) for AOF/RDB; consider AOF everysec vs always based on storage speed<br>8. <b>Monitoring</b>: Prometheus exporter (redis_exporter), Grafana dashboards",
  ["expert", "L5", "kubernetes"])

c("Expert",
  "How does Redis work with serverless platforms (Upstash, Cloudflare)?",
  "<b>Upstash</b>: Serverless Redis (and Kafka) with per-request pricing and REST API access — no persistent connections needed. Ideal for Vercel/Netlify/Cloudflare Workers where long-lived TCP to Redis is impractical. Supports Redis wire protocol via HTTP proxy.<br><b>Cloudflare</b>: Workers can connect to Redis via TCP (paid plan) or HTTP-based gateways (Upstash). Redis in serverless faces challenges:<br>1. Connection limits: Serverless functions can't maintain connection pools — each cold start = new TCP connection<br>2. Connection exhaustion: Spike of concurrent functions can exhaust Redis connection limit (<code>maxclients</code>)<br>3. Mitigations: Use single Redis client per function instance (global var), connection pooling proxies (Envoy, Twemproxy), or HTTP-based Redis access (Upstash, Redis Cloud REST API)",
  ["expert", "L5", "serverless"])

c("Expert",
  "What are Lua scripts vs Redis Functions (Redis 7+)?",
  "<b>Lua scripts</b> (<code>EVAL</code>, <code>EVALSHA</code>):<br>• Sent by client on each execution<br>• Cached by SHA1 hash (volatile — lost on restart/SCRIPT FLUSH)<br>• Script logic lives in application code<br>• No libraries or code organization<br>• Must handle NOSCRIPT fallback on cache miss<br><b>Redis Functions</b> (<code>FUNCTION LOAD</code>, <code>FCALL</code> — Redis 7+):<br>• Stored on the server persistently (loaded at startup via <code>redis.conf</code> or <code>LOAD</code>)<br>• Survive restarts, replicated to replicas<br>• Support libraries, code organization, and versioning<br>• <code>FCALL func_name numkeys key [...] arg [...]</code> — Executes like EVAL but durable<br>• Engineered to replace EVAL — better engineering for server-side logic<br>• Supports <code>no-writes</code>, <code>no-cluster</code>, and <code>allow-oom</code> flags per function",
  ["expert", "L5", "functions", "lua"])

c("Expert",
  "What is client-side caching (RESP3) in Redis?",
  "Client-side caching (Redis 6+ with RESP3) allows clients to cache server responses locally. Two modes:<br>1. <b>Default mode (server-assisted)</b>: Server tracks which keys each client has cached. When a key is modified, the server sends <b>invalidation messages</b> to affected clients. Use <code>CLIENT TRACKING ON</code> (opt-in).<br>2. <b>Broadcast mode</b>: Server broadcasts invalidation for any modified key matching a prefix pattern. Clients subscribe to prefixes. Use <code>CLIENT TRACKING ON BCAST PREFIX user:</code>.<br>Benefits: Near-zero latency for repeated reads, reduced server load, especially useful for read-heavy applications with hot keys. RESP3 protocol required for the PUSH message type used for invalidation.<br>Limitation: Each client connection with tracking consumes server memory (the tracking table — <code>tracking-table-max-keys</code>).",
  ["expert", "L5", "client-side-caching"])

c("Expert",
  "What is the Redis Module API and how do you build custom data types?",
  "The <b>Redis Module API</b> (C API) allows creating custom data types, commands, and extensions loaded at runtime. Key components:<br>1. <code>REDISMODULE_INIT</code> — Module entry point<br>2. <code>RM_CreateDataType()</code> — Register a new data type with callbacks (rdb load/save, aof rewrite, free, mem usage, digest)<br>3. <code>RM_CreateCommand()</code> — Register custom commands (with flags: write, readonly, deny-oom, etc.)<br>4. <code>RM_OpenKey()</code> — Access keys of your custom type<br>5. RDB/AOF callbacks: Serialize/deserialize for persistence<br>6. <code>RM_ReplicateVerbatim()</code> — Replicate command to replicas/AOF<br>Modules are loaded via <code>redis.conf</code>: <code>loadmodule /path/to/module.so [args...]</code> or <code>MODULE LOAD</code> at runtime. Examples: RediSearch, RedisJSON, RedisTimeSeries, RedisBloom.",
  ["expert", "L6", "modules", "api"])

c("Expert",
  "What is Redis Gears and what can it do?",
  "<b>Redis Gears</b> is a serverless data-processing engine within Redis. It executes Python (or C) functions triggered by events (data changes, timers, or external triggers). Key capabilities:<br>1. <b>Stream processing</b>: <code>GearsBuilder('StreamReader').foreach(process).register('mystream')</code><br>2. <b>Write-Behind caching</b>: Trigger on key writes, write to external DB (MySQL, PostgreSQL, Cassandra)<br>3. <b>Event-driven pipelines</b>: React to keyspace changes (<code>KeysReader</code>) or PubSub messages<br>4. <b>Batch operations</b>: Process all keys matching a pattern (<code>KeysOnlyReader('user:*')</code>)<br>5. <b>Function chaining</b>: map → filter → groupby → foreach<br>6. <b>Cluster support</b>: Shard-local execution in cluster mode<br>Use for: ETL pipelines, data synchronization, reactive cache invalidation, real-time aggregation.",
  ["expert", "L6", "redisgears", "modules"])

c("Expert",
  "What is RediSearch and what are its full-text search capabilities?",
  "RediSearch provides secondary indexing, full-text search, aggregation, and vector search. Full-text features:<br>• <b>Exact phrase matching</b>: <code>\"hello world\"</code><br>• <b>Prefix/infix/suffix matching</b>: <code>hel*</code>, <code>*ello</code>, <code>*ell*</code><br>• <b>Fuzzy matching</b>: <code>%hell%</code> (1-3 Levenshtein distance)<br>• <b>Boolean operators</b>: AND, OR, NOT, <code>|</code>, <code>-</code><br>• <b>Stemming</b>: Automatic word stemming (configurable per language)<br>• <b>Stop words</b>: Configurable stop words list<br>• <b>Scoring</b>: BM25 (default) or TF-IDF<br>• <b>Numeric/geo/tag filters</b>: Combined with text search<br>• <b>Aggregation pipeline</b>: GROUPBY, SORTBY, APPLY, FILTER, LIMIT<br>• <b>Autocomplete/suggestions</b>: <code>FT.SUGADD</code> / <code>FT.SUGGET</code><br>Use for: product search, content discovery, log search, document indexing, hybrid search (text + vector).",
  ["expert", "L6", "redisearch", "modules"])

c("Expert",
  "What internal data encodings does Redis use to optimize memory?",
  "Redis uses encoding polymorphism — small collections use compact encodings, switched to standard structures when they grow:<br><b>Strings</b>: <code>int</code> (embedded in the redisObject), <code>embstr</code> (single allocation, <= 44 bytes), <code>raw</code> (two allocations).<br><b>Hashes</b>: <code>listpack</code> (<= 512 fields, each <= 64 bytes), <code>hashtable</code> (larger).<br><b>Lists</b>: <code>quicklist</code> (linked list of listpacks, default since 3.2).<br><b>Sets</b>: <code>intset</code> (all integers, <= 512 members), <code>listpack</code> (small strings), <code>hashtable</code> (large).<br><b>Sorted Sets</b>: <code>listpack</code> (<= 128 members, each <= 64 bytes), <code>skiplist + hashtable</code>.<br><code>hash-max-listpack-entries</code>, <code>set-max-intset-entries</code>, etc. tune these thresholds. Lower thresholds = more memory but faster conversion from listpack on updates.",
  ["expert", "L6", "encoding", "internals"])

c("Expert",
  "What are Redis Enterprise features?",
  "Redis Enterprise (commercial offering) adds:<br>1. <b>Active-Active geo-distribution (CRDTs)</b>: Conflict-free replicated data types for multi-region writes with automatic conflict resolution<br>2. <b>Auto-tiering (Redis on Flash)</b>: Hot data in RAM, cold data on SSD — larger datasets at lower cost<br>3. <b>Linear scaling</b>: Add/remove nodes without downtime or resharding complexity<br>4. <b>99.999% uptime SLA</b>: Proven topology with automated failover<br>5. <b>Multi-tenancy</b>: Run multiple isolated Redis databases on shared infrastructure<br>6. <b>Built-in replication engine</b>: WAN-optimized replication<br>7. <b>Role-based access control (RBAC)</b>: Fine-grained ACLs beyond Redis 6 ACLs<br>8. <b>Redis on Flash</b>: Extends dataset size 10x by combining RAM + NVMe SSDs<br>Use for: Large-scale production, multi-region deployments, regulatory compliance.",
  ["expert", "L6", "enterprise"])

c("Expert",
  "How does Redis as a Vector Database compare to dedicated solutions?",
  "Redis vector search (via RediSearch HNSW index) competes with Pinecone, Weaviate, Milvus, Qdrant. Advantages:<br>• <b>Single infrastructure</b>: One Redis instance handles caching, session store, rate limiting, AND vector search — reduce operational complexity<br>• <b>Ultra-low latency</b>: In-memory vectors + HNSW = sub-millisecond KNN queries<br>• <b>Hybrid queries</b>: Combine full-text search + vector search + numeric filters in one query (not all vector DBs support this)<br>• <b>Rich ecosystem</b>: Existing Redis client libraries, monitoring, backup<br>Limitations:<br>• RAM-dependent: Vector indexes are in-memory (no disk-optimized ANN yet)<br>• Scaling: Redis Cluster for horizontal scaling (by hash slot, not vector-partitioned)<br>• Less specialized: Dedicated vector DBs may have more ANN algorithms (IVF, PQ, DiskANN)<br>Best for: Teams already using Redis who want to add semantic search/RAG without new infrastructure.",
  ["expert", "L6", "vector-db", "comparison"])

c("Expert",
  "What is RedisAI and how does it serve ML models?",
  "<b>RedisAI</b> module executes deep learning models directly within the Redis server, reducing data movement latency. Supports TensorFlow, PyTorch, ONNX, and ONNX-ML. Key commands:<br><code>AI.MODELSET model_key TF CPU INPUTS a b OUTPUTS c BLOB model_binary</code> — Load a model<br><code>AI.TENSORSET input_tensor FLOAT 1 784 VALUES vals ...</code> — Create input tensor<br><code>AI.MODELRUN model_key INPUTS input_tensor OUTPUTS output_tensor</code> — Run inference<br><code>AI.SCRIPTSTORE script_key CPU SOURCE \"def predict(tensor): ...\"</code> — TorchScript<br>Use cases: Real-time inference serving (recommendations, fraud detection), preprocess → predict → postprocess pipeline in one hop, reduce serialization overhead between app and model server, edge deployment with Redis.",
  ["expert", "L6", "redisai", "ml"])

c("Expert",
  "What is the Redis Stack decision framework?",
  "Decide which Redis Stack components to use based on requirements:<br><b>Need caching with TTL and simple ops?</b> → Redis OSS (no modules)<br><b>Need full-text search in your data?</b> → + RediSearch<br><b>Storing and querying JSON documents?</b> → + RedisJSON<br><b>Time-series sensor/metrics data?</b> → + RedisTimeSeries (with auto-compaction rules)<br><b>Approximate counting or membership tests?</b> → + RedisBloom (BF, CF, CMS, TDigest, Top-K)<br><b>Semantic/vector search for AI?</b> → RediSearch HNSW index (part of Redis Stack)<br><b>Complex event processing, ETL?</b> → + RedisGears<br><b>ML inference at Redis speed?</b> → + RedisAI<br><b>Graph data (social networks, recommendations)?</b> → + RedisGraph<br><b>Need all of above?</b> → Use Redis Stack (all bundled, tested together). Start small and add modules incrementally — each module adds memory and CPU overhead.",
  ["expert", "L6", "redis-stack", "decision-framework"])

c("Expert",
  "What are Redis module encodings for RDB and AOF compatibility?",
  "Modules must implement two callbacks for persistence:<br>1. <b>RDB save</b>: Serialize data type to RDB binary format with <code>RM_SaveUnsigned()</code>, <code>RM_SaveStringBuffer()</code>, <code>RM_SaveDouble()</code>, <code>RM_SaveLongDouble()</code>. Use <code>RM_SaveDataTypeToString()</code> for string-based serialization.<br>2. <b>RDB load</b>: Deserialize from RDB with corresponding <code>RM_Load*()</code> functions. Handle <code>REDISMODULE_ AUX_*</code> for module-specific aux fields (before keys).<br>3. <b>AOF rewrite</b>: Emit the command(s) that would recreate the key's state — use <code>RM_EmitAOF()</code> or return the command string from the callback.<br>4. <b>Digest</b>: <code>RM_DigestAddStringBuffer()</code> for DEBUG DIGEST.<br>5. <b>Free</b>: <code>RM_Free()</code> or custom deallocation when key is deleted.<br>Without RDB callbacks, modules lose data on restart/replication. Without AOF callback, AOF cannot reconstruct module data.",
  ["expert", "L6", "modules", "persistence"])

c("Expert",
  "How does Redis replication work for Redis modules?",
  "Module commands must be explicitly replicated to replicas/AOF:<br>1. <code>RM_Replicate()</code> — Replicate the invoking command itself (most common)<br>2. <code>RM_ReplicateVerbatim()</code> — Replicate an arbitrary command string (e.g., module constructs a synthetic command)<br>3. If a module command writes to keys but <b>doesn't call RM_Replicate()</b>, the replica won't see the change → data divergence. Best practice: wrap every write in a replication call.<br>For non-deterministic commands (random, time-based): use <code>RM_ReplicateVerbatim()</code> with the specific command + arguments that produce the same result, or use <code>RM_CreateCommand()</code> with <code>getkeys-api</code> flag for automatic key extraction + replication.",
  ["expert", "L6", "modules", "replication"])

c("Expert",
  "What is the replica-of command used for?",
  "<code>REPLICAOF host port</code> makes the server a replica of the specified primary (starts replication). <code>REPLICAOF NO ONE</code> promotes the replica to primary (stops replication, keeps data). Use cases:<br>1. <b>Data migration</b>: Point new instance at old instance → data syncs → <code>REPLICAOF NO ONE</code> → cut over<br>2. <b>Zero-downtime upgrades</b>: Sync new Redis version as replica → promote (combined with Sentinel)<br>3. <b>Read scaling</b>: Add replicas for read-only traffic<br>4. <b>Geo-distribution</b>: Replica in another region for local reads (~async replication latency)<br><code>SLAVEOF</code> is the deprecated equivalent (still works for backward compatibility, but REPLICAOF is preferred since Redis 5).",
  ["expert", "L6", "replication", "migration"])

c("Expert",
  "What is the TTL mechanism internals and how does Redis handle expiry?",
  "Redis handles key expiry in two ways:<br>1. <b>Passive expiry</b>: When a client accesses an expired key, Redis checks the expiry and deletes it — returns \"key not found\". No background cleanup needed.<br>2. <b>Active expiry</b>: Redis periodically (10 times/second, configurable via <code>active-expire-effort 1-10</code>) scans a random sample of keys with TTL, deletes expired ones. If > 25% of sampled keys are expired, it repeats the cycle (probabilistic cleanup). This prevents memory bloat from expired-but-unaccessed keys.<br>3. <b>Lazy expiry on replication</b>: Replica doesn't actively expire keys — it waits for DEL command from primary. This prevents clock skew between primary and replica from causing divergence.<br>Expiry accuracy is probabilistic: expired keys may persist briefly until passive or active expiry catches them.",
  ["expert", "L6", "internals", "ttl"])

c("Expert",
  "How does Redis pipeline write replication to AOF and replicas?",
  "When a write command arrives, Redis:<br>1. Executes the command on the in-memory data<br>2. If AOF is enabled: appends the command (in RESP format) to the AOF buffer (in-memory), which is fsynced to disk per <code>appendfsync</code> policy<br>3. If replication is active: appends the command to each replica's <b>output buffer</b> (replication backlog is separate, for reconnecting replicas)<br>4. The command propagates to AOF child + replica connections asynchronously after the response is sent to the original client<br>If a replica's output buffer exceeds <code>client-output-buffer-limit replica</code> (hard limit), the replica is disconnected. This protects the primary from slow replicas causing unbounded memory growth. Default: <code>256mb / 64mb 60</code> (hard limit 256 MB, soft limit 64 MB for 60 seconds).",
  ["expert", "L6", "internals", "replication"])

c("Expert",
  "What are ACLs (Access Control Lists) in Redis 6+?",
  "Redis 6+ provides fine-grained ACLs for multi-user access control. Key commands and concepts:<br><code>ACL LIST</code> — List all ACL rules<br><code>ACL SETUSER alice on >password ~cached:* +@all -@dangerous</code> — Create user: password=password, key prefix=cached:*, allow all safe commands, deny dangerous ones<br><code>ACL DELUSER alice</code> — Remove user<br><code>ACL WHOAMI</code> — Current user<br><code>ACL CAT [category]</code> — List command categories<br><code>ACL GENPASS</code> — Generate secure password<br><code>AUTH username password</code> — Authenticate (Redis 6+ supports username; AUTH password still works for default user)<br>Use <code>aclfile /etc/redis/users.acl</code> in config for persistent ACLs. Categories: <code>@admin</code>, <code>@dangerous</code>, <code>@fast</code>, <code>@slow</code>, <code>@keyspace</code>, <code>@read</code>, <code>@write</code>, <code>@pubsub</code>, <code>@set</code>, <code>@sortedset</code>, etc.",
  ["expert", "L6", "security", "acl"])

c("Expert",
  "What is Redis Stack's recommendation for JSON + Search together?",
  "Combining RedisJSON and RediSearch enables indexing and querying specific JSON fields without full document scans. Pattern:<br><code>JSON.SET user:1 $ '{\"name\":\"Alice\",\"email\":\"alice@example.com\",\"tags\":[\"vip\"]}'</code><br><code>FT.CREATE users_idx ON JSON PREFIX 1 user: SCHEMA $.name AS name TEXT $.email AS email TAG $.tags.* AS tags TAG</code><br><code>FT.SEARCH users_idx '@name:Alice @tags:{vip}'</code> — Full-text on name + exact tag match<br>Benefits: Store rich JSON documents (nested objects, arrays), query by content with RediSearch indexing, atomic JSON updates (<code>JSON.NUMINCRBY user:1 $.visits 1</code>) with immediate index reflection. No need for secondary SQL database for document search — single Redis Stack instance handles both storage and search.",
  ["expert", "L6", "json", "redisearch", "redis-stack"])

c("Expert",
  "What is RedisGraph and how does its Cypher query language work?",
  "<b>RedisGraph</b> (module, based on GraphBLAS) stores and queries graph data using a subset of the Cypher query language (same as Neo4j). Key commands:<br><code>GRAPH.QUERY graph \"CREATE (:Person {name:'Alice', age:30})-[:KNOWS]->(:Person {name:'Bob'})\"</code> — Create nodes and edges<br><code>GRAPH.QUERY graph \"MATCH (a:Person)-[:KNOWS]->(b:Person) RETURN a.name, b.name\"</code> — Query relationships<br><code>GRAPH.QUERY graph \"MATCH (a:Person) WHERE a.age > 25 RETURN a.name ORDER BY a.age\"</code> — Filtered query<br>Supports: WHERE, ORDER BY, LIMIT, SKIP, aggregation (COUNT, SUM, AVG), shortestPath, and parameterized queries. Use for social graphs, recommendation engines, fraud detection (relationship analysis), dependency graphs, network topology.<br>Deprecation note: RedisGraph has been deprecated in Redis Stack 7.4+ (replaced by FalkorDB fork).",
  ["expert", "L6", "redisgraph", "modules"])

c("Expert",
  "What is CLIENT REPLY and how does it affect performance?",
  "<code>CLIENT REPLY OFF|ON|SKIP</code> controls whether the server sends command replies to the client. <code>CLIENT REPLY OFF</code> disables replies — commands execute but the client doesn't wait for or receive responses. <code>CLIENT REPLY SKIP</code> skips only the next command's reply. Use for fire-and-forget patterns (logging, telemetry, analytics) where the client doesn't need confirmation. Reduces network bandwidth and client-side processing. Warning: with REPLY OFF, the client has no indication of command success/failure — use only for commands where failure is acceptable or monitored externally.",
  ["expert", "L6", "performance"])

# ============================================================
# Build the package
# ============================================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
