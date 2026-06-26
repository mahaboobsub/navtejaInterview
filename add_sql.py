import json
import os

def load_db():
    if os.path.exists('modules.json'):
        with open('modules.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(db):
    with open('modules.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def main():
    db = load_db()
    
    sql_module = {
        "id": 1,
        "name": "SQL",
        "short": "SQL",
        "color": "c-teal",
        "count": 55,
        "subs": [
            {
                "head": "DDL / DML / Basics",
                "qs": [
                    {
                        "q": "What is the difference between DDL, DML, DCL, and TCL? Give examples of each.",
                        "a": "<h4>SQL Sublanguages</h4>"
                            "<ul>"
                            "<li><strong>DDL (Data Definition Language):</strong> Defines/modifies database structures. Examples: <code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code>.</li>"
                            "<li><strong>DML (Data Manipulation Language):</strong> Manages data within objects. Examples: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>.</li>"
                            "<li><strong>DCL (Data Control Language):</strong> Controls privileges and permissions. Examples: <code>GRANT</code>, <code>REVOKE</code>.</li>"
                            "<li><strong>TCL (Transaction Control Language):</strong> Manages transactions. Examples: <code>COMMIT</code>, <code>ROLLBACK</code>, <code>SAVEPOINT</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between DELETE, TRUNCATE, and DROP?",
                        "a": "<h4>DELETE vs. TRUNCATE vs. DROP</h4>"
                            "<table>"
                            "<tr><th>Feature</th><th>DELETE</th><th>TRUNCATE</th><th>DROP</th></tr>"
                            "<tr><td><strong>Type</strong></td><td>DML</td><td>DDL</td><td>DDL</td></tr>"
                            "<tr><td><strong>Action</strong></td><td>Removes specified rows (where clause allowed)</td><td>Removes all rows from table</td><td>Deletes table structure and all data</td></tr>"
                            "<tr><td><strong>Rollback</strong></td><td>Yes (writes to log)</td><td>No (depends on DB engines, usually auto-commits)</td><td>No</td></tr>"
                            "<tr><td><strong>Speed</strong></td><td>Slower</td><td>Fast</td><td>Fastest</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is a PRIMARY KEY vs a UNIQUE constraint?",
                        "a": "<h4>PRIMARY KEY vs. UNIQUE</h4>"
                            "<ul>"
                            "<li><strong>PRIMARY KEY:</strong> Uniquely identifies each row. Does not allow <code>NULL</code> values. Only one per table. Automatically creates a clustered index.</li>"
                            "<li><strong>UNIQUE constraint:</strong> Ensures all values in a column are unique. Allows <code>NULL</code> values (usually one null depending on database system). Multiple UNIQUE constraints allowed per table.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a FOREIGN KEY? What does ON DELETE CASCADE do?",
                        "a": "<h4>Foreign Keys & Cascade</h4>"
                            "<ul>"
                            "<li><strong>FOREIGN KEY:</strong> A column or group of columns that establishes a link between data in two tables (enforcing referential integrity).</li>"
                            "<li><strong>ON DELETE CASCADE:</strong> If a row in the parent table is deleted, all matching rows in the child table containing that foreign key are automatically deleted.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a composite key?",
                        "a": "<h4>Composite Key</h4>"
                            "A primary key composed of two or more columns to uniquely identify a row in a table. Used when a single column is insufficient to guarantee uniqueness."
                    },
                    {
                        "q": "What is the difference between CHAR and VARCHAR?",
                        "a": "<h4>CHAR vs. VARCHAR</h4>"
                            "<ul>"
                            "<li><strong>CHAR:</strong> Fixed-length character data type. Pads spaces to fill maximum length if input is shorter. Fast access.</li>"
                            "<li><strong>VARCHAR:</strong> Variable-length character data type. Stores only characters entered plus a length byte. More storage-efficient.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between DATETIME and TIMESTAMP?",
                        "a": "<h4>DATETIME vs. TIMESTAMP</h4>"
                            "<ul>"
                            "<li><strong>DATETIME:</strong> Stores date and time independently of timezone (ranges 1000 to 9999).</li>"
                            "<li><strong>TIMESTAMP:</strong> Stores date and time converted to UTC time. Auto-converts to client timezone when fetched (ranges 1970 to 2038).</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "JOINs",
                "qs": [
                    {
                        "q": "What are the different types of JOINs? Explain each with an example.",
                        "a": "<h4>SQL JOIN Types</h4>"
                            "<ul>"
                            "<li><strong>INNER JOIN:</strong> Returns rows that have matching values in both tables.</li>"
                            "<li><strong>LEFT JOIN:</strong> Returns all rows from left table, plus matched rows from right (fills NULLs if no match).</li>"
                            "<li><strong>RIGHT JOIN:</strong> Returns all rows from right table, plus matched rows from left.</li>"
                            "<li><strong>FULL JOIN:</strong> Returns rows when there is a match in either table.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between INNER JOIN and OUTER JOIN?",
                        "a": "<h4>INNER vs. OUTER JOIN</h4>"
                            "<ul>"
                            "<li><strong>INNER JOIN:</strong> Drops rows that do not have matching partners in both tables.</li>"
                            "<li><strong>OUTER JOIN (Left/Right/Full):</strong> Retains non-matching rows and pads missing columns with <code>NULL</code> values.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a SELF JOIN? When is it useful?",
                        "a": "<h4>Self Joins</h4>"
                            "A join where a table is joined with itself. Requires assigning alias names (e.g. <code>T1</code>, <code>T2</code>).<br/>"
                            "<em>Use case:</em> Querying organizational hierarchy (finding Employee and their matching Manager inside the same <code>Employee</code> table)."
                    },
                    {
                        "q": "What is the difference between CROSS JOIN and FULL OUTER JOIN?",
                        "a": "<h4>CROSS vs. FULL JOIN</h4>"
                            "<ul>"
                            "<li><strong>CROSS JOIN:</strong> Returns the Cartesian product (every row of table A matched with every row of table B). No <code>ON</code> clause.</li>"
                            "<li><strong>FULL OUTER JOIN:</strong> Matches tables based on join condition, keeping unmatched rows from both tables.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a NATURAL JOIN? What are its risks?",
                        "a": "<h4>Natural Join</h4>"
                            "Joins tables automatically based on columns that have the exact same name and data type in both tables.<br/>"
                            "<strong>Risks:</strong> Very dangerous. If a new column with same name is added to either table, query logic silently changes and breaks without warning."
                    },
                    {
                        "q": "Write a query to find employees who earn more than their manager.",
                        "a": "<h4>Employee-Manager Salary Comparison</h4>"
                            "<pre>SELECT e.name AS Employee\nFROM Employee e\n"
                            "JOIN Employee m ON e.manager_id = m.id\n"
                            "WHERE e.salary > m.salary;</pre>"
                    }
                ]
            },
            {
                "head": "Filtering & Aggregation",
                "qs": [
                    {
                        "q": "What is the difference between WHERE and HAVING?",
                        "a": "<h4>WHERE vs. HAVING</h4>"
                            "<ul>"
                            "<li><strong>WHERE:</strong> Filters rows BEFORE grouping is performed. Cannot evaluate aggregate functions.</li>"
                            "<li><strong>HAVING:</strong> Filters group results AFTER GROUP BY. Can evaluate aggregates like <code>SUM()</code> or <code>COUNT()</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between GROUP BY and ORDER BY?",
                        "a": "<h4>Grouping vs. Sorting</h4>"
                            "<ul>"
                            "<li><strong>GROUP BY:</strong> Collapses rows sharing same values into aggregate summary rows.</li>"
                            "<li><strong>ORDER BY:</strong> Sorts the final output records (ascending or descending).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are aggregate functions? Name all of them.",
                        "a": "<h4>Aggregate Functions</h4>"
                            "Functions that compute a single summary value from a set of input column values.<br/>"
                            "<em>Common list:</em> <code>SUM()</code>, <code>AVG()</code>, <code>COUNT()</code>, <code>MIN()</code>, <code>MAX()</code>."
                    },
                    {
                        "q": "What is the difference between COUNT(*) and COUNT(column_name)?",
                        "a": "<h4>COUNT Comparisons</h4>"
                            "<ul>"
                            "<li><strong><code>COUNT(*)</code>:</strong> Counts all rows in the group, including duplicate values and NULL rows.</li>"
                            "<li><strong><code>COUNT(column_name)</code>:</strong> Counts only non-NULL entries in that column.</li>"
                            "</ul>"
                    },
                    {
                        "q": "How does SQL handle NULL in aggregate functions?",
                        "a": "<h4>NULL in Aggregates</h4>"
                            "All aggregate functions (except <code>COUNT(*)</code>) silently ignore <code>NULL</code> values during computation. If all values are NULL, the function returns NULL."
                    },
                    {
                        "q": "What is the difference between IS NULL and = NULL?",
                        "a": "<h4>= NULL vs. IS NULL</h4>"
                            "<ul>"
                            "<li><strong><code>IS NULL</code>:</strong> The correct syntax to check for empty values.</li>"
                            "<li><strong><code>= NULL</code>:</strong> Incorrect. NULL indicates unknown state, so comparing <code>value = NULL</code> evaluates to <code>UNKNOWN</code> (never returns true).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is COALESCE? Give a use case.",
                        "a": "<h4>COALESCE() Function</h4>"
                            "Returns the first non-null value in the argument list.<br/>"
                            "<pre>SELECT COALESCE(phone, email, 'No Contact') FROM users;</pre>"
                    },
                    {
                        "q": "What is the CASE statement in SQL? Give an example.",
                        "a": "<h4>SQL CASE Statement</h4>"
                            "Conditional statement to return specific values based on conditions.<br/>"
                            "<pre>SELECT name,\nCASE\n  WHEN score >= 90 THEN 'A'\n  ELSE 'B'\nEND AS Grade\nFROM students;</pre>"
                    },
                    {
                        "q": "What is the difference between EXISTS and IN? Which is faster?",
                        "a": "<h4>EXISTS vs. IN</h4>"
                            "<ul>"
                            "<li><strong>IN:</strong> Scans the entire subquery result list. Good for small subquery sets.</li>"
                            "<li><strong>EXISTS:</strong> Short-circuits (stops execution once first match is found). Faster for large tables and when using correlated subqueries.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between ANY and ALL operators?",
                        "a": "<h4>ANY vs. ALL</h4>"
                            "<ul>"
                            "<li><strong>ANY:</strong> Evaluates to TRUE if any value returned by the subquery meets the condition.</li>"
                            "<li><strong>ALL:</strong> Evaluates to TRUE only if all values returned by the subquery meet the condition.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Subqueries & CTEs",
                "qs": [
                    {
                        "q": "What is a subquery? What are the types of subqueries?",
                        "a": "<h4>Subqueries</h4>"
                            "A query nested inside another query (such as SELECT, INSERT, UPDATE, DELETE).<br/>"
                            "<h4>Types:</h4>"
                            "<ul>"
                            "<li><strong>Single-row:</strong> Returns one value. Used with <code>=</code>, <code>&gt;</code>.</li>"
                            "<li><strong>Multi-row:</strong> Returns list of values. Used with <code>IN</code>, <code>ANY</code>, <code>ALL</code>.</li>"
                            "<li><strong>Correlated:</strong> Subquery depends on the outer query row.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a correlated subquery? How is it different from a non-correlated subquery?",
                        "a": "<h4>Correlated vs. Non-Correlated</h4>"
                            "<ul>"
                            "<li><strong>Non-Correlated:</strong> Runs independently of outer query. Executed once.</li>"
                            "<li><strong>Correlated:</strong> References columns of the outer query. Runs repeatedly (once for each row processed by the outer query).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a CTE (Common Table Expression)? Write the syntax.",
                        "a": "<h4>CTEs</h4>"
                            "A temporary named result set available only during execution of a single query. Improves readability over subqueries.<br/>"
                            "<pre>WITH SalesCTE AS (\n  SELECT dept_id, SUM(amount) AS total\n  FROM sales GROUP BY dept_id\n)\n"
                            "SELECT * FROM SalesCTE WHERE total > 10000;</pre>"
                    },
                    {
                        "q": "What is a recursive CTE? Give an example (e.g., hierarchy tree).",
                        "a": "<h4>Recursive CTE</h4>"
                            "A CTE that references itself to query hierarchical data.<br/>"
                            "<pre>WITH RECURSIVE EmpHierarchy AS (\n"
                            "  SELECT id, name, manager_id FROM employees WHERE manager_id IS NULL\n"
                            "  UNION ALL\n"
                            "  SELECT e.id, e.name, e.manager_id \n"
                            "  FROM employees e JOIN EmpHierarchy h ON e.manager_id = h.id\n"
                            ") SELECT * FROM EmpHierarchy;</pre>"
                    },
                    {
                        "q": "What is the difference between UNION and UNION ALL?",
                        "a": "<h4>UNION vs. UNION ALL</h4>"
                            "<ul>"
                            "<li><strong>UNION:</strong> Merges results of two queries, removing duplicates. Slower due to duplicate sorting.</li>"
                            "<li><strong>UNION ALL:</strong> Merges results of two queries, retaining duplicate rows. Much faster.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is INTERSECT and EXCEPT (MINUS)?",
                        "a": "<h4>INTERSECT & EXCEPT</h4>"
                            "<ul>"
                            "<li><strong>INTERSECT:</strong> Returns only rows shared in common by both queries.</li>"
                            "<li><strong>EXCEPT (MINUS in Oracle):</strong> Returns rows from first query not present in second query.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Window Functions",
                "qs": [
                    {
                        "q": "What are window functions? How are they different from aggregate functions?",
                        "a": "<h4>Window Functions</h4>"
                            "Perform calculations across a set of table rows related to the current row without collapsing them into a single row.<br/>"
                            "<em>Syntax:</em> Uses the <code>OVER()</code> clause."
                    },
                    {
                        "q": "What is the difference between ROW_NUMBER(), RANK(), and DENSE_RANK()?",
                        "a": "<h4>Row Numbering & Ranking</h4>"
                            "For values [100, 100, 200, 300]:"
                            "<ul>"
                            "<li><strong>ROW_NUMBER():</strong> Assigns unique linear numbers: [1, 2, 3, 4].</li>"
                            "<li><strong>RANK():</strong> Assigns matching rank, skipping numbers: [1, 1, 3, 4].</li>"
                            "<li><strong>DENSE_RANK():</strong> Assigns matching rank, no gaps: [1, 1, 2, 3].</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is PARTITION BY in a window function?",
                        "a": "<h4>PARTITION BY</h4>"
                            "Divides rows into groups/partitions (e.g. by Department) to calculate window metrics independently within each group."
                    },
                    {
                        "q": "What is LEAD() and LAG()? Give a use case.",
                        "a": "<h4>LEAD & LAG</h4>"
                            "<ul>"
                            "<li><strong><code>LAG()</code>:</strong> Accesses data from a previous row at a specified offset.</li>"
                            "<li><strong><code>LEAD()</code>:</strong> Accesses data from a subsequent row at a specified offset.</li>"
                            "</ul>"
                            "<em>Use case:</em> Calculating year-over-year sales growth."
                    },
                    {
                        "q": "What is NTILE()?",
                        "a": "<h4>NTILE()</h4>"
                            "Divides ordered rows in a partition into a specified number of ranked groups (e.g. <code>NTILE(4)</code> creates quartiles)."
                    },
                    {
                        "q": "Write a query to find the top 3 salaries per department using window functions.",
                        "a": "<h4>Top Salaries per Department</h4>"
                            "<pre>SELECT dept_id, name, salary FROM (\n"
                            "  SELECT dept_id, name, salary,\n"
                            "  DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rk\n"
                            "  FROM employees\n) t WHERE rk <= 3;</pre>"
                    }
                ]
            },
            {
                "head": "Indexes & Performance",
                "qs": [
                    {
                        "q": "What is an index? How does it speed up queries?",
                        "a": "<h4>Database Indexes</h4>"
                            "A data structure (usually B-Tree) that stores pointers to data rows to quickly locate records without scanning the entire table (Full Table Scan)."
                    },
                    {
                        "q": "What is the difference between a clustered and a non-clustered index?",
                        "a": "<h4>Clustered vs. Non-Clustered</h4>"
                            "<ul>"
                            "<li><strong>Clustered:</strong> Sorts and stores physical data rows in index order. Only one per table (typically Primary Key).</li>"
                            "<li><strong>Non-Clustered:</strong> Separate structure containing index columns and row pointers. Multiple allowed.</li>"
                            "</ul>"
                    },
                    {
                        "q": "When should you NOT add an index?",
                        "a": "<h4>When to Avoid Indexes</h4>"
                            "<ul>"
                            "<li>On small tables (FTS is faster).</li>"
                            "<li>On tables with frequent writes/updates (updates are slowed down by index updates).</li>"
                            "<li>On columns with low selectivity (e.g. Gender flags).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is an execution plan and how do you read it?",
                        "a": "<h4>Execution Plans</h4>"
                            "The execution steps chosen by the query optimizer (using <code>EXPLAIN</code>). Look for indices used vs. scans (Index Scan vs Table Scan) to identify bottlenecks."
                    },
                    {
                        "q": "How do you optimize a slow-running SQL query?",
                        "a": "<h4>Optimization Checklist</h4>"
                            "1. Use <code>EXPLAIN</code> to analyze access path.<br/>"
                            "2. Add indices on WHERE, JOIN, and ORDER BY columns.<br/>"
                            "3. Avoid <code>SELECT *</code> (fetch only required columns).<br/>"
                            "4. Use JOINs instead of correlated subqueries.<br/>"
                            "5. Avoid wildcards at beginning of patterns (e.g. <code>LIKE '%term'</code>)."
                    },
                    {
                        "q": "What is a covering index?",
                        "a": "<h4>Covering Index</h4>"
                            "An index that contains all columns requested by the SELECT query. The database engine can satisfy the query entirely from the index without reading table blocks."
                    }
                ]
            },
            {
                "head": "Views & Stored Objects",
                "qs": [
                    {
                        "q": "What is a VIEW? What are its advantages?",
                        "a": "<h4>Views</h4>"
                            "A virtual table based on the result set of an SQL query.<br/>"
                            "<strong>Advantages:</strong> Simplifies complex queries, provides secure column access, maintains logical interface consistency."
                    },
                    {
                        "q": "What is the difference between a view and a materialized view?",
                        "a": "<h4>View vs. Materialized View</h4>"
                            "<ul>"
                            "<li><strong>Standard View:</strong> Virtual table, executes query dynamically every time it is referenced.</li>"
                            "<li><strong>Materialized View:</strong> Physical table, saves query output. Needs periodic refresh, very fast for heavy aggregates.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a stored procedure? Write a simple example.",
                        "a": "<h4>Stored Procedure</h4>"
                            "A group of SQL statements saved and executed on the database server side.<br/>"
                            "<pre>CREATE PROCEDURE GetDeptSalary(IN d_id INT, OUT total DECIMAL)\n"
                            "BEGIN\n"
                            "  SELECT SUM(salary) INTO total FROM employees WHERE dept_id = d_id;\n"
                            "END;</pre>"
                    },
                    {
                        "q": "What is the difference between a stored procedure and a function?",
                        "a": "<h4>Procedure vs. Function</h4>"
                            "<ul>"
                            "<li><strong>Function:</strong> Must return a single value. Can be called inline in SELECT (e.g. <code>SELECT func()</code>). Cannot perform DML updates.</li>"
                            "<li><strong>Stored Procedure:</strong> Does not require returning values. Cannot be called inside SELECT. Can run updates and transaction controls.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a TRIGGER? When would you use one?",
                        "a": "<h4>Triggers</h4>"
                            "An automated database action that fires when DML events (INSERT, UPDATE, DELETE) occur on a table.<br/>"
                            "<em>Use case:</em> Maintaining audit tables or enforcing data entry validations."
                    }
                ]
            },
            {
                "head": "Transactions & Locking",
                "qs": [
                    {
                        "q": "What are transactions? Explain the ACID properties.",
                        "a": "<h4>ACID Properties</h4>"
                            "<ul>"
                            "<li><strong>Atomicity:</strong> All statements in transaction succeed, or all fail together.</li>"
                            "<li><strong>Consistency:</strong> Database transitions only from one valid state to another.</li>"
                            "<li><strong>Isolation:</strong> Transactions execute independently without cross-leakage.</li>"
                            "<li><strong>Durability:</strong> Changes are permanently saved in database even during power outages.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between COMMIT and ROLLBACK?",
                        "a": "<h4>COMMIT vs. ROLLBACK</h4>"
                            "<ul>"
                            "<li><strong>COMMIT:</strong> Permanently saves transaction updates.</li>"
                            "<li><strong>ROLLBACK:</strong> Undoes all changes back to the start of the transaction.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a SAVEPOINT?",
                        "a": "<h4>SAVEPOINT</h4>"
                            "Creates checkpoint references inside a transaction to allow partial rollback of statements without canceling the entire transaction."
                    },
                    {
                        "q": "What are the SQL isolation levels? (Read Uncommitted, Read Committed, Repeatable Read, Serializable)",
                        "a": "<h4>Transaction Isolation Levels</h4>"
                            "<table>"
                            "<tr><th>Isolation Level</th><th>Dirty Read</th><th>Non-Repeatable Read</th><th>Phantom Read</th></tr>"
                            "<tr><td><strong>Read Uncommitted</strong></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>"
                            "<tr><td><strong>Read Committed</strong></td><td>No</td><td>Yes</td><td>Yes</td></tr>"
                            "<tr><td><strong>Repeatable Read</strong></td><td>No</td><td>No</td><td>Yes</td></tr>"
                            "<tr><td><strong>Serializable</strong></td><td>No</td><td>No</td><td>No</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is a dirty read, phantom read, and non-repeatable read?",
                        "a": "<h4>Concurrency Anomalies</h4>"
                            "<ul>"
                            "<li><strong>Dirty Read:</strong> Reading uncommitted changes from another transaction (which might get rolled back later).</li>"
                            "<li><strong>Non-Repeatable Read:</strong> Reading the same row twice yields different column values because another transaction updated it.</li>"
                            "<li><strong>Phantom Read:</strong> Re-executing a range query yields new insert rows matching criteria because another transaction added them.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between optimistic and pessimistic locking?",
                        "a": "<h4>Locking Strategies</h4>"
                            "<ul>"
                            "<li><strong>Optimistic:</strong> Assumes conflicts are rare. Uses version checks at update time. No database lock held during read.</li>"
                            "<li><strong>Pessimistic:</strong> Assumes conflicts are common. Locks the records immediately on read (e.g. <code>SELECT ... FOR UPDATE</code>).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a deadlock in SQL? How is it resolved?",
                        "a": "<h4>SQL Deadlocks</h4>"
                            "Two transactions wait for locks held by each other. The database engine automatically detects deadlocks, cancels one transaction (victim), and rolls it back."
                    }
                ]
            },
            {
                "head": "Normalization",
                "qs": [
                    {
                        "q": "What is normalization? Explain 1NF, 2NF, and 3NF with examples.",
                        "a": "<h4>Database Normalization</h4>"
                            "Structuring tables to minimize data redundancy and dependency issues.<br/>"
                            "<ul>"
                            "<li><strong>1NF (First Normal Form):</strong> Values in each cell must be atomic (no multi-valued lists).</li>"
                            "<li><strong>2NF (Second Normal Form):</strong> Must be in 1NF. All non-key attributes must be fully functionally dependent on the entire primary key (no partial dependencies).</li>"
                            "<li><strong>3NF (Third Normal Form):</strong> Must be in 2NF. No transitive dependencies (non-key columns cannot depend on other non-key columns).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is BCNF?",
                        "a": "<h4>BCNF (Boyce-Codd Normal Form)</h4>"
                            "A slightly stronger version of 3NF. Requires that for any functional dependency A -> B, the determinant A must be a super key."
                    },
                    {
                        "q": "What is denormalization? When is it appropriate?",
                        "a": "<h4>Denormalization</h4>"
                            "Purposely introducing redundancy (joining tables back) to speed up complex queries by reducing expensive JOIN operations. Appropriate in high-read Data Warehouses (OLAP)."
                    }
                ]
            },
            {
                "head": "Practical Queries",
                "qs": [
                    {
                        "q": "Write a query to find the second highest salary.",
                        "a": "<h4>Second Highest Salary</h4>"
                            "<pre>SELECT MAX(salary) FROM employees\n"
                            "WHERE salary < (SELECT MAX(salary) FROM employees);</pre>"
                    },
                    {
                        "q": "Write a query to find duplicate records in a table.",
                        "a": "<h4>Find Duplicates</h4>"
                            "<pre>SELECT email, COUNT(*)\nFROM users\n"
                            "GROUP BY email\nHAVING COUNT(*) > 1;</pre>"
                    },
                    {
                        "q": "Write a query to delete duplicate rows while keeping one.",
                        "a": "<h4>Delete Duplicates</h4>"
                            "<pre>DELETE u1 FROM users u1\n"
                            "JOIN users u2 ON u1.email = u2.email\n"
                            "WHERE u1.id > u2.id; -- deletes higher IDs, keeping lowest</pre>"
                    },
                    {
                        "q": "Write a query to find the nth highest salary.",
                        "a": "<h4>Nth Highest Salary</h4>"
                            "<pre>SELECT DISTINCT salary FROM employees e1\nWHERE (n - 1) = (\n"
                            "  SELECT COUNT(DISTINCT salary) FROM employees e2\n"
                            "  WHERE e2.salary > e1.salary\n);</pre>"
                    },
                    {
                        "q": "Write a query to pivot rows into columns.",
                        "a": "<h4>Pivot Query</h4>"
                            "<pre>SELECT year,\n"
                            "  SUM(CASE WHEN month = 'Jan' THEN sales ELSE 0 END) as Jan_Sales,\n"
                            "  SUM(CASE WHEN month = 'Feb' THEN sales ELSE 0 END) as Feb_Sales\n"
                            "FROM monthly_sales GROUP BY year;</pre>"
                    }
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 1:
            idx = i
            break
    if idx != -1:
        db[idx] = sql_module
    else:
        db.append(sql_module)
        
    save_db(db)
    print("SQL data populated successfully.")

if __name__ == '__main__':
    main()
