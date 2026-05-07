import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "PostgreSQL"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "SQL":          genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-SQL-Basics"),
    "AdvancedSQL":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Advanced-SQL"),
    "Schema":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Schema-Types"),
    "Indexes":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Indexes-Performance"),
    "Transactions": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Transactions-Concurrency"),
    "Admin":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Administration"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::09-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# =============================================
# 01 - FUNDAMENTALS
# =============================================

c("Fundamentals",
  "What is PostgreSQL?",
  "An open-source, object-relational database management system (ORDBMS) emphasizing extensibility, SQL compliance, and ACID transactions. It runs as a client-server system where the <code>postgres</code> server process accepts connections from clients (psql, apps, drivers).",
  ["postgresql", "definition"])

c("Fundamentals",
  "Describe PostgreSQL's client-server architecture.",
  "A single <b>postmaster</b> process listens on a port (default 5432). For each client connection, it <b>forks</b> a dedicated backend process. All backends share memory via a <b>shared buffers</b> pool and coordinate through the <b>WAL</b> (Write-Ahead Log).",
  ["architecture", "client-server"])

c("Fundamentals",
  "What is MVCC in PostgreSQL?",
  "<b>Multi-Version Concurrency Control</b> - instead of locking rows on write, PostgreSQL keeps multiple versions of each row. Readers never block writers, writers never block readers. Each transaction sees a <b>snapshot</b> of the database at a point in time using tuple visibility rules (<code>xmin</code>, <code>xmax</code>). Old versions are cleaned by <code>VACUUM</code>.",
  ["mvcc", "concurrency"])

c("Fundamentals",
  "What is WAL (Write-Ahead Log)?",
  "WAL is a sequential log of all changes made to the database. <b>Before</b> any data file modification, the change is first written to the WAL. This guarantees crash recovery (replay WAL after crash) and enables replication (streaming WAL to replicas). Located in <code>pg_wal/</code>.",
  ["wal", "write-ahead-log", "durability"])

c("Fundamentals",
  "What does ACID stand for and how does PostgreSQL implement each?",
  "<b>A</b>tomicity - transactions are all-or-nothing (ROLLBACK undoes everything).<br><b>C</b>onsistency - constraints (FK, CHECK, UNIQUE) enforced at commit.<br><b>I</b>solation - MVCC snapshots provide isolation per configured level.<br><b>D</b>urability - WAL ensures committed data survives crashes.",
  ["acid", "transactions"])

c("Fundamentals",
  "What is the difference between a PostgreSQL database and a schema?",
  "A <b>database</b> is a separate catalog with its own set of schemas, tables, roles, and physical files. Connections are per-database. A <b>schema</b> is a namespace within a database - like a folder for tables. The default schema is <code>public</code>. Cross-database queries require <code>dblink</code> or FDW; cross-schema queries work natively with <code>schema.table</code>.",
  ["schema", "database", "namespace"])

c("Fundamentals",
  "What is the difference between a role and a user in PostgreSQL?",
  "In PostgreSQL, <b>roles</b> and <b>users</b> are the same thing - a <code>USER</code> is just a <code>ROLE</code> with the <code>LOGIN</code> attribute by default.<br><code>CREATE ROLE bob;</code> vs <code>CREATE USER bob;</code> (same but user gets LOGIN). Roles can own objects, be granted permissions, and be members of other roles.",
  ["roles", "users", "authentication"])

c("Fundamentals",
  "What is a tablespace in PostgreSQL?",
  "A <b>tablespace</b> maps a logical name to a physical directory on disk. It lets you control where data files are stored - useful for placing hot tables on fast SSDs and cold tables on slower storage.<br><code>CREATE TABLESPACE fastspace LOCATION '/mnt/ssd/pgdata';</code>",
  ["tablespace", "storage"])

c("Fundamentals",
  "What are PostgreSQL extensions and how do you use them?",
  "Extensions are modular add-ons that extend PostgreSQL's capabilities without modifying core. <b>Enable</b> with:<br><code>CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";</code><br>Check installed: <code>SELECT * FROM pg_extension;</code><br>Popular: <code>postgis</code>, <code>pgvector</code>, <code>timescaledb</code>, <code>pg_cron</code>, <code>pg_stat_statements</code>.",
  ["extensions", "plugins"])

c("Fundamentals",
  "PostgreSQL vs MySQL - key differences?",
  "<b>MVCC</b>: PG uses multi-version rows natively; MySQL InnoDB uses undo logs.<br><b>Extensions</b>: PG supports custom types, operators, languages; MySQL is less extensible.<br><b>JSON</b>: PG has JSONB with indexing (GIN); MySQL has JSON with generated columns.<br><b>Replication</b>: PG has logical+physical streaming; MySQL has binlog-based.<br><b>GIS</b>: PostGIS >> MySQL spatial.<br><b>Licensing</b>: PG is PostgreSQL license (liberal); MySQL is GPL/Oracle.",
  ["postgresql-vs-mysql", "comparison"])

c("Fundamentals",
  "PostgreSQL vs SQLite - when to choose which?",
  "<b>SQLite</b>: Embedded, zero-config, single-file, no server. Best for mobile apps, embedded devices, single-user desktop apps, testing, small-scale read-heavy.<br><b>PostgreSQL</b>: Client-server, concurrent multi-user, full ACID, advanced features. Best for web apps, APIs, analytics, wherever concurrency and features matter.<br>If you need >1 concurrent writer, choose PostgreSQL.",
  ["postgresql-vs-sqlite", "comparison"])

c("Fundamentals",
  "How does PostgreSQL maintain its commit log (clog)?",
  "The <b>commit log</b> (clog, in <code>pg_xact/</code>) records the commit status (committed, aborted, in-progress) of every transaction ID. During MVCC visibility checks, PostgreSQL consults the clog to determine if a row version's creating transaction committed. VACUUM eventually freezes old XIDs so clog entries can be truncated.",
  ["clog", "commit-log", "mvcc"])

c("Fundamentals",
  "What is the PostgreSQL Global Development Group?",
  "The core team and community that develops PostgreSQL. PostgreSQL is <b>not owned</b> by any single company - it's a community-driven open-source project under the PostgreSQL license (similar to MIT/BSD). Major contributors include EnterpriseDB, Crunchy Data, Microsoft, and Amazon.",
  ["community", "governance"])

c("Fundamentals",
  "What is TOAST in PostgreSQL?",
  "<b>The Oversized-Attribute Storage Technique</b> - automatically compresses and/or out-of-lines large field values (>2KB) into a separate TOAST table. Default strategy is <b>EXTENDED</b> (compress first, then out-of-line if still too big). Check with <code>\\d+ table_name</code>. TOAST allows rows to remain under the 8KB page size while storing large values.",
  ["toast", "storage", "large-objects"])

# =============================================
# 02 - SQL BASICS
# =============================================

c("SQL",
  "Write a basic SELECT with filtering and ordering.",
  "<pre><code>SELECT first_name, email\nFROM users\nWHERE created_at >= '2024-01-01'\n  AND active = true\nORDER BY created_at DESC\nLIMIT 10;</code></pre>",
  ["select", "where", "order-by"])

c("SQL",
  "How does INSERT work and what is RETURNING?",
  "<pre><code>INSERT INTO users (name, email)\nVALUES ('Alice', 'a@x.com')\n  , ('Bob',   'b@x.com')\nRETURNING id, created_at;\n-- RETURNING returns the inserted row(s) - hugely useful\n-- for getting generated IDs without a separate SELECT.</code></pre>",
  ["insert", "returning"])

c("SQL",
  "How does UPDATE with RETURNING work?",
  "<pre><code>UPDATE products\nSET price = price * 0.9\n   , updated_at = NOW()\nWHERE category = 'clearance'\nRETURNING id, name, price AS new_price;</code></pre>",
  ["update", "returning"])

c("SQL",
  "How does DELETE with RETURNING work?",
  "<pre><code>DELETE FROM sessions\nWHERE expires_at < NOW()\nRETURNING id, user_id, expires_at;\n-- RETURNING on DELETE tells you exactly what was removed.</code></pre>",
  ["delete", "returning"])

c("SQL",
  "What is the difference between WHERE and HAVING?",
  "<code>WHERE</code> filters rows <b>before</b> aggregation. <code>HAVING</code> filters <b>after</b> aggregation (groups).<br><pre><code>SELECT dept_id, COUNT(*) AS cnt\nFROM employees\nWHERE salary > 50000          -- row filter first\nGROUP BY dept_id\nHAVING COUNT(*) > 5;         -- group filter after</code></pre>",
  ["where", "having", "group-by"])

c("SQL",
  "How does GROUP BY work with aggregates?",
  "<pre><code>SELECT department, AVG(salary)::NUMERIC(10,2) AS avg_salary\n     , COUNT(*) AS headcount\nFROM employees\nGROUP BY department\nORDER BY avg_salary DESC;</code></pre><b>Rule</b>: Every column in SELECT must be either in GROUP BY or inside an aggregate.",
  ["group-by", "aggregate"])

c("SQL",
  "How do LIMIT and OFFSET work?",
  "LIMIT restricts the number of rows returned. OFFSET skips rows before starting.<br><pre><code>-- Page 3 with 20 items per page:\nSELECT * FROM products\nORDER BY id\nLIMIT 20 OFFSET 40;\n-- WARNING: OFFSET scans and discards skipped rows -\n-- consider keyset pagination for large tables.</code></pre>",
  ["limit", "offset", "pagination"])

c("SQL",
  "What does DISTINCT do and what about DISTINCT ON?",
  "<code>SELECT DISTINCT col1, col2 FROM t</code> - returns unique combinations of col1, col2.<br><code>DISTINCT ON (col)</code> is a PostgreSQL extension that returns the <b>first row for each distinct value</b> of the specified column(s), according to ORDER BY:<br><pre><code>SELECT DISTINCT ON (user_id) user_id, logged_at\nFROM logins\nORDER BY user_id, logged_at DESC;\n-- Latest login per user</code></pre>",
  ["distinct", "distinct-on"])

c("SQL",
  "How do LIKE and ILIKE work?",
  "<code>LIKE</code> is case-sensitive pattern matching; <code>ILIKE</code> is case-insensitive.<br><b>Wildcards</b>: <code>%</code> matches zero or more chars; <code>_</code> matches exactly one char.<br><pre><code>SELECT * FROM users\nWHERE email LIKE '%@gmail.com';\n-- Case-insensitive name search:\nSELECT * FROM users\nWHERE name ILIKE '%john%';</code></pre>",
  ["like", "ilike", "pattern-matching"])

c("SQL",
  "How does the IN operator work?",
  "<pre><code>SELECT * FROM orders\nWHERE status IN ('shipped', 'delivered', 'returned');\n-- Works with subqueries too:\nSELECT * FROM users\nWHERE id IN (SELECT user_id FROM orders WHERE total > 1000);</code></pre><code>NOT IN</code> is dangerous with NULLs - prefer <code>NOT EXISTS</code>.",
  ["in", "subquery"])

c("SQL",
  "How does BETWEEN work?",
  "<code>BETWEEN x AND y</code> is <b>inclusive</b> on both ends (equivalent to <code>>= x AND <= y</code>).<br><pre><code>SELECT * FROM events\nWHERE event_date BETWEEN '2024-01-01' AND '2024-12-31';\n-- Also works with numbers and text ranges.\n-- Use NOT BETWEEN for exclusive ranges.</code></pre>",
  ["between", "range"])

c("SQL",
  "How do IS NULL and IS NOT NULL work?",
  "<code>NULL</code> means unknown, not zero or empty string. <b>Never</b> use <code>= NULL</code> - always <code>IS NULL</code> or <code>IS NOT NULL</code>.<br><pre><code>SELECT * FROM users WHERE deleted_at IS NULL;\nSELECT * FROM users WHERE bio IS NOT NULL AND bio != '';</code></pre>",
  ["null", "is-null"])

c("SQL",
  "What does COALESCE do?",
  "Returns the <b>first non-NULL</b> value from a list. Useful for defaults.<br><pre><code>SELECT name, COALESCE(phone, 'No phone') AS contact\nFROM users;\n-- Multiple fallbacks:\nSELECT COALESCE(work_email, personal_email, 'none@none.com');</code></pre>",
  ["coalesce", "null-handling"])

c("SQL",
  "What does NULLIF do?",
  "Returns NULL if two values are equal, otherwise returns the first value. Guards against <b>division by zero</b>:<br><pre><code>SELECT revenue / NULLIF(orders, 0) AS avg_order_value\nFROM metrics;\n-- If orders=0, NULLIF returns NULL, making the whole expression NULL\n-- instead of raising division-by-zero error.</code></pre>",
  ["nullif", "division-by-zero"])

c("SQL",
  "How does CASE / WHEN work?",
  "<pre><code>SELECT name,\n  CASE\n    WHEN salary > 150000 THEN 'high'\n    WHEN salary > 80000  THEN 'medium'\n    ELSE 'low'\n  END AS pay_band\nFROM employees;\n-- Also supports simple form:\nCASE department WHEN 'sales' THEN 'front office' ELSE 'back office' END</code></pre>",
  ["case", "conditional"])

c("SQL",
  "What are the JOIN types in PostgreSQL?",
  "<b>INNER JOIN</b> - rows that match in both tables.<br><b>LEFT JOIN</b> - all rows from left + matching right (NULL if no match).<br><b>RIGHT JOIN</b> - all rows from right + matching left.<br><b>FULL OUTER JOIN</b> - all rows from both, NULLs where no match.<br><b>CROSS JOIN</b> - Cartesian product (every left row x every right row).<br><b>NATURAL JOIN</b> - joins on columns with same name (avoid - fragile).<br><b>LATERAL JOIN</b> - subquery can reference columns from preceding tables.",
  ["joins", "join-types"])

c("SQL",
  "Write an example of INNER JOIN.",
  "<pre><code>SELECT u.name, o.total, o.created_at\nFROM users u\nINNER JOIN orders o ON o.user_id = u.id\nWHERE o.total > 100\nORDER BY o.created_at DESC;</code></pre>",
  ["inner-join", "join-example"])

c("SQL",
  "Write an example of LEFT JOIN.",
  "<pre><code>SELECT u.name, COUNT(o.id) AS order_count\nFROM users u\nLEFT JOIN orders o ON o.user_id = u.id\nGROUP BY u.id, u.name\nORDER BY order_count DESC;\n-- Includes users with zero orders.</code></pre>",
  ["left-join", "join-example"])

c("SQL",
  "What is a LATERAL JOIN?",
  "A <code>LATERAL</code> subquery can reference columns from preceding tables in the FROM clause - like a <b>for-each loop</b> in SQL:<br><pre><code>SELECT u.name, latest.title\nFROM users u\nLEFT JOIN LATERAL (\n  SELECT title FROM posts\n  WHERE author_id = u.id\n  ORDER BY created_at DESC\n  LIMIT 1\n) latest ON true;</code></pre>",
  ["lateral-join", "subquery"])

c("SQL",
  "What are subqueries and how are they used?",
  "A subquery is a query nested inside another query. Types:<br><b>Scalar</b> - returns one value, usable in SELECT/WHERE:<br><code>SELECT name, (SELECT AVG(salary) FROM employees) AS avg FROM employees;</code><br><b>Row / Table</b> - returns multiple rows, usable in FROM or WHERE with IN/EXISTS:<br><code>SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);</code>",
  ["subquery", "nested-query"])

