import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "SQLite"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Querying":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Querying-Data"),
    "Schema":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Schema-Design"),
    "Performance":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Performance-Indexes"),
    "Transactions": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Transactions-Locking"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# =============================================
# 01 — FUNDAMENTALS (L0 Primitives)
# =============================================

c("Fundamentals", "What is SQLite?",
  "A <b>serverless, self-contained, zero-config</b> SQL database engine. It reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views is contained in a single <code>.db</code> file. It is the most widely deployed database engine in the world.",
  ["L0_primitives"])

c("Fundamentals", "How does SQLite differ from a client-server database (like PostgreSQL or MySQL)?",
  "SQLite has <b>no separate server process</b> — your application links the SQLite library directly. Reads/writes go to a local file. No network, no authentication, no users, no port to listen on. Client-server DBs require a running daemon, network round-trips, user management. SQLite = library; PG/MySQL = service.",
  ["L0_primitives"])

c("Fundamentals", "What type of application is SQLite <b>NOT</b> well-suited for?",
  "<ul><li>High-concurrency writes (single-writer lock)</li><li>Massive scale (> 1TB or billions of rows — can work but tuned setups needed)</li><li>Network-accessible databases (no built-in server)</li><li>Multi-user with separate credentials (no built-in user/auth system)</li><li>Frequent concurrent writes from many processes</li></ul>",
  ["L0_primitives"])

c("Fundamentals", "What is SQLite's storage engine based on?",
  "<b>B-tree</b> (B+tree variant). Each table and each index is stored in its own separate B-tree within the single database file. Pages are 4KB by default (configurable via <code>PRAGMA page_size</code>). B-trees provide O(log n) lookups, inserts, and range scans.",
  ["L0_primitives"])

c("Fundamentals", "What does 'single-writer' mean in SQLite?",
  "Only <b>one writer at a time</b> can hold the write lock. Multiple readers can read concurrently, but if a write is in progress, all other readers and writers must wait for the lock to be released. This is enforced at the OS file-lock level. WAL mode relaxes this: readers and one writer can operate concurrently.",
  ["L0_primitives"])

c("Fundamentals", "What is WAL (Write-Ahead Log) mode?",
  "Instead of writing changes directly to the main database file, changes are first appended to a <b>separate WAL file</b> (<code>-wal</code>). Allows concurrent readers to read the old committed state while a writer appends to the WAL. Periodically, the WAL is 'checkpointed' back into the main database. Enabled with <code>PRAGMA journal_mode=WAL;</code>.",
  ["L0_primitives"])

c("Fundamentals", "What does 'zero-config' mean for SQLite?",
  "No installation, no daemon, no config files, no <code>CREATE DATABASE</code>, no user setup. Just <code>sqlite3_open(\"my.db\")</code> and you have a fully functional SQL database. The database file is self-contained — copy the file, you've copied the whole database.",
  ["L0_primitives"])

c("Fundamentals", "What is SQLite's type system?",
  "SQLite uses <b>type affinity</b> with <b>dynamic (flexible) typing</b>. Values have storage classes (NULL, INTEGER, REAL, TEXT, BLOB). Column types suggest a preferred storage class (affinity) but do not enforce it. An INTEGER column can hold TEXT. <code>STRICT</code> tables (SQLite 3.37+) enforce declared types.",
  ["L0_primitives"])

c("Fundamentals", "What are the 5 storage classes in SQLite?",
  "<ol><li><b>NULL</b> — absent value</li><li><b>INTEGER</b> — signed integer, stored in 1,2,3,4,6, or 8 bytes</li><li><b>REAL</b> — 8-byte IEEE floating point</li><li><b>TEXT</b> — string, stored in the database encoding (UTF-8, UTF-16BE, or UTF-16LE)</li><li><b>BLOB</b> — raw binary data, stored exactly as input</li></ol>",
  ["L0_primitives"])

c("Fundamentals", "What is type affinity?",
  "Each column has an <b>affinity</b> (TEXT, NUMERIC, INTEGER, REAL, BLOB) that determines SQLite's <b>preferred</b> storage class for values inserted. Affinity is derived from the declared column type (e.g., <code>INT</code> → INTEGER affinity, <code>VARCHAR(255)</code> → TEXT affinity). It's a suggestion, not a constraint.",
  ["L0_primitives"])

c("Fundamentals", "How do you determine a column's affinity from its type declaration?",
  "<table><tr><th>Declaration contains</th><th>Affinity</th></tr><tr><td><code>INT</code></td><td>INTEGER</td></tr><tr><td><code>CHAR, CLOB, TEXT</code></td><td>TEXT</td></tr><tr><td><code>BLOB</code> (or no type)</td><td>BLOB</td></tr><tr><td><code>REAL, FLOA, DOUB</code></td><td>REAL</td></tr><tr><td>Other</td><td>NUMERIC</td></tr></table>",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between <code>INTEGER</code> and <code>INT</code> affinity?",
  "Both map to INTEGER affinity. Rule: if the type name contains the string <code>'INT'</code>, it gets INTEGER affinity. So <code>BIGINT, TINYINT, INT, INTEGER, MEDIUMINT</code> all have INTEGER affinity.",
  ["L0_primitives"])

c("Fundamentals", "What is an <code>sqlite_sequence</code> table?",
  "An internal table automatically created when a table uses <code>AUTOINCREMENT</code>. Stores the largest <code>rowid</code> ever used for that table. Used to ensure <code>AUTOINCREMENT</code> never reuses rowids of deleted rows.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>sqlite_master</code> table?",
  "The <b>schema table</b> that stores the definition of all tables, indexes, views, and triggers in the database. Query it: <code>SELECT * FROM sqlite_master;</code>. Each row has <code>type, name, tbl_name, rootpage, sql</code>. Every SQLite database has this.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>rowid</code> (or <code>_rowid_</code> or <code>oid</code>)?",
  "Every row in a standard SQLite table has a <b>unique 64-bit signed integer key</b> called <code>rowid</code>. If you declare <code>INTEGER PRIMARY KEY</code>, that column becomes an alias for <code>rowid</code>. <code>WITHOUT ROWID</code> tables omit this implicit column.",
  ["L0_primitives"])

c("Fundamentals", "What is a typical SQLite database file size limit?",
  "Up to <b>281 TB</b> (2^47 bytes = 140 TB per database, ~2^48 with tuning). Most practical limits are much lower. Individual rows can be up to ~1 GB. Default maximum number of attached databases is 10.",
  ["L0_primitives"])

# =============================================
# 02 — CORE OPERATIONS (L1 Mechanics: CLI & DDL basics)
# =============================================

c("CoreOps", "How do you open/create a database with the <code>sqlite3</code> CLI?",
  "<code>sqlite3 mydatabase.db</code><br>Creates the file if it doesn't exist, opens it if it does. Use <code>sqlite3 :memory:</code> for a transient in-memory DB. Use <code>sqlite3 ''</code> for a temporary on-disk database that is deleted when closed.",
  ["L1_mechanics"])

c("CoreOps", "How do you list all tables in the sqlite3 CLI?",
  "<code>.tables</code> — lists all user tables.<br><code>.tables '%pattern%'</code> — filter by pattern.<br><code>SELECT name FROM sqlite_master WHERE type='table';</code> — SQL equivalent.",
  ["L1_mechanics"])

c("CoreOps", "How do you view a table's schema in the sqlite3 CLI?",
  "<code>.schema tablename</code> — shows the CREATE TABLE statement.<br><code>.schema</code> — shows schema for all tables, indexes, views, triggers.<br><code>.schema '%pat%'</code> — filter by pattern.",
  ["L1_mechanics"])

c("CoreOps", "What does <code>.headers on</code> do in sqlite3 CLI?",
  "Shows <b>column names</b> as the first row of query output. Without it, only data rows are shown. Usually paired with <code>.mode column</code> for readable table output.",
  ["L1_mechanics"])

c("CoreOps", "What CLI modes are available with <code>.mode</code>?",
  "<ul><li><b>list</b> — default, pipe-separated</li><li><b>csv</b> — comma-separated</li><li><b>column</b> — aligned columns</li><li><b>html</b> — HTML table</li><li><b>insert</b> — INSERT statements</li><li><b>json</b> — JSON array</li><li><b>line</b> — one value per line</li><li><b>markdown</b> — Markdown table</li><li><b>tabs</b> — tab-separated</li><li><b>quote</b> — SQL-quoted values</li></ul>",
  ["L1_mechanics"])

