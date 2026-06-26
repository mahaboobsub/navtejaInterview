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
    
    adv_java = {
        "id": 2,
        "name": "Adv Java",
        "short": "Adv Java",
        "color": "c-coral",
        "count": 55,
        "subs": [
            {
                "head": "JDBC — Core",
                "qs": [
                    {
                        "q": "What is JDBC and what are its main components?",
                        "a": "<h4>JDBC Fundamentals</h4>"
                            "Java Database Connectivity (JDBC) is a Java API used to connect and execute queries with databases.<br/>"
                            "<h4>Key Components:</h4>"
                            "<ul>"
                            "<li><code>DriverManager</code>: Manages database driver registrations.</li>"
                            "<li><code>Connection</code>: Represents session interface with the database.</li>"
                            "<li><code>Statement</code>: Container for submitting SQL text query plans.</li>"
                            "<li><code>ResultSet</code>: Holds output data rows returned by database.</li>"
                            "<li><code>SQLException</code>: Class handling query errors.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are the steps to connect to a database using JDBC?",
                        "a": "<h4>JDBC Connection Steps</h4>"
                            "<ol>"
                            "<li>Import packages: <code>import java.sql.*;</code></li>"
                            "<li>Load and register driver class (optional in JDBC 4.0+): <code>Class.forName(\"com.mysql.cj.jdbc.Driver\");</code></li>"
                            "<li>Establish connection: <code>Connection conn = DriverManager.getConnection(url, user, password);</code></li>"
                            "<li>Create Statement: <code>Statement stmt = conn.createStatement();</code></li>"
                            "<li>Execute query: <code>ResultSet rs = stmt.executeQuery(\"SELECT * FROM users\");</code></li>"
                            "<li>Process results and Close resources inside try-with-resources.</li>"
                            "</ol>"
                    },
                    {
                        "q": "What is the JDBC URL format? Write the MySQL URL format.",
                        "a": "<h4>JDBC URL Format</h4>"
                            "A connection string that points database drivers to target servers.<br/>"
                            "<em>Syntax:</em> <code>jdbc:&lt;subprotocol&gt;:&lt;subname&gt;</code><br/>"
                            "<em>MySQL Syntax:</em> <code>jdbc:mysql://localhost:3306/db_name?useSSL=false&serverTimezone=UTC</code>"
                    },
                    {
                        "q": "What is the role of Class.forName() in JDBC (older vs newer approach)?",
                        "a": "<h4>Class.forName()</h4>"
                            "Used to dynamically load and register the database driver class into JVM memory.<br/>"
                            "<ul>"
                            "<li><strong>Older:</strong> Mandatory. Executing <code>Class.forName()</code> initialized the static blocks in driver classes which registered themselves with <code>DriverManager</code>.</li>"
                            "<li><strong>Newer (JDBC 4.0+):</strong> Optional. Drivers matching standard Service Provider Interface (SPI) are auto-loaded from JAR classpath class manifest lookups.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between Statement, PreparedStatement, and CallableStatement?",
                        "a": "<h4>Statement Comparisons</h4>"
                            "<ul>"
                            "<li><strong>Statement:</strong> Compiles and runs static SQL queries dynamically. Vulnerable to SQL injection.</li>"
                            "<li><strong>PreparedStatement:</strong> Compiles query structures once, allowing parameter placeholders (<code>?</code>). Prevents SQL injection, faster execution.</li>"
                            "<li><strong>CallableStatement:</strong> Extends PreparedStatement to call database stored procedures, managing IN/OUT parameters.</li>"
                            "</ul>"
                    },
                    {
                        "q": "Why is PreparedStatement preferred over Statement?",
                        "a": "<h4>Why Use PreparedStatement?</h4>"
                            "1. <strong>Precompilation:</strong> DB compiles SQL outline once, caching execution plan for repeat parameters.<br/>"
                            "2. <strong>Security:</strong> Parameters are treated strictly as literal values, stripping SQL command structures to prevent SQL Injection.<br/>"
                            "3. <strong>Readability:</strong> Code is cleaner compared to messy string concatenation."
                    },
                    {
                        "q": "What are the execute(), executeQuery(), and executeUpdate() methods?",
                        "a": "<h4>JDBC Execution Methods</h4>"
                            "<ul>"
                            "<li><strong><code>executeQuery()</code>:</strong> Used for SELECT statements. Returns a single <code>ResultSet</code> object.</li>"
                            "<li><strong><code>executeUpdate()</code>:</strong> Used for INSERT, UPDATE, DELETE. Returns integer count of affected rows.</li>"
                            "<li><strong><code>execute()</code>:</strong> General method. Returns true if first result is a ResultSet (SELECT), false if it is an update count or yields no results.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are the types of ResultSet (scroll sensitivity + updatability)?",
                        "a": "<h4>ResultSet Types</h4>"
                            "<ul>"
                            "<li><strong>Scroll Sensitivity:</strong>"
                            "<ul>"
                            "<li><code>TYPE_FORWARD_ONLY</code>: Default. Move cursor forward only.</li>"
                            "<li><code>TYPE_SCROLL_INSENSITIVE</code>: Bidirectional scrolling, does not reflect active database changes made by others.</li>"
                            "<li><code>TYPE_SCROLL_SENSITIVE</code>: Bidirectional, reflects live database updates.</li>"
                            "</ul>"
                            "</li>"
                            "<li><strong>Updatability:</strong>"
                            "<ul>"
                            "<li><code>CONCUR_READ_ONLY</code>: Cannot modify data through ResultSet.</li>"
                            "<li><code>CONCUR_UPDATABLE</code>: Allows updating database tables through ResultSet cursor methods.</li>"
                            "</ul>"
                            "</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is DatabaseMetaData? What information does it provide?",
                        "a": "<h4>DatabaseMetaData</h4>"
                            "Metadata details about the database server (capabilities, limits, configuration).<br/>"
                            "<em>Information:</em> database product name, version, driver name, supported transaction isolation levels, list of tables, database columns."
                    },
                    {
                        "q": "What is ResultSetMetaData?",
                        "a": "<h4>ResultSetMetaData</h4>"
                            "Metadata details about the columns inside a returned ResultSet.<br/>"
                            "<em>Information:</em> number of columns, column names, column data types, table origin names."
                    }
                ]
            },
            {
                "head": "JDBC — Advanced",
                "qs": [
                    {
                        "q": "What is connection pooling? Why is it critical in production?",
                        "a": "<h4>Connection Pooling</h4>"
                            "A pool of pre-created active database connections managed by a broker (e.g. HikariCP).<br/>"
                            "<strong>Importance:</strong> Creating database TCP sockets and authenticating takes considerable time. Pooling enables clients to instantly acquire, use, and release connections back, avoiding latency spikes and resource exhaustion."
                    },
                    {
                        "q": "What is a DataSource? How does it differ from DriverManager?",
                        "a": "<h4>DataSource vs. DriverManager</h4>"
                            "<ul>"
                            "<li><strong>DriverManager:</strong> Traditional approach. Generates new connections directly using driver classes on every request. Not configurable via JNDI.</li>"
                            "<li><strong>DataSource:</strong> Modern enterprise standard interface. Wraps database connection details, supports pooling, caching, distributed transactions, and can be registered in JNDI directories.</li>"
                            "</ul>"
                    },
                    {
                        "q": "How do you perform a batch update in JDBC?",
                        "a": "<h4>Batching in JDBC</h4>"
                            "Enables sending multiple SQL statements in a single network round-trip to database.<br/>"
                            "<pre>conn.setAutoCommit(false);\n"
                            "PreparedStatement ps = conn.prepareStatement(\"INSERT INTO log VALUES(?)\");\n"
                            "for(String m : logs) {\n"
                            "  ps.setString(1, m);\n"
                            "  ps.addBatch();\n"
                            "}\n"
                            "int[] results = ps.executeBatch();\n"
                            "conn.commit();</pre>"
                    },
                    {
                        "q": "How do you manage transactions manually in JDBC?",
                        "a": "<h4>Manual Transactions</h4>"
                            "<ol>"
                            "<li>Turn off auto-commit: <code>conn.setAutoCommit(false);</code></li>"
                            "<li>Execute statements.</li>"
                            "<li>On success: <code>conn.commit();</code></li>"
                            "<li>On exception: <code>conn.rollback();</code></li>"
                            "</ol>"
                    },
                    {
                        "q": "What is auto-commit mode and when would you turn it off?",
                        "a": "<h4>Auto-Commit Mode</h4>"
                            "Default JDBC behavior where every statement executes as an independent transaction and commits immediately.<br/>"
                            "<strong>When to turn off:</strong> When grouping multiple statements as a single atomic unit of work (e.g. money transfer debit/credit) or doing batch updates."
                    },
                    {
                        "q": "How do you call a stored procedure using CallableStatement?",
                        "a": "<h4>Calling Stored Procedures</h4>"
                            "<pre>CallableStatement cs = conn.prepareCall(\"{call getSalary(?, ?)}\");\n"
                            "cs.setInt(1, 101); // IN parameter\n"
                            "cs.registerOutParameter(2, Types.DECIMAL); // OUT parameter\n"
                            "cs.execute();\n"
                            "double salary = cs.getDouble(2);</pre>"
                    },
                    {
                        "q": "What is a RowSet? What are the types?",
                        "a": "<h4>RowSet</h4>"
                            "A wrapper around ResultSet which is easier to pass around. Can be disconnected from the database.<br/>"
                            "<h4>Types:</h4>"
                            "<ul>"
                            "<li><code>JdbcRowSet</code>: Connected wrapper.</li>"
                            "<li><code>CachedRowSet</code>: Disconnected container. Can cache data in memory and sync back.</li>"
                            "<li><code>WebRowSet</code>: Can read/write XML data representations.</li>"
                            "</ul>"
                    },
                    {
                        "q": "How do you handle a BLOB/CLOB using JDBC?",
                        "a": "<h4>BLOB / CLOB</h4>"
                            "<ul>"
                            "<li><strong>BLOB (Binary Large Object):</strong> For files, images. Read using <code>getBlob()</code>, write using <code>setBinaryStream()</code>.</li>"
                            "<li><strong>CLOB (Character Large Object):</strong> For large text docs. Read using <code>getClob()</code>, write using <code>setCharacterStream()</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "How do you prevent SQL injection in JDBC?",
                        "a": "<h4>Preventing SQL Injection</h4>"
                            "Always use <code>PreparedStatement</code> parameterized inputs instead of raw string concatenations. Never build SQL by gluing variables directly: <code>\"SELECT * FROM users WHERE name='\" + input + \"'\"</code>."
                    },
                    {
                        "q": "What is the difference between JDBC 3.0 and JDBC 4.0?",
                        "a": "<h4>JDBC 3.0 vs. JDBC 4.0</h4>"
                            "<ul>"
                            "<li><strong>Auto-loading drivers:</strong> JDBC 4.0 loads drivers from classpath automatically (no <code>Class.forName</code> needed).</li>"
                            "<li><strong>Annotations:</strong> Supported XML metadata configurations can be simplified using annotations.</li>"
                            "<li><strong>SQLXML support:</strong> Adds native types for handling XML files.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Servlets — Lifecycle & Config",
                "qs": [
                    {
                        "q": "What is a Servlet and what is its complete lifecycle?",
                        "a": "<h4>Servlet Definition & Lifecycle</h4>"
                            "A Java class that extends dynamic server processing capabilities, running on a web container to handle HTTP requests.<br/>"
                            "<h4>Lifecycle Phases:</h4>"
                            "<ol>"
                            "<li><strong>Loading & Instantiation:</strong> Web container reads config files and instantiates servlet instance.</li>"
                            "<li><strong>Initialization:</strong> Container runs <code>init(ServletConfig)</code> once.</li>"
                            "<li><strong>Service execution:</strong> Runs <code>service(req, res)</code> on every incoming request (dispatches to doGet, doPost, etc.). Executed in separate threads.</li>"
                            "<li><strong>Destruction:</strong> Container runs <code>destroy()</code> before removing the servlet from memory.</li>"
                            "</ol>"
                    },
                    {
                        "q": "What is the difference between GenericServlet and HttpServlet?",
                        "a": "<h4>GenericServlet vs. HttpServlet</h4>"
                            "<ul>"
                            "<li><strong>GenericServlet:</strong> Protocol-independent. Implements basic lifecycle. Must override <code>service()</code> method.</li>"
                            "<li><strong>HttpServlet:</strong> Protocol-specific (HTTP). Extends GenericServlet. Automates dispatching to methods like <code>doGet()</code>, <code>doPost()</code>, etc.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between init(), service(), and destroy()?",
                        "a": "<h4>Servlet Lifecycle Methods</h4>"
                            "<ul>"
                            "<li><strong><code>init()</code>:</strong> Runs once to setup config variables. Called during initialization.</li>"
                            "<li><strong><code>service()</code>:</strong> Called repeatedly for every single HTTP request. Decides GET/POST types.</li>"
                            "<li><strong><code>destroy()</code>:</strong> Runs once when container shuts down, releasing file sockets or DB connections.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is web.xml and what does it configure?",
                        "a": "<h4>web.xml Deployment Descriptor</h4>"
                            "The configuration file for servlet applications. Defines web assets mappings: servlet class paths, routing URLs (servlet-mapping), security constraints, filters, session timeouts, and listeners."
                    },
                    {
                        "q": "What is the @WebServlet annotation?",
                        "a": "<h4>@WebServlet (Servlet 3.0+)</h4>"
                            "Annotation to define a class as a Servlet and map URL paths directly in java classes, eliminating the need to declare servlets in <code>web.xml</code>.<br/>"
                            "<pre>@WebServlet(\"/users\")\npublic class UserServlet extends HttpServlet { ... }</pre>"
                    },
                    {
                        "q": "What is the difference between ServletConfig and ServletContext?",
                        "a": "<h4>ServletConfig vs. ServletContext</h4>"
                            "<table>"
                            "<tr><th>ServletConfig</th><th>ServletContext</th></tr>"
                            "<tr><td>One instance per Servlet definition.</td><td>One instance per Web Application context.</td></tr>"
                            "<tr><td>Used to pass init parameters to a specific servlet.</td><td>Used to share parameters globally across all servlets in the app.</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What are init-param and context-param?",
                        "a": "<h4>Init vs Context Parameters</h4>"
                            "<ul>"
                            "<li><strong>init-param:</strong> Key-value configurations defined within a specific servlet in web.xml. Accessed using <code>getServletConfig().getInitParameter()</code>.</li>"
                            "<li><strong>context-param:</strong> Global parameters defined outside any servlet tags. Accessed using <code>getServletContext().getInitParameter()</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a welcome file list?",
                        "a": "<h4>Welcome File List</h4>"
                            "Configuration in <code>web.xml</code> that defines files (like <code>index.html</code>, <code>home.jsp</code>) to load automatically if a user requests the root directory URL path."
                    }
                ]
            },
            {
                "head": "Servlets — Request/Response",
                "qs": [
                    {
                        "q": "What is the difference between doGet() and doPost()?",
                        "a": "<h4>doGet vs. doPost</h4>"
                            "<ul>"
                            "<li><strong><code>doGet()</code>:</strong> Appends parameters to the URL query string (visible, limited size, cached, bookmarkable). Used to fetch data.</li>"
                            "<li><strong><code>doPost()</code>:</strong> Sends data in HTTP body (hidden, unlimited size, not cached). Used to modify/create resource state.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between the HTTP GET and POST methods?",
                        "a": "<h4>HTTP GET vs. POST</h4>"
                            "GET is designed for safe, idempotent queries without side-effects. POST is designed for modifications, database updates, and non-idempotent operations."
                    },
                    {
                        "q": "What is RequestDispatcher? What is the difference between forward() and include()?",
                        "a": "<h4>RequestDispatcher</h4>"
                            "Used to delegate requests to other web components (servlets, JSPs, HTML).<br/>"
                            "<ul>"
                            "<li><strong><code>forward()</code>:</strong> Transfers request processing entirely. Target component takes over control, response is committed by target. Url on client browser doesn't change.</li>"
                            "<li><strong><code>include()</code>:</strong> Temporarily includes content from another resource, then returns execution back to original servlet to finish response.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between sendRedirect() and forward()?",
                        "a": "<h4>forward() vs. sendRedirect()</h4>"
                            "<table>"
                            "<tr><th>Feature</th><th>forward()</th><th>sendRedirect()</th></tr>"
                            "<tr><td><strong>Routing location</strong></td><td>Internal server-side forwarding</td><td>Client-side redirect (returns 302 code)</td></tr>"
                            "<li><strong>HTTP Requests</strong></td><td>1 request/response cycle</td><td>2 separate request cycles</td></tr>"
                            "<li><strong>URL Browser</strong></td><td>Remains original servlet URL</td><td>Changes to redirected URL location</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "How do you read request parameters in a Servlet?",
                        "a": "<h4>Reading Parameters</h4>"
                            "Use the <code>HttpServletRequest</code> methods:<br/>"
                            "<ul>"
                            "<li><code>getParameter(\"name\")</code>: Returns single parameter string.</li>"
                            "<li><code>getParameterValues(\"hobbies\")</code>: Returns string array (checkboxes).</li>"
                            "</ul>"
                    },
                    {
                        "q": "How do you handle file uploads in a Servlet (Multipart)?",
                        "a": "<h4>File Uploads (Servlet 3.0+)</h4>"
                            "Annotate servlet with <code>@MultipartConfig</code> and fetch file parts using request APIs:<br/>"
                            "<pre>@MultipartConfig\npublic class Upload extends HttpServlet {\n"
                            "  protected void doPost(request, response) {\n"
                            "    Part filePart = request.getPart(\"file\");\n"
                            "    filePart.write(\"output.txt\");\n"
                            "  }\n"
                            "}</pre>"
                    },
                    {
                        "q": "What is a Servlet filter? Give a real use case.",
                        "a": "<h4>Servlet Filters</h4>"
                            "A component that intercepts requests and responses before they reach the servlet to perform pre/post-processing tasks.<br/>"
                            "<em>Real use cases:</em> Logging request details, verifying user authentication tokens, converting string formats (encoding), and CORS header management."
                    },
                    {
                        "q": "What is a Servlet listener? Name some listener interfaces.",
                        "a": "<h4>Servlet Listeners</h4>"
                            "Objects that monitor life events of the web application (context load, session creation, request lifecycle changes).<br/>"
                            "<em>Examples:</em> <code>ServletContextListener</code>, <code>HttpSessionListener</code>, <code>ServletRequestListener</code>."
                    },
                    {
                        "q": "How do you handle thread safety in a Servlet?",
                        "a": "<h4>Thread Safety in Servlets</h4>"
                            "Servlet containers run a single shared servlet instance, invoking <code>service()</code> in multiple parallel threads. To stay thread-safe:<br/>"
                            "<ul>"
                            "<li>Avoid class instance variables (state).</li>"
                            "<li>Keep variables confined inside local method scopes (method variables are allocated on thread stack).</li>"
                            "<li>Synchronize shared objects explicitly if necessary (though not recommended as it reduces performance).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is SingleThreadModel and why was it deprecated?",
                        "a": "<h4>SingleThreadModel</h4>"
                            "A deprecated legacy interface that forced containers to instantiate a pool of servlets or run requests sequentially (single thread per servlet). It did not truly solve concurrency bugs, consumed too much memory, and hurt performance."
                    }
                ]
            },
            {
                "head": "Session Management",
                "qs": [
                    {
                        "q": "What is session management? Why is it needed in HTTP?",
                        "a": "<h4>Session Management</h4>"
                            "A method to maintain client state across multiple page requests. Needed because HTTP is a <strong>stateless protocol</strong>; each request is treated as independent and holds no history of previous actions."
                    },
                    {
                        "q": "What are the four techniques of session management?",
                        "a": "<h4>Session Tracking Techniques</h4>"
                            "1. <strong>Cookies:</strong> Key-value text stored on client browser, sent in headers automatically.<br/>"
                            "2. <strong>HttpSession API:</strong> Key identifier (JSESSIONID) stored in client cookie, mapping to memory storage on the server.<br/>"
                            "3. <strong>URL Rewriting:</strong> Appending session ID directly into all hyperlinks: <code>url?jsessionid=123</code>.<br/>"
                            "4. <strong>Hidden Form Fields:</strong> Using invisible input fields inside HTML forms: <code>&lt;input type='hidden' name='session' value='123'&gt;</code>."
                    },
                    {
                        "q": "What is HttpSession? Key methods?",
                        "a": "<h4>HttpSession API</h4>"
                            "Server-side mechanism for user session persistence.<br/>"
                            "<em>Key methods:</em> <code>setAttribute(key, val)</code>, <code>getAttribute(key)</code>, <code>removeAttribute(key)</code>, <code>invalidate()</code> (destroys session)."
                    },
                    {
                        "q": "What is the difference between HttpSession, Cookies, and URL Rewriting?",
                        "a": "<h4>Session Comparison</h4>"
                            "<ul>"
                            "<li><strong>Cookies:</strong> Stores data entirely on client side. Vulnerable to modification and can be disabled by users.</li>"
                            "<li><strong>HttpSession:</strong> Stores data securely on server side. Client only holds the unique session ID.</li>"
                            "<li><strong>URL Rewriting:</strong> Works even if client browser cookies are disabled, but exposes session parameters in browser URL.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is session timeout and how do you configure it?",
                        "a": "<h4>Session Timeout</h4>"
                            "The period of inactivity after which the server automatically invalidates a session.<br/>"
                            "<em>Configuration:</em> Defined in <code>web.xml</code> using minutes:<br/>"
                            "<pre>&lt;session-config&gt;\n  &lt;session-timeout&gt;30&lt;/session-timeout&gt;\n&lt;/session-config&gt;</pre>"
                    },
                    {
                        "q": "What is JSESSIONID?",
                        "a": "<h4>JSESSIONID</h4>"
                            "A unique session identifier token generated automatically by servlet containers to associate incoming requests with their matching HttpSession stored in server memory."
                    }
                ]
            },
            {
                "head": "JSP — Basics",
                "qs": [
                    {
                        "q": "What is JSP and how is it different from Servlet?",
                        "a": "<h4>JSP vs. Servlet</h4>"
                            "<ul>"
                            "<li><strong>JSP (JavaServer Pages):</strong> Document-centric (looks like HTML with Java tags embedded). Used mainly for view rendering. Auto-compiles to a servlet behind the scenes.</li>"
                            "<li><strong>Servlet:</strong> Java-centric code. Used mainly for controller logic, parsing forms, database operations, routing.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the JSP page lifecycle?",
                        "a": "<h4>JSP Lifecycle</h4>"
                            "During request, container reads JSP and compiles it into a Java Servlet class:<br/>"
                            "<code>Translation</code> -> <code>Compilation (.class)</code> -> <code>Instantiation</code> -> <code>_jspInit()</code> -> <code>_jspService()</code> -> <code>_jspDestroy()</code>."
                    },
                    {
                        "q": "What are JSP directives? Name all three and their purpose.",
                        "a": "<h4>JSP Directives</h4>"
                            "Instructions that direct the container on how to process the page. Syntax: <code>&lt;%@ directive ... %&gt;</code>.<br/>"
                            "1. <strong>page:</strong> Defines page-specific settings (imports, error pages).<br/>"
                            "2. <strong>include:</strong> Inserts file content during translation phase (static include).<br/>"
                            "3. <strong>taglib:</strong> Declares custom tag libraries (JSTL) used on page."
                    },
                    {
                        "q": "What are the 9 JSP implicit objects?",
                        "a": "<h4>JSP Implicit Objects</h4>"
                            "Predefined Java objects available inside JSP scriptlets automatically:<br/>"
                            "1. <code>request</code> (HttpServletRequest)<br/>"
                            "2. <code>response</code> (HttpServletResponse)<br/>"
                            "3. <code>out</code> (JspWriter)<br/>"
                            "4. <code>session</code> (HttpSession)<br/>"
                            "5. <code>application</code> (ServletContext)<br/>"
                            "6. <code>config</code> (ServletConfig)<br/>"
                            "7. <code>pageContext</code> (PageContext)<br/>"
                            "8. <code>page</code> (this servlet class instance)<br/>"
                            "9. <code>exception</code> (Throwable - only inside error pages)"
                    },
                    {
                        "q": "What is the difference between JSP scriptlet, expression, and declaration?",
                        "a": "<h4>JSP Scripting Elements</h4>"
                            "<ul>"
                            "<li><strong>Scriptlets (<code>&lt;% ... %&gt;</code>):</strong> Embeds executable Java statements into the service method.</li>"
                            "<li><strong>Expressions (<code>&lt;%= ... %&gt;</code>):</strong> Evaluates expressions, prints values directly to response. No semicolons.</li>"
                            "<li><strong>Declarations (<code>&lt;%! ... %&gt;</code>):</strong> Declares variables or helper methods outside the service method (as class-level members).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is Expression Language (EL)? Why is it preferred over scriptlets?",
                        "a": "<h4>Expression Language (EL)</h4>"
                            "A simplified expression syntax (e.g. <code>${user.name}</code>) to access data models.<br/>"
                            "<strong>Why preferred:</strong> Enables building JSPs without embedding ugly Java scriptlet code, improving design isolation and readability."
                    },
                    {
                        "q": "What is JSTL? Name key JSTL tag libraries.",
                        "a": "<h4>JSTL (JSP Standard Tag Library)</h4>"
                            "A standard library of tags for common JSP design logic (loops, conditions, database access).<br/>"
                            "<em>Libraries:</em> Core (<code>c:if</code>, <code>c:forEach</code>), Formatting (<code>fmt</code>), SQL (<code>sql</code>), XML (<code>x</code>)."
                    }
                ]
            },
            {
                "head": "JSP — Advanced",
                "qs": [
                    {
                        "q": "What is the difference between the include directive and <jsp:include> action?",
                        "a": "<h4>JSP Includes</h4>"
                            "<ul>"
                            "<li><strong>include directive (<code>&lt;%@ include %&gt;</code>):</strong> Static inclusion. Happens during translation phase. Merges file contents first, compiles once. Best for static headers.</li>"
                            "<li><strong>include action (<code>&lt;jsp:include&gt;</code>):</strong> Dynamic inclusion. Executes target page at runtime, inserts result output. Best for dynamic page layouts.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between <jsp:forward> and sendRedirect()?",
                        "a": "<h4>JSP Forward vs. Redirect</h4>"
                            "<ul>"
                            "<li><strong><code>&lt;jsp:forward&gt;</code>:</strong> Server-side forward using RequestDispatcher. URL remains unchanged.</li>"
                            "<li><strong><code>sendRedirect()</code>:</strong> Client-side redirect. Involves browser reloading another URL.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are JSP custom tags?",
                        "a": "<h4>JSP Custom Tags</h4>"
                            "User-defined elements that execute customized Java handlers to replace Java scriptlets, keeping views clean. Formats extend SimpleTagSupport classes."
                    },
                    {
                        "q": "What is the difference between session scope, request scope, and application scope?",
                        "a": "<h4>JSP Scope Scopes</h4>"
                            "<ul>"
                            "<li><strong>request:</strong> Data persists only for the duration of the current request/response cycle.</li>"
                            "<li><strong>session:</strong> Data persists across multiple user page views until session invalidates.</li>"
                            "<li><strong>application:</strong> Data is shared globally across all users of the entire web application.</li>"
                            "</ul>"
                    },
                    {
                        "q": "How do you pass data from Servlet to JSP?",
                        "a": "<h4>Servlet to JSP Data Sharing</h4>"
                            "Set attributes in request or session scopes in the servlet, then forward request to JSP:<br/>"
                            "<pre>// In Servlet:\nrequest.setAttribute(\"info\", \"success\");\n"
                            "request.getRequestDispatcher(\"view.jsp\").forward(request, response);\n"
                            "// In JSP:\nString msg = (String) request.getAttribute(\"info\"); // or ${info}</pre>"
                    },
                    {
                        "q": "What is the MVC pattern in Servlet+JSP? Explain roles of each layer.",
                        "a": "<h4>MVC Pattern</h4>"
                            "<ul>"
                            "<li><strong>Model:</strong> Plain Java objects (POJO, Entities) representing application state, database data, business logic.</li>"
                            "<li><strong>View:</strong> JSP files rendering HTML/CSS UI interface containing data passed from Controller.</li>"
                            "<li><strong>Controller:</strong> Servlet intercepts incoming client requests, manages models, chooses which JSPs to route output results.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the page directive in JSP? Key attributes?",
                        "a": "<h4>JSP Page Directive</h4>"
                            "Defines properties for the entire JSP file.<br/>"
                            "<em>Key attributes:</em> <code>import</code>, <code>contentType</code>, <code>errorPage</code>, <code>isErrorPage</code>, <code>session</code> (boolean)."
                    },
                    {
                        "q": "How do you handle exceptions in JSP (errorPage attribute)?",
                        "a": "<h4>JSP Error Pages</h4>"
                            "Configure error bindings using page directives:<br/>"
                            "1. In source page: <code>&lt;%@ page errorPage=\"error.jsp\" %&gt;</code><br/>"
                            "2. In error handler page: <code>&lt;%@ page isErrorPage=\"true\" %&gt;</code> (this unlocks the <code>exception</code> implicit object)."
                    },
                    {
                        "q": "What is the difference between out.print() and out.println() in JSP?",
                        "a": "<h4>out.print vs. out.println</h4>"
                            "Both write characters to the client output writer. <code>println()</code> appends a platform-dependent line separator (newline) to the output stream, but in HTML this is rendered as standard white space rather than a line break (<code>&lt;br&gt;</code>)."
                    },
                    {
                        "q": "What is CORS? How would you handle it in a Servlet filter?",
                        "a": "<h4>CORS (Cross-Origin Resource Sharing)</h4>"
                            "A browser security mechanism that blocks scripts running on origin A from accessing resources hosted at origin B. Handle by injecting CORS headers in filter responses:<br/>"
                            "<pre>res.setHeader(\"Access-Control-Allow-Origin\", \"*\");\n"
                            "res.setHeader(\"Access-Control-Allow-Methods\", \"GET, POST, OPTIONS\");</pre>"
                    }
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 2:
            idx = i
            break
    if idx != -1:
        db[idx] = adv_java
    else:
        db.append(adv_java)
        
    save_db(db)
    print("Adv Java data populated successfully.")

if __name__ == '__main__':
    main()