c("SQL",
  "How do UNION, INTERSECT, and EXCEPT work?",
  "<code>UNION</code> - combines results from two queries, removes duplicates.<br><code>UNION ALL</code> - combines and <b>keeps</b> duplicates (faster).<br><code>INTERSECT</code> - returns rows present in both queries.<br><code>EXCEPT</code> - returns rows from first query not in second.<br><pre><code>SELECT email FROM users\nUNION\nSELECT email FROM newsletter_subscribers;\n-- All unique emails across both tables.</code></pre>",
  ["union", "intersect", "except", "set-operations"])

c("SQL",
  "What are the common aggregate functions?",
  "<code>COUNT(*)</code> - number of rows (including NULLs).<br><code>COUNT(col)</code> - number of non-NULL values.<br><code>SUM(col)</code>, <code>AVG(col)</code> - sum/average.<br><code>MIN(col)</code>, <code>MAX(col)</code> - minimum/maximum.<br><code>STRING_AGG(col, ',')</code> - concatenate strings.<br><code>ARRAY_AGG(col)</code> - build an array.<br><code>JSON_AGG(col)</code>, <code>JSONB_AGG(col)</code> - build JSON array.<br><code>BOOL_AND(cond)</code>, <code>BOOL_OR(cond)</code> - logical aggregate.",
  ["aggregate", "functions"])

c("SQL",
  "What are common PostgreSQL string functions?",
  "<code>LENGTH(s)</code> - character count.<br><code>UPPER(s)</code> / <code>LOWER(s)</code> - case conversion.<br><code>TRIM(s)</code> / <code>LTRIM(s)</code> / <code>RTRIM(s)</code> - strip whitespace.<br><code>SUBSTRING(s FROM pos FOR len)</code> - extract substring.<br><code>REPLACE(s, old, new)</code> - replace substring.<br><code>SPLIT_PART(s, delim, n)</code> - split by delimiter, return nth part.<br><code>REGEXP_REPLACE(s, pattern, repl)</code> - regex replacement.<br><code>FORMAT(fmt, args...)</code> - sprintf-style formatting.<br><code>CONCAT(a, b, c)</code> - concatenation (NULL-safe).<br><code>||</code> - string concatenation operator.",
  ["strings", "functions"])

c("SQL",
  "What are the key PostgreSQL date/time types and functions?",
  "<b>Types</b>: <code>DATE</code>, <code>TIME</code>, <code>TIMESTAMP</code>, <code>TIMESTAMPTZ</code>, <code>INTERVAL</code>.<br><b>Functions</b>:<br><code>NOW()</code> - current timestamp with timezone.<br><code>CURRENT_DATE</code> - today's date.<br><code>AGE(end, start)</code> - interval between dates.<br><code>DATE_TRUNC('month', ts)</code> - truncate to precision.<br><code>EXTRACT(YEAR FROM ts)</code> - extract a field.<br><code>ts AT TIME ZONE 'UTC'</code> - convert timezone.<br><code>GENERATE_SERIES(start, stop, INTERVAL)</code> - generate date series.",
  ["date", "time", "functions"])

c("SQL",
  "What is the :: type-casting operator?",
  "PostgreSQL's shorthand for <code>CAST(expr AS type)</code>.<br><pre><code>SELECT '123'::INTEGER;                -- 123\nSELECT '2024-01-15'::DATE;            -- date\nSELECT 42::TEXT;                       -- '42'\nSELECT (total / count)::NUMERIC(10,2); -- decimal\n-- Full form: CAST('123' AS INTEGER)</code></pre>",
  ["type-casting", "cast"])

c("SQL",
  "What does the RETURNING clause do?",
  "<code>RETURNING</code> works with INSERT, UPDATE, DELETE to return the affected rows - without a separate SELECT. Essential for getting generated IDs, computed columns, or confirming what changed.<br><pre><code>INSERT INTO logs (msg) VALUES ('boom')\nRETURNING id, inserted_at;\n\nDELETE FROM queue WHERE id = 5\nRETURNING *;</code></pre>",
  ["returning", "dml"])

c("SQL",
  "How does ON CONFLICT (upsert) work?",
  "<code>ON CONFLICT</code> handles unique-violation errors by either updating existing rows or doing nothing - known as <b>upsert</b> (update-or-insert).<br><pre><code>INSERT INTO users (email, name)\nVALUES ('a@b.com', 'Alice')\nON CONFLICT (email) DO UPDATE\nSET name = EXCLUDED.name\n   , updated_at = NOW();\n-- ON CONFLICT (email) DO NOTHING;  -- skip silently</code></pre>",
  ["upsert", "on-conflict", "insert"])

c("SQL",
  "Write an INSERT ... ON CONFLICT DO NOTHING example.",
  "<pre><code>INSERT INTO daily_visits (date, count)\nVALUES (CURRENT_DATE, 1)\nON CONFLICT (date) DO NOTHING;\n-- Ignores insert if the date already exists.\n-- Combine with RETURNING to know if it was inserted:\nINSERT INTO daily_visits (date, count)\nVALUES (CURRENT_DATE, 1)\nON CONFLICT (date) DO NOTHING\nRETURNING *;</code></pre>",
  ["upsert", "on-conflict", "do-nothing"])

c("SQL",
  "How do you use ORDER BY with multiple columns and NULLS FIRST/LAST?",
  "<pre><code>SELECT * FROM tasks\nORDER BY priority ASC NULLS LAST\n       , created_at DESC;\n-- NULLS FIRST puts NULLs at the top (default for DESC)\n-- NULLS LAST puts NULLs at the bottom (default for ASC)</code></pre>",
  ["order-by", "nulls"])

c("SQL",
  "What is the difference between COUNT(*) and COUNT(column)?",
  "<code>COUNT(*)</code> counts every row regardless of NULLs.<br><code>COUNT(column)</code> counts only non-NULL values in that column.<br><pre><code>SELECT COUNT(*) AS all_rows\n     , COUNT(email) AS with_email\n     , COUNT(DISTINCT email) AS unique_emails\nFROM users;</code></pre>",
  ["count", "aggregate", "null"])

# =============================================
# 03 - ADVANCED SQL
# =============================================

c("AdvancedSQL",
  "What are window functions and how do they differ from GROUP BY?",
  "Window functions perform calculations across a set of rows <b>without collapsing rows</b> - each row keeps its identity. GROUP BY collapses rows into summary rows.<br><pre><code>SELECT name, department, salary,\n  AVG(salary) OVER (PARTITION BY department) AS dept_avg\nFROM employees;\n-- Every row still appears, with the department average appended.</code></pre>",
  ["window-functions", "over"])

c("AdvancedSQL",
  "How do ROW_NUMBER, RANK, and DENSE_RANK differ?",
  "<code>ROW_NUMBER()</code> - unique sequential number per partition. No ties.<br><code>RANK()</code> - same values get same rank, gaps after ties (e.g., 1,2,2,4).<br><code>DENSE_RANK()</code> - same values get same rank, no gaps (e.g., 1,2,2,3).<br><pre><code>SELECT name, salary,\n  ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,\n  RANK()       OVER (ORDER BY salary DESC) AS rank_pos,\n  DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_pos\nFROM employees;</code></pre>",
  ["row-number", "rank", "dense-rank", "window-functions"])

c("AdvancedSQL",
  "How do LAG and LEAD work?",
  "<code>LAG(col, offset, default)</code> - get value from a <b>previous</b> row in the window.<br><code>LEAD(col, offset, default)</code> - get value from a <b>subsequent</b> row.<br><pre><code>SELECT event_date, revenue,\n  LAG(revenue)  OVER (ORDER BY event_date) AS prev_day_rev,\n  LEAD(revenue) OVER (ORDER BY event_date) AS next_day_rev,\n  revenue - LAG(revenue) OVER (ORDER BY event_date) AS change\nFROM daily_finance;\n-- NULL for first/last rows where no previous/next exists.</code></pre>",
  ["lag", "lead", "window-functions"])

c("AdvancedSQL",
  "How do FIRST_VALUE, LAST_VALUE, and NTH_VALUE work?",
  "<code>FIRST_VALUE(col)</code> - first value in the window frame.<br><code>LAST_VALUE(col)</code> - last value in the window frame (with proper frame clause).<br><code>NTH_VALUE(col, n)</code> - nth value in the window frame.<br><pre><code>SELECT name, salary,\n  FIRST_VALUE(salary) OVER (PARTITION BY dept ORDER BY salary DESC) AS highest,\n  LAST_VALUE(salary)  OVER (PARTITION BY dept ORDER BY salary DESC\n    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS lowest\nFROM employees;</code></pre>",
  ["first-value", "last-value", "window-functions"])

c("AdvancedSQL",
  "What does NTILE do?",
  "<code>NTILE(n)</code> divides rows into <code>n</code> approximately equal buckets, numbered 1 through n. Useful for percentiles/quartiles.<br><pre><code>SELECT name, salary,\n  NTILE(4) OVER (ORDER BY salary DESC) AS quartile\nFROM employees;\n-- 1 = top 25%, 4 = bottom 25%.</code></pre>",
  ["ntile", "window-functions"])

c("AdvancedSQL",
  "What is the difference between PARTITION BY and ORDER BY in window functions?",
  "<code>PARTITION BY</code> divides rows into separate groups (like GROUP BY without collapsing). The window function resets for each partition.<br><code>ORDER BY</code> within the window defines the order rows are processed and determines the default frame (<code>RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW</code> for most functions).<br><pre><code>ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)\n-- Numbers employees 1,2,3... per department, highest salary first.</code></pre>",
  ["partition-by", "order-by", "window-functions"])

c("AdvancedSQL",
  "What are CTEs (Common Table Expressions)?",
  "CTEs (<code>WITH</code> queries) create named temporary result sets, improving readability and enabling recursive queries.<br><pre><code>WITH recent_orders AS (\n  SELECT user_id, SUM(total) AS spent\n  FROM orders\n  WHERE created_at > NOW() - INTERVAL '30 days'\n  GROUP BY user_id\n)\nSELECT u.name, r.spent\nFROM users u\nJOIN recent_orders r ON r.user_id = u.id\nWHERE r.spent > 500;</code></pre>",
  ["cte", "with", "common-table-expression"])

c("AdvancedSQL",
  "How do recursive CTEs work?",
  "Recursive CTEs have a <b>base case</b> (non-recursive) UNIONed with a <b>recursive</b> step that references the CTE itself. They iterate until the recursive part returns no rows.<br><pre><code>WITH RECURSIVE subordinates AS (\n  -- Base: top-level manager\n  SELECT id, name, manager_id, 1 AS depth\n  FROM employees WHERE manager_id IS NULL\n  UNION ALL\n  -- Recursive: direct reports\n  SELECT e.id, e.name, e.manager_id, s.depth + 1\n  FROM employees e\n  JOIN subordinates s ON e.manager_id = s.id\n)\nSELECT * FROM subordinates ORDER BY depth, name;\n-- Traverses the entire org hierarchy.</code></pre>",
  ["recursive-cte", "with-recursive", "hierarchy"])

c("AdvancedSQL",
  "Write a recursive CTE that generates a numbers series.",
  "<pre><code>WITH RECURSIVE numbers AS (\n  SELECT 1 AS n          -- base case\n  UNION ALL\n  SELECT n + 1           -- recursive step\n  FROM numbers\n  WHERE n < 100          -- termination condition\n)\nSELECT n FROM numbers;\n-- Generates integers 1 through 100.\n-- WARNING: without a termination condition it loops forever\n-- (actually PostgreSQL limits to work_mem exhaustion).</code></pre>",
  ["recursive-cte", "series", "generate-series"])

c("AdvancedSQL",
  "What does DISTINCT ON do and how is it used?",
  "PostgreSQL extension that returns the <b>first row for each distinct combination</b> of the specified columns, according to ORDER BY. Unlike GROUP BY, it returns <b>complete rows</b>.<br><pre><code>-- Latest login per user:\nSELECT DISTINCT ON (user_id)\n  user_id, logged_at, ip_address\nFROM logins\nORDER BY user_id, logged_at DESC;\n-- The ORDER BY must start with the DISTINCT ON columns.</code></pre>",
  ["distinct-on", "postgres-specific"])

c("AdvancedSQL",
  "How do array types and array operations work in PostgreSQL?",
  "<b>Array definition</b>: <code>INTEGER[]</code>, <code>TEXT[][]</code><br><b>Array literal</b>: <code>ARRAY[1,2,3]</code> or <code>'{1,2,3}'::INTEGER[]</code><br><b>Access</b>: <code>arr[1]</code> (1-based index)<br><b>Contains</b>: <code>arr @> ARRAY[2]</code> (contains element 2?)<br><b>Overlap</b>: <code>arr && ARRAY[1,2]</code> (any overlap?)<br><b>unnest</b>: expand array into rows: <code>SELECT UNNEST(ARRAY[1,2,3]);</code><br><code>ARRAY_AGG(col)</code> - aggregate rows into an array.<br><code>ANY(arr)</code> - <code>WHERE 3 = ANY(arr)</code><br><code>ALL(arr)</code> - <code>WHERE 3 > ALL(ARRAY[1,2,4])</code>",
  ["arrays", "unnest", "array_agg"])

c("AdvancedSQL",
  "What is JSON vs JSONB in PostgreSQL?",
  "<code>JSON</code> - text storage of JSON, preserves whitespace and key ordering, slower operations (re-parsed every time).<br><code>JSONB</code> - binary storage, compressed, supports indexing (GIN), faster operations, de-duplicates keys (last key wins), does not preserve order or whitespace.<br><b>Use JSONB 99% of the time</b> - it's the practical choice.<br><pre><code>CREATE TABLE events (\n  id SERIAL PRIMARY KEY,\n  payload JSONB NOT NULL\n);</code></pre>",
  ["json", "jsonb", "semi-structured"])

c("AdvancedSQL",
  "What are the JSON/JSONB operators in PostgreSQL?",
  "<code>-></code> - get JSON object field as JSON (text): <code>data -> 'name'</code><br><code>->></code> - get JSON object field as TEXT: <code>data ->> 'name'</code><br><code>#></code> - get object at path as JSON: <code>data #> '{address,city}'</code><br><code>#>></code> - get object at path as TEXT: <code>data #>> '{address,city}'</code><br><code>@></code> - contains: <code>data @> '{\"key\":\"val\"}'</code><br><code><@</code> - contained by (reverse of @>)<br><code>?</code> - does key/top-level string exist?: <code>data ? 'name'</code><br><code>?|</code> - any of these keys exist?: <code>data ?| ARRAY['a','b']</code><br><code>?&</code> - all of these keys exist?: <code>data ?& ARRAY['a','b']</code>",
  ["jsonb-operators", "json"])

c("AdvancedSQL",
  "What are key JSONB functions?",
  "<code>JSONB_SET(target, path, new_value)</code> - set/update a value at path.<br><code>JSONB_SET(data, '{name}', '\"Bob\"')</code><br><code>JSONB_INSERT(data, path, value)</code> - insert if key missing.<br><code>JSONB_STRIP_NULLS(data)</code> - remove null fields.<br><code>JSONB_BUILD_OBJECT('key', val, ...)</code> - build object from pairs.<br><code>JSONB_ARRAY_ELEMENTS(arr)</code> - expand JSON array to rows.<br><code>JSONB_EACH(obj)</code> - expand object to key-value rows.<br><code>TO_JSONB(anyelement)</code> - convert row/type to JSONB.<br><pre><code>SELECT JSONB_ARRAY_ELEMENTS('[\"a\",\"b\"]'::JSONB);\n-- Returns two rows: \"a\" and \"b\".</code></pre>",
  ["jsonb-functions", "json"])