c("CoreOps", "How do you export query results to a file in sqlite3 CLI?",
  "<code>.output filename.txt</code> — redirect subsequent output to file.<br><code>.once filename.txt</code> — redirect only the next query result.<br><code>.output</code> — reset output to stdout.<br>Combine with <code>.mode csv</code> then a <code>SELECT</code> to export CSV.",
  ["L1_mechanics"])

c("CoreOps", "How do you dump/backup an entire database to SQL text?",
  "<code>.dump</code> — outputs the entire database as SQL statements (reproducible schema + data).<br><code>.dump tablename</code> — dumps only that table.<br><code>.output backup.sql</code> then <code>.dump</code> to save to file. Restore with <code>.read backup.sql</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you import a CSV file into a table?",
  "<code>.mode csv</code><br><code>.import data.csv tablename</code><br>For CSV with headers: <code>.import --csv --skip 1 data.csv tablename</code>. Table must already exist. Use <code>.separator</code> to change delimiter for TSV etc.",
  ["L1_mechanics"])

c("CoreOps", "How do you execute SQL from a file in sqlite3 CLI?",
  "<code>.read script.sql</code> — reads and executes SQL from a file.<br>From shell: <code>sqlite3 my.db &lt; script.sql</code><br>Or: <code>sqlite3 my.db \"$(cat script.sql)\"</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>.backup</code> and <code>.clone</code> in sqlite3 CLI?",
  "<code>.backup backup.db</code> — creates a backup copy (online, consistent snapshot even during writes).<br><code>.clone newdb.db</code> — copies current database into a new file (creates if not exists). Both are online operations.",
  ["L1_mechanics"])

c("CoreOps", "What is a PRAGMA statement?",
  "A SQLite-specific SQL statement for <b>querying and modifying the database's operational parameters</b>. <code>PRAGMA journal_mode=WAL;</code> (set), <code>PRAGMA journal_mode;</code> (get). Controls page_size, cache_size, foreign_keys, synchronous, etc.",
  ["L1_mechanics"])

c("CoreOps", "What are the most important PRAGMA settings?",
  "<ul><li><code>PRAGMA journal_mode=WAL;</code> — enable WAL for concurrency</li><li><code>PRAGMA foreign_keys=ON;</code> — enforce FK constraints</li><li><code>PRAGMA synchronous=NORMAL;</code> — balance durability vs speed</li><li><code>PRAGMA cache_size=-8000;</code> — set cache in KB (negative = KB)</li><li><code>PRAGMA busy_timeout=5000;</code> — wait 5s instead of immediate SQLITE_BUSY</li><li><code>PRAGMA mmap_size=268435456;</code> — 256MB memory-mapped I/O</li></ul>",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>datetime()</code> functions in SQLite?",
  "<code>datetime('now')</code> — current UTC datetime<br><code>datetime('now', '+1 day')</code> — modifier<br><code>date('now')</code> — date only<br><code>time('now')</code> — time only<br><code>strftime('%Y-%m-%d', 'now')</code> — custom format<br><code>julianday('now')</code> — Julian day number<br><code>unixepoch('now')</code> — Unix timestamp",
  ["L1_mechanics"])

c("CoreOps", "How do you store dates/times in SQLite? (Three formats)",
  "<ol><li><b>TEXT</b> as ISO-8601: <code>'2024-01-15 10:30:00'</code></li><li><b>REAL</b> as Julian day number: <code>2460324.5</code></li><li><b>INTEGER</b> as Unix timestamp: <code>1705314600</code></li></ol>All <code>datetime()</code> functions work with any format. SQLite has no native DATE/TIME type.",
  ["L1_mechanics"])

c("CoreOps", "What is the <code>typeof()</code> function?",
  "Returns the <b>storage class</b> of a value: <code>'null', 'integer', 'real', 'text', 'blob'</code>. Example: <code>SELECT typeof(42)</code> → <code>'integer'</code>. <code>SELECT typeof(3.14)</code> → <code>'real'</code>. Useful for debugging type affinity surprises.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a table in SQLite?",
  "<code>CREATE TABLE users (</code><br><code>  id INTEGER PRIMARY KEY,</code><br><code>  name TEXT NOT NULL,</code><br><code>  email TEXT UNIQUE,</code><br><code>  age INTEGER CHECK(age &gt;= 0),</code><br><code>  created_at TEXT DEFAULT (datetime('now'))</code><br><code>);</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you insert data into a table?",
  "<code>INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 30);</code><br><code>INSERT INTO users VALUES (NULL, 'Bob', 'bob@x.com', 25, datetime('now'));</code><br><code>INSERT INTO users (name) VALUES ('Charlie');</code><br>Multiple rows: <code>INSERT INTO users (name) VALUES ('A'), ('B'), ('C');</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you update rows?",
  "<code>UPDATE users SET age = 31 WHERE name = 'Alice';</code><br><code>UPDATE users SET age = age + 1;</code> — increment all<br><code>UPDATE users SET email = 'new@x.com', age = 40 WHERE id = 1;</code><br><b>Always use WHERE</b> unless you intend to update all rows.",
  ["L1_mechanics"])

c("CoreOps", "How do you delete rows?",
  "<code>DELETE FROM users WHERE id = 5;</code><br><code>DELETE FROM users;</code> — deletes ALL rows (use <code>WHERE</code>!)<br>After deleting all rows, <code>AUTOINCREMENT</code> still won't reuse old rowids — use <code>DELETE FROM</code> followed by <code>VACUUM</code> or plain <code>INTEGER PRIMARY KEY</code> (without AUTOINCREMENT) to allow rowid reuse.",
  ["L1_mechanics"])

# =============================================
# 03 — QUERYING DATA (L1 Mechanics)
# =============================================

c("Querying", "Write a basic SELECT with WHERE, ORDER BY, LIMIT.",
  "<code>SELECT name, age FROM users</code><br><code>WHERE age &gt; 18</code><br><code>ORDER BY age DESC, name ASC</code><br><code>LIMIT 10 OFFSET 20;</code><br>Returns columns name and age for adults, ordered by age descending with pagination.",
  ["L1_mechanics"])

c("Querying", "What does <code>DISTINCT</code> do?",
  "Removes duplicate rows from the result set. <code>SELECT DISTINCT city FROM users;</code> — list unique cities. <code>SELECT COUNT(DISTINCT city) FROM users;</code> — count unique cities. <code>DISTINCT</code> applies to all selected columns combined.",
  ["L1_mechanics"])

c("Querying", "How do <code>LIKE</code> and <code>GLOB</code> differ?",
  "<code>LIKE</code> — SQL pattern matching with <code>%</code> (any chars) and <code>_</code> (single char). <b>Case-insensitive for ASCII</b>. <code>WHERE name LIKE 'A%'</code>.<br><code>GLOB</code> — Unix-style glob with <code>*</code> (any chars) and <code>?</code> (single char). <b>Case-sensitive</b>. <code>WHERE name GLOB 'A*'</code>.",
  ["L1_mechanics"])

c("Querying", "How to use <code>IN</code> and <code>NOT IN</code>?",
  "<code>SELECT * FROM users WHERE city IN ('Prague', 'Brno', 'Ostrava');</code><br><code>SELECT * FROM users WHERE id NOT IN (SELECT banned_user_id FROM bans);</code><br>Works with both explicit lists and subqueries.",
  ["L1_mechanics"])

c("Querying", "How to use <code>BETWEEN</code>?",
  "<code>SELECT * FROM orders WHERE total BETWEEN 100 AND 500;</code><br>Equivalent to: <code>WHERE total &gt;= 100 AND total &lt;= 500</code>. Works with numbers, dates, text. <code>NOT BETWEEN</code> for the inverse.",
  ["L1_mechanics"])

c("Querying", "How to handle NULL in queries?",
  "<code>IS NULL</code> and <code>IS NOT NULL</code> — correct way. <code>= NULL</code> always returns NULL (not true), because NULL means unknown. <code>SELECT * FROM users WHERE email IS NOT NULL;</code>. <code>COALESCE(x, default)</code> returns first non-NULL. <code>IFNULL(x, default)</code> is a 2-arg shorthand.",
  ["L1_mechanics"])

c("Querying", "What is a subquery?",
  "A <code>SELECT</code> nested inside another query. <code>SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE total &gt; 1000);</code>. Can appear in FROM (derived table), WHERE (with IN/EXISTS), or SELECT list (scalar subquery).",
  ["L1_mechanics"])

