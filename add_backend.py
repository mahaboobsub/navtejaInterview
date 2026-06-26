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
    
    backend_module = {
        "id": 5,
        "name": "Backend",
        "short": "Backend",
        "color": "c-green",
        "count": 55,
        "subs": [
            {
                "head": "REST API Fundamentals",
                "qs": [
                    {
                        "q": "What is REST? What are the six REST architectural constraints?",
                        "a": "<h4>REST (Representational State Transfer)</h4>"
                            "An architectural style for designing networked applications using stateless, client-server communications.<br/>"
                            "<h4>Six Constraints:</h4>"
                            "1. Uniform Interface<br/>"
                            "2. Client-Server<br/>"
                            "3. Stateless<br/>"
                            "4. Cacheable<br/>"
                            "5. Layered System<br/>"
                            "6. Code on Demand (optional)"
                    },
                    {
                        "q": "What is the difference between REST and SOAP?",
                        "a": "<h4>REST vs. SOAP</h4>"
                            "<table>"
                            "<tr><th>REST</th><th>SOAP</th></tr>"
                            "<tr><td>Architectural style using simple HTTP protocols.</td><td>Strict XML-based protocol.</td></tr>"
                            "<tr><td>Supports JSON, XML, Plain text, HTML formats.</td><td>Supports XML format only.</td></tr>"
                            "<tr><td>Stateless, flexible, lightweight.</td><td>Heavyweight, has built-in security specifications (WS-Security).</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What are the HTTP methods and when to use each? (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)",
                        "a": "<h4>HTTP Methods</h4>"
                            "<ul>"
                            "<li><code>GET</code>: Fetches resources.</li>"
                            "<li><code>POST</code>: Creates new resources.</li>"
                            "<li><code>PUT</code>: Replaces existing resources entirely.</li>"
                            "<li><code>PATCH</code>: Modifies resources partially.</li>"
                            "<li><code>DELETE</code>: Removes resources.</li>"
                            "<li><code>HEAD</code>: Fetches headers only (no body).</li>"
                            "<li><code>OPTIONS</code>: Inspects allowed HTTP methods.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between PUT and PATCH?",
                        "a": "<h4>PUT vs. PATCH</h4>"
                            "<ul>"
                            "<li><strong><code>PUT</code>:</strong> Replaces the resource completely. Requires sending all resource attributes.</li>"
                            "<li><strong><code>PATCH</code>:</strong> Updates only the specific properties supplied in request.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What does idempotent mean? Which HTTP methods are idempotent?",
                        "a": "<h4>Idempotence</h4>"
                            "An operation is idempotent if executing it multiple times yields the exact same state and side-effects as executing it once.<br/>"
                            "<em>Idempotent methods:</em> <code>GET</code>, <code>PUT</code>, <code>DELETE</code>, <code>HEAD</code>, <code>OPTIONS</code>. <code>POST</code> is NOT idempotent."
                    },
                    {
                        "q": "What is statelessness in REST?",
                        "a": "<h4>Statelessness</h4>"
                            "Every request from client must contain all context and authentication tokens required to understand and process the request. No session history is saved on server memory."
                    },
                    {
                        "q": "What is content negotiation?",
                        "a": "<h4>Content Negotiation</h4>"
                            "The process where client and server negotiate output formats (e.g. JSON or XML) using headers: <code>Accept</code> (client requests format) and <code>Content-Type</code> (server returns format)."
                    },
                    {
                        "q": "What is HATEOAS?",
                        "a": "<h4>HATEOAS</h4>"
                            "Hypermedia As The Engine Of Application State. A REST constraint where API responses contain navigation links directing clients dynamically to next available actions."
                    }
                ]
            },
            {
                "head": "HTTP Status Codes",
                "qs": [
                    {
                        "q": "What are the 5 HTTP status code classes? Give 3 examples each.",
                        "a": "<h4>HTTP Status Code Classes</h4>"
                            "<ul>"
                            "<li><strong>1xx (Informational):</strong> 100 Continue, 101 Switching Protocols, 102 Processing.</li>"
                            "<li><strong>2xx (Success):</strong> 200 OK, 201 Created, 204 No Content.</li>"
                            "<li><strong>3xx (Redirection):</strong> 301 Moved Permanently, 302 Found, 304 Not Modified.</li>"
                            "<li><strong>4xx (Client Error):</strong> 400 Bad Request, 401 Unauthorized, 403 Forbidden.</li>"
                            "<li><strong>5xx (Server Error):</strong> 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between 200 OK and 201 Created?",
                        "a": "<h4>200 OK vs. 201 Created</h4>"
                            "<ul>"
                            "<li><strong>200 OK:</strong> General success code returning request results (typically GET, PUT, PATCH updates).</li>"
                            "<li><strong>201 Created:</strong> Success code indicating that a new resource has been successfully created. Often returns resource URL in Location headers (typically POST).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is 204 No Content?",
                        "a": "<h4>204 No Content</h4>"
                            "Request executed successfully but response body is intentionally empty (typically returned on DELETE requests)."
                    },
                    {
                        "q": "What is the difference between 400, 401, 403, and 404?",
                        "a": "<h4>Client Error Codes</h4>"
                            "<ul>"
                            "<li><strong>400 Bad Request:</strong> Syntax error, missing params, invalid JSON body.</li>"
                            "<li><strong>401 Unauthorized:</strong> Client identity missing or unauthenticated.</li>"
                            "<li><strong>403 Forbidden:</strong> Client identity is known but lacks access privileges.</li>"
                            "<li><strong>404 Not Found:</strong> Target resource URL does not exist.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is 409 Conflict?",
                        "a": "<h4>409 Conflict</h4>"
                            "Indicates that the request conflicts with database state (e.g. attempting to register a user email that already exists)."
                    },
                    {
                        "q": "What is 422 Unprocessable Entity?",
                        "a": "<h4>422 Unprocessable Entity</h4>"
                            "Syntax is correct (valid JSON) but parameters contain validation errors (e.g. age value must be positive)."
                    },
                    {
                        "q": "What is 429 Too Many Requests?",
                        "a": "<h4>429 Too Many Requests</h4>"
                            "The client has exceeded API rate limits within a specified time window."
                    },
                    {
                        "q": "What is 500 vs 503?",
                        "a": "<h4>500 vs. 503</h4>"
                            "<ul>"
                            "<li><strong>500 Internal Server Error:</strong> General unhandled server crash exception.</li>"
                            "<li><strong>503 Service Unavailable:</strong> Server is overloaded, down, or undergoing maintenance.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "API Design",
                "qs": [
                    {
                        "q": "What is API versioning? What are the common strategies?",
                        "a": "<h4>API Versioning</h4>"
                            "Managing API changes without breaking existing clients.<br/>"
                            "<em>Strategies:</em> URI path (<code>/v1/users</code>), Request Parameter (<code>/users?version=1</code>), Custom Headers (<code>X-API-Version: 1</code>), Accept Header Media Type (<code>Accept: application/vnd.company.v1+json</code>)."
                    },
                    {
                        "q": "What is pagination in REST APIs? (offset vs cursor-based)",
                        "a": "<h4>Pagination Strategies</h4>"
                            "<ul>"
                            "<li><strong>Offset Pagination:</strong> Uses page/limit query inputs. Easy to map but slows down on high offsets and can skip/duplicate rows if records are updated.</li>"
                            "<li><strong>Cursor-Based:</strong> Returns a pointer (ID/timestamp of last item). Highly performant, immune to concurrent data writes. Best for infinite scroll feeds.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is rate limiting and how is it implemented?",
                        "a": "<h4>Rate Limiting</h4>"
                            "Throttling request limits per client to prevent API abuse. Implemented using Token Bucket or Leaky Bucket algorithms, often integrated into API Gateways or middleware using Redis counters."
                    },
                    {
                        "q": "What is an API Gateway?",
                        "a": "<h4>API Gateway</h4>"
                            "A single entry point for microservices that routes requests, handles authentication, applies rate limits, aggregates service outputs, and executes load balancing."
                    },
                    {
                        "q": "What is Swagger/OpenAPI? Why is documentation important?",
                        "a": "<h4>Swagger / OpenAPI</h4>"
                            "A standard specification language describing REST API endpoints, inputs, outputs, and security schemes, generating interactive UI docs (Swagger UI)."
                    },
                    {
                        "q": "What is CORS and how do you handle it in a Spring Boot app?",
                        "a": "<h4>CORS in Spring Boot</h4>"
                            "Use the <code>@CrossOrigin</code> annotation on controllers, or configure a global <code>WebMvcConfigurer</code> bean mapping allowed origins and headers."
                    },
                    {
                        "q": "What is an interceptor in Spring?",
                        "a": "<h4>Interceptors</h4>"
                            "A class that intercepts controller requests before/after execution (implementing <code>HandlerInterceptor</code>) to log metrics, verify authentication tokens, or modify data models."
                    },
                    {
                        "q": "What is idempotency key?",
                        "a": "<h4>Idempotency Key</h4>"
                            "A unique UUID token sent by client in request headers (e.g. <code>Idempotency-Key: <uuid></code>). The server caches this key; if a duplicate request is received, it returns the cached response, preventing duplicate operations."
                    }
                ]
            },
            {
                "head": "Architecture",
                "qs": [
                    {
                        "q": "What is the difference between monolithic and microservices architecture?",
                        "a": "<h4>Monolithic vs. Microservices</h4>"
                            "<ul>"
                            "<li><strong>Monolithic:</strong> Entire system compiled and deployed as a single application package. Simple deployment, fast local calls, but hard to scale and slow to compile.</li>"
                            "<li><strong>Microservices:</strong> System split into small, independently deployable services collaborating over network APIs. Scalable and resilient, but complex to coordinate.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are the advantages and disadvantages of microservices?",
                        "a": "<h4>Microservices Trade-offs</h4>"
                            "<strong>Pros:</strong> Independent scaling, technology freedom, isolated fault scopes, fast team iterations.<br/>"
                            "<strong>Cons:</strong> Network overhead, complex transactions (requires Saga pattern), logging fragmentation, deployment orchestration."
                    },
                    {
                        "q": "What is service discovery? (Eureka)",
                        "a": "<h4>Service Discovery</h4>"
                            "A database directory tracking active microservice instance IP locations dynamically. Instances register with registry servers (like Netflix Eureka) at startup, and clients lookup paths dynamically to route traffic."
                    },
                    {
                        "q": "What is a load balancer? Types?",
                        "a": "<h4>Load Balancers</h4>"
                            "Distributes traffic across multiple backend instances.<br/>"
                            "<em>Types:</em> Hardware vs Software load balancers; Layer 4 (Transport layer TCP routing) vs Layer 7 (Application layer URL routing)."
                    },
                    {
                        "q": "What is a message queue? Difference between RabbitMQ and Kafka?",
                        "a": "<h4>Message Queues</h4>"
                            "Systems enabling asynchronous, decoupled service communications.<br/>"
                            "<ul>"
                            "<li><strong>RabbitMQ:</strong> Smart broker/dumb consumer model. Messages are routed, processed, and deleted immediately once consumed. Good for complex routing.</li>"
                            "<li><strong>Apache Kafka:</strong> Distributed log model. Messages are persistent, structured in partitions. Consumers read messages from offsets. High throughput, good for event streaming.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is synchronous vs asynchronous communication in microservices?",
                        "a": "<h4>Sync vs. Async</h4>"
                            "<ul>"
                            "<li><strong>Synchronous:</strong> Caller blocks waiting for response (e.g. HTTP, gRPC). Tight coupling.</li>"
                            "<li><strong>Asynchronous:</strong> Caller sends event message and continues immediately without blocking (e.g. RabbitMQ, Kafka). Loose coupling.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the Circuit Breaker pattern? (Hystrix/Resilience4j)",
                        "a": "<h4>Circuit Breakers</h4>"
                            "Prevents cascading microservice failures. If calls to a downstream service fail repeatedly, the breaker opens, immediately returning default fallback responses without overwhelming the failing service. Transitions: Closed -> Open -> Half-Open."
                    },
                    {
                        "q": "What is an API gateway pattern?",
                        "a": "<h4>API Gateway Pattern</h4>"
                            "Architectural design declaring a reverse proxy gateway routing API queries, ensuring backend services are hidden from public clients."
                    }
                ]
            },
            {
                "head": "Caching & Databases",
                "qs": [
                    {
                        "q": "What is caching? What are the different cache strategies? (write-through, write-behind, cache-aside)",
                        "a": "<h4>Caching Strategies</h4>"
                            "<ul>"
                            "<li><strong>Cache-Aside (Lazy loading):</strong> Application checks cache. If miss, queries DB, saves in cache, returns.</li>"
                            "<li><strong>Write-Through:</strong> Application writes to cache, which writes to DB immediately before returning success.</li>"
                            "<li><strong>Write-Behind (Write-Back):</strong> Application writes to cache, which updates DB asynchronously in batches. Fast writes, but potential data loss risk.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is Redis? What data structures does it support?",
                        "a": "<h4>Redis</h4>"
                            "An in-memory key-value database, cache, and message broker.<br/>"
                            "<em>Structures:</em> Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLogs, Geospatial indexes."
                    },
                    {
                        "q": "What is the difference between SQL and NoSQL databases?",
                        "a": "<h4>SQL vs. NoSQL</h4>"
                            "<table>"
                            "<tr><th>SQL Databases</th><th>NoSQL Databases</th></tr>"
                            "<tr><td>Relational table schemas, structured.</td><td>Schema-less (Key-value, Document, Graph, Column).</td></tr>"
                            "<tr><td>Enforces ACID properties.</td><td>Focuses on scaling and availability (BASE properties).</td></tr>"
                            "<tr><td>Vertical scaling.</td><td>Horizontal scaling.</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "When would you choose NoSQL over SQL?",
                        "a": "<h4>Choosing NoSQL</h4>"
                            "Choose NoSQL when handling massive data volumes, schema layouts change rapidly, high write speeds are needed, or scaling horizontally across distributed nodes is a requirement."
                    },
                    {
                        "q": "What is MongoDB? What is a document in MongoDB?",
                        "a": "<h4>MongoDB</h4>"
                            "A document NoSQL database. A <strong>document</strong> is a JSON-like key-value format (BSON) representing a record (like a table row in SQL but with nested sub-structures)."
                    },
                    {
                        "q": "What is connection pooling and why does it matter?",
                        "a": "<h4>Connection Pooling</h4>"
                            "Keeps database socket connections active for reuse, avoiding expensive TCP connection handshake overhead on every query."
                    }
                ]
            },
            {
                "head": "Security",
                "qs": [
                    {
                        "q": "What is JWT? How does JWT-based authentication flow work?",
                        "a": "<h4>JWT Authentication</h4>"
                            "1. Client logins with credentials.<br/>"
                            "2. Server validates login, signs a JWT token with key secrets, and returns it.<br/>"
                            "3. Client stores token (localStorage/cookie) and attaches it in <code>Authorization</code> headers.<br/>"
                            "4. Server validates signature on every request, extracting user details without database lookups."
                    },
                    {
                        "q": "What is OAuth2? What are the grant types?",
                        "a": "<h4>OAuth2 Grant Types</h4>"
                            "<ul>"
                            "<li><strong>Authorization Code:</strong> Best for web server apps (most secure, uses authorization codes).</li>"
                            "<li><strong>Client Credentials:</strong> Best for machine-to-machine service integration.</li>"
                            "<li><strong>Implicit:</strong> Deprecated legacy flow for SPA web clients.</li>"
                            "<li><strong>Password Credentials:</strong> Deprecated flow exchanging user password directly.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between session-based and token-based authentication?",
                        "a": "<h4>Session vs. Token Auth</h4>"
                            "<ul>"
                            "<li><strong>Session-Based:</strong> Stateful. Server stores session details in memory; client holds session ID in cookie. Hard to scale across distributed nodes.</li>"
                            "<li><strong>Token-Based:</strong> Stateless. Server signs a self-contained token; client holds it. Server needs no session storage, easily scales horizontally.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is HTTPS? How does SSL/TLS handshake work?",
                        "a": "<h4>HTTPS / TLS Handshake</h4>"
                            "Secure HTTP protocol using SSL/TLS encryption. Handshake steps:<br/>"
                            "1. Client Hello (supported cipher lists).<br/>"
                            "2. Server Hello + Certificate validation.<br/>"
                            "3. Key exchange (Client creates pre-master secret key encrypted using Server public key).<br/>"
                            "4. Session keys generated for fast symmetric encryption of data traffic."
                    },
                    {
                        "q": "What is SQL injection? How do you prevent it?",
                        "a": "<h4>SQL Injection Prevention</h4>"
                            "Attack execution where SQL queries are modified via malicious form inputs. Prevent using <strong>Parameterized Queries</strong> (PreparedStatement) and input sanitization."
                    },
                    {
                        "q": "What is XSS and CSRF?",
                        "a": "<h4>Web Vulnerabilities</h4>"
                            "<ul>"
                            "<li><strong>XSS (Cross-Site Scripting):</strong> Malicious script injected into a webpage, executing on client browsers. Prevent using input escaping.</li>"
                            "<li><strong>CSRF (Cross-Site Request Forgery):</strong> Tricking a logged-in user's browser into executing unauthorized actions on a web app. Prevent using CSRF anti-forgery tokens.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "Design Patterns & Principles",
                "qs": [
                    {
                        "q": "What is the Singleton pattern? Thread-safe Singleton?",
                        "a": "<h4>Singleton Pattern</h4>"
                            "Guarantees that a class has only one instance per JVM, providing a global access point.<br/>"
                            "<em>Thread-safe implementation:</em> Double-Checked Locking:<br/>"
                            "<pre>public class Singleton {\n"
                            "  private static volatile Singleton instance;\n"
                            "  private Singleton() {}\n"
                            "  public static Singleton getInstance() {\n"
                            "    if (instance == null) {\n"
                            "      synchronized (Singleton.class) {\n"
                            "        if (instance == null) instance = new Singleton();\n"
                            "      }\n"
                            "    }\n"
                            "    return instance;\n"
                            "  }\n"
                            "}</pre>"
                    },
                    {
                        "q": "What is the Factory pattern?",
                        "a": "<h4>Factory Pattern</h4>"
                            "Creational pattern that abstracts object instantiation logic, returning concrete class instances based on input parameters."
                    },
                    {
                        "q": "What is the Builder pattern? When is it better than telescoping constructors?",
                        "a": "<h4>Builder Pattern</h4>"
                            "Creational pattern used to construct complex objects step-by-step. Better than telescoping constructors because it improves readability, handles optional parameters cleanly, and enforces object immutability."
                    },
                    {
                        "q": "What is the Repository pattern?",
                        "a": "<h4>Repository Pattern</h4>"
                            "Decouples domain business logic from the actual data persistence layer, providing a collection-like interface to access database records."
                    },
                    {
                        "q": "What is the MVC pattern?",
                        "a": "<h4>MVC Pattern</h4>"
                            "Splits UI applications into three distinct roles: Model (data), View (UI), and Controller (routing request dispatcher)."
                    },
                    {
                        "q": "What is the SOLID principle? Explain each letter.",
                        "a": "<h4>SOLID Principles</h4>"
                            "<ul>"
                            "<li><strong>S (Single Responsibility):</strong> A class should have only one reason to change.</li>"
                            "<li><strong>O (Open/Closed):</strong> Open for extension, closed for modification.</li>"
                            "<li><strong>L (Liskov Substitution):</strong> Subclasses must be substitutable for their parent classes.</li>"
                            "<li><strong>I (Interface Segregation):</strong> Avoid fat interfaces; split them into small, specific interfaces.</li>"
                            "<li><strong>D (Dependency Inversion):</strong> Depend on abstractions, not concretions.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the DRY principle?",
                        "a": "<h4>DRY (Don't Repeat Yourself)</h4>"
                            "Every piece of knowledge or logic must have a single, unambiguous, authoritative representation within a system, reducing code duplication."
                    },
                    {
                        "q": "What is the difference between coupling and cohesion?",
                        "a": "<h4>Coupling vs. Cohesion</h4>"
                            "<ul>"
                            "<li><strong>Cohesion:</strong> How closely focused the code/responsibilities inside a single class are. Best: High Cohesion.</li>"
                            "<li><strong>Coupling:</strong> How dependent classes are on each other. Best: Low/Loose Coupling.</li>"
                            "</ul>"
                    }
                ]
            },
            {
                "head": "DevOps & Tools",
                "qs": [
                    {
                        "q": "What is Docker? What is the difference between a container and a VM?",
                        "a": "<h4>Docker vs. Virtual Machines</h4>"
                            "<ul>"
                            "<li><strong>Virtual Machine:</strong> Bundles application, libraries, and a complete Guest OS. Runs on a hypervisor, consuming heavy memory and boot time.</li>"
                            "<li><strong>Docker Container:</strong> Shares host OS kernel, packaging only code and libraries. Extremely lightweight, boots in milliseconds.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a Dockerfile? What is a Docker image vs container?",
                        "a": "<h4>Docker Terminology</h4>"
                            "<ul>"
                            "<li><strong>Dockerfile:</strong> A text script containing commands to build a Docker image.</li>"
                            "<li><strong>Docker Image:</strong> A read-only snapshot template containing libraries and runtime configurations.</li>"
                            "<li><strong>Docker Container:</strong> A runnable active instance of a Docker image.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is CI/CD? Name tools.",
                        "a": "<h4>CI/CD (Continuous Integration / Continuous Delivery)</h4>"
                            "Automates code compilation, testing, and deployment pipelines.<br/>"
                            "<em>Tools:</em> Jenkins, GitHub Actions, GitLab CI, CircleCI."
                    },
                    {
                        "q": "What is Maven? What is a POM file?",
                        "a": "<h4>Maven & POM</h4>"
                            "A project management and build automation tool. The <strong>POM (Project Object Model - pom.xml)</strong> is the XML configuration file declaring dependencies, plug-ins, versions, and build tasks."
                    },
                    {
                        "q": "What are the Maven lifecycle phases?",
                        "a": "<h4>Maven Lifecycle Phases</h4>"
                            "Standard build steps executed sequentially: <code>validate</code> -> <code>compile</code> -> <code>test</code> -> <code>package</code> -> <code>verify</code> -> <code>install</code> -> <code>deploy</code>."
                    },
                    {
                        "q": "What is Git? What is the difference between git merge and git rebase?",
                        "a": "<h4>Git Branching Methods</h4>"
                            "<ul>"
                            "<li><strong>git merge:</strong> Joins branch histories, creating a merge commit. Preserves exact history.</li>"
                            "<li><strong>git rebase:</strong> Moves branch commits on top of another base, creating a flat linear commit history. Avoids merge commits, but rewrites history.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a webhook?",
                        "a": "<h4>Webhooks</h4>"
                            "An HTTP POST callback notification sent automatically by source systems to a target URL when events occur (e.g. notifications sent to Slack when build completes)."
                    },
                    {
                        "q": "What is the difference between vertical scaling and horizontal scaling?",
                        "a": "<h4>Scaling Strategies</h4>"
                            "<ul>"
                            "<li><strong>Vertical Scaling (Scale-up):</strong> Adding more resources (CPU/RAM) to a single database/server node. Has physical limits.</li>"
                            "<li><strong>Horizontal Scaling (Scale-out):</strong> Adding more server nodes to cluster networks. Highly scalable.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is an idempotent operation in backend design?",
                        "a": "<h4>Backend Idempotency</h4>"
                            "Design ensuring API requests can fail and retry safely (e.g. charge requests) without executing actions twice."
                    }
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 5:
            idx = i
            break
    if idx != -1:
        db[idx] = backend_module
    else:
        db.append(backend_module)
        
    save_db(db)
    print("Backend data populated successfully.")

if __name__ == '__main__':
    main()