c("AdvancedSQL",
  "How do you index JSONB data?",
  "Use a <b>GIN index</b> on the JSONB column for fast <code>@></code>, <code>?</code>, <code>?|</code>, <code>?&</code> queries:<br><pre><code>CREATE INDEX ON events USING GIN (payload);\n-- Or with jsonb_path_ops for containment only (smaller, faster):\nCREATE INDEX ON events USING GIN (payload jsonb_path_ops);\n-- For specific key lookups, use an expression index:\nCREATE INDEX ON events ((payload ->> 'type'));</code></pre>",
  ["jsonb-index", "gin", "index"])

c("AdvancedSQL",
  "How does PostgreSQL Full-Text Search work?",
  "FTS uses <b>tsvector</b> (parsed, normalized document) and <b>tsquery</b> (search expression) types with GIN indexes for fast text search.<br><pre><code>-- Build search column:\nALTER TABLE articles ADD COLUMN fts TSVECTOR\n  GENERATED ALWAYS AS (\n    TO_TSVECTOR('english', title || ' ' || body)\n  ) STORED;\n-- Index it:\nCREATE INDEX idx_fts ON articles USING GIN (fts);\n-- Search with ranking:\nSELECT *, TS_RANK(fts, QUERY) AS rank\nFROM articles, TO_TSQUERY('english', 'postgresql & performance') AS QUERY\nWHERE fts @@ QUERY\nORDER BY rank DESC;</code></pre>",
  ["full-text-search", "tsvector", "tsquery"])

c("AdvancedSQL",
  "What are the key FTS functions and operators?",
  "<code>TO_TSVECTOR('english', text)</code> - tokenize and normalize text into a tsvector.<br><code>TO_TSQUERY('english', 'term & another')</code> - parse search query string.<br><code>PLAINTO_TSQUERY('english', 'simple query')</code> - simpler parser, no operators.<br><code>@@</code> - match operator: <code>tsvector @@ tsquery</code>.<br><code>TS_RANK(tsv, tq)</code> - relevance score (term frequency based).<br><code>TS_HEADLINE('english', text, tq)</code> - generate highlighted snippet.<br><code>WEBSEARCH_TO_TSQUERY('english', 'query')</code> - web-search syntax (quotes, OR, -).",
  ["full-text-search", "fts-functions"])

c("AdvancedSQL",
  "What are range types in PostgreSQL?",
  "Built-in range types include <code>INT4RANGE</code>, <code>INT8RANGE</code>, <code>NUMRANGE</code>, <code>TSRANGE</code> (timestamp), <code>TSTZRANGE</code> (timestamptz), <code>DATERANGE</code>. Operators: <code>@></code> (contains), <code>&&</code> (overlaps), <code>-|-</code> (adjacent), <code>+</code> (union), <code>*</code> (intersection).<br><pre><code>CREATE TABLE reservations (\n  id SERIAL PRIMARY KEY,\n  room INT NOT NULL,\n  during DATERANGE NOT NULL,\n  EXCLUDE USING GIST (room WITH =, during WITH &&)\n);\n-- Prevents overlapping reservations for the same room.</code></pre>",
  ["range-types", "daterange", "tsrange"])

c("AdvancedSQL",
  "What are ROW types and composite types?",
  "PostgreSQL automatically creates a composite type for every table. You can query entire rows as single values.<br><pre><code>-- Select entire rows:\nSELECT u FROM users u WHERE id = 1;\n-- Returns: (1,\"Alice\",\"a@x.com\",\"2024-01-01\")\n\n-- Access fields from row variable:\nSELECT (u).name, (u).email FROM users u;\n\n-- Custom composite type:\nCREATE TYPE address AS (street TEXT, city TEXT, zip TEXT);\nCREATE TABLE contacts (id INT, addr ADDRESS);\nINSERT INTO contacts VALUES (1, ROW('123 Main','NYC','10001')::ADDRESS);</code></pre>",
  ["row-types", "composite-types"])

c("AdvancedSQL",
  "What are materialized views and how do they differ from regular views?",
  "A <b>regular view</b> is a saved query - each access re-executes the underlying query. A <b>materialized view</b> stores the result physically - reads are fast, but data can be stale. Refresh manually or on a schedule.<br><pre><code>CREATE MATERIALIZED VIEW monthly_sales AS\nSELECT date_trunc('month', order_date) AS month,\n       SUM(total) AS revenue\nFROM orders GROUP BY 1;\n\nREFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales;\n-- CONCURRENTLY requires a unique index and allows reads during refresh.</code></pre>",
  ["materialized-view", "view"])

c("AdvancedSQL",
  "What are generated columns in PostgreSQL?",
  "Generated columns are computed from other columns in the same row, automatically updated. PostgreSQL supports <b>STORED</b> (physically stored, not virtual).<br><pre><code>CREATE TABLE users (\n  first_name TEXT,\n  last_name  TEXT,\n  full_name  TEXT GENERATED ALWAYS AS\n    (first_name || ' ' || last_name) STORED\n);\nINSERT INTO users (first_name, last_name) VALUES ('Alice', 'Smith');\nSELECT full_name; -- 'Alice Smith'</code></pre>",
  ["generated-columns", "computed-columns"])

c("AdvancedSQL",
  "How do you create and call a PL/pgSQL function?",
  "<pre><code>CREATE OR REPLACE FUNCTION double_price(price NUMERIC)\nRETURNS NUMERIC AS $$\nBEGIN\n  RETURN price * 2;\nEND;\n$$ LANGUAGE plpgsql IMMUTABLE;\n-- IMMUTABLE: always returns same output for same input (optimizable)\n-- STABLE: same within a single table scan\n-- VOLATILE: can return different results (default)\n\nSELECT double_price(99.99); -- 199.98\n\n-- Set-returning function:\nCREATE OR REPLACE FUNCTION get_users_by_status(active BOOLEAN)\nRETURNS SETOF users AS $$\nBEGIN\n  RETURN QUERY SELECT * FROM users WHERE active = $1;\nEND;\n$$ LANGUAGE plpgsql STABLE;\n\nSELECT * FROM get_users_by_status(true);</code></pre>",
  ["plpgsql", "functions", "stored-procedures"])

c("AdvancedSQL",
  "What is the difference between a FUNCTION and a PROCEDURE in PostgreSQL?",
  "<b>FUNCTION</b> - returns a value (scalar, row, or set), usable in SELECT. Cannot control transactions.<br><b>PROCEDURE</b> (PG 11+) - does not return a value, called with CALL. Can COMMIT/ROLLBACK inside the procedure body - useful for complex transactional logic.<br><pre><code>CREATE PROCEDURE transfer(from_id INT, to_id INT, amt NUMERIC)\nLANGUAGE plpgsql AS $$\nBEGIN\n  UPDATE accounts SET balance = balance - amt WHERE id = from_id;\n  UPDATE accounts SET balance = balance + amt WHERE id = to_id;\n  COMMIT;  -- allowed in procedures, not in functions\nEND;\n$$;\n\nCALL transfer(1, 2, 100);</code></pre>",
  ["function-vs-procedure", "plpgsql"])

c("AdvancedSQL",
  "What are triggers and trigger functions?",
  "A <b>trigger</b> automatically executes a trigger function in response to INSERT, UPDATE, DELETE events. Can fire BEFORE, AFTER, or INSTEAD OF (for views). Can operate FOR EACH ROW or FOR EACH STATEMENT.<br><pre><code>CREATE OR REPLACE FUNCTION update_timestamp()\nRETURNS TRIGGER AS $$\nBEGIN\n  NEW.updated_at = NOW();\n  RETURN NEW;\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE TRIGGER set_updated_at\n  BEFORE UPDATE ON users\n  FOR EACH ROW EXECUTE FUNCTION update_timestamp();</code></pre>",
  ["triggers", "trigger-functions", "automation"])

c("AdvancedSQL",
  "What are event triggers in PostgreSQL?",
  "Event triggers fire on DDL events (CREATE, ALTER, DROP) rather than DML. Useful for auditing schema changes, preventing certain DDL, or auto-granting permissions.<br><pre><code>CREATE OR REPLACE FUNCTION log_ddl()\nRETURNS EVENT_TRIGGER AS $$\nBEGIN\n  INSERT INTO ddl_log (tag, object, when)\n  VALUES (TG_TAG, TG_EVENT, NOW());\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE EVENT TRIGGER log_all_ddl\n  ON ddl_command_end\n  EXECUTE FUNCTION log_ddl();</code></pre>",
  ["event-triggers", "ddl", "audit"])

c("AdvancedSQL",
  "How does LISTEN/NOTIFY work for pub/sub?",
  "PostgreSQL's built-in lightweight pub/sub mechanism. Clients <code>LISTEN</code> on a channel and receive <code>NOTIFY</code> messages (with optional payload).<br><pre><code>-- Session 1 (listener):\nLISTEN order_channel;\n-- Then poll for notifications (driver-dependent) or use async.\n\n-- Session 2 (sender):\nNOTIFY order_channel, 'order_id=123';\n-- Session 1 receives: Asynchronous notification\n-- \"order_channel\" received with payload \"order_id=123\"\n\n-- Trigger-based notify:\nCREATE OR REPLACE FUNCTION notify_new_order()\nRETURNS TRIGGER AS $$\nBEGIN\n  PERFORM PG_NOTIFY('order_channel', 'id=' || NEW.id);\n  RETURN NEW;\nEND;\n$$ LANGUAGE plpgsql;</code></pre>",
  ["listen", "notify", "pubsub"])
# =============================================
# 04 - SCHEMA / TYPES
# =============================================

c("Schema",
  "What are the main PostgreSQL numeric types?",
  "<code>SMALLINT</code> - 2 bytes, -32768 to +32767.<br><code>INTEGER</code> - 4 bytes, -2.1B to +2.1B.<br><code>BIGINT</code> - 8 bytes, -9.2e18 to +9.2e18.<br><code>SERIAL</code> - auto-incrementing INTEGER (uses SEQUENCE).<br><code>BIGSERIAL</code> - auto-incrementing BIGINT.<br><code>NUMERIC(precision, scale)</code> - exact arbitrary-precision decimal.<br><code>NUMERIC(10,2)</code> stores up to 99,999,999.99.<br><code>REAL</code> - 4-byte IEEE float (6 decimal digits precision).<br><code>DOUBLE PRECISION</code> - 8-byte IEEE float (15 decimal digits).<br><b>Use NUMERIC for money, BIGINT for counts.</b>",
  ["data-types", "numeric", "integer", "serial"])

c("Schema",
  "What are the main PostgreSQL character types?",
  "<code>TEXT</code> - unlimited length (preferred, no performance penalty).<br><code>VARCHAR(n)</code> - variable-length with limit n characters (optional limit).<br><code>CHAR(n)</code> - fixed-length, blank-padded to n (rarely useful, mostly for legacy).<br><b>Best practice: just use TEXT</b> - there is virtually no performance difference. Use VARCHAR(n) only when the application requires a hard length limit.",
  ["data-types", "text", "varchar", "char"])

c("Schema",
  "What are the boolean, bytea, and uuid types?",
  "<code>BOOLEAN</code> - TRUE, FALSE, NULL. Accepts 't'/'f', 'true'/'false', 'yes'/'no', '1'/'0' as input.<br><code>BYTEA</code> - binary data (byte array). Stored as hex or escape format. Use for small blobs; for large files consider large objects or object storage.<br><code>UUID</code> - 128-bit universally unique identifier. Generate with <code>uuid-ossp</code> extension (<code>uuid_generate_v4()</code>) or <code>GEN_RANDOM_UUID()</code> (PG 13+).<br><pre><code>CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";\nSELECT UUID_GENERATE_V4(); -- random UUID\nSELECT GEN_RANDOM_UUID();  -- PG 13+ native</code></pre>",
  ["data-types", "boolean", "bytea", "uuid"])

c("Schema",
  "What are inet, cidr, and macaddr types?",
  "<code>INET</code> - IPv4 or IPv6 host address, optionally with netmask: <code>'192.168.1.5/24'</code><br><code>CIDR</code> - IPv4 or IPv6 network specification (netmask required): <code>'192.168.1.0/24'</code><br><code>MACADDR</code> / <code>MACADDR8</code> - MAC addresses: <code>'08:00:2b:01:02:03'</code><br><pre><code>SELECT '192.168.1.5'::INET << '192.168.1.0/24'::INET; -- t (contained by)\nSELECT '192.168.1.0/24'::CIDR >>= '192.168.1.0/25'::CIDR; -- t (contains or equals)</code></pre>",
  ["data-types", "inet", "cidr", "macaddr", "network"])

c("Schema",
  "What geometric types does PostgreSQL support?",
  "<code>POINT</code> - (x, y).<br><code>LINE</code> - infinite line: <code>{A,B,C}</code>.<br><code>LSEG</code> - line segment.<br><code>BOX</code> - rectangular box.<br><code>PATH</code> - closed or open path.<br><code>POLYGON</code> - closed polygon.<br><code>CIRCLE</code> - center point and radius.<br><pre><code>SELECT '(1,2)'::POINT <-> '(4,6)'::POINT; -- distance (5.0)\nCREATE TABLE locations (pos POINT, area BOX);\nINSERT INTO locations VALUES ('(3,4)', '((0,0),(10,10))');</code></pre>",
  ["data-types", "geometric", "point", "polygon"])

c("Schema",
  "What is the difference between TIMESTAMP and TIMESTAMPTZ?",
  "<code>TIMESTAMP</code> (aka timestamp without time zone) - stores date+time as-is. Ambiguous if across timezones.<br><code>TIMESTAMPTZ</code> (aka timestamp with time zone) - stores in UTC internally, converts to the session timezone on display. <b>Use TIMESTAMPTZ for almost everything</b> - it prevents timezone bugs.<br><pre><code>SET TIMEZONE = 'America/New_York';\nSELECT '2024-01-15 12:00:00+00'::TIMESTAMPTZ;\n-- 2024-01-15 07:00:00-05\nSELECT NOW();         -- TIMESTAMPTZ\nSELECT CURRENT_DATE;  -- DATE</code></pre>",
  ["data-types", "timestamp", "timestamptz", "timezone"])

c("Schema",
  "What is the INTERVAL type and how do you use arithmetic with it?",
  "<code>INTERVAL</code> stores a span of time. Supports addition/subtraction with dates and timestamps.<br><pre><code>SELECT NOW() + INTERVAL '7 days';          -- one week from now\nSELECT NOW() - INTERVAL '3 months 2 hours';\nSELECT '2024-12-25'::DATE - CURRENT_DATE; -- days until Christmas\nSELECT AGE('2024-12-31', '2024-01-01');   -- 11 mons 30 days\nSELECT JUSTIFY_HOURS('30 hours'::INTERVAL); -- 1 day 06:00:00\nSELECT JUSTIFY_DAYS('35 days'::INTERVAL);   -- 1 mon 5 days</code></pre>",
  ["data-types", "interval", "date-arithmetic"])

c("Schema",
  "What are enum types and when should you use them?",
  "Custom types with a fixed set of values. Useful for status columns with a limited, stable set of options.<br><pre><code>CREATE TYPE order_status AS ENUM (\n  'pending', 'confirmed', 'shipped', 'delivered', 'cancelled'\n);\n\nCREATE TABLE orders (\n  id SERIAL PRIMARY KEY,\n  status ORDER_STATUS DEFAULT 'pending'\n);\n-- Adding values (append only):\nALTER TYPE order_status ADD VALUE 'returned';\n-- Cannot remove values once added (without table rewrite).\n-- Alternative: TEXT with CHECK constraint - more flexible.</code></pre>",
  ["enum", "data-types", "custom-types"])