c("Querying", "What are aggregate functions in SQLite?",
  "<code>COUNT(*)</code> — number of rows<br><code>COUNT(col)</code> — count non-NULL values<br><code>SUM(col)</code> — total sum<br><code>AVG(col)</code> — average<br><code>MAX(col)</code> / <code>MIN(col)</code> — maximum/minimum<br><code>GROUP_CONCAT(col, ',')</code> — concatenate values<br><code>TOTAL(col)</code> — like SUM but returns 0.0 for NULL",
  ["L1_mechanics"])

c("Querying", "How does <code>GROUP BY</code> work?",
  "Groups rows that have the same values in specified columns. <code>SELECT city, COUNT(*), AVG(age) FROM users GROUP BY city;</code>. Every non-aggregated column in SELECT must be in GROUP BY. Use <code>HAVING</code> to filter groups (like WHERE for aggregated rows).",
  ["L1_mechanics"])

c("Querying", "What does <code>HAVING</code> do?",
  "Filters <b>groups</b> after aggregation, whereas <code>WHERE</code> filters rows before aggregation. <code>SELECT city, COUNT(*) FROM users GROUP BY city HAVING COUNT(*) &gt; 5;</code>. Can reference aggregate functions; WHERE cannot.",
  ["L1_mechanics"])

c("Querying", "What are the JOIN types in SQLite?",
  "<ul><li><b>INNER JOIN</b> — rows where condition matches in both tables</li><li><b>LEFT JOIN</b> — all rows from left table, NULL for unmatched right</li><li><b>CROSS JOIN</b> — Cartesian product of both tables</li><li><b>NATURAL JOIN</b> — auto-join on columns with same names (avoid)</li></ul>SQLite does not support RIGHT JOIN or FULL OUTER JOIN.",
  ["L1_mechanics"])

c("Querying", "Write an INNER JOIN example.",
  "<code>SELECT users.name, orders.total</code><br><code>FROM users</code><br><code>INNER JOIN orders ON users.id = orders.user_id</code><br><code>WHERE orders.total &gt; 100;</code><br>Returns only users who have matching orders with total > 100.",
  ["L1_mechanics"])

c("Querying", "Write a LEFT JOIN example.",
  "<code>SELECT u.name, COUNT(o.id) AS order_count</code><br><code>FROM users u</code><br><code>LEFT JOIN orders o ON u.id = o.user_id</code><br><code>GROUP BY u.id</code><br><code>ORDER BY order_count DESC;</code><br>Returns ALL users, even those with no orders (order_count = 0).",
  ["L1_mechanics"])

c("Querying", "What are set operations: UNION, INTERSECT, EXCEPT?",
  "<code>UNION</code> — combines results, removes duplicates<br><code>UNION ALL</code> — combines results, keeps duplicates (faster)<br><code>INTERSECT</code> — rows present in both queries<br><code>EXCEPT</code> — rows in first query but not second<br>All set operations require same number and type of columns in both SELECTs.",
  ["L1_mechanics"])

c("Querying", "What is a CTE (Common Table Expression)?",
  "A <b>named temporary result set</b> defined with <code>WITH</code>:<br><code>WITH cte_name AS (SELECT ...)</code><br><code>SELECT * FROM cte_name;</code><br>Can be referenced multiple times in the same query. Supports recursive CTEs: <code>WITH RECURSIVE</code>. Makes complex queries readable and reusable.",
  ["L1_mechanics"])

c("Querying", "Write a recursive CTE example.",
  "<code>WITH RECURSIVE counter(n) AS (</code><br><code>  SELECT 1</code><br><code>  UNION ALL</code><br><code>  SELECT n + 1 FROM counter WHERE n &lt; 10</code><br><code>) SELECT * FROM counter;</code><br>Generates numbers 1 through 10. Recursive CTEs are powerful for tree traversal, graph queries, and series generation.",
  ["L1_mechanics"])

c("Querying", "What are window functions in SQLite?",
  "Functions that operate across a <b>window</b> of related rows without collapsing them (unlike GROUP BY). <code>SELECT name, salary, RANK() OVER (ORDER BY salary DESC) FROM employees;</code>. Supported: <code>ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE(), LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE(), SUM/AVG/COUNT OVER()</code>. Available since SQLite 3.25.",
  ["L1_mechanics"])

c("Querying", "Write a window function example with <code>PARTITION BY</code>.",
  "<code>SELECT name, department, salary,</code><br><code>  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank</code><br><code>FROM employees;</code><br>Ranks employees by salary <b>within each department</b>. Each partition resets the ranking.",
  ["L1_mechanics"])

c("Querying", "What is <code>UPSERT</code> (ON CONFLICT) in SQLite?",
  "Atomic insert-or-update: <code>INSERT INTO users (id, name) VALUES (1, 'Alice')</code><br><code>ON CONFLICT(id) DO UPDATE SET name = excluded.name;</code><br>If row with id=1 exists, update name; otherwise insert. <code>excluded</code> refers to the would-be-inserted row. <code>DO NOTHING</code> to silently skip conflicts.",
  ["L1_mechanics"])

c("Querying", "How do you use <code>json_extract()</code> in queries?",
  "<code>SELECT json_extract(data, '$.name') FROM logs;</code> — extract scalar value.<br><code>SELECT json_extract(data, '$.items[0].id') FROM logs;</code> — array indexing.<br><code>SELECT * FROM users, json_each(users.tags)</code> — iterate JSON array.<br>Requires json1 extension (enabled by default in most builds).",
  ["L1_mechanics"])

c("Querying", "How to concatenate strings in SQLite?",
  "Use the <code>||</code> operator: <code>SELECT 'Hello' || ' ' || 'World';</code> → <code>Hello World</code>.<br><code>SELECT name || ' &lt;' || email || '&gt;' FROM users;</code> → <code>Alice &lt;alice@x.com&gt;</code>.<br>Equivalent to <code>CONCAT()</code> in other DBs. NULL || 'anything' = NULL; use <code>COALESCE()</code> to handle.",
  ["L1_mechanics"])

c("Querying", "How do you use <code>CASE</code> expressions?",
  "<code>SELECT name,</code><br><code>  CASE</code><br><code>    WHEN score &gt;= 90 THEN 'A'</code><br><code>    WHEN score &gt;= 80 THEN 'B'</code><br><code>    WHEN score &gt;= 70 THEN 'C'</code><br><code>    ELSE 'F'</code><br><code>  END AS grade</code><br><code>FROM students;</code>",
  ["L1_mechanics"])

# =============================================
# 04 — SCHEMA DESIGN (L2 Composition)
# =============================================

c("Schema", "What are the main table constraints in SQLite?",
  "<ul><li><b>PRIMARY KEY</b> — unique identifier</li><li><b>AUTOINCREMENT</b> — never reuse rowids</li><li><b>NOT NULL</b> — value required</li><li><b>UNIQUE</b> — no duplicate values</li><li><b>CHECK</b> — custom validation expression</li><li><b>DEFAULT</b> — fallback value</li><li><b>FOREIGN KEY</b> — referential integrity</li></ul>",
  ["L2_composition"])

c("Schema", "What is the difference between <code>INTEGER PRIMARY KEY</code> and <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>?",
  "<b>INTEGER PRIMARY KEY</b>: becomes alias for <code>rowid</code>. If you insert NULL, SQLite assigns the next auto-generated rowid (max(rowid) + 1). Deleted rowids may be reused.<br><b>AUTOINCREMENT</b>: guarantees rowids are strictly increasing and never reused. Uses <code>sqlite_sequence</code> table for tracking. Slightly slower and uses extra space. Recommended only when reuse prevention matters.",
  ["L2_composition"])

c("Schema", "How do you enforce foreign keys in SQLite?",
  "Foreign keys are <b>not enforced by default</b>. Must enable with <code>PRAGMA foreign_keys = ON;</code>. Must be set per-connection. Without this, FK constraints are parsed and stored but <b>ignored</b>. Most common SQLite gotcha.",
  ["L2_composition"])

c("Schema", "Write a CREATE TABLE with FOREIGN KEY.",
  "<code>CREATE TABLE orders (</code><br><code>  id INTEGER PRIMARY KEY,</code><br><code>  user_id INTEGER NOT NULL,</code><br><code>  total REAL,</code><br><code>  FOREIGN KEY (user_id) REFERENCES users(id)</code><br><code>    ON DELETE CASCADE</code><br><code>    ON UPDATE SET NULL</code><br><code>);</code><br>Options: CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION.",
  ["L2_composition"])

c("Schema", "What are <code>WITHOUT ROWID</code> tables?",
  "Tables that <b>omit the implicit rowid column</b>. Must have a PRIMARY KEY (single or composite). Data is stored in a B-tree keyed by the primary key — faster for primary key lookups and range scans. Smaller storage (no extra rowid index). <code>CREATE TABLE t(a TEXT, b INT, PRIMARY KEY(a,b)) WITHOUT ROWID;</code>",
  ["L2_composition"])

