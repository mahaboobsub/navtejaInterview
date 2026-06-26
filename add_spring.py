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
    
    spring_module = {
        "id": 4,
        "name": "Spring Core",
        "short": "Spring",
        "color": "c-blue",
        "count": 55,
        "subs": [
            {
                "head": "IoC & DI Fundamentals",
                "qs": [
                    {
                        "q": "What is the Spring Framework and what are its core modules?",
                        "a": "<h4>Spring Framework</h4>"
                            "An open-source enterprise Java framework providing comprehensive infrastructure support.<br/>"
                            "<em>Core modules:</em> Spring Core (IoC, DI), Spring AOP (aspects), Spring JDBC/ORM (data access), Spring Web (MVC, REST), and Spring Test."
                    },
                    {
                        "q": "What is Inversion of Control (IoC)?",
                        "a": "<h4>Inversion of Control (IoC)</h4>"
                            "A design principle in which control over object creation, configuration, and lifecycles is transferred from the program code to an external container or framework (the Spring IoC container)."
                    },
                    {
                        "q": "What is Dependency Injection (DI)? What problem does it solve?",
                        "a": "<h4>Dependency Injection (DI)</h4>"
                            "A design pattern executing IoC. Objects do not instantiate their dependencies directly; instead, dependencies are supplied/injected by the container (e.g. constructor/setter).<br/>"
                            "<strong>Problems solved:</strong> Decouples classes, simplifies unit testing (allows mock injections), and increases code reusability."
                    },
                    {
                        "q": "What are the types of Dependency Injection in Spring?",
                        "a": "<h4>Types of DI</h4>"
                            "1. <strong>Constructor Injection:</strong> Dependencies are passed via class constructor.<br/>"
                            "2. <strong>Setter Injection:</strong> Dependencies are passed via public setter methods.<br/>"
                            "3. <strong>Field Injection:</strong> Dependencies are injected directly into class attributes using reflection (annotated with <code>@Autowired</code>)."
                    },
                    {
                        "q": "What is the difference between constructor injection and setter injection? When to prefer each?",
                        "a": "<h4>Constructor vs. Setter Injection</h4>"
                            "<ul>"
                            "<li><strong>Constructor Injection:</strong> Best for mandatory dependencies. Guarantees object immutability, prevents null-pointer risks, and simplifies unit tests. Highly recommended.</li>"
                            "<li><strong>Setter Injection:</strong> Best for optional or mutable dependencies. Allows changing dependencies dynamically later.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the Spring IoC container?",
                        "a": "<h4>Spring IoC Container</h4>"
                            "The core manager of the Spring framework. It instantiates, configures, wires, and manages the entire lifecycle of application objects (Spring Beans)."
                    },
                    {
                        "q": "What is the difference between BeanFactory and ApplicationContext?",
                        "a": "<h4>BeanFactory vs. ApplicationContext</h4>"
                            "<table>"
                            "<tr><th>BeanFactory</th><th>ApplicationContext</th></tr>"
                            "<tr><td>Basic IoC container.</td><td>Advanced enterprise-level IoC container.</td></tr>"
                            "<tr><td>Loads beans lazily (on demand).</td><td>Pre-instantiates singleton beans at startup (eager).</td></tr>"
                            "<tr><td>Minimal resources, good for lightweight devices.</td><td>Adds internationalization (i18n), AOP integration, and application event listeners.</td></tr>"
                            "</table>"
                    }
                ]
            },
            {
                "head": "Bean Lifecycle & Scopes",
                "qs": [
                    {
                        "q": "What is a Spring Bean?",
                        "a": "<h4>Spring Beans</h4>"
                            "Objects instantiated, managed, and wired together by the Spring IoC container."
                    },
                    {
                        "q": "What is the complete Spring Bean lifecycle?",
                        "a": "<h4>Bean Lifecycle Steps</h4>"
                            "1. Instantiate Class<br/>"
                            "2. Populate properties (Dependency Injection)<br/>"
                            "3. Call aware interfaces (e.g. BeanNameAware)<br/>"
                            "4. BeanPostProcessor pre-initialization (<code>postProcessBeforeInitialization</code>)<br/>"
                            "5. Custom Initialization (<code>@PostConstruct</code>, <code>afterPropertiesSet</code>, custom init-method)<br/>"
                            "6. BeanPostProcessor post-initialization (<code>postProcessAfterInitialization</code>)<br/>"
                            "7. Bean is ready for use<br/>"
                            "8. Destruction (<code>@PreDestroy</code>, <code>destroy()</code>, custom destroy-method)"
                    },
                    {
                        "q": "What is init-method and destroy-method in Spring?",
                        "a": "<h4>init-method and destroy-method</h4>"
                            "Declarative initialization and cleanup hooks configured inside bean metadata:<br/>"
                            "<pre>@Bean(initMethod = \"setup\", destroyMethod = \"cleanup\")</pre>"
                    },
                    {
                        "q": "What are @PostConstruct and @PreDestroy?",
                        "a": "<h4>Lifecycle Annotations</h4>"
                            "<ul>"
                            "<li><strong><code>@PostConstruct</code>:</strong> Applied to methods to execute custom initialization code after dependency injections complete.</li>"
                            "<li><strong><code>@PreDestroy</code>:</strong> Applied to methods to execute cleanup before the bean is destroyed inside context.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are the bean scopes in Spring? (singleton, prototype, request, session, application)",
                        "a": "<h4>Bean Scopes</h4>"
                            "<ul>"
                            "<li><strong>singleton (default):</strong> Only one shared instance created per IoC container.</li>"
                            "<li><strong>prototype:</strong> Creates a new bean instance every time it is requested.</li>"
                            "<li><strong>request:</strong> Creates one instance per HTTP request lifecycle (web apps).</li>"
                            "<li><strong>session:</strong> Creates one instance per HTTP session lifecycle (web apps).</li>"
                            "<li><strong>application:</strong> Shared global instance per ServletContext.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between singleton and prototype scope in detail?",
                        "a": "<h4>Singleton vs. Prototype</h4>"
                            "<ul>"
                            "<li><strong>Singleton:</strong> Cached in memory, shared across all injections. Container controls entire lifecycle.</li>"
                            "<li><strong>Prototype:</strong> Instantiated on demand. Container injects dependencies but hands control to client (destruction lifecycle hooks are not called automatically).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is bean wiring?",
                        "a": "<h4>Bean Wiring</h4>"
                            "The process of injecting dependencies and linking bean references within the IoC container (can be configured via XML, Java Config, or Autowired annotations)."
                    }
                ]
            },
            {
                "head": "Annotations",
                "qs": [
                    {
                        "q": "What is @Component? How is it different from @Bean?",
                        "a": "<h4>@Component vs. @Bean</h4>"
                            "<ul>"
                            "<li><strong><code>@Component</code>:</strong> Class-level annotation. Spring automatically detects and registers classes using component scanning. Used for classes you write.</li>"
                            "<li><strong><code>@Bean</code>:</strong> Method-level annotation inside <code>@Configuration</code> classes. Tells Spring to register the returned object instance as a bean. Used for third-party libraries.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between @Component, @Service, @Repository, and @Controller?",
                        "a": "<h4>Component Specializations</h4>"
                            "They are structural stereotypes for auto-detection:<br/>"
                            "<ul>"
                            "<li><code>@Component</code>: Generic component flag.</li>"
                            "<li><code>@Service</code>: Indicates business service logic.</li>"
                            "<li><code>@Repository</code>: Indicates DAO database persistence layer. Translates database exceptions automatically.</li>"
                            "<li><code>@Controller</code>: Indicates MVC UI request handler.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @Autowired? Where can it be applied?",
                        "a": "<h4>@Autowired</h4>"
                            "Instructs Spring to perform automatic dependency injection. Can be applied to constructors, setter methods, or fields."
                    },
                    {
                        "q": "What is @Qualifier? When do you need it?",
                        "a": "<h4>@Qualifier</h4>"
                            "Used when multiple beans of the same class type exist in the container. Helps target a specific bean to resolve injection ambiguity:<br/>"
                            "<pre>@Autowired\n@Qualifier(\"sqlEngine\")\nprivate Engine engine;</pre>"
                    },
                    {
                        "q": "What is @Primary?",
                        "a": "<h4>@Primary</h4>"
                            "Gives default priority to a specific bean when multiple implementation candidates exist for injection."
                    },
                    {
                        "q": "What is @Value? How do you inject a property from application.properties?",
                        "a": "<h4>@Value Property Injection</h4>"
                            "Injects configuration properties directly into bean fields:<br/>"
                            "<pre>@Value(\"${server.port}\")\nprivate int port;</pre>"
                    },
                    {
                        "q": "What is @Configuration?",
                        "a": "<h4>@Configuration</h4>"
                            "Registers a class as a source of bean definitions containing <code>@Bean</code> methods."
                    },
                    {
                        "q": "What is @ComponentScan?",
                        "a": "<h4>@ComponentScan</h4>"
                            "Tells Spring to scan packages for classes annotated with stereotypes (Component, Service, etc.) and register them in the context."
                    },
                    {
                        "q": "What is the difference between @Autowired and @Inject?",
                        "a": "<h4>@Autowired vs. @Inject</h4>"
                            "<ul>"
                            "<li><code>@Autowired</code>: Spring-specific annotation.</li>"
                            "<li><code>@Inject</code>: Standard Java CDI annotation (JSR-330). Requires additional dependencies.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @Lazy?",
                        "a": "<h4>@Lazy</h4>"
                            "Instructs the container to initialize a bean only when requested, rather than eagerly at startup."
                    }
                ]
            },
            {
                "head": "AOP",
                "qs": [
                    {
                        "q": "What is Aspect-Oriented Programming (AOP)?",
                        "a": "<h4>Aspect-Oriented Programming (AOP)</h4>"
                            "A programming paradigm that complements OOP by isolating cross-cutting concerns (e.g. logging, transactions, security) from business logic using modular structures called Aspects."
                    },
                    {
                        "q": "What is an Aspect, Advice, Pointcut, and JoinPoint?",
                        "a": "<h4>AOP Terminology</h4>"
                            "<ul>"
                            "<li><strong>Aspect:</strong> Module containing cross-cutting logic.</li>"
                            "<li><strong>JoinPoint:</strong> Any candidate location in code (e.g., method execution) where advice can be applied.</li>"
                            "<li><strong>Advice:</strong> Action logic to run at a JoinPoint (e.g. log before execution).</li>"
                            "<li><strong>Pointcut:</strong> Expression targeting specific JoinPoints to execute Advice.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are the types of Advice in Spring AOP?",
                        "a": "<h4>AOP Advice Types</h4>"
                            "Defined using annotations: <code>@Before</code>, <code>@After</code>, <code>@AfterReturning</code>, <code>@AfterThrowing</code>, <code>@Around</code>."
                    },
                    {
                        "q": "What is the @Before, @After, @AfterReturning, @AfterThrowing, and @Around advice?",
                        "a": "<h4>Advice Annotations</h4>"
                            "<ul>"
                            "<li><code>@Before</code>: Executes before method starts.</li>"
                            "<li><code>@After</code>: Executes after method completes (regardless of outcome).</li>"
                            "<li><code>@AfterReturning</code>: Executes only after successful method execution.</li>"
                            "<li><code>@AfterThrowing</code>: Executes only if method throws exceptions.</li>"
                            "<li><code>@Around</code>: Wraps method execution, managing parameters, returns, and execution control.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between Spring AOP and AspectJ AOP?",
                        "a": "<h4>Spring AOP vs. AspectJ</h4>"
                            "<ul>"
                            "<li><strong>Spring AOP:</strong> Proxy-based, runtime compilation. Only supports method-execution joinpoints. Lightweight.</li>"
                            "<li><strong>AspectJ:</strong> Compiler/weaver-based, compile/post-compile weaving. Supports field access, constructor, and method execution. Heavyweight, high performance.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a proxy in Spring AOP? (JDK dynamic vs CGLIB)",
                        "a": "<h4>Spring AOP Proxies</h4>"
                            "Spring wraps classes inside proxy objects to apply aspects.<br/>"
                            "<ul>"
                            "<li><strong>JDK Dynamic Proxy:</strong> Default for classes implementing interfaces. Uses Java reflection APIs.</li>"
                            "<li><strong>CGLIB Proxy:</strong> Used if a class doesn't implement interfaces. Generates subclass definitions dynamically.</li>"
                            "</ul>"
                    },
                    {
                        "q": "Give a real use case where AOP is useful (logging, security, transactions).",
                        "a": "<h4>AOP Use Cases</h4>"
                            "<em>Example:</em> Declarative Transaction management (<code>@Transactional</code>). The transaction aspect opens a transaction before method start, commits on success, and rolls back on exception automatically, keeping code clean."
                    }
                ]
            },
            {
                "head": "Spring MVC",
                "qs": [
                    {
                        "q": "What is Spring MVC? What is the DispatcherServlet?",
                        "a": "<h4>Spring MVC</h4>"
                            "Model-View-Controller framework built around a central front controller servlet, the <code>DispatcherServlet</code>, which coordinates incoming request routing and response rendering."
                    },
                    {
                        "q": "What is the request flow in Spring MVC?",
                        "a": "<h4>Request Handling Flow</h4>"
                            "1. Client sends request to <code>DispatcherServlet</code>.<br/>"
                            "2. DispatcherServlet consults <code>HandlerMapping</code> to find target Controller.<br/>"
                            "3. Controller processes request, returning a <code>ModelAndView</code> object.<br/>"
                            "4. DispatcherServlet consults <code>ViewResolver</code> to locate actual View file.<br/>"
                            "5. DispatcherServlet dispatches data to View for rendering, returning output to Client."
                    },
                    {
                        "q": "What is @RequestMapping? What are its attributes?",
                        "a": "<h4>@RequestMapping</h4>"
                            "Maps URL paths to controller classes or methods.<br/>"
                            "<em>Attributes:</em> <code>value</code> (path), <code>method</code> (GET/POST), <code>headers</code>, <code>params</code>, <code>produces</code>/<code>consumes</code>."
                    },
                    {
                        "q": "What is the difference between @GetMapping/@PostMapping and @RequestMapping?",
                        "a": "<h4>GET/POST Annotations</h4>"
                            "<code>@GetMapping</code> and <code>@PostMapping</code> are specialized shortcut annotations representing <code>@RequestMapping(method = RequestMethod.GET)</code> etc."
                    },
                    {
                        "q": "What is @PathVariable vs @RequestParam?",
                        "a": "<h4>Path vs Query Parameters</h4>"
                            "<ul>"
                            "<li><strong><code>@PathVariable</code>:</strong> Extracts variables embedded directly in URL path segment: <code>/users/{id}</code>.</li>"
                            "<li><strong><code>@RequestParam</code>:</strong> Extracts standard HTTP query parameters: <code>/users?id=123</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @RequestBody and @ResponseBody?",
                        "a": "<h4>Body Mapping</h4>"
                            "<ul>"
                            "<li><strong><code>@RequestBody</code>:</strong> Deserializes incoming HTTP request body JSON into a Java object.</li>"
                            "<li><strong><code>@ResponseBody</code>:</strong> Serializes Java return objects into HTTP response JSON.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between @RestController and @Controller?",
                        "a": "<h4>@Controller vs. @RestController</h4>"
                            "<ul>"
                            "<li><strong>@Controller:</strong> Used to return traditional Views (HTML pages).</li>"
                            "<li><strong>@RestController:</strong> Groups <code>@Controller</code> and <code>@ResponseBody</code>. Returns serialized data models (JSON/XML) directly. Best for REST APIs.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is ModelAndView?",
                        "a": "<h4>ModelAndView</h4>"
                            "A container wrapping both target View name strings and data model attributes returned by controller methods."
                    },
                    {
                        "q": "What is a ViewResolver?",
                        "a": "<h4>ViewResolver</h4>"
                            "A component that translates abstract view names returned by controllers (e.g. \"home\") into physical view paths (e.g. \"/WEB-INF/views/home.jsp\")."
                    },
                    {
                        "q": "What is @ExceptionHandler and @ControllerAdvice?",
                        "a": "<h4>Global Exception Handling</h4>"
                            "<ul>"
                            "<li><strong><code>@ExceptionHandler</code>:</strong> Declares an exception handling method inside a specific controller.</li>"
                            "<li><strong><code>@ControllerAdvice</code>:</strong> Declares a global exception handler intercepting errors across all controllers.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @ResponseStatus?",
                        "a": "<h4>@ResponseStatus</h4>"
                            "Binds an explicit HTTP status code (e.g. <code>HttpStatus.NOT_FOUND</code>) to a controller method or custom exception class."
                    }
                ]
            },
            {
                "head": "Spring Data & Transactions",
                "qs": [
                    {
                        "q": "What is Spring Data JPA?",
                        "a": "<h4>Spring Data JPA</h4>"
                            "Abstraction framework eliminating standard JPA repository boilerplate code using interfaces that auto-generate database operations."
                    },
                    {
                        "q": "What is JpaRepository? What methods does it provide?",
                        "a": "<h4>JpaRepository</h4>"
                            "Interface providing CRUD, sorting, and pagination methods (e.g. <code>save()</code>, <code>findAll()</code>, <code>deleteById()</code>)."
                    },
                    {
                        "q": "What are derived query methods in Spring Data JPA?",
                        "a": "<h4>Derived Query Methods</h4>"
                            "Database queries compiled automatically from interface method names: <code>findByEmailAddress(String email)</code> translates into SQL WHERE clauses."
                    },
                    {
                        "q": "What is @Transactional? What is transaction propagation?",
                        "a": "<h4>@Transactional & Propagation</h4>"
                            "Defines declarative transactional boundaries on classes or methods. <strong>Propagation</strong> defines transaction boundaries behavior if a method is called inside an existing transaction."
                    },
                    {
                        "q": "What are the propagation types? (REQUIRED, REQUIRES_NEW, NESTED, etc.)",
                        "a": "<h4>Propagation Types</h4>"
                            "<ul>"
                            "<li><strong>REQUIRED (default):</strong> Joins existing transaction or creates a new one.</li>"
                            "<li><strong>REQUIRES_NEW:</strong> Always creates a new transaction, suspending any active ones.</li>"
                            "<li><strong>NESTED:</strong> Executes inside a nested transaction using savepoints.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is rollbackFor in @Transactional?",
                        "a": "<h4>rollbackFor</h4>"
                            "Configures transactional rollbacks for specific checked exceptions. By default, Spring only rolls back transactions for unchecked/runtime exceptions."
                    },
                    {
                        "q": "What is the difference between @Transactional on a class vs method?",
                        "a": "<h4>Transactional Scope</h4>"
                            "Applying to a class makes all its public methods transactional, while applying to a method restricts transactional boundaries to that specific method only."
                    }
                ]
            },
            {
                "head": "Spring Boot",
                "qs": [
                    {
                        "q": "What is Spring Boot? How is it different from Spring Framework?",
                        "a": "<h4>Spring Boot vs. Spring Framework</h4>"
                            "<ul>"
                            "<li><strong>Spring Framework:</strong> Lightweight dependency core requiring extensive XML or Java configs, web setups, and deployment descriptors.</li>"
                            "<li><strong>Spring Boot:</strong> Extension of Spring providing pre-configured starters, auto-configurations, and embedded servers to build production-ready applications instantly.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is auto-configuration in Spring Boot?",
                        "a": "<h4>Auto-Configuration</h4>"
                            "A mechanism where Spring Boot automatically configures beans based on JAR libraries found in the classpath (e.g. auto-configures DataSource beans if MySQL connector is present)."
                    },
                    {
                        "q": "What is a Spring Boot starter?",
                        "a": "<h4>Starters</h4>"
                            "Dependency descriptors grouping common libraries together under a single entry (e.g., <code>spring-boot-starter-web</code> includes Tomcat, Spring Web, and JSON mapping packages)."
                    },
                    {
                        "q": "What is @SpringBootApplication? What annotations does it combine?",
                        "a": "<h4>@SpringBootApplication</h4>"
                            "The bootstrap entry point annotation. Combines three annotations:<br/>"
                            "1. <code>@SpringBootConfiguration</code><br/>"
                            "2. <code>@EnableAutoConfiguration</code><br/>"
                            "3. <code>@ComponentScan</code>"
                    },
                    {
                        "q": "What is the embedded server in Spring Boot? How does it work?",
                        "a": "<h4>Embedded Server</h4>"
                            "Bundles the application container (Apache Tomcat/Jetty) inside the executable JAR. Eliminates the need to deploy WAR files to external application servers."
                    },
                    {
                        "q": "What is application.properties vs application.yml?",
                        "a": "<h4>Configuration Formats</h4>"
                            "<ul>"
                            "<li><strong>properties:</strong> Flat key-value format (<code>server.port=8080</code>).</li>"
                            "<li><strong>yml:</strong> Hierarchical, nested structure using indentation (more readable for large configurations).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the Spring Boot actuator?",
                        "a": "<h4>Actuator</h4>"
                            "A library providing production-ready monitoring endpoints to check app health, metrics, configurations, thread dumps, and logs."
                    },
                    {
                        "q": "What is CommandLineRunner?",
                        "a": "<h4>CommandLineRunner</h4>"
                            "Interface whose <code>run()</code> method executes automatically once the Spring Boot application starts up."
                    }
                ]
            },
            {
                "head": "Security",
                "qs": [
                    {
                        "q": "What is Spring Security basics?",
                        "a": "<h4>Spring Security</h4>"
                            "A customizable authentication and access-control framework protecting Spring applications."
                    },
                    {
                        "q": "What is the difference between authentication and authorization?",
                        "a": "<h4>Authentication vs. Authorization</h4>"
                            "<ul>"
                            "<li><strong>Authentication:</strong> Verifying user identity (Who are you?).</li>"
                            "<li><strong>Authorization:</strong> Verifying resource permissions (What are you allowed to do?).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a security filter chain in Spring Security?",
                        "a": "<h4>Security Filter Chain</h4>"
                            "A chain of filter components that intercept requests to parse credentials, verify security tokens, evaluate URL rules, and authenticate endpoints."
                    },
                    {
                        "q": "What is JWT? How does the token flow work?",
                        "a": "<h4>JWT (JSON Web Token)</h4>"
                            "A secure, stateless JSON token signed cryptographically. The client logs in, receives a token, and includes it in the <code>Authorization: Bearer <token></code> header of subsequent requests. The server validates the token signature without database queries."
                    },
                    {
                        "q": "What is Basic Auth vs Token Auth?",
                        "a": "<h4>Basic vs. Token Auth</h4>"
                            "<ul>"
                            "<li><strong>Basic Auth:</strong> Sends base64-encoded username/password in headers of every request. Stateless, but credentials are exposed.</li>"
                            "<li><strong>Token Auth:</strong> Sends a temporary cryptographically secure key token instead of credentials.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is @PreAuthorize?",
                        "a": "<h4>@PreAuthorize</h4>"
                            "A method-level annotation enforcing security rules using SpEL expressions before the method executes:<br/>"
                            "<pre>@PreAuthorize(\"hasRole('ADMIN')\")</pre>"
                    },
                    {
                        "q": "What is OAuth2 at a conceptual level?",
                        "a": "<h4>OAuth2</h4>"
                            "An industry-standard authorization framework enabling third-party applications to obtain limited access to user resources using token exchanges without exposing user passwords."
                    }
                ]
            }
        ]
    }
    
    # Check if exists, replace or append
    idx = -1
    for i, m in enumerate(db):
        if m['id'] == 4:
            idx = i
            break
    if idx != -1:
        db[idx] = spring_module
    else:
        db.append(spring_module)
        
    save_db(db)
    print("Spring Core data populated successfully.")

if __name__ == '__main__':
    main()