c("Schema",
  "What are domain types?",
  "A <b>domain</b> is a user-defined type based on an existing type, with optional constraints. It provides reusable validation without creating a full new type.<br><pre><code>CREATE DOMAIN email AS TEXT\n  CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');\n\nCREATE DOMAIN positive_money AS NUMERIC(12,2)\n  CHECK (VALUE >= 0);\n\nCREATE TABLE users (\n  id SERIAL PRIMARY KEY,\n  email EMAIL NOT NULL,\n  balance POSITIVE_MONEY DEFAULT 0\n);</code></pre>",
  ["domain", "data-types", "custom-types"])

c("Schema",
  "What are the main CREATE TABLE constraints?",
  "<code>PRIMARY KEY</code> - unique + not null, creates a unique index. Usually one per table.<br><code>FOREIGN KEY</code> - enforces referential integrity. Options: <code>ON DELETE CASCADE</code>, <code>ON DELETE SET NULL</code>, <code>ON DELETE RESTRICT</code>.<br><code>UNIQUE</code> - all values in column(s) must be distinct (allows NULLs as distinct in PG).<br><code>CHECK</code> - boolean expression must be true (or NULL).<br><code>NOT NULL</code> - column cannot be NULL.<br><code>DEFAULT</code> - default value if not supplied.<br><code>EXCLUDE</code> - generalized uniqueness (e.g., no overlapping date ranges).",
  ["constraints", "create-table", "ddl"])

c("Schema",
  "Give a complete CREATE TABLE with all constraint types.",
  "<pre><code>CREATE TABLE products (\n  id          SERIAL PRIMARY KEY,\n  sku         TEXT NOT NULL UNIQUE,\n  name        TEXT NOT NULL,\n  category_id INT REFERENCES categories(id) ON DELETE SET NULL,\n  price       NUMERIC(10,2) NOT NULL CHECK (price > 0),\n  discount    NUMERIC(10,2) DEFAULT 0 CHECK (discount >= 0),\n  tags        TEXT[] DEFAULT '{}',\n  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),\n  updated_at  TIMESTAMPTZ,\n  EXCLUDE USING GIST (\n    sku WITH =,\n    (COALESCE(updated_at, created_at)) WITH &&\n  )\n);</code></pre>",
  ["constraints", "create-table", "example"])

c("Schema",
  "How does table partitioning work in PostgreSQL?",
  "Partitioning splits a large table into smaller physical tables (<b>partitions</b>) while presenting a single logical table. Three methods:<br><b>RANGE</b> - by value range (e.g., date ranges per month).<br><b>LIST</b> - by discrete values (e.g., region codes).<br><b>HASH</b> - by hash of key(s) (uniform distribution).<br><pre><code>CREATE TABLE orders (\n  id SERIAL,\n  created_at DATE NOT NULL,\n  total NUMERIC\n) PARTITION BY RANGE (created_at);\n\nCREATE TABLE orders_2024q1 PARTITION OF orders\n  FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');\nCREATE TABLE orders_2024q2 PARTITION OF orders\n  FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');\nCREATE TABLE orders_default PARTITION OF orders DEFAULT;</code></pre>",
  ["partitioning", "range", "list", "hash"])

c("Schema",
  "How does table inheritance work and how is it different from partitioning?",
  "PostgreSQL supports native <b>table inheritance</b> - child tables inherit columns from parent tables. Partitioning (PG 10+) is implemented using inheritance internally, but declarative partitioning should be preferred now.<br><pre><code>CREATE TABLE people (id SERIAL, name TEXT);\nCREATE TABLE students (major TEXT) INHERITS (people);\nCREATE TABLE staff (department TEXT) INHERITS (people);\n\nINSERT INTO students (name, major) VALUES ('Alice', 'CS');\nSELECT * FROM people;       -- shows Alice (rows in children appear in parent)\nSELECT * FROM ONLY people;  -- ONLY excludes child tables</code></pre>",
  ["inheritance", "partitioning-legacy"])

c("Schema",
  "What are sequences and how do identity columns differ?",
  "<b>SEQUENCE</b> - a number generator: <code>CREATE SEQUENCE myseq START 1000;</code> used with <code>SERIAL</code>.<br><b>IDENTITY columns</b> (PG 10+) - SQL-standard auto-increment, preferred over SERIAL because the sequence is <b>tightly coupled</b> to the column, preventing accidental drops and being more standards-compliant.<br><pre><code>-- New way (preferred):\nCREATE TABLE users (\n  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n  name TEXT\n);\n-- Old way (still widely used):\nCREATE TABLE users (\n  id SERIAL PRIMARY KEY,\n  name TEXT\n);\n-- Insert without specifying id:\nINSERT INTO users (name) VALUES ('Bob') RETURNING id;</code></pre>",
  ["sequences", "identity-columns", "serial"])

c("Schema",
  "What are the normal forms (1NF, 2NF, 3NF)?",
  "<b>1NF</b> - Atomic values. No repeating groups. Each cell holds a single value. No arrays of values in a single column (conceptually; PG arrays are a deliberate denormalization).<br><b>2NF</b> - 1NF + no partial dependencies. Non-key columns must depend on the <b>entire</b> primary key (relevant for composite keys).<br><b>3NF</b> - 2NF + no transitive dependencies. Non-key columns must not depend on other non-key columns.<br><pre><code>-- 3NF violation: city depends on zip, zip depends on city\nCREATE TABLE bad (id PK, city TEXT, zip TEXT, state TEXT);\n-- Fix: separate zip_codes(city, state) table, reference by zip.</code></pre>",
  ["normal-forms", "1nf", "2nf", "3nf", "database-design"])

c("Schema",
  "What is Row-Level Security (RLS)?",
  "RLS restricts which rows a user can access or modify, based on policies. Enabled per-table with <code>ALTER TABLE ... ENABLE ROW LEVEL SECURITY</code>. Policies use boolean expressions and a USING/CHECK clause.<br><pre><code>ALTER TABLE documents ENABLE ROW LEVEL SECURITY;\n\nCREATE POLICY user_docs ON documents\n  FOR SELECT\n  USING (owner_id = current_setting('app.current_user_id')::INT);\n\nCREATE POLICY user_docs_insert ON documents\n  FOR INSERT\n  WITH CHECK (owner_id = current_setting('app.current_user_id')::INT);\n-- Superusers and BYPASSRLS roles bypass RLS by default.</code></pre>",
  ["rls", "row-level-security", "security"])

# =============================================
# 05 - INDEXES / PERFORMANCE
# =============================================

c("Indexes",
  "What is the default index type (B-tree) and when is it used?",
  "<b>B-tree</b> is the default index type. It handles equality (<code>=</code>) and range (<code><, >, >=, <=, BETWEEN</code>) lookups, <code>IS NULL</code>, and <code>LIKE 'prefix%'</code> (anchored pattern). It does <b>NOT</b> support <code>LIKE '%anywhere%'</code> efficiently. B-trees are balanced, self-organizing, and work for most OLTP workloads.<br><pre><code>CREATE INDEX idx_users_email ON users (email);\n-- Equivalent to:\nCREATE INDEX idx_users_email ON users USING BTREE (email);</code></pre>",
  ["btree", "index-types", "default"])

c("Indexes",
  "What is a Hash index and when should you use it?",
  "Hash indexes support only <b>equality</b> comparisons (<code>=</code>). No range scans, no ordering. Smaller than B-tree for large keys. Since PG 10, Hash indexes are WAL-logged and crash-safe (safe for replicas).<br><pre><code>CREATE INDEX ON users USING HASH (email);\n-- Good for: WHERE email = 'user@example.com'\n-- Bad for:  WHERE email > 'a'  (not supported)\n-- Generally: B-tree is almost always good enough.\n-- Hash can save space on very wide keys with only equality checks.</code></pre>",
  ["hash", "index-types"])

c("Indexes",
  "What is a GIN index and when is it used?",
  "<b>Generalized Inverted Index</b> - indexes composite values (arrays, JSONB, tsvector, hstore). Each index entry maps a single key value (word, element, tag) to all rows containing that key. Slower to build/maintain than B-tree, but fast for <code>@></code>, <code>?</code>, <code>@@</code> lookups.<br><pre><code>CREATE INDEX ON events USING GIN (payload);\nSELECT * FROM events WHERE payload @> '{\"type\":\"login\"}';\nCREATE INDEX ON articles USING GIN (TO_TSVECTOR('english', body));\nSELECT * FROM articles WHERE TO_TSVECTOR('english', body) @@ PLAINTO_TSQUERY('postgresql');</code></pre>",
  ["gin", "index-types", "jsonb", "full-text-search"])

c("Indexes",
  "What is a GiST index and when is it used?",
  "<b>Generalized Search Tree</b> - a balanced tree structure supporting extensible search predicates. Used for geometric data (<code><<, &&, &<, <@</code>), full-text search (alternative to GIN), range types, and EXCLUDE constraints.<br><pre><code>CREATE INDEX ON locations USING GIST (pos);\nSELECT * FROM locations WHERE pos <@ '((0,0),(10,10))'::BOX;\n\n-- Range exclusion:\nCREATE TABLE rooms (room INT, during DATERANGE,\n  EXCLUDE USING GIST (room WITH =, during WITH &&)\n);</code></pre>",
  ["gist", "index-types", "geometric"])

c("Indexes",
  "What is an SP-GiST index?",
  "<b>Space-Partitioned GiST</b> - supports partitioned search trees where the search space is divided into non-overlapping regions. Used for GIS (quadtrees, k-d trees), IP routing (radix trees), and phone numbers. Generally more specialized than GiST.<br><pre><code>-- Useful for PostGIS geometry types internally.\nCREATE INDEX ON points USING SPGIST (location);\n-- PostGIS uses GiST more commonly; SP-GiST is for specific operators.</code></pre>",
  ["sp-gist", "index-types"])

c("Indexes",
  "What is a BRIN index?",
  "<b>Block Range INdex</b> - stores min/max summaries for <b>ranges of physical blocks</b> (e.g., 128 pages per range). Extremely small compared to B-tree (often 1000x smaller). Best for very large tables where data is physically correlated with the indexed column (e.g., append-only INSERT with increasing timestamps).<br><pre><code>CREATE INDEX ON sensor_readings USING BRIN (recorded_at)\n  WITH (pages_per_range = 32);\n-- Checks: is the value possibly in this range of pages?\n-- Pre-filter for large sequential-ish data.</code></pre>",
  ["brin", "index-types", "large-tables"])

c("Indexes",
  "What is a partial index?",
  "A partial index indexes only rows matching a WHERE clause, reducing index size and maintenance cost. Ideal for queries on a subset of data (e.g., active users, unprocessed items).<br><pre><code>-- Index only active users:\nCREATE INDEX idx_active_users ON users (email)\n  WHERE active = true;\n-- Index only unshipped orders:\nCREATE INDEX idx_pending_orders ON orders (created_at)\n  WHERE status = 'pending';\n-- Index only non-deleted rows:\nCREATE INDEX idx_soft_delete ON documents (title)\n  WHERE deleted_at IS NULL;</code></pre>",
  ["partial-index", "index"])

c("Indexes",
  "What is a covering index (INCLUDE)?",
  "A covering index uses <code>INCLUDE</code> to store extra columns in the index leaf nodes - enabling <b>index-only scans</b> without needing to visit the table. Key columns are part of the tree structure; included columns are just payload.<br><pre><code>CREATE INDEX idx_orders_user_date ON orders (user_id, created_at)\n  INCLUDE (total, status);\n\nSELECT user_id, created_at, total, status\nFROM orders\nWHERE user_id = 42 AND created_at > '2024-01-01';\n-- Can use index-only scan - no heap lookup needed.</code></pre>",
  ["covering-index", "include", "index-only-scan"])

c("Indexes",
  "What is an expression index?",
  "An index on an expression (function result) rather than raw column values. Used when queries filter or sort by transformed values.<br><pre><code>-- Case-insensitive email lookup:\nCREATE INDEX ON users (LOWER(email));\nSELECT * FROM users WHERE LOWER(email) = 'alice@example.com';\n\n-- Date extraction:\nCREATE INDEX ON orders ((created_at::DATE));\nSELECT * FROM orders WHERE created_at::DATE = '2024-03-15';\n\n-- JSONB path extraction:\nCREATE INDEX ON events ((payload ->> 'type'));\nSELECT * FROM events WHERE payload ->> 'type' = 'login';</code></pre>",
  ["expression-index", "index"])

c("Indexes",
  "How does column order matter in multicolumn indexes?",
  "B-tree multicolumn indexes follow the <b>leftmost prefix rule</b>: an index on <code>(a, b, c)</code> supports:<br>- <code>WHERE a = 1</code><br>- <code>WHERE a = 1 AND b = 2</code><br>- <code>WHERE a = 1 AND b = 2 AND c = 3</code><br>- <code>WHERE a = 1 AND c = 3</code> (skips b, but a still leads)<br>It does <b>NOT</b> support: <code>WHERE b = 2</code> (misses leading column).<br>Put the <b>most selective / most frequently filtered</b> column <b>first</b>.",
  ["multicolumn-index", "column-order", "btree"])

c("Indexes",
  "What does the CLUSTER command do?",
  "<code>CLUSTER</code> physically reorders a table's rows to match an index order, improving sequential read performance. It's a one-time operation (not maintained automatically) and holds an ACCESS EXCLUSIVE lock.<br><pre><code>CLUSTER users USING idx_users_created_at;\n\n-- Cluster all tables that have been clustered before:\nCLUSTER;\n\n-- Check correlation:\nSELECT tablename, attname, correlation\nFROM pg_stats WHERE tablename = 'users';\n-- correlation close to 1 or -1 = physically ordered.</code></pre>",
  ["cluster", "table-ordering", "performance"])

c("Indexes",
  "What is REINDEX and when should you use it?",
  "<code>REINDEX</code> rebuilds an index from scratch, removing bloat and restoring performance. Use after large DELETE/UPDATE operations or when <code>pg_stat_user_indexes</code> shows high bloat.<br><pre><code>REINDEX INDEX idx_users_email;        -- single index\nREINDEX TABLE users;                    -- all indexes on table\nREINDEX INDEX CONCURRENTLY idx_email;   -- non-blocking (PG 12+)\nREINDEX SCHEMA CONCURRENTLY public;     -- all indexes in schema</code></pre>",
  ["reindex", "index-maintenance"])

c("Indexes",
  "What does CREATE INDEX CONCURRENTLY do?",
  "Building an index normally takes a <code>SHARE</code> lock (blocks writes). <code>CONCURRENTLY</code> builds the index without blocking writes by performing two table scans and a validation pass - takes longer but is production-safe.<br><pre><code>CREATE INDEX CONCURRENTLY idx_users_email ON users (email);\n-- Must run outside a transaction block (auto-commit mode).\n-- Cannot be used inside a transaction.</code></pre>",
  ["concurrently", "index-creation", "production"])

c("Indexes",
  "What are index-only scans, bitmap scans, and sequential scans?",
  "<b>Sequential Scan</b> - reads every page of the table. Fast for small tables or when fetching a large fraction of rows (no index overhead).<br><b>Index Scan</b> - traverses index, then fetches heap rows. Good for selective queries.<br><b>Index-Only Scan</b> - all needed columns are in the index (covering), no heap fetch. Requires <code>VACUUM</code> to keep visibility map up to date.<br><b>Bitmap Index Scan -> Bitmap Heap Scan</b> - builds a bitmap of matching rows from the index (combining multiple indexes), then fetches heap pages in physical order. Used for moderate selectivity or multi-index combinations.",
  ["scan-types", "sequential-scan", "index-scan", "bitmap-scan"])