c("Schema", "When should you use a <code>WITHOUT ROWID</code> table?",
  "Use when: (1) The table has a meaningful primary key (natural or composite). (2) You primarily query by primary key. (3) You want to reduce storage and lookups. Do NOT use when: the primary key is large, you need AUTOINCREMENT, or you frequently scan without using the PK.",
  ["L2_composition"])

c("Schema", "What are <code>STRICT</code> tables? (SQLite 3.37+)",
  "Tables that enforce declared column types at insert time. <code>CREATE TABLE users (id INT, name TEXT) STRICT;</code>. Inserting a string into an INT column will raise an error. Without STRICT, SQLite uses flexible type affinity. Recommended for new applications to catch type bugs early.",
  ["L2_composition"])

c("Schema", "What is a generated column? (SQLite 3.31+)",
  "A column whose value is computed from other columns. <code>CREATE TABLE items (price REAL, tax REAL, total REAL GENERATED ALWAYS AS (price + tax) VIRTUAL);</code>. <code>VIRTUAL</code> — computed on read (no storage). <code>STORED</code> — computed on write (takes up space but indexable). Cannot be directly inserted or updated.",
  ["L2_composition"])

c("Schema", "What is a VIEW in SQLite?",
  "A virtual table defined by a <code>SELECT</code> query. <code>CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;</code>. Views are read-only in SQLite. They don't store data — the underlying query runs each time the view is referenced. <code>DROP VIEW view_name;</code> to remove.",
  ["L2_composition"])

c("Schema", "What is a TRIGGER in SQLite?",
  "A <b>named database object</b> that automatically executes SQL when a specified table event occurs. Events: <code>BEFORE/AFTER/INSTEAD OF</code> + <code>INSERT/UPDATE/DELETE</code>. <code>FOR EACH ROW</code> triggers fire once per affected row (with OLD/NEW references). <code>FOR EACH STATEMENT</code> fires once per SQL statement (not supported in SQLite).",
  ["L2_composition"])

c("Schema", "Write a trigger that logs when a user is deleted.",
  "<code>CREATE TRIGGER log_user_delete</code><br><code>AFTER DELETE ON users</code><br><code>FOR EACH ROW</code><br><code>BEGIN</code><br><code>  INSERT INTO audit_log (action, user_name, timestamp)</code><br><code>  VALUES ('DELETE', OLD.name, datetime('now'));</code><br><code>END;</code>",
  ["L2_composition"])

c("Schema", "What are <code>OLD</code> and <code>NEW</code> in triggers?",
  "<b>OLD</b>: reference to the row <b>before</b> the change. Available in DELETE and UPDATE.<br><b>NEW</b>: reference to the row <b>after</b> the change. Available in INSERT and UPDATE.<br>Not available in <code>INSTEAD OF</code> triggers on views (use BEFORE/AFTER on views).",
  ["L2_composition"])

c("Schema", "What is <code>INSTEAD OF</code> trigger?",
  "A trigger on a VIEW that intercepts INSERT/UPDATE/DELETE and performs custom logic. Makes a view 'writable'. <code>CREATE TRIGGER insert_active INSTEAD OF INSERT ON active_users ...</code>. Only valid on views, not tables.",
  ["L2_composition"])

c("Schema", "What is a CHECK constraint?",
  "A validation rule enforced on INSERT/UPDATE. <code>CREATE TABLE products (price REAL CHECK(price &gt; 0), stock INTEGER CHECK(stock &gt;= 0));</code>. Complex: <code>CHECK(start_date &lt; end_date)</code>. Table-level: <code>CHECK(price IS NOT NULL OR discount_reason IS NOT NULL)</code>. Disabled by default in legacy mode (always enforce in modern SQLite).",
  ["L2_composition"])

c("Schema", "What is FTS5 (Full-Text Search)?",
  "A <b>virtual table</b> extension for full-text indexing and search. <code>CREATE VIRTUAL TABLE docs USING fts5(title, body);</code>. Query with <code>MATCH</code>: <code>SELECT * FROM docs WHERE docs MATCH 'sqlite AND tutorial';</code>. Supports: ranking, highlighting, prefix queries, phrase queries, BM25 ranking, custom tokenizers.",
  ["L2_composition"])

c("Schema", "Write an FTS5 search with relevance ranking.",
  "<code>CREATE VIRTUAL TABLE articles USING fts5(title, content);</code><br><code>SELECT title, snippet(articles, 1, '&lt;b&gt;', '&lt;/b&gt;', '...', 32), bm25(articles, 0)</code><br><code>FROM articles</code><br><code>WHERE articles MATCH 'sqlite'</code><br><code>ORDER BY bm25(articles, 0);</code>",
  ["L2_composition"])

c("Schema", "What is the R*Tree virtual table?",
  "A <b>spatial index</b> extension for range queries over numeric intervals. <code>CREATE VIRTUAL TABLE geo USING rtree(id, minX, maxX, minY, maxY);</code>. Efficiently answers queries like 'find all rectangles overlapping a given region'. Useful for geospatial, bounding-box searches, time-range overlaps. Much faster than B-tree for multi-dimensional ranges.",
  ["L2_composition"])

c("Schema", "What is the json1 extension?",
  "SQLite extension providing <b>JSON functions</b>. <code>json_extract()</code> — get value by path. <code>json_set()</code> — modify value. <code>json_array()</code> — create array. <code>json_object()</code> — create object. <code>json_each()</code> — iterate. <code>json_tree()</code> — recursive tree walk. <code>json_group_array()</code> — aggregate into JSON array. <code>json_valid()</code> — validate JSON.",
  ["L2_composition"])

c("Schema", "How to use <code>json_each()</code> to expand a JSON array?",
  "<code>SELECT u.name, je.value</code><br><code>FROM users u, json_each(u.tags) je</code><br><code>WHERE json_valid(u.tags);</code><br>Expands each user's JSON array of tags into separate rows. <code>json_each</code> returns columns: <code>key, value, type, atom, id, parent, fullkey, path</code>.",
  ["L2_composition"])

c("Schema", "What does <code>ALTER TABLE</code> support in SQLite?",
  "Limited compared to other DBs:<br><code>ALTER TABLE t RENAME TO new_name;</code><br><code>ALTER TABLE t ADD COLUMN col TYPE;</code><br><code>ALTER TABLE t RENAME COLUMN old TO new;</code> (3.25+)<br><code>ALTER TABLE t DROP COLUMN col;</code> (3.35+)<br>Cannot: drop constraints, change column type, reorder columns. Workaround: create new table, copy data, drop old, rename.",
  ["L2_composition"])

c("Schema", "How to add a foreign key constraint to an existing table?",
  "SQLite doesn't support <code>ALTER TABLE ... ADD CONSTRAINT</code>. Workaround: (1) <code>PRAGMA foreign_keys=OFF;</code> (2) Create new table with FK constraint. (3) Copy data. (4) Drop old table. (5) Rename new table. (6) <code>PRAGMA foreign_keys=ON;</code>",
  ["L2_composition"])

# =============================================
# 05 — PERFORMANCE & INDEXES (L3 Design)
# =============================================

c("Performance", "How do you create an index in SQLite?",
  "<code>CREATE INDEX idx_users_email ON users(email);</code><br><code>CREATE UNIQUE INDEX idx_users_email ON users(email);</code><br><code>CREATE INDEX idx_users_city_age ON users(city, age);</code> — composite index.<br><code>CREATE INDEX idx_users_lower_name ON users(LOWER(name));</code> — expression index (3.9+).<br><code>DROP INDEX idx_users_email;</code>",
  ["L3_design"])

c("Performance", "What is a partial index?",
  "An index on a <b>subset of rows</b>: <code>CREATE INDEX idx_active_users ON users(email) WHERE active = 1;</code>. Smaller, faster to scan, faster to maintain. Only used when the WHERE clause in the query matches the index's WHERE clause.",
  ["L3_design"])

c("Performance", "What is a covering index?",
  "An index that contains <b>all columns</b> needed by a query, so SQLite can answer the query from the index alone without touching the main table. <code>CREATE INDEX idx_cov ON orders(user_id, total, created_at);</code>. <code>SELECT user_id, total FROM orders WHERE user_id = 5;</code> uses the index only (no table access). Speeds up queries dramatically.",
  ["L3_design"])

