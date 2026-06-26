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
    
    hib_module = {
        "id": 3,
        "name": "Hibernate",
        "short": "Hibernate",
        "color": "c-amber",
        "count": 50,
        "subs": [
            {
                "head": "ORM & Setup",
                "qs": [
                    {
                        "q": "What is Hibernate? What problem does ORM solve over plain JDBC?",
                        "a": "<h4>Hibernate & ORM</h4>"
                            "Hibernate is an Object-Relational Mapping (ORM) framework for Java. It maps Java domain objects to database tables.<br/>"
                            "<h4>Problems solved over JDBC:</h4>"
                            "<ul>"
                            "<li>Eliminates boilerplate SQL mappings.</li>"
                            "<li>Provides object caching (First/Second level).</li>"
                            "<li>Ensures database independence (dialects translate HQL to specific SQL dialects).</li>"
                            "<li>Automates transaction management and connection pooling integrations.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between JDBC and Hibernate?",
                        "a": "<h4>JDBC vs. Hibernate</h4>"
                            "<table>"
                            "<tr><th>JDBC</th><th>Hibernate</th></tr>"
                            "<tr><td>Low-level database connectivity API.</td><td>High-level ORM framework built on JDBC.</td></tr>"
                            "<tr><td>Developer writes raw, platform-specific SQL queries.</td><td>Developer works with objects; Hibernate generates SQL.</td></tr>"
                            "<tr><td>No built-in caching mechanism.</td><td>Contains automatic caching strategies.</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is hibernate.cfg.xml? What are the essential properties?",
                        "a": "<h4>hibernate.cfg.xml</h4>"
                            "The main configuration file setting up DB connections, dialects, and mappings.<br/>"
                            "<em>Essential properties:</em> <code>connection.url</code>, <code>connection.username</code>, <code>connection.password</code>, <code>dialect</code> (translates queries), <code>show_sql</code> (logs SQL to console), <code>hbm2ddl.auto</code> (auto schema updates)."
                    },
                    {
                        "q": "What is an entity in Hibernate? What are the mandatory annotations?",
                        "a": "<h4>Hibernate Entities</h4>"
                            "A Java class mapped to a database table. It must meet POJO standards (default constructor, getter/setters).<br/>"
                            "<em>Mandatory annotations:</em> <code>@Entity</code> (marks class as entity) and <code>@Id</code> (marks primary key field)."
                    },
                    {
                        "q": "What is @Entity, @Table, @Id, @Column?",
                        "a": "<h4>Core JPA/Hibernate Annotations</h4>"
                            "<ul>"
                            "<li><strong><code>@Entity</code>:</strong> Registers class as mapped entity.</li>"
                            "<li><strong><code>@Table</code>:</strong> Specifies table name (optional, defaults to class name).</li>"
                            "<li><strong><code>@Id</code>:</strong> Declares primary key.</li>"
                            "<li><strong><code>@Column</code>:</strong> Maps attribute to specific database column name/limits.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are GenerationType strategies? (AUTO, IDENTITY, SEQUENCE, TABLE)",
                        "a": "<h4>Primary Key Generation Strategies</h4>"
                            "<ul>"
                            "<li><strong>IDENTITY:</strong> Database auto-increment column (e.g. MySQL <code>AUTO_INCREMENT</code>). Disables Hibernate batch inserts because ID requires insert immediate.</li>"
                            "<li><strong>SEQUENCE:</strong> Uses database Sequence generators. Highly efficient, supports batching.</li>"
                            "<li><strong>TABLE:</strong> Uses a separate database table to track key counters. Poor performance, rarely used.</li>"
                            "<li><strong>AUTO:</strong> Delegates strategy choice to Hibernate based on database support.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between openSession() and getCurrentSession()?",
                        "a": "<h4>openSession() vs. getCurrentSession()</h4>"
                            "<ul>"
                            "<li><strong><code>openSession()</code>:</strong> Always creates a new, independent Session. Must close manually.</li>"
                            "<li><strong><code>getCurrentSession()</code>:</strong> Binds session lifecycle to current transaction. Automatically flushes and closes when transaction ends.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the SessionFactory and when is it built?",
                        "a": "<h4>SessionFactory</h4>"
                            "A thread-safe, heavyweight factory object holding compiled mappings. Built during application startup. Usually one SessionFactory per database source."
                    }
                ]
            },
            {
                "head": "Entity Lifecycle",
                "qs": [
                    {
                        "q": "What are the states of a Hibernate entity? (Transient, Persistent, Detached, Removed)",
                        "a": "<h4>Entity Lifecycle States</h4>"
                            "<ul>"
                            "<li><strong>Transient:</strong> Object created in memory but not associated with Hibernate Session or database (no ID).</li>"
                            "<li><strong>Persistent:</strong> Object monitored by Session, representing a database row. Changes are auto-synchronized to DB during flush.</li>"
                            "<li><strong>Detached:</strong> Session is closed or cleared; object exists but is no longer monitored.</li>"
                            "<li><strong>Removed:</strong> Scheduled for deletion on transaction commit.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between save(), persist(), saveOrUpdate(), and merge()?",
                        "a": "<h4>Lifecycle Methods</h4>"
                            "<ul>"
                            "<li><strong><code>persist()</code>:</strong> JPA standard. Makes a transient instance persistent. Returns void. Does not guarantee immediate ID assign.</li>"
                            "<li><strong><code>save()</code>:</strong> Hibernate specific. Returns generated identifier immediately.</li>"
                            "<li><strong><code>saveOrUpdate()</code>:</strong> Saves if transient, updates if detached.</li>"
                            "<li><strong><code>merge()</code>:</strong> Copies state of detached object to a persistent instance, returning the persistent reference.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between get() and load()?",
                        "a": "<h4>get() vs. load()</h4>"
                            "<table>"
                            "<tr><th>get()</th><th>load()</th></tr>"
                            "<tr><td>Fetches data immediately from database.</td><td>Returns a lazy proxy object immediately. DB query runs only on field access.</td></tr>"
                            "<tr><td>Returns <code>null</code> if ID doesn't exist.</td><td>Throws <code>ObjectNotFoundException</code> if ID doesn't exist.</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is a dirty check in Hibernate? When does it trigger an UPDATE?",
                        "a": "<h4>Dirty Checking</h4>"
                            "Automatic update mechanism. At flush time, Hibernate compares current object field values with snapshots taken during load. If updates are found, it generates and executes SQL UPDATE statements automatically."
                    },
                    {
                        "q": "What is the difference between evict(), clear(), and close() on a Session?",
                        "a": "<h4>Releasing Session State</h4>"
                            "<ul>"
                            "<li><strong><code>evict(entity)</code>:</strong> Detaches a single entity instance from Session cache.</li>"
                            "<li><strong><code>clear()</code>:</strong> Detaches all entities, clearing the entire session.</li>"
                            "<li><strong><code>close()</code>:</strong> Terminates session instance entirely, releasing database resources.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Querying",
                "qs": [
                    {
                        "q": "What is HQL? How is it different from SQL?",
                        "a": "<h4>HQL vs. SQL</h4>"
                            "<ul>"
                            "<li><strong>HQL (Hibernate Query Language):</strong> Object-oriented query language targeting Java Class names and entity properties.</li>"
                            "<li><strong>SQL:</strong> Database-specific language targeting actual Table names and columns.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a named query (@NamedQuery)? Advantage?",
                        "a": "<h4>Named Queries</h4>"
                            "Static queries defined using annotations on entity classes.<br/>"
                            "<strong>Advantage:</strong> Pre-compiled at boot time, catching syntax errors early. Improves security and query organization."
                    },
                    {
                        "q": "What is the Criteria API (JPA Criteria)?",
                        "a": "<h4>Criteria API</h4>"
                            "A programmatic, type-safe API used to build dynamic queries using Java object methods, preventing runtime SQL syntax errors."
                    },
                    {
                        "q": "What is the difference between HQL and Criteria API?",
                        "a": "<h4>HQL vs. Criteria API</h4>"
                            "HQL is written as textual queries (easier for simple commands), whereas Criteria API uses object-oriented code interfaces (better for compiling complex, dynamic query forms)."
                    },
                    {
                        "q": "How do you use native SQL queries in Hibernate?",
                        "a": "<h4>Native SQL in Hibernate</h4>"
                            "Use the <code>createNativeQuery()</code> method:<br/>"
                            "<pre>List<Object[]> users = session.createNativeQuery(\"SELECT * FROM tbl_user\").list();</pre>"
                    },
                    {
                        "q": "What is pagination in Hibernate? (setFirstResult / setMaxResults)",
                        "a": "<h4>Pagination</h4>"
                            "Configure offsets directly using method parameters:<br/>"
                            "<pre>Query q = session.createQuery(\"from User\");\n"
                            "q.setFirstResult(10); // offset index\n"
                            "q.setMaxResults(5);   // limit size</pre>"
                    }
                ]
            },
            {
                "head": "Fetching & N+1",
                "qs": [
                    {
                        "q": "What is lazy loading vs eager loading?",
                        "a": "<h4>Lazy vs. Eager</h4>"
                            "<ul>"
                            "<li><strong>Lazy Loading:</strong> Child entities/collections are not fetched from DB until explicitly accessed in code. Saves database resources.</li>"
                            "<li><strong>Eager Loading:</strong> Fetches parent and children together in one single query. Can cause heavy memory usage.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is FetchType.LAZY vs FetchType.EAGER?",
                        "a": "<h4>JPA Fetch Types</h4>"
                            "Mapped using relation parameters:<br/>"
                            "<code>@ManyToOne(fetch = FetchType.LAZY)</code>. In JPA, <code>@OneToMany</code> defaults to LAZY, and <code>@ManyToOne</code> defaults to EAGER."
                    },
                    {
                        "q": "What is the N+1 select problem? How do you solve it?",
                        "a": "<h4>N+1 Select Problem</h4>"
                            "A performance bottleneck where fetching 1 parent entity requires N additional database queries to fetch matching child collections individually (usually during loops).<br/>"
                            "<strong>Solutions:</strong> Use <code>JOIN FETCH</code> queries, define <code>@BatchSize</code> on collection mappings, or configure <code>EntityGraph</code> profiles."
                    },
                    {
                        "q": "What is JOIN FETCH in HQL?",
                        "a": "<h4>JOIN FETCH</h4>"
                            "Tells Hibernate to fetch associated collections in the same initial query using an SQL JOIN, avoiding lazy-load N+1 select triggers."
                    },
                    {
                        "q": "What is batch fetching? How is it configured?",
                        "a": "<h4>Batch Fetching</h4>"
                            "An optimization fetching child collections in batches (e.g. 10 at a time) using IN clauses instead of individual queries.<br/>"
                            "<em>Configuration:</em> Mapped using <code>@BatchSize(size = 10)</code> on collection declarations."
                    }
                ]
            },
            {
                "head": "Associations",
                "qs": [
                    {
                        "q": "How do you map a @OneToMany relationship?",
                        "a": "<h4>@OneToMany Mapping</h4>"
                            "<pre>@Entity\npublic class Department {\n"
                            "  @OneToMany(mappedBy = \"department\")\n"
                            "  private List<Employee> employees;\n"
                            "}</pre>"
                    },
                    {
                        "q": "What is the difference between @OneToMany and @ManyToOne?",
                        "a": "<h4>One-to-Many vs. Many-to-One</h4>"
                            "They represent the two sides of a bidirectional relationship. <code>@ManyToOne</code> represents the child side pointing to a parent and holds the actual foreign key column (owning side)."
                    },
                    {
                        "q": "How do you map a @ManyToMany relationship (join table)?",
                        "a": "<h4>@ManyToMany Mapping</h4>"
                            "Requires a third intermediary join table:<br/>"
                            "<pre>@ManyToMany\n"
                            "@JoinTable(\n"
                            "  name = \"student_course\",\n"
                            "  joinColumns = @JoinColumn(name = \"student_id\"),\n"
                            "  inverseJoinColumns = @JoinColumn(name = \"course_id\")\n"
                            ")\n"
                            "private Set<Course> courses;</pre>"
                    },
                    {
                        "q": "What is @OneToOne? Unidirectional vs bidirectional?",
                        "a": "<h4>@OneToOne</h4>"
                            "One-to-One relation mapping. In unidirectional mapping, only one entity has a foreign key to the other. In bidirectional, the child entity uses <code>mappedBy</code> pointing back to the owning entity."
                    },
                    {
                        "q": "What is the mappedBy attribute? When is it required?",
                        "a": "<h4>mappedBy Attribute</h4>"
                            "Tells Hibernate that this side is the inverse (non-owning) relationship partner and matching foreign key attributes are mapped on the target entity class. Required in bidirectional relationships."
                    },
                    {
                        "q": "What is @JoinColumn?",
                        "a": "<h4>@JoinColumn</h4>"
                            "Defines the actual physical foreign key column name to create inside the database table."
                    },
                    {
                        "q": "What is @Embeddable and @Embedded?",
                        "a": "<h4>Embedded Components</h4>"
                            "Used to store modular property sets (e.g. <code>Address</code> containing zip, city) in the same database table as the parent entity.<br/>"
                            "<ul>"
                            "<li><code>@Embeddable</code>: Placed on component class.</li>"
                            "<li><code>@Embedded</code>: Placed on parent class attribute.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @Transient in Hibernate?",
                        "a": "<h4>@Transient</h4>"
                            "Declares that a field is purely temporary and should not be mapped to any database column."
                    },
                    {
                        "q": "What are CascadeType options? What does CascadeType.ALL include?",
                        "a": "<h4>Cascade Types</h4>"
                            "Propagates changes made on a parent object down to child objects automatically.<br/>"
                            "<em>Options:</em> <code>PERSIST</code>, <code>MERGE</code>, <code>REMOVE</code>, <code>REFRESH</code>, <code>DETACH</code>.<br/>"
                            "<code>CascadeType.ALL</code> groups all of the above options."
                    },
                    {
                        "q": "What is orphanRemoval?",
                        "a": "<h4>orphanRemoval</h4>"
                            "If set to true (<code>orphanRemoval = true</code>), removing a child entity reference from a parent collection will automatically delete that child row from the database."
                    }
                ]
            },
            {
                "head": "Caching",
                "qs": [
                    {
                        "q": "What is first-level cache in Hibernate? Can you disable it?",
                        "a": "<h4>First-Level Cache</h4>"
                            "Session-level, transactional cache. Enabled by default for all sessions and **cannot be disabled**. Keeps track of loaded entities within the current active session boundary."
                    },
                    {
                        "q": "What is second-level cache? How do you configure it (EhCache)?",
                        "a": "<h4>Second-Level Cache</h4>"
                            "Heavyweight SessionFactory-level cache. Shared across all user sessions. Remains disabled by default.<br/>"
                            "<em>Configuration:</em> Configured by setting cache providers in config files (e.g., <code>org.hibernate.cache.ehcache.EhCacheRegionFactory</code>) and mapping entities using <code>@Cacheable</code> annotations."
                    },
                    {
                        "q": "What is a query cache?",
                        "a": "<h4>Query Cache</h4>"
                            "Caches the actual query result IDs for exact parameters. Works in combination with second-level cache."
                    },
                    {
                        "q": "What is the difference between read-only and read-write second-level cache strategies?",
                        "a": "<h4>Cache Concurrency Strategies</h4>"
                            "<ul>"
                            "<li><strong>read-only:</strong> Good for static reference tables that never change. Simple, fast.</li>"
                            "<li><strong>read-write:</strong> Used if data is updated. Uses soft-locks to guarantee transaction isolation during concurrent database modifications.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Advanced",
                "qs": [
                    {
                        "q": "What is inheritance mapping in Hibernate? Name the three strategies.",
                        "a": "<h4>Inheritance Mapping</h4>"
                            "Mapping subclass OOP models to relational tables.<br/>"
                            "1. <code>SINGLE_TABLE</code> (default)<br/>"
                            "2. <code>JOINED</code><br/>"
                            "3. <code>TABLE_PER_CLASS</code>"
                    },
                    {
                        "q": "Explain SINGLE_TABLE vs JOINED vs TABLE_PER_CLASS with trade-offs.",
                        "a": "<h4>Inheritance Strategies Comparison</h4>"
                            "<ul>"
                            "<li><strong>SINGLE_TABLE:</strong> Saves all classes in one table using a discriminator column. Fast, but columns of subclasses must allow NULLs.</li>"
                            "<li><strong>JOINED:</strong> Subclasses have separate tables linked via join keys. Clean relational structure, but slow due to JOINS.</li>"
                            "<li><strong>TABLE_PER_CLASS:</strong> Subclasses have fully duplicated tables. No null columns, but query queries across parent types require slow UNION commands.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is optimistic locking? How is @Version used?",
                        "a": "<h4>Optimistic Locking</h4>"
                            "Locks data conceptually without database locks. Maps a version column (<code>@Version</code>). If a write operation conflicts with an updated version, Hibernate aborts and throws an <code>OptimisticLockException</code>."
                    },
                    {
                        "q": "What is pessimistic locking in Hibernate?",
                        "a": "<h4>Pessimistic Locking</h4>"
                            "Uses database-level locks directly (e.g., <code>FOR UPDATE</code>) to block other readers/writers until current transaction ends."
                    },
                    {
                        "q": "What is connection pooling in Hibernate? (C3P0, HikariCP)",
                        "a": "<h4>Hibernate Connection Pools</h4>"
                            "Configured using properties in <code>hibernate.cfg.xml</code> (e.g. <code>hibernate.hikari.maximumPoolSize</code>) to enable and manage database socket pooling libraries."
                    },
                    {
                        "q": "What does the hbm2ddl.auto (ddl-auto) property do? Values?",
                        "a": "<h4>hbm2ddl.auto</h4>"
                            "Controls schema generation at startup.<br/>"
                            "<em>Values:</em> <code>create</code> (drops and creates tables), <code>create-drop</code> (creates at startup, drops at shutdown), <code>update</code> (modifies table schemas dynamically), <code>validate</code> (checks structures but makes no modifications)."
                    },
                    {
                        "q": "What is batch processing in Hibernate and why is flush+clear needed?",
                        "a": "<h4>Hibernate Batch Processing</h4>"
                            "When updating thousands of records, Hibernate accumulates instances in the first-level cache. To avoid <code>OutOfMemoryError</code>, we must commit batch changes and clean the cache at intervals:<br/>"
                            "<pre>if (i % 50 == 0) {\n  session.flush();\n  session.clear();\n}</pre>"
                    },
                    {
                        "q": "What is the difference between Hibernate and JPA?",
                        "a": "<h4>JPA vs. Hibernate</h4>"
                            "<ul>"
                            "<li><strong>JPA:</strong> Java Persistence API is a specification (a set of interfaces/rules).</li>"
                            "<li><strong>Hibernate:</strong> A concrete provider framework that implements the JPA specification.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is Spring Data JPA and how does it relate to Hibernate?",
                        "a": "<h4>Spring Data JPA</h4>"
                            "An abstraction layer built on top of JPA providers (like Hibernate). It eliminates DAO implementation boilerplate using repository interfaces (e.g., JpaRepository)."
                    }
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 3:
            idx = i
            break
    if idx != -1:
        db[idx] = hib_module
    else:
        db.append(hib_module)
        
    save_db(db)
    print("Hibernate data populated successfully.")

if __name__ == '__main__':
    main()