c("Indexes",
  "How do you read EXPLAIN ANALYZE output?",
  "<pre><code>EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)\nSELECT * FROM orders WHERE user_id = 42;\n\n-- Key metrics:\n-- actual time=0.123..4.567  (first row..last row, ms)\n-- rows=1500                (actual rows returned)\n-- loops=1                  (how many times this node executed)\n-- Buffers: shared hit=12 read=3  (hit=cached, read=disk)\n-- Planning Time: 0.123 ms\n-- Execution Time: 5.678 ms\n\n-- Look for:\n-- - Seq Scan on large tables (missing index)\n-- - Lots of 'read' buffers (cold cache / not enough shared_buffers)\n-- - High (actual rows) vs (estimated rows) - bad statistics\n-- - Nested Loop with high loops (missing index on join column)</code></pre>",
  ["explain-analyze", "query-planning", "performance"])

c("Indexes",
  "What does SET enable_seqscan = off do?",
  "Temporarily disables sequential scans to force the planner to use an index. Useful for testing whether an index would help - but <b>never</b> use in production. The planner usually knows better.<br><pre><code>SET enable_seqscan = off;\nEXPLAIN SELECT * FROM users WHERE id = 42;\n-- Now compare plan with seqscan on vs off.\nSET enable_seqscan = on;  -- reset</code></pre>",
  ["enable-seqscan", "query-planning", "testing"])

c("Indexes",
  "What useful information is in pg_stat_user_indexes?",
  "<pre><code>SELECT schemaname, tablename, indexrelname,\n  idx_scan,    -- number of index scans\n  idx_tup_read,  -- tuples returned from index scans\n  idx_tup_fetch  -- live rows fetched from table\nFROM pg_stat_user_indexes\nORDER BY idx_scan ASC;\n-- idx_scan = 0 -> unused index (candidate for dropping)\n-- idx_tup_fetch close to idx_tup_read -> mostly index-only potential</code></pre>",
  ["pg-stat-user-indexes", "monitoring", "index-usage"])

c("Indexes",
  "What is VACUUM and why is it critical?",
  "VACUUM reclaims storage occupied by dead tuples (old MVCC row versions no longer visible to any transaction). Without VACUUM, tables grow indefinitely (bloat). It also updates the <b>visibility map</b> for index-only scans and freezes old transaction IDs to prevent wraparound.<br><pre><code>VACUUM (VERBOSE, ANALYZE) users;\n-- ANALYZE also updates statistics for the query planner.\n-- Regular VACUUM doesn't return space to OS (marks pages reusable).\n-- VACUUM FULL rewrites entire table, reclaims disk space, but locks exclusively.\n\n-- Autovacuum is enabled by default - it runs automatically.</code></pre>",
  ["vacuum", "autovacuum", "maintenance"])

c("Indexes",
  "What is autovacuum and how do you tune it?",
  "Autovacuum is a background worker that automatically runs VACUUM and ANALYZE. Tuning parameters (postgresql.conf):<br><pre><code>autovacuum = on                          -- enable (default)\nautovacuum_max_workers = 5               -- concurrent workers\nautovacuum_naptime = 60s                 -- how often it wakes up\nautovacuum_vacuum_threshold = 50         -- base threshold\nautovacuum_vacuum_scale_factor = 0.2     -- 20% of table rows changed\nautovacuum_vacuum_cost_limit = 200       -- throttle limit\n-- Per-table tuning:\nALTER TABLE users SET (\n  autovacuum_vacuum_scale_factor = 0.05  -- vacuum after 5% changes\n);</code></pre>",
  ["autovacuum", "tuning", "maintenance"])

c("Indexes",
  "What is table bloat and what is fillfactor?",
  "<b>Bloat</b>: dead tuples occupy space inside pages. Caused by frequent UPDATE/DELETE without enough VACUUM. Measured with <code>pgstattuple</code> extension or querying <code>pg_stat_user_tables.n_dead_tup</code>.<br><b>FILLFACTOR</b>: percentage of a page to fill on INSERT (default=100). Lower values (e.g., 70) leave room for in-page UPDATEs, reducing fragmentation for hot-update tables.<br><pre><code>CREATE TABLE metrics (id INT, val INT) WITH (fillfactor = 70);\nALTER TABLE users SET (fillfactor = 80);\n-- Rebuild to apply: VACUUM FULL users; or CLUSTER;</code></pre>",
  ["bloat", "fillfactor", "vacuum"])

# =============================================
# 06 - TRANSACTIONS / CONCURRENCY
# =============================================

c("Transactions",
  "How do BEGIN, COMMIT, and ROLLBACK work?",
  "<pre><code>BEGIN;\n  UPDATE accounts SET balance = balance - 100 WHERE id = 1;\n  UPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;\n-- If anything fails before COMMIT:\n-- ROLLBACK;\n\n-- Every statement is auto-committed outside explicit transactions.\n-- A single BEGIN...COMMIT block = one atomic unit.\n-- Nested transactions don't exist - use SAVEPOINT instead.</code></pre>",
  ["begin", "commit", "rollback", "transaction"])

c("Transactions",
  "What are savepoints?",
  "Savepoints create sub-transaction checkpoints - you can roll back to a savepoint without aborting the entire transaction.<br><pre><code>BEGIN;\n  UPDATE accounts SET balance = balance - 100 WHERE id = 1;\n  SAVEPOINT transfer_to_2;\n  UPDATE accounts SET balance = balance + 100 WHERE id = 2;\n  -- Oops, wrong account:\n  ROLLBACK TO transfer_to_2;\n  UPDATE accounts SET balance = balance + 100 WHERE id = 3;\nCOMMIT;</code></pre>",
  ["savepoints", "sub-transactions"])

c("Transactions",
  "What are PostgreSQL's transaction isolation levels?",
  "<b>PostgreSQL actually implements only 3 of 4 SQL standard levels:</b><br><code>READ COMMITTED</code> - default. Each statement sees committed data as of the statement's start time.<br><code>REPEATABLE READ</code> - sees snapshot as of transaction start. No phantom reads in PG (PG's RR is actually 'snapshot isolation').<br><code>SERIALIZABLE</code> - serializable snapshot isolation (SSI). Detects serialization anomalies and aborts transactions that would violate serializability.<br><code>READ UNCOMMITTED</code> - accepted but treated as READ COMMITTED (PG doesn't have dirty reads).<br><pre><code>BEGIN ISOLATION LEVEL SERIALIZABLE;\nSHOW TRANSACTION_ISOLATION;</code></pre>",
  ["isolation-levels", "read-committed", "repeatable-read", "serializable"])

c("Transactions",
  "What are the phantom reads, dirty reads, and non-repeatable reads?",
  "<b>Dirty Read</b> - reading uncommitted data from another transaction. PG prevents these entirely.<br><b>Non-Repeatable Read</b> - same SELECT returns different data because another transaction committed an UPDATE. Prevented by REPEATABLE READ and above.<br><b>Phantom Read</b> - same SELECT returns different data because another transaction committed an INSERT. Prevented by REPEATABLE READ in PG (strict definition) and SERIALIZABLE.<br><b>Serialization Anomaly</b> - concurrent transactions produced a result impossible in any serial order. Prevented only by SERIALIZABLE.<br><pre><code>-- Summary:\n-- Isolation Level    | Dirty | Non-Repeat | Phantom | Serial Anomaly\n-- READ UNCOMMITTED   | No(PG)|  Yes       | Yes     | Yes\n-- READ COMMITTED     | No    |  Yes       | Yes     | Yes\n-- REPEATABLE READ    | No    |  No        | No (PG) | Yes\n-- SERIALIZABLE       | No    |  No        | No      | No</code></pre>",
  ["isolation-levels", "phantom-reads", "dirty-reads"])

c("Transactions",
  "How does MVCC tuple visibility work internally?",
  "Each row version (tuple) has hidden system columns:<br><code>xmin</code> - transaction ID that <b>created</b> this version.<br><code>xmax</code> - transaction ID that <b>deleted/updated</b> this version (0 if still alive).<br><b>Visibility check</b>: a tuple is visible to transaction T if:<br>1. <code>xmin</code> is committed and <code>xmin < T</code> (created before T).<br>2. <code>xmax</code> is 0 or not yet committed or <code>xmax > T</code> (not yet deleted).<br>3. <code>xmin</code> is not T's own aborted sub-transaction, etc.<br><pre><code>SELECT xmin, xmax, * FROM users;\n-- Shows internal transaction IDs - useful for debugging.</code></pre>",
  ["mvcc", "xmin", "xmax", "visibility"])

c("Transactions",
  "What are deadlocks and how does PostgreSQL handle them?",
  "A <b>deadlock</b> occurs when two transactions each hold locks the other needs. PostgreSQL automatically detects deadlocks (usually within <code>deadlock_timeout</code>, default 1s) and aborts one transaction (the 'victim') with error <code>40P01: deadlock detected</code>.<br><pre><code>-- Example: T1 locks row A, T2 locks row B\n-- T1 tries to lock row B - waits\n-- T2 tries to lock row A - deadlock detected\n-- PostgreSQL kills one, the other proceeds.\n\n-- Prevention: always lock resources in the same order across transactions.</code></pre>",
  ["deadlocks", "concurrency", "locking"])

c("Transactions",
  "What are advisory locks?",
  "Application-defined locks not tied to any database object. Useful for coordinating application-level resources (e.g., singleton job execution, distributed mutex).<br><pre><code>-- Session-level (held until release or disconnect):\nSELECT PG_ADVISORY_LOCK(123);   -- blocks until acquired\nSELECT PG_TRY_ADVISORY_LOCK(123); -- returns FALSE if not available\nSELECT PG_ADVISORY_UNLOCK(123);\n\n-- Transaction-level (released at commit/rollback):\nSELECT PG_ADVISORY_XACT_LOCK(456);\n\n-- Two-argument version (e.g., namespace + ID):\nSELECT PG_ADVISORY_LOCK(1, 42);</code></pre>",
  ["advisory-locks", "locking", "concurrency"])

c("Transactions",
  "What does SELECT ... FOR UPDATE do?",
  "Explicit row-level lock that blocks other <code>FOR UPDATE</code> / <code>FOR NO KEY UPDATE</code> on the same rows until the transaction commits. Used to prevent concurrent modifications.<br><pre><code>BEGIN;\nSELECT balance FROM accounts WHERE id = 1 FOR UPDATE;\n-- Other transaction trying FOR UPDATE on id=1 will wait.\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nCOMMIT;\n\n-- Variations:\nFOR NO KEY UPDATE - weaker, doesn't block non-key updates.\nFOR SHARE - blocks writes, allows reads (like a read lock).\nFOR KEY SHARE - weakest, allows non-key updates.</code></pre>",
  ["for-update", "row-locking", "concurrency"])

c("Transactions",
  "What do SKIP LOCKED and NOWAIT do?",
  "<code>SKIP LOCKED</code> - skip rows that are already locked by another transaction. Perfect for work queues (no blocking).<br><code>NOWAIT</code> - error immediately if any selected row is locked, instead of waiting.<br><pre><code>-- Queue worker pattern:\nBEGIN;\nSELECT * FROM tasks\nWHERE status = 'pending'\nORDER BY created_at\nLIMIT 1\nFOR UPDATE SKIP LOCKED;  -- grab next available task\n-- Process it...\nUPDATE tasks SET status = 'done' WHERE id = ...;\nCOMMIT;</code></pre>",
  ["skip-locked", "nowait", "for-update", "queue"])

c("Transactions",
  "What is Serializable Snapshot Isolation (SSI)?",
  "PostgreSQL's implementation of <code>SERIALIZABLE</code> uses SSI - it tracks <b>read-write dependencies</b> between concurrent transactions and detects <b>serialization anomalies</b>. If a dangerous pattern is detected, one transaction is aborted with <code>40001: could not serialize access</code>. The application must retry.<br><pre><code>BEGIN ISOLATION LEVEL SERIALIZABLE;\n-- ...\nCOMMIT;  -- may fail with serialization error - retry the whole transaction\n\n-- SERIALIZABLE overhead is moderate but higher than READ COMMITTED.\n-- Use when correctness requires total isolation, or use READ COMMITTED\n-- with explicit FOR UPDATE for specific conflict scenarios.</code></pre>",
  ["serializable", "ssi", "isolation"])

# =============================================
# 07 - ADMINISTRATION
# =============================================

c("Admin",
  "What are the essential psql meta-commands?",
  "<code>\\l</code> - list databases.<br><code>\\c dbname</code> - connect to a database.<br><code>\\d table</code> - describe table (columns, types, indexes).<br><code>\\dt</code> - list tables.<br><code>\\di</code> - list indexes.<br><code>\\dv</code> - list views.<br><code>\\dm</code> - list materialized views.<br><code>\\du</code> - list roles/users.<br><code>\\df</code> - list functions.<br><code>\\dn</code> - list schemas.<br><code>\\dx</code> - list extensions.<br><code>\\dp</code> - list table privileges.<br><code>\\d+</code> - verbose version (shows storage, access method).<br><code>\\x</code> - toggle expanded display (vertical output).<br><code>\\e</code> - open last query in editor ($EDITOR).<br><code>\\i file.sql</code> - execute SQL file.<br><code>\\timing</code> - toggle query timing display.<br><code>\\copy</code> - client-side COPY (works with local filesystem).<br><code>\\watch [sec]</code> - repeat query every N seconds.",
  ["psql", "meta-commands", "administration"])

c("Admin",
  "How does pg_dump and pg_restore work?",
  "<b>pg_dump</b> extracts a single database to a file. <b>pg_restore</b> restores from archive formats. <b>pg_dumpall</b> dumps all databases and global objects (roles, tablespaces).<br><pre><code># Plain SQL (restore with psql):\npg_dump -U postgres mydb > mydb.sql\n\n# Custom format (restore with pg_restore - flexible):\npg_dump -U postgres -Fc -f mydb.dump mydb\npg_restore -U postgres -d mydb -j 4 mydb.dump\n\n# Directory format (parallel dump):\npg_dump -U postgres -Fd -f dumpdir/ -j 4 mydb\n\n# Restore specific table from custom dump:\npg_restore -U postgres -d mydb -t users mydb.dump\n\n# Schema only / Data only:\npg_dump --schema-only mydb\npg_dump --data-only mydb</code></pre>",
  ["pg-dump", "pg-restore", "backup"])

c("Admin",
  "What is pg_basebackup and PITR?",
  "<b>pg_basebackup</b> - creates a physical (filesystem-level) backup of the entire PostgreSQL cluster. Basis for standby servers and PITR.<br><b>PITR (Point-In-Time Recovery)</b> - restore a base backup, then replay WAL segments up to a specific point in time. Requires WAL archiving to be configured.<br><pre><code># Create base backup:\npg_basebackup -D /backup/base -Ft -z -P\n\n# Archive WAL (postgresql.conf):\narchive_mode = on\narchive_command = 'cp %p /archive/%f'\n\n# PITR recovery (recovery.conf / signal files in PG 12+):\ntouch $PGDATA/recovery.signal\n# Set restore_command and recovery_target_time in postgresql.conf\nrestore_command = 'cp /archive/%f %p'\nrecovery_target_time = '2024-03-15 14:30:00'</code></pre>",
  ["backup", "pitr", "pg-basebackup", "wal"])

c("Admin",
  "What key information does pg_stat_activity show?",
  "<pre><code>SELECT pid, usename, application_name, state,\n       query_start, state_change, wait_event_type, wait_event,\n       LEFT(query, 80) AS query_preview\nFROM pg_stat_activity\nWHERE state != 'idle';\n\n-- Key columns:\n-- pid: process ID (use with pg_terminate_backend(pid))\n-- state: active, idle, idle in transaction, idle in transaction (aborted)\n-- wait_event: what it's waiting for (LWLock, Lock, IO, etc.)\n-- backend_start: connection time\n-- query_start: when current query started\n-- Age of transaction: now() - xact_start (long = problem)\n\n-- Kill a query:\nSELECT PG_TERMINATE_BACKEND(12345);\nSELECT PG_CANCEL_BACKEND(12345);  -- gentler, cancels the query only</code></pre>",
  ["pg-stat-activity", "monitoring", "sessions"])