c("Performance", "What is an expression index?",
  "An index on an expression rather than a column value. <code>CREATE INDEX idx_name_lower ON users(LOWER(name));</code>. Useful for queries like <code>SELECT * FROM users WHERE LOWER(name) = 'alice';</code>. Also supports <code>COALESCE</code> and <code>json_extract</code> expressions.",
  ["L3_design"])

c("Performance", "What does <code>EXPLAIN QUERY PLAN</code> do?",
  "Shows the <b>execution strategy</b> SQLite chooses: which tables, which indexes, scan order, join algorithm. <code>EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = 'a@b.com';</code>. Output shows <code>SEARCH TABLE ... USING COVERING INDEX</code> or <code>SCAN TABLE</code> (bad). Essential for query optimization.",
  ["L3_design"])

c("Performance", "What does the <code>ANALYZE</code> command do?",
  "Collects <b>statistics</b> about table/index contents and stores them in <code>sqlite_stat1</code>. The query planner uses these statistics to choose the best index and join order. Run periodically after significant data changes: <code>ANALYZE;</code> or <code>ANALYZE table_name;</code>.",
  ["L3_design"])

c("Performance", "When should you <b>NOT</b> create an index?",
  "<ul><li>On very small tables (full scan is faster)</li><li>On columns with few distinct values (low cardinality, e.g., boolean)</li><li>On columns frequently updated (index maintenance cost)</li><li>When the table is mostly written, seldom queried</li><li>On every column (indexes consume space, slow down writes)</li></ul>",
  ["L3_design"])

c("Performance", "How do you detect a full table scan?",
  "Use <code>EXPLAIN QUERY PLAN</code>. If you see <code>SCAN TABLE</code> on a large table, you likely need an index. Example: <code>EXPLAIN QUERY PLAN SELECT * FROM users WHERE email='x';</code> without an index on <code>email</code> shows <code>SCAN TABLE users</code> — linear scan of all rows.",
  ["L3_design"])

c("Performance", "What does <code>VACUUM</code> do?",
  "Rebuilds the database file to reclaim <b>fragmentation and free space</b>. Defragments data, repacks pages, and recovers space from deleted rows. <code>VACUUM;</code>. <code>VACUUM INTO 'file.db';</code> (3.27+) creates a vacuumed copy. Consider using <code>PRAGMA auto_vacuum=INCREMENTAL</code> for automatic space reclamation.",
  ["L3_design"])

c("Performance", "What is <code>PRAGMA optimize</code>?",
  "A no-op PRAGMA that tells SQLite to run <code>ANALYZE</code> on tables that might benefit from updated statistics. <code>PRAGMA optimize;</code>. Designed to be called on application startup or periodically. SQLite decides internally whether to actually do work — safe to call frequently.",
  ["L3_design"])

c("Performance", "How to use an in-memory database?",
  "Open with <code>:memory:</code> as filename: <code>sqlite3 :memory:</code> or <code>sqlite3_open(\":memory:\")</code>. Entire database lives in RAM — no disk I/O. Fast for temp data, caching, testing. Lost when connection closes unless backed up to disk. Multiple <code>:memory:</code> connections are independent (each gets its own DB).",
  ["L3_design"])

c("Performance", "What is <code>PRAGMA cache_size</code>?",
  "Sets the in-memory page cache size. <code>PRAGMA cache_size = -8000;</code> — 8000 KB (8 MB) cache. Negative values mean kilobytes. Positive values mean number of pages. Larger cache = more data in memory = fewer disk reads. Default is 2 MB (-2000).",
  ["L3_design"])

c("Performance", "What is <code>PRAGMA page_size</code>?",
  "Sets the database page size in bytes. <code>PRAGMA page_size = 4096;</code> (default). Powers of 2: 512 to 65536. Larger pages reduce B-tree depth but increase read amplification for point queries. Must be set before creating any tables. 4096 is a good default for most workloads.",
  ["L3_design"])

c("Performance", "What is <code>PRAGMA temp_store</code>?",
  "Controls where temporary tables and indices are stored. <code>PRAGMA temp_store = 0;</code> — default (file). <code>PRAGMA temp_store = 1;</code> — file (explicit). <code>PRAGMA temp_store = 2;</code> — memory. <code>PRAGMA temp_store = 3;</code> — memory (always, even if too large). Using memory for temp storage can speed up complex sorts and joins.",
  ["L3_design"])

c("Performance", "What is <code>PRAGMA mmap_size</code>?",
  "Enables <b>memory-mapped I/O</b> for reading the database file. <code>PRAGMA mmap_size = 268435456;</code> (256 MB). The OS maps database pages directly into process memory, avoiding read() system calls. Great for read-heavy workloads. Set to 0 to disable. Beware: mmap'd region counts toward process memory.",
  ["L3_design"])

c("Performance", "What is a composite/multi-column index and how does ordering matter?",
  "Index on multiple columns: <code>CREATE INDEX idx ON t(a, b, c);</code>. The index can be used for queries filtering on: <code>a</code>, <code>a AND b</code>, or <code>a AND b AND c</code>. Cannot use the index for queries only on <code>b</code> or <code>c</code> (must use leading columns). <b>Order columns from most selective to least selective</b>.",
  ["L3_design"])

c("Performance", "How to optimize queries with <code>LIMIT</code> and <code>OFFSET</code>?",
  "<code>OFFSET N</code> requires scanning N rows even though they aren't returned. For large offsets, use <b>keyset pagination</b>: <code>SELECT * FROM t WHERE id &gt; :last_id ORDER BY id LIMIT 20;</code>. Much faster than <code>LIMIT 20 OFFSET 100000</code>.",
  ["L3_design"])

c("Performance", "What is the difference between <code>COUNT(*)</code> and <code>COUNT(col)</code>?",
  "<code>COUNT(*)</code> counts rows (includes NULLs). <code>COUNT(col)</code> counts non-NULL values of col. For tables without WHERE, <code>COUNT(*)</code> is a fast operation in SQLite (reads the B-tree metadata). <code>COUNT(col)</code> may cause a full scan. Use <code>COUNT(*)</code> when you just need a row count.",
  ["L3_design"])

# =============================================
# 06 — TRANSACTIONS & LOCKING (L3 Design)
# =============================================

c("Transactions", "How do transactions work in SQLite?",
  "<code>BEGIN;</code> — start transaction<br><code>COMMIT;</code> — save changes permanently<br><code>ROLLBACK;</code> — revert all changes since BEGIN<br>By default, every statement outside a transaction is wrapped in an implicit auto-commit transaction. Explicit transactions group multiple changes atomically.",
  ["L3_design"])

c("Transactions", "What are savepoints?",
  "Nested transaction markers within a larger transaction. <code>SAVEPOINT sp1;</code> — create savepoint. <code>RELEASE sp1;</code> — commit savepoint (merge into parent). <code>ROLLBACK TO sp1;</code> — undo to savepoint without rolling back the entire transaction. Allows partial rollbacks.",
  ["L3_design"])

c("Transactions", "What are the three transaction types: DEFERRED, IMMEDIATE, EXCLUSIVE?",
  "<ul><li><b>DEFERRED</b> (default): acquires a write lock only when first write occurs. Readers can continue until then.</li><li><b>IMMEDIATE</b>: acquires RESERVED lock immediately. Prevents other writers from starting, but readers can still read.</li><li><b>EXCLUSIVE</b>: waits for all readers to finish, then acquires EXCLUSIVE lock. No concurrent readers during transaction.</li></ul>Use <code>BEGIN IMMEDIATE;</code> for write transactions to avoid <code>SQLITE_BUSY</code> on commit.",
  ["L3_design"])

c("Transactions", "What are the WAL journal mode versions?",
  "<b>DELETE</b> (default in rollback mode): journal file is deleted on commit.<br><b>TRUNCATE</b>: journal file truncated to zero (faster on some systems).<br><b>PERSIST</b>: journal file header zeroed (faster in some cases).<br><b>MEMORY</b>: journal in RAM only (fast but not crash-safe).<br><b>WAL</b>: write-ahead log — concurrent reads &amp; writes.<br><b>OFF</b>: no journal (dangerous — corruption on power loss).",
  ["L3_design"])

c("Transactions", "How does WAL mode improve concurrency?",
  "In WAL mode, <b>readers do not block writers and writers do not block readers</b>. Readers read the last checkpointed (committed) state from the main database file. Writers append new changes to the WAL. Only checkpoint operations (moving WAL data back to the main DB) require synchronization.",
  ["L3_design"])