c("Admin",
  "What does pg_stat_statements track?",
  "Extension that tracks execution statistics for <b>all queries</b>, normalized (parameters replaced with $1, $2). Essential for finding slow/top queries.<br><pre><code>CREATE EXTENSION pg_stat_statements;\n\n-- Top 10 slowest queries (mean time):\nSELECT calls, ROUND(mean_exec_time::NUMERIC, 2) AS avg_ms,\n       ROUND(total_exec_time::NUMERIC, 2) AS total_ms, rows,\n       LEFT(query, 150) AS query_preview\nFROM pg_stat_statements\nORDER BY mean_exec_time DESC\nLIMIT 10;\n\n-- Reset stats:\nSELECT PG_STAT_STATEMENTS_RESET();</code></pre>",
  ["pg-stat-statements", "monitoring", "query-analysis"])

c("Admin",
  "How do you monitor locks with pg_locks?",
  "<pre><code>SELECT l.pid, l.locktype, l.mode, l.granted,\n       l.relation::REGCLASS AS table_name,\n       a.query AS blocked_query\nFROM pg_locks l\nLEFT JOIN pg_stat_activity a ON a.pid = l.pid\nWHERE NOT l.granted;  -- only blocked lock requests\n\n-- Tree of blocking relationships:\nSELECT blocked.pid AS blocked_pid,\n       blocked.query AS blocked_query,\n       blocking.pid AS blocking_pid,\n       blocking.query AS blocking_query\nFROM pg_locks bl\nJOIN pg_stat_activity blocked ON blocked.pid = bl.pid\nJOIN pg_locks bk ON bl.locktype = bk.locktype\n  AND bl.database IS NOT DISTINCT FROM bk.database\n  AND bl.relation IS NOT DISTINCT FROM bk.relation\n  AND bl.page IS NOT DISTINCT FROM bk.page\n  AND bl.tuple IS NOT DISTINCT FROM bk.tuple\n  AND bl.transactionid IS NOT DISTINCT FROM bk.transactionid\nJOIN pg_stat_activity blocking ON blocking.pid = bk.pid\nWHERE NOT bl.granted AND bk.granted;</code></pre>",
  ["pg-locks", "monitoring", "locking"])

c("Admin",
  "What is pg_hba.conf and how does authentication work?",
  "<b>pg_hba.conf</b> (Host-Based Authentication) controls who can connect and how. Each line specifies: type, database, user, address, auth method.<br><pre><code># TYPE  DATABASE  USER  ADDRESS          METHOD\nlocal   all       all                    peer       # local socket\nhost    all       all   127.0.0.1/32     scram-sha-256\nhost    all       all   10.0.0.0/8       scram-sha-256\nhost    mydb      app   0.0.0.0/0        scram-sha-256\nhost    all       all   0.0.0.0/0        reject     # block all else\n\n# Auth methods: trust, peer, scram-sha-256 (recommended),\n#               md5 (deprecated), password (plaintext, DON'T),\n#               cert, ldap, gssapi, radius</code></pre>",
  ["pg-hba", "authentication", "security"])

c("Admin",
  "What are the key postgresql.conf settings?",
  "<b>Memory</b>:<br><code>shared_buffers</code> - 25% of RAM (for dedicated PG server).<br><code>effective_cache_size</code> - 50-75% of RAM (planner hint).<br><code>work_mem</code> - per-operation sort/hash memory (start 4MB, raise for analytics).<br><code>maintenance_work_mem</code> - for VACUUM, CREATE INDEX (10% of RAM).<br><br><b>Connections</b>:<br><code>max_connections</code> - hard limit (use PgBouncer if > 200).<br><br><b>WAL</b>:<br><code>wal_level = replica</code> (for replication).<br><code>max_wal_size</code> - max WAL kept before checkpoint.<br><br><b>Planning</b>:<br><code>random_page_cost</code> - 1.1 for SSD, 4.0 for HDD.<br><pre><code>SELECT name, setting, unit, context\nFROM pg_settings\nWHERE name IN ('shared_buffers','work_mem','max_connections');</code></pre>",
  ["postgresql-conf", "configuration", "tuning"])

c("Admin",
  "How do GRANT and REVOKE work with roles and privileges?",
  "PostgreSQL has a rich privilege system. Privileges: <code>SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER</code> (per table), <code>CREATE, CONNECT, TEMP</code> (per database), <code>USAGE, CREATE</code> (per schema), <code>EXECUTE</code> (per function).<br><pre><code>-- Grant table access:\nGRANT SELECT, INSERT ON users TO app_role;\n\n-- Grant usage on schema (needed to access objects in it):\nGRANT USAGE ON SCHEMA public TO app_role;\n\n-- Grant all on all existing tables in a schema:\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO app_role;\n\n-- Grant defaults for future tables:\nALTER DEFAULT PRIVILEGES IN SCHEMA public\n  GRANT SELECT ON TABLES TO app_role;\n\n-- Revoke:\nREVOKE INSERT ON users FROM app_role;\n\n-- Role membership:\nGRANT app_role TO bob;\nREVOKE app_role FROM bob;</code></pre>",
  ["grant", "revoke", "permissions", "security"])

c("Admin",
  "What are role attributes?",
  "Roles can have attributes that control their capabilities:<br><code>LOGIN</code> - can connect (without this, role is a group only).<br><code>SUPERUSER</code> - bypass all permission checks.<br><code>CREATEDB</code> - can create databases.<br><code>CREATEROLE</code> - can create/drop/alter roles.<br><code>REPLICATION</code> - can initiate replication connections.<br><code>BYPASSRLS</code> - bypasses row-level security.<br><code>INHERIT</code> - inherits privileges from parent roles (default).<br><pre><code>CREATE ROLE app_readonly WITH LOGIN PASSWORD 'secret';\nCREATE ROLE app_writer WITH LOGIN CREATEDB INHERIT;\nALTER ROLE app_readonly WITH NOLOGIN;  -- disable login\nALTER ROLE app_writer WITH SUPERUSER;   -- grant superuser</code></pre>",
  ["roles", "attributes", "security"])

c("Admin",
  "How do schemas and search_path work?",
  "<code>search_path</code> determines the order in which schemas are searched for unqualified object names. Default: <code>\"$user\", public</code> (user-named schema first, then public).<br><pre><code>-- Set search path:\nSET search_path = myschema, public;\n\n-- Permanent for a role:\nALTER ROLE app_user SET search_path = app, public;\n\n-- Permanent for a database:\nALTER DATABASE mydb SET search_path = app, public;\n\n-- Create objects in a specific schema:\nCREATE TABLE myschema.my_table (id INT);\n\n-- Check current search path:\nSHOW search_path;\n\n-- Note: never put untrusted users' schemas early in search_path\n-- (the \"$user\" default can be a security risk in multi-tenant setups).</code></pre>",
  ["schemas", "search-path", "namespaces"])

c("Admin",
  "What are pg_cron and pg_partman?",
  "<b>pg_cron</b> - a cron-like job scheduler inside PostgreSQL. Schedules SQL commands or procedures in the database itself (no external cron).<br><pre><code>CREATE EXTENSION pg_cron;\nSELECT CRON.SCHEDULE(\n  'nightly-vacuum',   -- job name\n  '0 3 * * *',        -- cron schedule (3 AM daily)\n  'VACUUM ANALYZE orders'\n);\nSELECT * FROM CRON.JOB;  -- list scheduled jobs\nSELECT CRON.UNSCHEDULE('nightly-vacuum');</code></pre><b>pg_partman</b> - extension for automated partition management. Creates new partitions automatically and detaches old ones based on configuration.<br><pre><code>CREATE EXTENSION pg_partman;\nSELECT PARTMAN.CREATE_PARENT(\n  p_parent_table := 'public.orders',\n  p_control := 'created_at',\n  p_type := 'native',\n  p_interval := '1 month',\n  p_premake := 4  -- create 4 future partitions\n);</code></pre>",
  ["pg-cron", "pg-partman", "extensions"])

# =============================================
# 08 - GOTCHAS
# =============================================

c("Gotchas",
  "What happens when autovacuum falls behind?",
  "Dead tuples accumulate, causing <b>table bloat</b> - tables and indexes grow far beyond their live data size. Queries slow down because they must scan past dead tuples. Visibility map becomes stale, disabling index-only scans. Eventually, <b>transaction ID wraparound</b> risk emerges (aggressive vacuum kicks in, heavily impacting performance).<br><b>Causes</b>: high write rate on a single table, long-running transactions holding old snapshots, autovacuum throttled too aggressively, or <code>autovacuum_max_workers</code> too low.<br><b>Fix</b>: tune autovacuum, run manual VACUUM during low traffic, reduce long transactions.",
  ["autovacuum-blown", "bloat", "gotcha"])

c("Gotchas",
  "What is 'idle in transaction' and why is it dangerous?",
  "A connection in state <b>idle in transaction</b> has a transaction open but is doing nothing. It:<br>- Holds locks (blocking others)<br>- Holds a snapshot (preventing VACUUM from cleaning dead tuples created after it)<br>- Consumes a connection slot<br>- Can accumulate for hours, causing cascading performance issues<br><pre><code>-- Find idle-in-transaction sessions:\nSELECT pid, usename, state, xact_start,\n       NOW() - xact_start AS tx_age\nFROM pg_stat_activity\nWHERE state = 'idle in transaction'\n  AND xact_start < NOW() - INTERVAL '5 minutes';\n\n-- Kill long-idle transactions:\nSELECT PG_TERMINATE_BACKEND(pid)\nFROM pg_stat_activity\nWHERE state = 'idle in transaction'\n  AND xact_start < NOW() - INTERVAL '15 minutes';</code></pre>",
  ["idle-in-transaction", "locking", "gotcha"])

c("Gotchas",
  "What is connection limit exhaustion?",
  "Each PostgreSQL connection spawns a backend process consuming memory (~5-10 MB minimum). <code>max_connections</code> hard-limits total connections. When exhausted, new clients get <code>FATAL: sorry, too many clients already</code>.<br><b>Fixes</b>:<br>- Use a connection pooler (<b>PgBouncer</b>) in front of PostgreSQL.<br>- Reduce idle timeouts in pooler and application.<br>- Monitor <code>numbackends</code> in <code>pg_stat_database</code>.<br>- Use <code>reserved_connections</code> (PG 16+) for superuser/admin emergencies.",
  ["connection-limits", "pooling", "gotcha"])

c("Gotchas",
  "Why do sequence values have gaps?",
  "<code>SERIAL</code> / <code>SEQUENCE</code> values are never rolled back on transaction failure - sequences operate <b>outside</b> transaction boundaries for performance. Also, cached sequence values (default cache=1) can be lost on crash.<br><pre><code>CREATE SEQUENCE s CACHE 10;  -- allocates 10 values at once\n-- If crash occurs, unused cached values are lost (gap).\n-- If ROLLBACK after nextval(), that value is never reused.\n-- Sequences guarantee UNIQUE, not GAPLESS.\n-- For gapless, use a counter table with explicit locking\n-- (but don't - gapless is usually not needed).</code></pre>",
  ["sequence-gaps", "serial", "gotcha"])

c("Gotchas",
  "What is transaction ID wraparound and how to prevent it?",
  "XIDs are 32-bit integers. When the counter approaches 2^31, it wraps around - making old frozen XIDs appear newer than active XIDs, corrupting MVCC. PostgreSQL <b>freezes</b> old XIDs (sets xmin to <code>FrozenTransactionId</code>=2) via VACUUM. If VACUUM can't keep up, the database shuts down to prevent corruption.<br><pre><code>-- Check age of oldest XID (critical if > 1 billion):\nSELECT datname, AGE(DATFROZENXID) AS xid_age\nFROM pg_database ORDER BY xid_age DESC;\n\n-- Per-table:\nSELECT relname, AGE(relfrozenxid) AS frozen_age\nFROM pg_class WHERE relkind = 'r' ORDER BY frozen_age DESC;\n\n-- Force-freeze:\nVACUUM FREEZE;</code></pre>",
  ["wraparound", "xid", "freeze", "gotcha"])

c("Gotchas",
  "Why is SELECT * bad in production code?",
  "- <b>Fragile</b>: adding a column may break consumers reading by position.<br>- <b>Inefficient</b>: fetches unnecessary columns, disabling index-only scans (needs all columns).<br>- <b>Bandwidth waste</b>: sending unused data over the network.<br>- <b>TOAST overhead</b>: might fetch large TEXT/BYTEA columns unnecessarily.<br>- <b>Security</b>: may expose sensitive columns (passwords, tokens) added later.<br><pre><code>-- Bad:\nSELECT * FROM users WHERE id = 42;\n\n-- Good: list only needed columns:\nSELECT id, name, email FROM users WHERE id = 42;\n\n-- Exception: ad-hoc debugging in psql, EXPLAIN output, CTEs for dynamic SQL.</code></pre>",
  ["select-star", "best-practices", "gotcha"])

c("Gotchas",
  "How do NULLs affect aggregate functions?",
  "Except <code>COUNT(*)</code>, <b>all aggregate functions ignore NULLs</b>. This can lead to surprising results:<br><pre><code>SELECT AVG(salary) FROM employees;\n-- Ignores NULL salaries; average may be higher than expected.\n-- AVG of (100, NULL, 200) = 150, not 100.\n-- SUM of (10, NULL) = 10.\n\n-- COUNT(*) includes NULLs; COUNT(col) excludes them.\nSELECT COUNT(*), COUNT(salary) FROM employees;\n\n-- Use COALESCE to handle:\nSELECT AVG(COALESCE(salary, 0));  -- treat NULL as 0\nSELECT SUM(salary) / COUNT(*) AS true_avg;  -- manual avg with nulls as 0</code></pre>",
  ["nulls-in-aggregates", "gotcha"])

c("Gotchas",
  "What is the CTE optimization fence and how was it fixed?",
  "<b>Pre-PG 12</b>: CTEs were always materialized (optimization fence) - the planner couldn't push WHERE clauses into a CTE or reorder joins across CTE boundaries. This caused poor performance when filtering on CTE results.<br><pre><code>-- Pre-PG 12: CTE materialized, all 1M rows processed before filtering\nWITH all_orders AS (\n  SELECT * FROM orders  -- 1M rows\n)\nSELECT * FROM all_orders WHERE user_id = 42;  -- filter applied late\n\n-- PG 12+: CTEs are NOT MATERIALIZED by default (inline like subqueries)\n-- Same query now pushes user_id filter into the scan.\n\n-- Force old behavior:\nWITH all_orders AS MATERIALIZED (SELECT * FROM orders)\nSELECT * FROM all_orders WHERE user_id = 42;\n\n-- Force inlining (if default still materializes):\nWITH cte AS NOT MATERIALIZED (SELECT ...)</code></pre>",
  ["cte-fence", "optimization", "postgresql-12", "gotcha"])

c("Gotchas",
  "How do ORMs cause N+1 query problems?",
  "ORMs (ActiveRecord, SQLAlchemy, Hibernate, Prisma) often execute one query to fetch a list, then one query <b>per item</b> to fetch related data - the N+1 problem.<br><pre><code>-- ORM generates:\nSELECT * FROM users WHERE active = true;           -- 1 query (1000 rows)\nSELECT * FROM posts WHERE user_id = 1;  -- N queries\nSELECT * FROM posts WHERE user_id = 2;  -- one per user\nSELECT * FROM posts WHERE user_id = 3;\n-- ... 1000 more queries!\n\n-- PostgreSQL can do this in ONE query:\nSELECT u.*, p.*\nFROM users u\nLEFT JOIN posts p ON p.user_id = u.id\nWHERE u.active = true;\n\n-- Or with array aggregation for nesting:\nSELECT u.*,\n  COALESCE(JSONB_AGG(JSONB_BUILD_OBJECT('id', p.id, 'title', p.title))\n    FILTER (WHERE p.id IS NOT NULL), '[]') AS posts\nFROM users u\nLEFT JOIN posts p ON p.user_id = u.id\nWHERE u.active = true\nGROUP BY u.id;</code></pre>",
  ["orm", "n-plus-one", "gotcha"])

c("Gotchas",
  "Why should you always index foreign key columns?",
  "Unindexed foreign keys cause <b>full table scans</b> on the referencing table when the parent row is UPDATEd or DELETEd (to enforce referential integrity). Also, JOINs on the FK column will do sequential scans.<br><pre><code>-- Users table\nCREATE TABLE users (id SERIAL PRIMARY KEY);\n-- Posts table with FK but NO INDEX:\nCREATE TABLE posts (id SERIAL, user_id INT REFERENCES users(id));\n\n-- When DELETE FROM users WHERE id=42 runs, PostgreSQL must scan\n-- ALL of posts to find rows with user_id=42 - very slow!\n\n-- Always add:\nCREATE INDEX idx_posts_user_id ON posts (user_id);\n\n-- Find unindexed FKs:\nSELECT c.conname, c.conrelid::REGCLASS AS table,\n       a.attname AS fk_column\nFROM pg_constraint c\nJOIN pg_attribute a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid\nWHERE c.contype = 'f'\n  AND NOT EXISTS (\n    SELECT 1 FROM pg_index i\n    WHERE i.indrelid = c.conrelid\n      AND i.indkey[0] = c.conkey[0]\n  );</code></pre>",
  ["foreign-key-index", "unindexed-fk", "gotcha"])

c("Gotchas",
  "What are dead tuples and how do you detect bloat?",
  "Dead tuples are old MVCC row versions no longer visible to any transaction. They accumulate until VACUUM cleans them. Detect with <code>pgstattuple</code>:<br><pre><code>CREATE EXTENSION pgstattuple;\n\nSELECT * FROM PGSTATTUPLE('orders');\n-- dead_tuple_percent: percentage of dead tuples\n-- free_percent: free space in pages\n\n-- Approximate dead rows from stats:\nSELECT schemaname, relname, n_live_tup, n_dead_tup,\n       CASE WHEN n_live_tup > 0\n         THEN ROUND(100.0 * n_dead_tup / (n_live_tup + n_dead_tup), 1)\n       END AS dead_pct\nFROM pg_stat_user_tables\nWHERE n_dead_tup > 0\nORDER BY n_dead_tup DESC;</code></pre>",
  ["dead-tuples", "bloat", "gotcha"])

c("Gotchas",
  "How should you handle SERIALIZABLE conflicts?",
  "Under <code>SERIALIZABLE</code> isolation, transactions can be aborted with error <code>40001: could not serialize access</code>. The application <b>must</b> implement a retry loop for the entire transaction.<br><pre><code>-- Application pseudocode:\ndef execute_serializable():\n    for attempt in range(MAX_RETRIES):\n        try:\n            cursor.execute(\"BEGIN ISOLATION LEVEL SERIALIZABLE\")\n            # ... business logic ...\n            cursor.execute(\"COMMIT\")\n            return\n        except SerializationFailure:\n            cursor.execute(\"ROLLBACK\")\n            time.sleep(random.uniform(0, 2 ** attempt))  # exponential backoff\n    raise Exception(\"Max retries exceeded\")\n\n-- PostgreSQL retries are expensive (re-execute all work).\n-- Consider READ COMMITTED with FOR UPDATE for high-contention scenarios.</code></pre>",
  ["serializable-conflicts", "retry", "gotcha"])

c("Gotchas",
  "What are connection pooling issues?",
  "Without a pooler, each application connection = one PostgreSQL process. Problems:<br>- <b>Too many connections</b>: memory pressure, context switching, throughput drops.<br>- <b>Connection churn</b>: opening/closing connections frequently wastes time on SSL and authentication.<br>- <b>SET statements leak</b>: temporary settings (search_path, role) may persist across pooled connections if not properly reset.<br>- <b>Prepared statements</b>: named prepared statements persist per session and may collide across pool connections.<br><b>Solution</b>: PgBouncer in <b>transaction mode</b> - releases connection to pool after transaction ends, handles most reset issues automatically.",
  ["connection-pooling", "pgbouncer", "gotcha"])

c("Gotchas",
  "What are common deployment migration gotchas?",
  "<b>Adding a NOT NULL column with no default</b>: blocks the entire table (ACCESS EXCLUSIVE lock) while scanning to verify no NULLs exist.<br><pre><code>-- Bad (locks table for duration of scan):\nALTER TABLE users ADD COLUMN bio TEXT NOT NULL;\n\n-- Good (PG 11+): add with default first, then set NOT NULL:\nALTER TABLE users ADD COLUMN bio TEXT DEFAULT '';\nALTER TABLE users ALTER COLUMN bio SET NOT NULL;\n\n-- Renaming a column used by application code - breaks queries.\n-- Always deploy schema changes first, then code referencing new schema.\n-- Dropping a column without checking dependencies.\n-- Changing column type requires a full table rewrite (unless compatible).\n-- Index CONCURRENTLY in migration fails silently in transaction blocks;\n  must be run separately.</code></pre>",
  ["migrations", "deployment", "gotcha"])

c("Gotchas",
  "What is index bloat?",
  "Indexes bloat just like tables - dead tuples leave entries in index pages. <code>REINDEX</code> rebuilds from scratch. Identify bloated indexes with <code>pgstattuple</code>:<br><pre><code>CREATE EXTENSION pgstattuple;\n\nSELECT indexrelname, avg_leaf_density, leaf_fragmentation\nFROM PGSTATINDEX('idx_orders_user_id');\n-- avg_leaf_density: lower = more bloat (target > 50%)\n-- leaf_fragmentation: higher = more fragmentation\n\n-- Approximate bloat from pg_stat_user_indexes:\nSELECT indexrelname, idx_scan, idx_tup_read, idx_tup_fetch\nFROM pg_stat_user_indexes\nWHERE idx_tup_read / NULLIF(idx_scan, 0) > 10;  -- suspicious ratio\n\n-- B-tree page-split-heavy workloads cause index bloat.\n-- Monitor and REINDEX periodically or use pg_repack.</code></pre>",
  ["index-bloat", "reindex", "gotcha"])
# =============================================
# 09 - EXPERT
# =============================================

c("Expert",
  "PostgreSQL vs MySQL - when to choose which (detailed)?",
  "<b>Choose PostgreSQL when</b>:<br>- You need advanced SQL features (CTEs, window functions, LATERAL).<br>- Data integrity is critical (stricter defaults, no silent truncation).<br>- You need GIS (PostGIS is best-in-class).<br>- You need extensibility (custom types, languages, extensions).<br>- JSONB with indexing matters.<br>- You want a liberal open-source license (no GPL risk).<br><br><b>Choose MySQL when</b>:<br>- You're on managed cloud with MySQL-specific ecosystem (PlanetScale, TiDB).<br>- You need multi-source replication (MySQL supports it natively).<br>- Your app framework strongly prefers MySQL (WordPress, Magento).<br>- You value simpler administration (MySQL has fewer tuning knobs).<br>- Read-heavy workloads with simple queries (MySQL can be faster on reads with the right config).<br><br>Both are excellent; PostgreSQL is generally the better default for new projects.",
  ["postgresql-vs-mysql", "comparison", "expert"])

c("Expert",
  "ORM vs raw SQL - what are the tradeoffs?",
  "<b>ORM benefits</b>:<br>- Productivity: auto-mapping, migration tooling, type safety.<br>- Portability: database-agnostic queries (rarely works perfectly).<br>- Security: parameterized queries by default (SQL injection protection).<br><br><b>ORM drawbacks</b>:<br>- N+1 problems (eager loading must be explicit).<br>- Generates inefficient queries for complex logic.<br>- Abstracts away database features (you miss CTEs, LATERAL, DISTINCT ON).<br>- Schema drift: ORM's model != actual database state.<br><br><b>Best approach</b>: ORM for simple CRUD, raw SQL or query builder for complex queries. Use ORM migration management but write complex reporting/analytics in SQL. Consider SQL-first tools like <b>sqlc</b> (Go), <b>Slonik</b> or <b>Kysely</b> (TypeScript), or <b>Diesel</b> (Rust) that type-check SQL at compile time.",
  ["orm-vs-raw-sql", "best-practices", "expert"])

c("Expert",
  "What is PgBouncer and how does it work?",
  "PgBouncer is a lightweight connection pooler for PostgreSQL. It maintains a small pool of persistent PostgreSQL connections and multiplexes many client connections onto them. Three pooling modes:<br><b>Session pooling</b>: one client -> one server connection for duration of session (like direct PG).<br><b>Transaction pooling</b> (recommended): client gets a server connection only for duration of a transaction, then released. Much higher concurrency (1000s of clients on ~50 DB connections).<br><b>Statement pooling</b>: per-statement, even more aggressive (breaks multi-statement transactions).<br><pre><code># pgbouncer.ini\n[databases]\n* = host=localhost port=5432\n\n[pgbouncer]\nlisten_addr = 0.0.0.0\nlisten_port = 6432\nauth_type = scram-sha-256\nauth_file = /etc/pgbouncer/userlist.txt\npool_mode = transaction\nmax_client_conn = 1000\ndefault_pool_size = 25</code></pre>",
  ["pgbouncer", "connection-pooling", "expert"])

c("Expert",
  "What is Pgpool-II and how does it compare to PgBouncer?",
  "<b>Pgpool-II</b> does connection pooling PLUS more: load balancing across replicas, automatic failover, read-write splitting, parallel query (limited), and online recovery. It's more feature-rich but heavier and more complex.<br><b>PgBouncer</b> does ONE thing (connection pooling) and does it extremely well - low overhead, simple config, battle-tested at scale.<br><b>Recommendation</b>: PgBouncer for connection pooling. If you need load balancing + HA, use PgBouncer + HAProxy (or managed cloud provider's solution) instead of Pgpool-II, unless you specifically need Pgpool's integrated approach.",
  ["pgpool", "pgbouncer", "comparison", "expert"])

c("Expert",
  "RDS vs self-hosted PostgreSQL - what to consider?",
  "<b>RDS (managed) benefits</b>:<br>- Automatic backups, PITR, multi-AZ failover.<br>- Patching, minor version upgrades with a click.<br>- Monitoring (CloudWatch, Performance Insights).<br>- Encryption at rest (KMS) and in transit (TLS).<br>- No need to manage servers/patching/backups.<br><br><b>Self-hosted benefits</b>:<br>- Full control over configuration, extensions, C collation.<br>- No vendor lock-in.<br>- Lower cost at large scale (reserved instances in cloud add up).<br>- Can use bleeding-edge PostgreSQL versions.<br>- Access to filesystem (custom extensions, pg_dump directly).<br>- No RDS limitations (e.g., no SUPERUSER, limited extension whitelist, max 64 TB).",
  ["rds", "self-hosted", "managed", "expert"])

c("Expert",
  "JSONB vs normalized tables - when to use which?",
  "<b>Use normalized tables when</b>:<br>- Data has a stable, known schema.<br>- You need referential integrity (FKs).<br>- You query by individual fields frequently (index individual columns).<br>- You need UPDATEs to individual fields.<br>- Data volumes are large and you want storage efficiency.<br><br><b>Use JSONB when</b>:<br>- Schema is unpredictable or varies per row (event payloads, user preferences, API responses).<br>- Data is always read/written as a whole document.<br>- You need flexibility for rapid iteration without migrations.<br>- Nesting is deep and complex (JSONB @> is concise).<br><br><b>Hybrid approach</b>: normalized columns for frequently-queried fields + JSONB for the rest.<br><pre><code>CREATE TABLE events (\n  id SERIAL PRIMARY KEY,\n  type TEXT NOT NULL,              -- indexed, queried\n  user_id INT NOT NULL,            -- FK, indexed\n  occurred_at TIMESTAMPTZ DEFAULT NOW(),\n  payload JSONB NOT NULL           -- flexible payload\n);\nCREATE INDEX ON events (type, occurred_at);\nCREATE INDEX ON events USING GIN (payload);</code></pre>",
  ["jsonb-vs-normalized", "database-design", "expert"])

c("Expert",
  "UUID vs serial/bigserial for primary keys - tradeoffs?",
  "<b>UUID advantages</b>:<br>- Globally unique - no collision when merging databases or sharding.<br>- Client-side generation - no roundtrip needed to get the ID.<br>- Doesn't leak sequence information (e.g., user count).<br><br><b>UUID disadvantages</b>:<br>- 16 bytes vs 4/8 bytes - larger indexes, more WAL, slower joins.<br>- Random UUIDs (v4) fragment B-tree indexes (pages split randomly).<br>- Harder to read/debug/log (long hex strings).<br><br><b>Best practice</b>: Use <b>UUID v7</b> (time-ordered) for best of both worlds - it's sortable (good for B-trees) and globally unique. Requires extension (<code>uuid-ossp</code> doesn't do v7; use <code>pg_uuidv7</code> or generate in app).<br>Otherwise: <b>BIGSERIAL</b> for internal/OLTP, <b>UUID</b> for distributed/external-facing IDs.",
  ["uuid-vs-serial", "primary-key", "expert"])

c("Expert",
  "How do you approach partitioning large tables in practice?",
  "Partitioning is a <b>management</b> tool first, performance second. Key considerations:<br>1. <b>Choose the partition key</b>: date (RANGE) for time-series, tenant_id (HASH/LIST) for multi-tenant.<br>2. <b>Keep partitions manageable</b>: aim for ~100s of partitions, not 100,000s.<br>3. <b>Use pg_partman</b> for automated creation/detachment.<br>4. <b>Ensure partition pruning</b>: always include the partition key in queries.<br>5. <b>Index each partition separately</b> - indexes on parent are not inherited.<br>6. <b>Detach/drop old partitions</b> instead of DELETE (instant vs very slow).<br>7. <b>Default partition</b> catches misrouted rows - monitor it for unexpected data.<br><pre><code>-- Detach and drop a partition (fast!):\nALTER TABLE orders DETACH PARTITION orders_2023q1;\nDROP TABLE orders_2023q1;\n\n-- Add a new partition:\nCREATE TABLE orders_2024q4 PARTITION OF orders\n  FOR VALUES FROM ('2024-10-01') TO ('2025-01-01');</code></pre>",
  ["partitioning", "large-tables", "expert"])