c("Transactions", "What are the locking states in SQLite?",
  "<ol><li><b>UNLOCKED</b> — no locks</li><li><b>SHARED</b> — reading (multiple readers allowed)</li><li><b>RESERVED</b> — writing intent (one writer, readers still ok)</li><li><b>PENDING</b> — waiting for readers to finish before exclusive lock</li><li><b>EXCLUSIVE</b> — writing (no other access)</li></ol>WAL mode skips PENDING — goes directly from RESERVED to EXCLUSIVE.",
  ["L3_design"])

c("Transactions", "What is <code>busy_timeout</code>?",
  "PRAGMA that sets how long SQLite waits when a lock is held (returns <code>SQLITE_BUSY</code> instead of immediate failure). <code>PRAGMA busy_timeout = 5000;</code> — wait up to 5 seconds for lock release. Sets an internal handler that sleeps and retries. Highly recommended for multi-process applications.",
  ["L3_design"])

c("Transactions", "What is <code>PRAGMA synchronous</code>?",
  "Controls how aggressively SQLite syncs data to disk via <code>fsync()</code>:<br><code>OFF</code> — no fsync (fast, unsafe on power loss)<br><code>NORMAL</code> — fsync at critical moments (good balance, WAL recommended)<br><code>FULL</code> — fsync at every commit (safest, slowest, default)<br><code>EXTRA</code> — like FULL plus extra syncs (paranoid level)",
  ["L3_design"])

c("Transactions", "What happens during an atomic commit in SQLite?",
  "SQLite ensures that an entire transaction is either <b>completely applied or completely rolled back</b>, even if the system crashes mid-write. In rollback-journal mode: write old page content to journal file before modifying the database file. On crash, journal is replayed to undo partial changes. In WAL mode: new content is in WAL; on crash, just discard partial WAL entries.",
  ["L3_design"])

c("Transactions", "How to handle concurrent writes in SQLite?",
  "<b>There is no concurrent writing</b> — only one writer at a time. Strategies: (1) Queue writes through a single writer thread/process. (2) Use WAL mode so readers aren't blocked during writes. (3) Use <code>busy_timeout</code> to gracefully wait for locks. (4) Design app so writes are fast (batch inserts, use transactions). (5) Shard data across multiple database files.",
  ["L3_design"])

c("Transactions", "What is <code>PRAGMA locking_mode</code>?",
  "Controls how file locks are managed:<br><code>NORMAL</code> — unlock database file after each read (default)<br><code>EXCLUSIVE</code> — hold an exclusive lock as long as the database is open. Prevents other connections entirely. Faster (no locking overhead) but only one connection allowed. Good for single-user apps.",
  ["L3_design"])

c("Transactions", "How does WAL checkpointing work?",
  "Checkpointing moves pages from the WAL file back into the main database file. Happens automatically when WAL reaches 1000 pages, or manually: <code>PRAGMA wal_checkpoint;</code>. Types: <b>PASSIVE</b> (auto, non-blocking), <b>FULL</b> (block until complete), <b>RESTART</b> (keep WAL after), <b>TRUNCATE</b> (truncate WAL to zero).",
  ["L3_design"])

c("Transactions", "What is 'writer starvation' in WAL mode?",
  "If readers keep the WAL open too long without a checkpoint, the WAL file grows unboundedly. A writer cannot perform a checkpoint while any reader is still holding pages in the WAL. Solution: <code>PRAGMA wal_autocheckpoint=1000;</code> (default), and ensure readers don't hold transactions open indefinitely.",
  ["L3_design"])

# =============================================
# 07 — GOTCHAS (L4 Diagnosis)
# =============================================

c("Gotchas", "What causes <code>SQLITE_BUSY</code> and how do you fix it?",
  "<b>Cause</b>: Another connection holds an incompatible lock (writing, or reading during a write in rollback-journal mode).<br><b>Fixes</b>: <ol><li>Enable WAL mode (<code>PRAGMA journal_mode=WAL;</code>)</li><li>Set <code>PRAGMA busy_timeout=5000;</code> to auto-retry</li><li>Use <code>BEGIN IMMEDIATE</code> for write transactions</li><li>Keep transactions short</li><li>Retry in application code with exponential backoff</li></ol>",
  ["L4_diagnosis"])

c("Gotchas", "What type affinity surprise happens when storing '123abc' in an INTEGER column?",
  "SQLite stores it <b>as-is</b> (as TEXT) because '123abc' cannot be converted to integer. No error. <code>SELECT typeof('123abc')</code> → <code>text</code>. An INTEGER affinity column tries to convert but fails — so it stores the original text. This is flexible typing at work. <b>Use STRICT tables to prevent this.</b>",
  ["L4_diagnosis"])

c("Gotchas", "What happens when you insert a non-integer into an <code>INTEGER PRIMARY KEY</code>?",
  "<code>INSERT INTO users (id, name) VALUES ('hello', 'Bob');</code><br>If 'hello' is not a valid integer, SQLite <b>stores it as-is</b> — the rowid column receives a generated integer value, but the <code>id</code> column (which aliases rowid) stores 'hello' as TEXT. This creates a confusing disconnect. STRICT tables catch this at insert time.",
  ["L4_diagnosis"])

c("Gotchas", "Why are foreign keys not enforced by default?",
  "Historical compatibility. SQLite was designed when FK enforcement was uncommon. <b>Must enable per-connection</b>: <code>PRAGMA foreign_keys = ON;</code>. If you forget, <code>DELETE FROM parent</code> succeeds even with child rows referencing it — data integrity silently violated. Test with <code>PRAGMA foreign_keys;</code> to verify.",
  ["L4_diagnosis"])

c("Gotchas", "Can you do schema changes (ALTER TABLE, CREATE INDEX) inside a transaction?",
  "<b>Yes, but be careful.</b> Some schema changes can be done inside transactions. However, in WAL mode, schema changes may cause 'schema changed' errors if another connection reads the old schema while a write transaction modifies it. In rollback-journal mode, schema changes outside transactions auto-commit immediately (breaking the transaction). Generally: do schema changes without concurrent connections.",
  ["L4_diagnosis"])

c("Gotchas", "What is the LIKE case sensitivity gotcha?",
  "<b>LIKE is case-insensitive for ASCII letters only</b> (A-Z). For Unicode characters (e.g., Č, ß, ά), LIKE is <b>case-sensitive</b>. <code>'café' LIKE 'CAFÉ'</code> may return false. Use <code>LOWER()</code> / <code>UPPER()</code> for consistent results, or ICU extension for full Unicode support.",
  ["L4_diagnosis"])

c("Gotchas", "How to detect and recover from a corrupted database?",
  "<b>Detection</b>: <code>PRAGMA integrity_check;</code> — returns errors if corrupted.<br><b>Recovery</b>: <ol><li><code>.dump</code> the good parts to SQL, create a fresh DB, <code>.read</code> back</li><li><code>.recover</code> (sqlite3 CLI, 3.31+) attempts to recover all possible data</li><li>Use backup files / Litestream replication</li><li>Set <code>PRAGMA journal_mode=WAL;</code> and <code>PRAGMA synchronous=NORMAL;</code> to reduce corruption risk</li></ol>",
  ["L4_diagnosis"])

c("Gotchas", "What are issues with decimal precision in SQLite?",
  "SQLite has no DECIMAL type. Use REAL (IEEE double) which is <b>approximate</b> — <code>0.1 + 0.2 != 0.3</code> in floating point. <b>Solutions</b>: (1) Store as <b>TEXT</b> and parse in application. (2) Store as <b>INTEGER</b> representing cents (integer arithmetic). (3) Use application-level decimal library. Never use REAL for money.",
  ["L4_diagnosis"])

c("Gotchas", "What are date/time storage gotchas?",
  "SQLite has no native DATE/TIME type. Common mistakes: (1) Storing as REAL (Julian day) and accidentally doing integer math. (2) Comparing ISO strings as text gives lexicographic order (works for YYYY-MM-DD but not all formats). (3) Timezone confusion — SQLite <code>datetime('now')</code> returns <b>UTC</b>, not local time. Store UTC, convert at display layer.",
  ["L4_diagnosis"])

c("Gotchas", "What happens with <code>NULL</code> in UNIQUE constraints?",
  "SQLite treats <code>NULLs</code> as <b>distinct from each other</b> for UNIQUE constraints. You can insert multiple rows with NULL in a UNIQUE column. This is per the SQL standard. Use <code>NOT NULL</code> if you don't want this behavior. Other databases (like SQL Server) may treat NULLs as equal for UNIQUE.",
  ["L4_diagnosis"])