c("Expert",
  "What is the PostgreSQL extension ecosystem?",
  "<b>Geospatial</b>:<br><code>PostGIS</code> - GIS/spatial data, geometry types, spatial indexes (GiST), raster support. Gold standard for geospatial databases.<br><br><b>Vector / AI</b>:<br><code>pgvector</code> - vector embeddings storage with similarity search (cosine, L2, inner product). Supports HNSW and IVFFlat indexes. Essential for RAG/LLM embeddings.<br><br><b>Time-series</b>:<br><code>TimescaleDB</code> - automatic partitioning (hypertables), compression, continuous aggregates, data retention policies. Turns PG into a time-series powerhouse.<br><br><b>Distributed</b>:<br><code>Citus</code> - shards PostgreSQL across multiple nodes (distributed tables, reference tables). Horizontal scaling for multi-tenant and real-time analytics.<br><br><b>Maintenance</b>:<br><code>pg_cron</code> - scheduled jobs inside PG.<br><code>pg_partman</code> - automated partition management.<br><code>pg_repack</code> - online table/index reorganization (VACUUM FULL without blocking).<br><code>pgAudit</code> - detailed session/object audit logging.<br><code>pg_stat_statements</code> - query performance tracking (built-in but needs enabling).",
  ["extensions", "postgis", "pgvector", "timescaledb", "citus", "expert"])

c("Expert",
  "What is PostGIS and why is it important?",
  "PostGIS is the <b>definitive</b> spatial database extension. It adds: geometry/geography types, 1000+ spatial functions (ST_Distance, ST_Intersects, ST_Within, ST_Buffer, ST_Union), spatial indexes (GiST), raster support, topology support, and format conversion (GeoJSON, KML, WKT/WKB).<br><pre><code>CREATE EXTENSION postgis;\n\nCREATE TABLE landmarks (\n  id SERIAL PRIMARY KEY,\n  name TEXT,\n  location GEOMETRY(Point, 4326)  -- SRID 4326 = WGS84 lat/lon\n);\n\nINSERT INTO landmarks (name, location)\nVALUES ('Eiffel Tower', ST_SetSRID(ST_MakePoint(2.2945, 48.8584), 4326));\n\n-- Find landmarks within 5km of a point:\nSELECT name\nFROM landmarks\nWHERE ST_DWithin(\n  location,\n  ST_SetSRID(ST_MakePoint(2.3522, 48.8566), 4326),\n  5000  -- meters\n);</code></pre>",
  ["postgis", "gis", "extensions", "expert"])

c("Expert",
  "What is pgvector and how do you use it?",
  "<code>pgvector</code> adds a <code>VECTOR</code> data type for storing embeddings with similarity search. Index types: IVFFlat (requires training, good recall) and HNSW (faster builds, memory-heavy).<br><pre><code>CREATE EXTENSION vector;\n\nCREATE TABLE documents (\n  id SERIAL PRIMARY KEY,\n  content TEXT,\n  embedding VECTOR(1536)  -- OpenAI ada-002 dimension\n);\n\n-- Cosine similarity search:\nSELECT id, content, 1 - (embedding <=> query_embedding) AS similarity\nFROM documents\nORDER BY embedding <=> query_embedding\nLIMIT 10;\n\n-- Create HNSW index:\nCREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);\n\n-- L2 distance:\nSELECT * FROM documents\nORDER BY embedding <-> query_embedding LIMIT 10;\n\n-- Operators: <-> (L2), <#> (inner product), <=> (cosine distance)</code></pre>",
  ["pgvector", "embeddings", "ai", "expert"])

c("Expert",
  "What is TimescaleDB?",
  "TimescaleDB packages PostgreSQL for time-series data. Key features:<br><b>Hypertables</b> - automatically partitioned by time (auto-creates chunks).<br><b>Compression</b> - columnar compression on old chunks (90%+ space savings).<br><b>Continuous aggregates</b> - automatically refreshing materialized views with time bucketing.<br><b>Data retention</b> - automatic dropping of old chunks.<br><b>Time-series functions</b>: <code>TIME_BUCKET()</code>, <code>FIRST()</code>, <code>LAST()</code>, <code>HISTOGRAM()</code>.<br><pre><code>CREATE EXTENSION timescaledb;\n\nCREATE TABLE sensor_data (\n  time TIMESTAMPTZ NOT NULL,\n  device_id INT,\n  temperature DOUBLE PRECISION\n);\n\nSELECT CREATE_HYPERTABLE('sensor_data', 'time');\n\n-- Add compression and retention:\nALTER TABLE sensor_data SET (\n  timescaledb.compress,\n  timescaledb.compress_segmentby = 'device_id',\n  timescaledb.compress_orderby = 'time DESC'\n);\nSELECT ADD_COMPRESSION_POLICY('sensor_data', INTERVAL '7 days');\nSELECT ADD_RETENTION_POLICY('sensor_data', INTERVAL '2 years');</code></pre>",
  ["timescaledb", "time-series", "extensions", "expert"])

c("Expert",
  "What is Citus and when do you use it?",
  "Citus transforms PostgreSQL into a <b>distributed database</b> by sharding tables across a cluster of PostgreSQL nodes. Each node is a standard PostgreSQL instance. It supports distributed SQL with automatic query routing and parallel execution across shards.<br><b>Good for</b>: multi-tenant SaaS apps (shard by tenant_id), real-time analytics on large datasets, high-throughput transactional workloads.<br><b>Not good for</b>: workloads with heavy cross-shard JOINs (expensive data shuffling).<br><pre><code>-- Coordinator node:\nSELECT MASTER_ADD_NODE('worker1', 5432);\nSELECT MASTER_ADD_NODE('worker2', 5432);\n\nCREATE TABLE events (\n  tenant_id INT NOT NULL,\n  id SERIAL,\n  data JSONB\n) PARTITION BY HASH (tenant_id);\n\nSELECT CREATE_DISTRIBUTED_TABLE('events', 'tenant_id');\n-- Now INSERT/UPDATE/SELECT are transparently routed to shards.</code></pre>",
  ["citus", "distributed", "sharding", "expert"])

c("Expert",
  "What is logical replication and when should you use it?",
  "Logical replication streams <b>logical changes</b> (INSERT, UPDATE, DELETE) at table level, allowing replication between different PostgreSQL major versions, selective table replication, and data transformations. Unlike streaming (physical) replication, which copies block-by-block identical data.<br><b>Use cases</b>:<br>- Zero-downtime major version upgrades.<br>- Replicate only specific tables to a reporting server.<br>- Consolidate data from multiple databases into one analytics DB.<br>- Feed changes to external systems via CDC (Change Data Capture).<br><pre><code>-- Publisher:\nCREATE PUBLICATION my_pub FOR TABLE users, orders;\nALTER PUBLICATION my_pub ADD TABLE products;\n\n-- Subscriber:\nCREATE SUBSCRIPTION my_sub\n  CONNECTION 'host=publisher dbname=mydb'\n  PUBLICATION my_pub;\n\n-- Monitor:\nSELECT * FROM PG_STAT_SUBSCRIPTION;\nSELECT * FROM PG_STAT_REPLICATION;</code></pre>",
  ["logical-replication", "replication", "expert"])

c("Expert",
  "What are FDWs (Foreign Data Wrappers)?",
  "FDWs let PostgreSQL query <b>external data sources</b> as if they were local tables, using SQL/MED (Management of External Data) standard. Each FDW implements a handler that translates PostgreSQL's query plan into the external data source's API.<br><pre><code>-- postgres_fdw: query another PostgreSQL database:\nCREATE EXTENSION postgres_fdw;\nCREATE SERVER remote_server\n  FOREIGN DATA WRAPPER postgres_fdw\n  OPTIONS (host '10.0.0.5', dbname 'analytics');\nCREATE USER MAPPING FOR CURRENT_USER\n  SERVER remote_server\n  OPTIONS (user 'reader', password 'secret');\n\nCREATE FOREIGN TABLE remote_orders (\n  id INT, total NUMERIC, created_at DATE\n) SERVER remote_server\n  OPTIONS (schema_name 'public', table_name 'orders');\n\nSELECT * FROM remote_orders WHERE total > 100;\n-- Note: WHERE clause is pushed to remote server if possible.\n\n-- Other FDWs: file_fdw (CSV), ogr_fdw (GIS), tds_fdw (SQL Server),\n-- mysql_fdw, redis_fdw, mongodb_fdw, s3_fdw</code></pre>",
  ["fdw", "foreign-data-wrapper", "postgres-fdw", "expert"])

c("Expert",
  "What is logical decoding and CDC?",
  "<b>Logical decoding</b> extracts changes from the WAL in a higher-level format (INSERT/UPDATE/DELETE with row data). It's the foundation for logical replication, CDC (Change Data Capture) tools (Debezium, Kafka Connect), and audit logging.<br><pre><code>-- Test with pgoutput plugin:\nCREATE PUBLICATION my_pub FOR TABLE users;\n\n-- External tools connect as a replication client:\n-- psql \"dbname=mydb replication=database\" -c\n--   \"CREATE_REPLICATION_SLOT my_slot LOGICAL pgoutput;\"\n\n-- Key WAL settings:\n-- wal_level = logical\n-- max_replication_slots = 10\n-- max_wal_senders = 10\n\n-- Common CDC pipeline:\n-- PostgreSQL -> pgoutput -> Debezium -> Kafka -> consumers\n-- Enables real-time downstream processing without polling.</code></pre>",
  ["logical-decoding", "cdc", "replication", "expert"])

c("Expert",
  "What is TABLESAMPLE?",
  "<code>TABLESAMPLE</code> fetches a <b>random sample</b> of rows from a table without reading every row. Much faster than <code>ORDER BY RANDOM() LIMIT n</code> for approximate analytics.<br><pre><code>-- Bernoulli: scans all pages, selects each row with probability (truly random):\nSELECT * FROM orders TABLESAMPLE BERNOULLI (1);  -- ~1% of rows\n\n-- System: selects random pages (fast, block-level):\nSELECT * FROM orders TABLESAMPLE SYSTEM (1);     -- ~1% of pages\n\n-- With REPEATABLE for reproducible samples:\nSELECT AVG(total) FROM orders TABLESAMPLE SYSTEM (5) REPEATABLE (42);\n\n-- Custom sampling methods:\nCREATE EXTENSION tsm_system_rows;\nSELECT * FROM orders TABLESAMPLE SYSTEM_ROWS (1000);  -- exactly ~1000 rows</code></pre>",
  ["tablesample", "sampling", "analytics", "expert"])

c("Expert",
  "How do you write a custom aggregate?",
  "A custom aggregate combines a <b>state transition function</b> (sfunc), optional <b>final function</b> (ffunc), and an initial state value.<br><pre><code>-- Simple aggregate: sum of squares\nCREATE OR REPLACE FUNCTION sum_squares_accum(state NUMERIC, val NUMERIC)\nRETURNS NUMERIC AS $$\nBEGIN\n  RETURN state + (val * val);\nEND;\n$$ LANGUAGE plpgsql IMMUTABLE;\n\nCREATE AGGREGATE SUM_SQUARES (NUMERIC) (\n  SFUNC = sum_squares_accum,\n  STYPE = NUMERIC,\n  INITCOND = '0'\n);\n\nSELECT SUM_SQUARES(value) FROM numbers;\n-- Returns sum of squares of all values.</code></pre>",
  ["custom-aggregate", "plpgsql", "expert"])

c("Expert",
  "What is parallel query execution in PostgreSQL?",
  "Starting in PG 9.6 (improved through PG 16+), PostgreSQL can execute parts of a query in <b>parallel</b> using multiple worker processes. Enabled by default with <code>max_parallel_workers_per_gather = 2</code>. Works for sequential scans, hash joins, aggregation, and B-tree creation.<br><pre><code>-- Check parallel settings:\nSELECT name, setting FROM pg_settings\nWHERE name LIKE '%parallel%';\n\n-- max_parallel_workers_per_gather (default 2)\n-- max_parallel_workers (default 8)\n-- parallel_tuple_cost, parallel_setup_cost\n-- min_parallel_table_scan_size, min_parallel_index_scan_size\n\n-- Force parallel:\nSET parallel_setup_cost = 0;\nSET parallel_tuple_cost = 0;\nEXPLAIN ANALYZE SELECT ...;\n\n-- Check if parallel was used:\nEXPLAIN (ANALYZE, VERBOSE)\nSELECT COUNT(*) FROM large_table;\n-- Look for: -> Parallel Seq Scan, -> Gather</code></pre>",
  ["parallel-query", "performance", "expert"])

c("Expert",
  "What is JIT compilation in PostgreSQL?",
  "PostgreSQL can use LLVM to <b>Just-In-Time compile</b> parts of queries (expressions, tuple deforming) into native machine code, improving performance for compute-heavy queries (complex WHERE clauses, aggregate expressions). Enabled in PG 11+ with <code>jit = on</code> (needs LLVM compiled in).<br><pre><code>-- Settings (postgresql.conf):\njit = on\njit_above_cost = 100000     -- only JIT if query cost > this\njit_inline_above_cost = 500000\njit_optimize_above_cost = 500000\n\n-- Verify JIT was used:\nEXPLAIN (ANALYZE)\nSELECT SUM(expensive_expression)\nFROM large_table;\n-- Look for: JIT: Functions: N</code></pre>",
  ["jit", "compilation", "performance", "expert"])

c("Expert",
  "What is custom extension development in PostgreSQL?",
  "Extensions can be written in C, SQL, PL/pgSQL, or other languages. They consist of a control file (<code>.control</code>), SQL installation script, and optionally C code compiled into a shared library (<code>.so</code>).<br><pre><code>-- Control file: myext.control\n# comment = 'My custom extension'\n# default_version = '1.0'\n# relocatable = true\n# module_pathname = '$libdir/myext'\n\n-- SQL file: myext--1.0.sql\nCREATE OR REPLACE FUNCTION hello(name TEXT)\nRETURNS TEXT AS $$\nBEGIN\n  RETURN 'Hello, ' || name || '!';\nEND;\n$$ LANGUAGE plpgsql;\n\n-- Install:\n-- Copy files to SHAREDIR/extension/\n-- Then: CREATE EXTENSION myext;</code></pre>",
  ["extension-development", "custom-extension", "expert"])

c("Expert",
  "What is pg_repack and when do you use it?",
  "<code>pg_repack</code> reorganizes tables and indexes <b>online</b> (without blocking reads/writes) - similar to VACUUM FULL but without the exclusive lock. It works by creating a new copy of the table, replicating changes via triggers, then swapping them.<br><pre><code># Reorganize a table online:\npg_repack -t orders -d mydb\n\n# Reorganize specific indexes:\npg_repack -i idx_orders_user_id -d mydb\n\n# Reorganize all tables in a database:\npg_repack -d mydb\n\n# Use when:\n# - VACUUM FULL would block production\n# - Tables show high bloat (pgstattuple)\n# - Indexes need rebuilding without downtime</code></pre>",
  ["pg-repack", "maintenance", "online-reorg", "expert"])

c("Expert",
  "How does streaming replication work in PostgreSQL?",
  "Streaming replication creates a read-only standby by continuously streaming WAL from primary. Types: <b>asynchronous</b> (default, risk of data loss on primary crash) and <b>synchronous</b> (<code>synchronous_commit = remote_apply</code>, zero data loss, wait for standby ack).<br><pre><code>-- Primary postgresql.conf:\nwal_level = replica\nmax_wal_senders = 5\nwal_keep_size = '1GB'\n\n-- Standby: restore from base backup, then create\n-- standby.signal file (PG 12+):\ntouch $PGDATA/standby.signal\n\n-- Standby postgresql.conf:\nprimary_conninfo = 'host=primary port=5432 user=replicator'\nprimary_slot_name = 'standby1'  -- optional, prevents WAL removal\nhot_standby = on  -- allow read-only queries on standby\n\n-- Check replication lag:\nSELECT client_addr, state, sync_state,\n       PG_WAL_LSN_DIFF(pg_current_wal_lsn(), sent_lsn) AS sent_lag,\n       PG_WAL_LSN_DIFF(pg_current_wal_lsn(), flush_lsn) AS flush_lag\nFROM pg_stat_replication;</code></pre>",
  ["streaming-replication", "high-availability", "expert"])
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