c("Gotchas", "Why might queries be slow even with indexes?",
  "<ul><li><code>ANALYZE</code> not run — stale statistics confuse the query planner</li><li>Using <code>LIKE '%pattern%'</code> with leading <code>%</code> — cannot use index</li><li>Index on <code>LOWER(name)</code> but query uses <code>WHERE name = 'X'</code> (no LOWER)</li><li>Type mismatch: <code>WHERE id = '5'</code> when <code>id</code> is INTEGER (may skip index)</li><li>OR across columns with no composite index</li><li>Query planner chooses a table scan because the index is not selective enough</li></ul>",
  ["L4_diagnosis"])

c("Gotchas", "What happens with <code>LIMIT</code> without <code>ORDER BY</code>?",
  "Results are returned in <b>an arbitrary order</b> determined by the query plan (which can change). <code>SELECT * FROM users LIMIT 10;</code> may return different rows on different runs. Always use <code>ORDER BY</code> when you need deterministic results, even with <code>LIMIT</code>.",
  ["L4_diagnosis"])

c("Gotchas", "How does <code>VACUUM</code> affect rowids and <code>AUTOINCREMENT</code>?",
  "After <code>DELETE FROM table;</code> and <code>VACUUM;</code>, rowids may be reassigned starting from 1 for non-AUTOINCREMENT tables. For AUTOINCREMENT tables, rowids continue from the last used value. <code>VACUUM</code> effectively creates a new database file and copies data — rowids may be reassigned.",
  ["L4_diagnosis"])

c("Gotchas", "What is the implicit AUTOINCREMENT behavior of <code>INTEGER PRIMARY KEY</code>?",
  "<code>INTEGER PRIMARY KEY</code> (without AUTOINCREMENT) <b>auto-generates</b> rowid if you insert NULL — reusing deleted rowids. This means if you export/import data with explicit IDs, you may get conflicts. <code>AUTOINCREMENT</code> guarantees a strictly larger rowid for every new INSERT NULL, never reusing old ones.",
  ["L4_diagnosis"])

c("Gotchas", "Can you use multiple database files in one connection?",
  "Yes, with <code>ATTACH DATABASE 'other.db' AS other;</code>. Max 10 attached databases by default (compile-time limit). <code>DETACH DATABASE other;</code>. Queries can join across attached databases. <code>SELECT * FROM main.users JOIN other.orders ON ...;</code>. Caveat: locks are acquired on all attached databases during writes.",
  ["L4_diagnosis"])

c("Gotchas", "What happens with concurrent <code>.dump</code> and writes?",
  "<code>.dump</code> reads the database while other connections may be writing. In rollback-journal mode, a writer may block <code>.dump</code> with <code>SQLITE_BUSY</code>. In WAL mode, <code>.dump</code> sees a consistent snapshot from when it started reading — changes made after that point are not included. Use <code>.backup</code> for consistent backups.",
  ["L4_diagnosis"])

# =============================================
# 08 — EXPERT (L5 Opinion / L6 Innovation)
# =============================================

c("Expert", "When is SQLite a good choice over PostgreSQL?",
  "<b>Good for</b>: mobile apps (iOS/Android), desktop apps, embedded/IoT devices, edge computing, single-server web apps (&lt;100k requests/day), application file format, local development/sandboxes, CI/CD test databases.<br><b>Bad for</b>: multi-service architectures with many concurrent writers, large-scale analytics, applications needing row-level security, data warehouses.",
  ["L5_opinion"])

c("Expert", "What is Litestream?",
  "An open-source tool for <b>real-time streaming replication of SQLite databases</b> to S3/GCS/Azure Blob. Continuously ships WAL frames to object storage, enabling point-in-time recovery. <code>litestream replicate my.db s3://bucket/path</code>. Makes SQLite viable for production with automatic backups — 'like a CDN for your database'.",
  ["L5_opinion"])

c("Expert", "What is Turso / libSQL?",
  "<b>libSQL</b> is an open-source fork of SQLite with extra features: native network replication, vector search, wasm user-defined functions, and a server mode. <b>Turso</b> is the managed cloud platform built on libSQL — offers edge-replicated SQLite databases with automatic sync. SQLite-compatible wire protocol.",
  ["L5_opinion"])

c("Expert", "What is Cloudflare D1?",
  "Cloudflare's <b>serverless SQLite database</b> at the edge. Based on SQLite, runs at Cloudflare's edge locations globally. Accessed via Workers (Cloudflare's serverless functions). Provides automatic replication, backups, and a REST API. Limits: 2 GB per database, 100 databases per account.",
  ["L5_opinion"])

c("Expert", "Why is WAL mode recommended as an 'always-on' setting?",
  "<b>Reasons</b>: (1) Readers and writers can work concurrently — no <code>SQLITE_BUSY</code> for reads during writes. (2) Faster writes in most cases — append to WAL is sequential I/O. (3) Enables backup tools like Litestream. (4) Better behavior under most workloads. The only downside: multiple files (.db, .db-wal, .db-shm) and a slightly larger disk footprint.",
  ["L5_opinion"])

c("Expert", "Why are STRICT tables recommended for new applications?",
  "They <b>prevent type bugs</b> at the database level: an INSERT of 'hello' into an INTEGER column fails immediately instead of silently storing text. Catches bugs early. Makes schema self-documenting. However, they limit flexible typing (which is sometimes a feature for loosely-structured data). Available since SQLite 3.37.0 (2021).",
  ["L5_opinion"])

c("Expert", "What is the <code>busy_timeout</code> vs manual <code>SQLITE_BUSY</code> retry loop debate?",
  "<b>busy_timeout</b> — let SQLite's internal handler sleep-and-retry. Simple, works for most cases. But retries are not configurable (fixed delay pattern).<br><b>Manual retry</b> — catch <code>SQLITE_BUSY</code> in your code, sleep with exponential backoff, retry. Gives you control over backoff strategy, logging, max retries. Preferred when you need fine-grained control or when using connection pools.",
  ["L5_opinion"])

c("Expert", "What does 'SQLite as an application file format' mean?",
  "Instead of inventing a custom file format (JSON, XML, binary blob), use a single <code>.sqlite</code> file as your application's document format. Benefits: (1) Full SQL queries without loading entire file into memory. (2) Atomic saves (transactions). (3) Incremental updates (INSERT/UPDATE/DELETE single rows). (4) Indexes for fast lookups. (5) Battle-tested reliability. Used by: Apple Photos, AutoCAD, many iOS/Android apps.",
  ["L5_opinion"])

c("Expert", "What is SQLAR?",
  "An archiving format built on SQLite — a <b>SQLite database that acts as a compressed archive</b> (like .zip or .tar). Stores files as BLOBs with metadata (name, mtime, permissions). Created with <code>sqlite3 archive.sqlar -acf archive.sqlar file1 file2</code>. Offers: compression per-file, random access extraction without decompressing the whole archive, SQL queries over archive contents.",
  ["L5_opinion"])

c("Expert", "How to create an application-defined SQL function (C API)?",
  "<code>sqlite3_create_function(db, \"my_upper\", 1, SQLITE_UTF8, NULL, &myUpperFunc, NULL, NULL);</code>. The callback is called for each row: <code>static void myUpperFunc(sqlite3_context *ctx, int argc, sqlite3_value **argv) { ... sqlite3_result_text(ctx, result, -1, free); }</code>. Then use in SQL: <code>SELECT my_upper(name) FROM users;</code>.",
  ["L6_innovation"])

c("Expert", "What are SQLite loadable extensions?",
  "Compiled shared libraries (.so/.dll) that add new SQL functions, virtual tables, collations, or VFS modules to SQLite at runtime. <code>.load ./my_extension</code> in CLI. <code>SELECT load_extension('./my_extension');</code>. Used by: json1, fts5, rtree, ICU, crypto extensions. Enable with <code>sqlite3_enable_load_extension()</code> or compile-time option.",
  ["L6_innovation"])

c("Expert", "What is a virtual table interface?",
  "A C API for creating <b>custom table-like objects</b> that look like SQL tables but get data from external sources. <code>CREATE VIRTUAL TABLE t USING my_module(arg1, arg2);</code>. You implement callbacks: <code>xOpen, xClose, xFilter, xNext, xEof, xColumn, xRowid</code>. Used to build: FTS5, R*Tree, CSV virtual tables, network-backed tables, in-memory data structures as views.",
  ["L6_innovation"])

c("Expert", "What is a custom VFS (Virtual File System)?",
  "SQLite's abstraction layer for file system operations. You can implement a custom VFS to intercept all file I/O. Use cases: (1) Database in shared memory (memvfs). (2) Database over the network. (3) Encryption at file level. (4) Compressed database files. Register with <code>sqlite3_vfs_register()</code>. Changing VFS: <code>sqlite3_open_v2(\"file.db\", flag, \"my_vfs\")</code>.",
  ["L6_innovation"])

c("Expert", "What is <code>sqlite3_auto_extension</code>?",
  "Registers an extension to be loaded automatically on every new database connection. <code>sqlite3_auto_extension((void(*)(void))sqlite3_math_init);</code>. Eliminates the need to call <code>LOAD_EXTENSION</code> for each connection. Used by applications that always want extensions like FTS5 or math functions available. Call before opening any database.",
  ["L6_innovation"])

c("Expert", "How to use <code>json_set()</code> and <code>json_insert()</code>?",
  "<code>UPDATE users SET data = json_set(data, '$.name', 'Bob', '$.age', 30) WHERE id = 1;</code> — sets/replaces values at paths.<br><code>json_insert()</code> — inserts only if key doesn't exist (no overwrite).<br><code>json_replace()</code> — replaces only if key exists.<br><code>json_remove(data, '$.temp_field')</code> — removes key.<br><code>json_patch()</code> — RFC 7396 Merge Patch.",
  ["L6_innovation"])

c("Expert", "What is <code>json_group_array()</code> and <code>json_group_object()</code>?",
  "<code>SELECT user_id, json_group_array(tag) FROM user_tags GROUP BY user_id;</code> — aggregates values into a JSON array: <code>[a, b, c]</code>.<br><code>SELECT dept, json_group_object(name, salary) FROM employees GROUP BY dept;</code> — aggregates into JSON object: <code>{\"Alice\": 5000, \"Bob\": 6000}</code>. Powerful for building nested JSON responses directly from queries.",
  ["L6_innovation"])

c("Expert", "What is FTS5 <code>highlight()</code> and <code>snippet()</code>?",
  "<code>highlight(fts_table, col_idx, '&lt;b&gt;', '&lt;/b&gt;')</code> — wraps all matching terms in the given HTML tags. Returns the full text with highlights.<br><code>snippet(fts_table, col_idx, '&lt;b&gt;', '&lt;/b&gt;', '...', 32)</code> — returns a short snippet (max 32 tokens) around the best matching terms, with highlights.<br>Both are auxiliary functions for display.",
  ["L6_innovation"])

c("Expert", "How to configure FTS5 tokenizers?",
  "<code>CREATE VIRTUAL TABLE docs USING fts5(title, body, tokenize='porter unicode61 remove_diacritics 2');</code>.<br><b>unicode61</b> — Unicode-aware (default).<br><b>porter</b> — stemming (running → run).<br><b>trigram</b> — substring matching for fuzzy/cjk search.<br><b>ascii</b> — ASCII only.<br><b>remove_diacritics</b> — strip accents (1=yes, 2=no).<br>Custom tokenizers can be built via the extension API.",
  ["L6_innovation"])

c("Expert", "What is <code>json_tree()</code> and how does it differ from <code>json_each()</code>?",
  "<code>json_each()</code> — iterates only over <b>top-level array elements or object values</b>. Returns one row per immediate child.<br><code>json_tree()</code> — <b>recursively</b> walks the entire JSON structure. Returns every node (objects, arrays, scalars) with path, parent reference, and nesting level. Use for deep inspection or flattening complex nested JSON.",
  ["L6_innovation"])

c("Expert", "How to use SQLite as a cache (like memcached/Redis)?",
  "Create an in-memory database (<code>:memory:</code>) or a temp file DB. Use: <code>CREATE TABLE cache (key TEXT PRIMARY KEY, value BLOB, expires INTEGER);</code>. Use <code>INSERT OR REPLACE</code> for upsert. Periodic <code>DELETE FROM cache WHERE expires &lt; unixepoch();</code>. For shared cache between connections: use a file DB in WAL mode with <code>PRAGMA cache_size=-500000;</code> + mmap. Not as fast as Redis, but zero infrastructure.",
  ["L6_innovation"])

c("Expert", "How to implement full-text search ranking with BM25 in FTS5?",
  "<code>SELECT *, bm25(articles, 0) AS rank</code><br><code>FROM articles</code><br><code>WHERE articles MATCH 'sqlite database'</code><br><code>ORDER BY rank;</code><br>BM25 (default FTS5 ranking) combines term frequency, inverse document frequency, and document length normalization. Lower score = better match. You can provide custom weights: <code>bm25(articles, weight_title, weight_body)</code>. Column index -1 = average weight across all columns.",
  ["L6_innovation"])

c("Expert", "How to enforce at-most-one row (singleton) pattern in SQLite?",
  "Use a CHECK constraint with a subquery (3.25+). Strangely, a <b>partial UNIQUE index</b> is more portable: <code>CREATE UNIQUE INDEX idx_single_row ON config_table ((1)) WHERE id IS NOT NULL;</code>. Forces that at most one row exists (any second insert would violate the unique index on the constant value 1).",
  ["L6_innovation"])

c("Expert", "What is the difference between <code>INTEGER PRIMARY KEY</code> and <code>TEXT PRIMARY KEY</code>?",
  "<code>INTEGER PRIMARY KEY</code> is an <b>alias for rowid</b> — fast, auto-generated if NULL, stored inline with row data. No separate index needed.<br><code>TEXT PRIMARY KEY</code> (or any non-integer PK) does NOT alias rowid — it creates a separate UNIQUE index. <code>WITHOUT ROWID</code> tables use the PK as the primary B-tree key regardless of type and avoid the extra rowid column entirely.",
  ["L6_innovation"])

c("Expert", "How to use <code>IIF()</code> (inline IF)?",
  "<code>IIF(condition, value_if_true, value_if_false)</code> — SQLite 3.32+. <code>SELECT name, IIF(active, 'Yes', 'No') FROM users;</code>. A shorthand for the longer CASE expression. Works just like Excel's IF / ternary operator.",
  ["L6_innovation"])

c("Expert", "How to batch insert efficiently in SQLite?",
  "<ol><li>Wrap in a <b>transaction</b>: <code>BEGIN; ... COMMIT;</code> — without a transaction, each INSERT is its own transaction (fsync per insert).</li><li>Set <code>PRAGMA synchronous=OFF;</code> (temporarily, for bulk loads).</li><li>Use <code>PRAGMA journal_mode=MEMORY;</code> (for bulk load, restore after).</li><li>Use multi-row INSERT: <code>INSERT INTO t VALUES (...), (...), (...);</code></li><li>Use <code>.import</code> for CSV (optimized path).</li></ol>Speedup can be 100-1000x.",
  ["L6_innovation"])

c("Expert", "What is <code>RETURNING</code> clause? (SQLite 3.35+)",
  "Returns the modified rows from INSERT/UPDATE/DELETE: <code>INSERT INTO users (name) VALUES ('Alice') RETURNING id, name;</code>. <code>DELETE FROM logs WHERE created &lt; date('now', '-30 days') RETURNING *;</code>. Eliminates the need for separate SELECT after DML. Works with UPSERT too: <code>... ON CONFLICT(id) DO UPDATE SET name=excluded.name RETURNING *;</code>.",
  ["L6_innovation"])

c("Expert", "What is SQLite's <code>.parameter</code> system in CLI?",
  "CLI feature to bind parameters to queries. <code>.parameter init</code> — enable.<br><code>.parameter set ?1 'Alice'</code><br><code>.parameter set :name 'Bob'</code><br><code>SELECT * FROM users WHERE name = ?1;</code><br><code>.parameter list</code> — show all.<br><code>.parameter clear</code> — reset.<br>Alternative to embedding values in SQL — helps with scripting.",
  ["L6_innovation"])

c("Expert", "How to get the rowid of the last inserted row?",
  "<code>SELECT last_insert_rowid();</code> — returns the rowid of the most recent INSERT on this connection. Thread-safe per-connection. Returns 0 if no INSERT has occurred. Equivalent to <code>sqlite3_last_insert_rowid()</code> in C API. For multi-row INSERTs, returns the rowid of the first inserted row.",
  ["L6_innovation"])

c("Expert", "What is <code>PRAGMA application_id</code> and <code>user_version</code>?",
  "File-level metadata stored in the database header:<br><code>PRAGMA application_id = 0x4D594150;</code> — 4-byte identifier (e.g., 'MYAP' as hex). Used to identify the owning application.<br><code>PRAGMA user_version = 42;</code> — a 32-bit version number for schema versioning/migration tracking. <code>PRAGMA user_version;</code> reads it. Essential for app-level migration management.",
  ["L6_innovation"])

# =============================================
# Build & Output
# =============================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
