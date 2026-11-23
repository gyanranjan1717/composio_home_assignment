"""Curated documentation facts and evidence for Apps 61-100."""

apps_61_100 = {
    # 7. Developer, Infra and Data platforms (61-70)
    61: {
        "id": 61, "name": "GitHub", "category": "Developer, Infra and Data platforms",
        "one_liner": "Cloud Git repository hosting, code collaboration, CI/CD (Actions), and developer platform.",
        "auth_methods": ["Bearer/token", "OAuth2", "Basic"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Personal Access Tokens (classic & fine-grained) can be created instantly for free in Developer Settings.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/github"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "GitHub REST API supports Bearer token authentication.", "url": "https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api", "quote": "Authenticate to GitHub using personal access tokens: Authorization: Bearer <TOKEN> or Authorization: token <TOKEN>."},
            {"claim": "Official GitHub MCP server is available.", "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/github", "quote": "GitHub Model Context Protocol server enabling LLMs to interact with repositories, issues, and pull requests."}
        ],
        "confidence": "high", "notes": "One of the most widely used developer toolkits.", "needs_human": False, "human_reason": None
    },
    62: {
        "id": 62, "name": "Vercel", "category": "Developer, Infra and Data platforms",
        "one_liner": "Frontend cloud platform for developing, previewing, and deploying web applications.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free hobby tier allows instant creation of personal access tokens in Account Settings > Tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/vercel"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Vercel REST API authenticates using Bearer access tokens.", "url": "https://vercel.com/docs/rest-api#authentication", "quote": "All API endpoints require authentication using a Bearer token in the Authorization header."},
            {"claim": "Personal tokens can be generated in Account Settings.", "url": "https://vercel.com/account/tokens", "quote": "Create personal access tokens with custom expiration and scope."}
        ],
        "confidence": "high", "notes": "Clean REST API for deployments and project management.", "needs_human": False, "human_reason": None
    },
    63: {
        "id": 63, "name": "Netlify", "category": "Developer, Infra and Data platforms",
        "one_liner": "Serverless cloud platform for building, deploying, and scaling modern web apps.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Starter plan allows creating personal access tokens directly under User Settings > Applications.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Netlify API uses Bearer token authentication.", "url": "https://docs.netlify.com/api/get-started/#authentication", "quote": "You can authenticate with the Netlify API by passing your personal access token: Authorization: Bearer <token>."},
            {"claim": "Tokens can be created in user settings.", "url": "https://app.netlify.com/user/applications#personal-access-tokens", "quote": "Generate a new personal access token to use with the Netlify API or CLI."}
        ],
        "confidence": "high", "notes": "Full OpenAPI specification available.", "needs_human": False, "human_reason": None
    },
    64: {
        "id": 64, "name": "Cloudflare", "category": "Developer, Infra and Data platforms",
        "one_liner": "Global cloud network providing CDN, DDoS protection, DNS, Workers, and edge computing.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes instant API Token creation with granular permissions in My Profile > API Tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://github.com/cloudflare/mcp-server-cloudflare"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Cloudflare API uses API Tokens with Bearer authentication.", "url": "https://developers.cloudflare.com/fundamentals/api/get-started/create-token/", "quote": "API tokens allow scoped access: Authorization: Bearer <API_TOKEN>."},
            {"claim": "Official Cloudflare MCP server is maintained by Cloudflare.", "url": "https://github.com/cloudflare/mcp-server-cloudflare", "quote": "Official Cloudflare MCP Server implementation to interact with Cloudflare resources."}
        ],
        "confidence": "high", "notes": "Official MCP server available.", "needs_human": False, "human_reason": None
    },
    65: {
        "id": 65, "name": "Supabase", "category": "Developer, Infra and Data platforms",
        "one_liner": "Open-source Firebase alternative providing Postgres database, Auth, Edge Functions, and Realtime.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier includes 2 free projects, instant Management API tokens and public/service_role API keys.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/supabase/mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Supabase Management API uses Bearer personal access tokens.", "url": "https://supabase.com/docs/reference/api/introduction", "quote": "All management API requests require a Bearer token in the Authorization header: Authorization: Bearer sbp_..."},
            {"claim": "Personal access tokens are self-serve in Account Settings.", "url": "https://supabase.com/dashboard/account/tokens", "quote": "Generate personal access tokens to interact with the Supabase Management API."}
        ],
        "confidence": "high", "notes": "PostgREST and Management API both available.", "needs_human": False, "human_reason": None
    },
    66: {
        "id": 66, "name": "Neo4j", "category": "Developer, Infra and Data platforms",
        "one_liner": "Graph database management system offering native graph storage and Cypher query language.",
        "auth_methods": ["Basic", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Neo4j AuraDB Free tier provides an instant cloud graph instance with basic credentials and HTTP Query API.",
        "api_surface": {"type": "REST / SDK", "breadth": "medium", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/neo4j-contrib/mcp-neo4j"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Neo4j Query API and Aura API use HTTP Basic or Bearer authentication.", "url": "https://neo4j.com/docs/aura/platform/api/authentication/", "quote": "Authenticate to the Aura API using Bearer tokens or Basic authentication with username and password for Cypher transactions."},
            {"claim": "Free instance available with Neo4j Aura Free.", "url": "https://neo4j.com/cloud/platform/aura-graph-database/", "quote": "Get started for free with Neo4j AuraDB Free without entering a credit card."}
        ],
        "confidence": "high", "notes": "Bolt protocol or HTTP query API.", "needs_human": False, "human_reason": None
    },
    67: {
        "id": 67, "name": "Snowflake", "category": "Developer, Infra and Data platforms",
        "one_liner": "Cloud data platform offering data warehousing, data lakes, and SQL analytics.",
        "auth_methods": ["JWT", "OAuth2", "Basic"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "30-day free trial ($400 credits) allows creating key-pair authentication for SQL API access.",
        "api_surface": {"type": "REST / SQL", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/snowflake"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Snowflake SQL API authenticates using Key-Pair JWT tokens or OAuth 2.0.", "url": "https://docs.snowflake.com/en/developer-guide/sql-api/authenticating", "quote": "To authenticate with the SQL API, use a JWT generated using key-pair authentication: Authorization: Bearer <jwt_token>."},
            {"claim": "Free trial provides full SQL API capability.", "url": "https://signup.snowflake.com/", "quote": "Sign up for a 30-day free trial with $400 worth of free usage."}
        ],
        "confidence": "high", "notes": "Snowflake SQL API enables stateless HTTP execution.", "needs_human": False, "human_reason": None
    },
    68: {
        "id": 68, "name": "MongoDB Atlas", "category": "Developer, Infra and Data platforms",
        "one_liner": "Fully managed cloud document database service with Atlas Admin and Data APIs.",
        "auth_methods": ["Basic", "API key", "other"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free M0 cluster tier available forever; Atlas Administration API keys generated under Project Access Manager.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/mongodb/mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "MongoDB Atlas Administration API authenticates using HTTP Digest authentication with API Keys.", "url": "https://www.mongodb.com/docs/atlas/api/overview/#authentication", "quote": "Atlas Administration API requires HTTP Digest Authentication using your public and private API keys."},
            {"claim": "Free shared M0 clusters are available indefinitely.", "url": "https://www.mongodb.com/pricing", "quote": "Deploy a free M0 cluster with 512 MB storage and shared RAM."}
        ],
        "confidence": "high", "notes": "Uses Digest auth for Admin API.", "needs_human": False, "human_reason": None
    },
    69: {
        "id": 69, "name": "Datadog", "category": "Developer, Infra and Data platforms",
        "one_liner": "Cloud monitoring and observability service for metrics, traces, and infrastructure logs.",
        "auth_methods": ["API key", "Bearer/token"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "14-day free trial provides API Key and Application Key access in Organization Settings.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Datadog API requires DD-API-KEY and DD-APPLICATION-KEY headers.", "url": "https://docs.datadoghq.com/api/latest/authentication/", "quote": "All endpoints require authentication using your Datadog API key and Application key passed in request headers: DD-API-KEY and DD-APPLICATION-KEY."},
            {"claim": "Keys can be generated in Organization Settings.", "url": "https://app.datadoghq.com/organization-settings/api-keys", "quote": "Manage your API and application keys in Organization Settings."}
        ],
        "confidence": "high", "notes": "Dual-key header pattern.", "needs_human": False, "human_reason": None
    },
    70: {
        "id": 70, "name": "Sentry", "category": "Developer, Infra and Data platforms",
        "one_liner": "Application performance monitoring and error tracking platform for software teams.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Developer free tier includes 5,000 errors/month and self-serve Auth Tokens in User Settings > API.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/getsentry/sentry-mcp"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Sentry Web API authenticates using Bearer auth tokens.", "url": "https://docs.sentry.io/api/auth/", "quote": "Pass your user auth token or internal integration token in the Authorization header: Authorization: Bearer <TOKEN>."},
            {"claim": "Auth tokens can be generated under user API settings.", "url": "https://sentry.io/settings/account/api/auth-tokens/", "quote": "Generate user auth tokens with granular scopes to query issues and events."}
        ],
        "confidence": "high", "notes": "Rich error search API.", "needs_human": False, "human_reason": None
    },

    # 8. Productivity and Project Management (71-80)
    71: {
        "id": 71, "name": "Notion", "category": "Productivity and Project Management",
        "one_liner": "Connected workspace for notes, wiki documentation, databases, and project management.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account enables instant Internal Integration token generation on developers.notion.com.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/notion"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Notion API uses Bearer authentication with internal or OAuth tokens.", "url": "https://developers.notion.com/docs/authorization", "quote": "All requests must include an Authorization header with a Bearer token: Authorization: Bearer secret_... and a Notion-Version header."},
            {"claim": "Internal integrations are free to create immediately.", "url": "https://www.notion.so/profile/integrations", "quote": "Create an internal integration secret to access workspace pages and databases."}
        ],
        "confidence": "high", "notes": "Requires Notion-Version header.", "needs_human": False, "human_reason": None
    },
    72: {
        "id": 72, "name": "Airtable", "category": "Productivity and Project Management",
        "one_liner": "Low-code cloud platform for building relational databases, workflows, and collaborative apps.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier includes instant Personal Access Token (PAT) creation with scoped base permissions.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/airtable"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Airtable Web API authenticates using Personal Access Tokens via Bearer header.", "url": "https://airtable.com/developers/web/api/authentication", "quote": "All API requests should include your Personal Access Token in the Authorization header: Authorization: Bearer pat..."},
            {"claim": "Personal access tokens can be created in the builder hub.", "url": "https://airtable.com/create/tokens", "quote": "Create and manage personal access tokens with specific scopes and base access."}
        ],
        "confidence": "high", "notes": "Legacy API keys were sunset in Feb 2024; PATs are now standard.", "needs_human": False, "human_reason": None
    },
    73: {
        "id": 73, "name": "Linear", "category": "Productivity and Project Management",
        "one_liner": "Purpose-built issue tracking and software project management tool for engineering teams.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier provides personal API keys created in Account Settings > Security & Access.",
        "api_surface": {"type": "GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/jerhadf/linear-mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Linear API is a GraphQL API authenticated via Personal API Key or OAuth 2.0.", "url": "https://developers.linear.app/docs/graphql/working-with-the-graphql-api", "quote": "The Linear API is built around GraphQL. Pass your personal API key directly in the Authorization header: Authorization: <API_KEY>."},
            {"claim": "Personal API keys can be created directly in profile settings.", "url": "https://linear.app/settings/api", "quote": "Create personal API keys for scripts and command-line tools."}
        ],
        "confidence": "high", "notes": "Modern GraphQL API.", "needs_human": False, "human_reason": None
    },
    74: {
        "id": 74, "name": "Jira", "category": "Productivity and Project Management",
        "one_liner": "Enterprise issue and project tracking software by Atlassian for agile teams.",
        "auth_methods": ["Basic", "OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier (up to 10 users) and free Atlassian developer cloud site with instant API token generation.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/jira"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Jira Cloud REST API authenticates using HTTP Basic auth with API tokens or OAuth 2.0 (3LO).", "url": "https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/", "quote": "Use your email address and API token as the basic auth credentials: Authorization: Basic base64(email:api_token)."},
            {"claim": "API tokens can be created in Atlassian account profile.", "url": "https://id.atlassian.com/manage-profile/security/api-tokens", "quote": "Create an API token to use with your Atlassian Cloud apps and scripts."}
        ],
        "confidence": "high", "notes": "Ubiquitous in enterprise software teams.", "needs_human": False, "human_reason": None
    },
    75: {
        "id": 75, "name": "Asana", "category": "Productivity and Project Management",
        "one_liner": "Work management and team project tracking platform for task coordination.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Personal access tokens can be created instantly for free in Developer App Console.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/asana"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Asana API supports Bearer Personal Access Tokens (PAT) and OAuth 2.0.", "url": "https://developers.asana.com/docs/personal-access-token", "quote": "Pass your personal access token in the Authorization header: Authorization: Bearer <personal_access_token>."},
            {"claim": "PATs can be generated in Developer Console.", "url": "https://app.asana.com/0/developer-console", "quote": "Generate personal access tokens directly within the Asana Developer Console."}
        ],
        "confidence": "high", "notes": "Standard REST API with rich webhooks.", "needs_human": False, "human_reason": None
    },
    76: {
        "id": 76, "name": "Monday.com", "category": "Productivity and Project Management",
        "one_liner": "Work operating system (Work OS) for customizable project management, CRM, and task boards.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes personal API tokens accessible under Avatar > Developers > Developer.",
        "api_surface": {"type": "GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Monday.com API is a GraphQL API authenticated via Authorization header.", "url": "https://developer.monday.com/api-reference/docs/authentication", "quote": "All API calls must include your API token in the Authorization header: Authorization: <your_api_token>."},
            {"claim": "API tokens can be found in Developer section.", "url": "https://developer.monday.com/api-reference/docs/authentication#how-to-get-your-api-token", "quote": "Retrieve your personal API token from your monday.com profile under Administration > API."}
        ],
        "confidence": "high", "notes": "Exclusively GraphQL API.", "needs_human": False, "human_reason": None
    },
    77: {
        "id": 77, "name": "ClickUp", "category": "Productivity and Project Management",
        "one_liner": "All-in-one productivity platform for tasks, docs, chat, goals, and project tracking.",
        "auth_methods": ["Bearer/token", "OAuth2", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Forever plan allows creating personal API keys in Settings > Apps > API.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/clickup"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "ClickUp API v2 supports personal API tokens and OAuth 2.0.", "url": "https://clickup.com/api/developer-portal/authentication/", "quote": "Pass your personal API token directly in the Authorization header: Authorization: pk_..."},
            {"claim": "Personal API keys are available in user settings.", "url": "https://help.clickup.com/hc/en-us/articles/6303426241687-ClickUp-API", "quote": "Go to Settings > ClickApps > API to generate a personal API token."}
        ],
        "confidence": "high", "notes": "Personal API key prefix is pk_.", "needs_human": False, "human_reason": None
    },
    78: {
        "id": 78, "name": "Coda", "category": "Productivity and Project Management",
        "one_liner": "All-in-one collaborative doc and canvas that blends documents, spreadsheets, and apps.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account enables creating API tokens in Account Settings > Coda API Tokens.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Coda API uses Bearer token authentication.", "url": "https://coda.io/developers/apis/v1", "quote": "Authenticate with the Coda API by supplying your API token in the Authorization header: Bearer <API_TOKEN>."},
            {"claim": "API tokens can be generated under account settings.", "url": "https://coda.io/account", "quote": "Generate API tokens with custom read and write restrictions in account settings."}
        ],
        "confidence": "high", "notes": "Straightforward REST API.", "needs_human": False, "human_reason": None
    },
    79: {
        "id": 79, "name": "Smartsheet", "category": "Productivity and Project Management",
        "one_liner": "Enterprise work execution platform offering grid, card, gantt, and calendar project views.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "30-day free trial or paid plan allows generating API Access Tokens under Account > Personal Settings > API Access.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Smartsheet REST API authenticates using Bearer access tokens.", "url": "https://smartsheet.redoc.ly/#section/Authentication", "quote": "All API requests require an Authorization header: Authorization: Bearer <ACCESS_TOKEN>."},
            {"claim": "Access tokens are generated in Personal Settings.", "url": "https://help.smartsheet.com/articles/2482389-generate-api-key", "quote": "Generate an API access token in Account > Personal Settings > API Access."}
        ],
        "confidence": "high", "notes": "Mature enterprise REST endpoints.", "needs_human": False, "human_reason": None
    },
    80: {
        "id": 80, "name": "Harvest", "category": "Productivity and Project Management",
        "one_liner": "Time tracking, invoicing, and project expense reporting software.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "30-day free trial provides instant Personal Access Token creation on id.getharvest.com/developers.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Harvest API v2 requires Authorization Bearer token and Harvest-Account-ID header.", "url": "https://help.getharvest.com/api-v2/authentication-api/overview/authentication/", "quote": "Requests require two headers: Authorization: Bearer <TOKEN> and Harvest-Account-Id: <ACCOUNT_ID>."},
            {"claim": "Personal access tokens can be created in developer tools.", "url": "https://id.getharvest.com/developers", "quote": "Create a personal access token for testing or accessing your Harvest account data."}
        ],
        "confidence": "high", "notes": "Requires both Bearer token and Harvest-Account-Id header.", "needs_human": False, "human_reason": None
    },

    # 9. Finance and Fintech (81-90)
    81: {
        "id": 81, "name": "Stripe", "category": "Finance and Fintech",
        "one_liner": "Financial infrastructure platform for payment processing, billing, and global commerce.",
        "auth_methods": ["Bearer/token", "Basic", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account sign-up includes instant test mode API keys (`sk_test_...`) without card or business verification.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/stripe/agent-toolkit"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Stripe API uses Bearer authentication with secret keys.", "url": "https://stripe.com/docs/api/authentication", "quote": "Authenticate your API requests by providing your secret API key in the Authorization header: Authorization: Bearer sk_..."},
            {"claim": "Test mode keys are available immediately upon registration.", "url": "https://stripe.com/docs/keys", "quote": "All Stripe accounts have test mode keys that can be used immediately without activating the account."}
        ],
        "confidence": "high", "notes": "Benchmark for developer experience.", "needs_human": False, "human_reason": None
    },
    82: {
        "id": 82, "name": "Plaid", "category": "Finance and Fintech",
        "one_liner": "Fintech API network connecting applications to user bank accounts for balances and transactions.",
        "auth_methods": ["API key", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Sandbox environment access is provided immediately upon developer sign up.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Plaid API authenticates using client_id and secret in JSON request body or custom headers.", "url": "https://plaid.com/docs/api/", "quote": "All requests must include your client_id and secret in the request body: PLAID-CLIENT-ID and PLAID-SECRET headers are also supported."},
            {"claim": "Plaid Sandbox provides free test access with fake financial institutions.", "url": "https://plaid.com/docs/sandbox/", "quote": "Use the Sandbox environment to test Plaid integrations for free with mock bank accounts."}
        ],
        "confidence": "high", "notes": "Sandbox is free and comprehensive; production requires compliance verification.", "needs_human": False, "human_reason": None
    },
    83: {
        "id": 83, "name": "Binance", "category": "Finance and Fintech",
        "one_liner": "Cryptocurrency exchange providing trading, market data, and spot/futures APIs.",
        "auth_methods": ["API key", "other"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Binance Spot Testnet provides instant self-serve API Key and Secret with mock crypto balances.",
        "api_surface": {"type": "REST / WebSocket", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Binance API uses X-MBX-APIKEY header and HMAC-SHA256 request signatures.", "url": "https://binance-docs.github.io/apidocs/spot/en/#endpoint-security-type", "quote": "Signed endpoints require passing an API-Key in the X-MBX-APIKEY header and a signature parameter created using HMAC SHA256."},
            {"claim": "Spot Testnet allows risk-free API testing.", "url": "https://testnet.binance.vision/", "quote": "Get an API key to test spot trading endpoints without risking real funds."}
        ],
        "confidence": "high", "notes": "Requires timestamp and HMAC signature calculation.", "needs_human": False, "human_reason": None
    },
    84: {
        "id": 84, "name": "Paygent Connect", "category": "Finance and Fintech",
        "one_liner": "Payment gateway connector and merchant processing infrastructure powered by NMI.",
        "auth_methods": ["API key", "Basic"],
        "self_serve": "partner_or_contact_sales",
        "self_serve_reason": "Requires commercial merchant underwriting and gateway setup via sales or partner contract.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "partner gate",
        "evidence": [
            {"claim": "NMI / Paygent gateway authenticates via security keys or API login IDs.", "url": "https://www.nmi.com/solutions/payment-gateway/", "quote": "Authenticate transactions using API Security Keys or merchant account credentials."},
            {"claim": "Gateway access requires an approved merchant account.", "url": "https://www.nmi.com/partner-with-nmi/", "quote": "Contact partner sales to establish payment gateway facilities and merchant boarding."}
        ],
        "confidence": "high", "notes": "Merchant gateway partner gate.", "needs_human": True, "human_reason": "Requires commercial merchant underwriting and payment gateway partnership."
    },
    85: {
        "id": 85, "name": "iPayX", "category": "Finance and Fintech",
        "one_liner": "AI-powered automated enterprise payment and invoice settlement platform.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "partner_or_contact_sales",
        "self_serve_reason": "Private beta / contact sales model; no open self-serve developer portal or public registration.",
        "api_surface": {"type": "REST", "breadth": "small", "public_docs": False, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "no", "main_blocker": "partner gate",
        "evidence": [
            {"claim": "iPayX is an enterprise AI payment platform in private access.", "url": "https://ipayx.ai/", "quote": "Enterprise AI agent payments; request demo or join waitlist for platform integration."},
            {"claim": "No open self-serve API sign up is available.", "url": "https://ipayx.ai/docs", "quote": "Developer access is granted on invitation or through enterprise pilot engagements."}
        ],
        "confidence": "medium", "notes": "Private beta AI fintech product.", "needs_human": True, "human_reason": "Private beta product requiring partner invitation and enterprise demo."
    },
    86: {
        "id": 86, "name": "QuickBooks", "category": "Finance and Fintech",
        "one_liner": "Small business accounting and bookkeeping software by Intuit.",
        "auth_methods": ["OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Intuit Developer Portal provides free developer account with sandbox company and instant OAuth 2.0 app credentials.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/quickbooks"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "QuickBooks Online Accounting API uses OAuth 2.0 protocol.", "url": "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization", "quote": "Intuit uses OAuth 2.0 for authenticating API requests. Pass the access token in the Authorization header: Bearer <access_token>."},
            {"claim": "Developer sandboxes are free and self-serve.", "url": "https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes", "quote": "Use sandbox companies to test API calls with sample accounting data."}
        ],
        "confidence": "high", "notes": "Standard accounting API.", "needs_human": False, "human_reason": None
    },
    87: {
        "id": 87, "name": "Xero", "category": "Finance and Fintech",
        "one_liner": "Cloud accounting software for small businesses, accountants, and bookkeepers.",
        "auth_methods": ["OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free developer account enables creating OAuth 2.0 apps and connecting to a free Demo Company sandbox.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Xero API authenticates via OAuth 2.0 Bearer tokens and xero-tenant-id header.", "url": "https://developer.xero.com/documentation/guides/oauth2/overview/", "quote": "Requests require an Authorization: Bearer <TOKEN> header and a xero-tenant-id header specifying the organization."},
            {"claim": "Developers can create free test applications with Demo Company.", "url": "https://developer.xero.com/myapps", "quote": "Sign in to the developer portal to register apps and access your Demo Company."}
        ],
        "confidence": "high", "notes": "Requires xero-tenant-id header in requests.", "needs_human": False, "human_reason": None
    },
    88: {
        "id": 88, "name": "Brex", "category": "Finance and Fintech",
        "one_liner": "Corporate cards, spend management, and corporate banking platform for startups and enterprises.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "Requires an active Brex corporate card/business account; user tokens generated in Developer Dashboard.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Brex API authenticates using Bearer user tokens or OAuth 2.0.", "url": "https://developer.brex.com/docs/authentication/", "quote": "Authenticate with the Brex API by passing your token in the Authorization header: Authorization: Bearer <token>."},
            {"claim": "Tokens are created in Brex dashboard for account holders.", "url": "https://developer.brex.com/docs/getting-started/", "quote": "Generate API tokens under Company Settings > Developer in your Brex dashboard."}
        ],
        "confidence": "high", "notes": "Corporate fintech account required.", "needs_human": False, "human_reason": None
    },
    89: {
        "id": 89, "name": "Ramp", "category": "Finance and Fintech",
        "one_liner": "Corporate cards, expense management, invoice bill pay, and finance automation.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "Requires an active Ramp corporate account; Developer API keys and OAuth apps created in Company Settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Ramp Developer API authenticates via OAuth 2.0 Bearer tokens.", "url": "https://docs.ramp.com/developer-api/authentication", "quote": "To authenticate with the Ramp API, include your access token as a Bearer token: Authorization: Bearer <token>."},
            {"claim": "API credentials are configured in Ramp company settings.", "url": "https://docs.ramp.com/developer-api/getting-started", "quote": "Create API credentials in Ramp under Company Settings > Developer."}
        ],
        "confidence": "high", "notes": "Modern corporate spend API.", "needs_human": False, "human_reason": None
    },
    90: {
        "id": 90, "name": "PitchBook", "category": "Finance and Fintech",
        "one_liner": "Private market financial data and research platform covering VC, PE, and M&A deals.",
        "auth_methods": ["API key", "Bearer/token"],
        "self_serve": "partner_or_contact_sales",
        "self_serve_reason": "Enterprise institutional data contract required ($10k-$50k+/year); no self-serve developer tier or free trial.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "partner gate",
        "evidence": [
            {"claim": "PitchBook Data API provides REST endpoints authenticated with API keys.", "url": "https://pitchbook.com/products/data/api", "quote": "Integrate PitchBook's comprehensive private market data into internal tools using REST API keys."},
            {"claim": "Access is restricted to licensed institutional subscribers.", "url": "https://pitchbook.com/products/data/api#request-demo", "quote": "Request a consultation to discuss licensing PitchBook API data feeds for your organization."}
        ],
        "confidence": "high", "notes": "High commercial paywall.", "needs_human": True, "human_reason": "High-value enterprise institutional contract required."
    },

    # 10. AI, Research and Media-native (91-100)
    91: {
        "id": 91, "name": "NotebookLM", "category": "AI, Research and Media-native",
        "one_liner": "AI research assistant and note-taking tool by Google powered by Gemini.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "no_public_api",
        "self_serve_reason": "NotebookLM as a consumer app has no standalone public REST API; enterprise access is mediated via Google Cloud Vertex AI / Gemini API.",
        "api_surface": {"type": "none", "breadth": "none", "public_docs": False, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "no API",
        "evidence": [
            {"claim": "NotebookLM has no direct standalone developer REST API.", "url": "https://cloud.google.com/gemini", "quote": "NotebookLM operates as a web application; programmable grounding and document synthesis are accessed through Google Cloud Vertex AI and Gemini APIs."},
            {"claim": "Enterprise grounding capabilities are consumed via Google Cloud.", "url": "https://cloud.google.com/vertex-ai/generative-ai/docs", "quote": "Use Vertex AI Search and Conversation for enterprise retrieval and document synthesis."}
        ],
        "confidence": "high", "notes": "No standalone public API for consumer NotebookLM; use Vertex AI Gemini API for programmatic agent tools.", "needs_human": True, "human_reason": "Consumer app without dedicated REST API (must use Vertex AI)."
    },
    92: {
        "id": 92, "name": "Otter AI", "category": "AI, Research and Media-native",
        "one_liner": "AI meeting assistant providing automated real-time audio transcription and summaries.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "REST API access requires an Otter Enterprise plan; community MCP server operates via session or Enterprise token.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/v-chao/otter-ai-mcp"},
        "buildable_today": "partial", "main_blocker": "paid-only",
        "evidence": [
            {"claim": "Otter API and webhook integrations require Enterprise plan credentials.", "url": "https://help.otter.ai/", "quote": "Otter API access and developer integrations are available for Enterprise accounts."},
            {"claim": "Community MCP server connects Otter transcripts to AI agents.", "url": "https://github.com/v-chao/otter-ai-mcp", "quote": "Model Context Protocol server for interacting with Otter.ai meeting notes and transcriptions."}
        ],
        "confidence": "high", "notes": "Enterprise gate for official API; community MCP exists.", "needs_human": False, "human_reason": None
    },
    93: {
        "id": 93, "name": "Fathom", "category": "AI, Research and Media-native",
        "one_liner": "AI meeting recorder that records, transcribes, and summarizes Zoom, Teams, and Google Meet calls.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account includes access to API keys generated under Settings > API / Webhooks.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Fathom API authenticates via Bearer API keys in request headers.", "url": "https://fathom.video/api", "quote": "Pass your API key in the Authorization header: Authorization: Bearer <API_KEY>."},
            {"claim": "API keys are generated under user settings.", "url": "https://fathom.video/", "quote": "Generate API keys to retrieve meeting transcripts and summaries programmatically."}
        ],
        "confidence": "high", "notes": "Popular meeting recorder with clean REST export.", "needs_human": False, "human_reason": None
    },
    94: {
        "id": 94, "name": "Consensus", "category": "AI, Research and Media-native",
        "one_liner": "AI-powered academic search engine that extracts findings and consensus from scientific research papers.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "no_public_api",
        "self_serve_reason": "Consensus does not offer an open self-serve public REST API for general 3rd party developers (API access is currently partner/waitlist gated).",
        "api_surface": {"type": "none", "breadth": "none", "public_docs": False, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "no", "main_blocker": "no API",
        "evidence": [
            {"claim": "Consensus does not have a public self-serve developer API.", "url": "https://consensus.app/", "quote": "Consensus search operates through web application; no public developer REST API portal is published."},
            {"claim": "API requests are handled through partnership inquiry.", "url": "https://consensus.app/contact", "quote": "For enterprise integrations and API partnerships, please contact the Consensus team."}
        ],
        "confidence": "high", "notes": "Partner/waitlist gated; no public API docs.", "needs_human": True, "human_reason": "No public developer API available; partner inquiry required."
    },
    95: {
        "id": 95, "name": "Reducto", "category": "AI, Research and Media-native",
        "one_liner": "Document ingestion and visual parsing API for complex PDFs, spreadsheets, and scanned tables.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account sign up provides $100 free developer credits and instant API key creation.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Reducto API authenticates using Bearer API keys.", "url": "https://docs.reducto.ai/api-reference/introduction", "quote": "Authenticate requests with: Authorization: Bearer <API_KEY>."},
            {"claim": "Free trial includes $100 credits upon registration.", "url": "https://reducto.ai/", "quote": "Sign up to receive $100 in free credits to parse documents and test extraction."}
        ],
        "confidence": "high", "notes": "State-of-the-art PDF parsing for RAG and agent toolkits.", "needs_human": False, "human_reason": None
    },
    96: {
        "id": 96, "name": "Devin", "category": "AI, Research and Media-native",
        "one_liner": "Autonomous AI software engineer by Cognition AI that plans, writes, and tests code.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "Requires an active Devin subscription; API keys and official MCP server are accessible in account settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://docs.devin.ai/mcp"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Devin REST API authenticates using Bearer API keys.", "url": "https://docs.devin.ai/api-reference/overview", "quote": "All API requests require an Authorization header: Authorization: Bearer <DEVIN_API_KEY>."},
            {"claim": "Official Devin MCP server is published.", "url": "https://docs.devin.ai/mcp", "quote": "Use the Devin Model Context Protocol (MCP) server to trigger Devin sessions from other AI agents and IDEs."}
        ],
        "confidence": "high", "notes": "Official MCP server available.", "needs_human": False, "human_reason": None
    },
    97: {
        "id": 97, "name": "higgsfield", "category": "AI, Research and Media-native",
        "one_liner": "Generative video and multimodal AI platform with Python SDK and CLI for video synthesis.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account includes initial credits; API keys are generated via CLI login or web dashboard.",
        "api_surface": {"type": "SDK / CLI", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Higgsfield provides Python SDK and CLI authenticated via API key.", "url": "https://higgsfield.ai/cli", "quote": "Authenticate the Higgsfield CLI using higgsfield login with your API key or token."},
            {"claim": "Free tier provides generation credits.", "url": "https://higgsfield.ai/", "quote": "Sign up to explore generative video models with free trial compute."}
        ],
        "confidence": "high", "notes": "CLI and Python library.", "needs_human": False, "human_reason": None
    },
    98: {
        "id": 98, "name": "Mermaid CLI", "category": "AI, Research and Media-native",
        "one_liner": "Command-line interface for Mermaid.js to compile diagram definition files into SVG, PNG, and PDF.",
        "auth_methods": ["none"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Open-source npm package (@mermaid-js/mermaid-cli); runs locally without any account or API key.",
        "api_surface": {"type": "CLI-only", "breadth": "small", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "CLI-only",
        "evidence": [
            {"claim": "Mermaid CLI is a Node command-line tool with no REST API.", "url": "https://github.com/mermaid-js/mermaid-cli", "quote": "Mermaid CLI takes a mermaid definition file, executes it in a headless browser, and generates SVG, PNG, or PDF output."},
            {"claim": "No API key or external service authentication is needed.", "url": "https://github.com/mermaid-js/mermaid-cli#installation", "quote": "Install via npm install -g @mermaid-js/mermaid-cli and run mmdc directly."}
        ],
        "confidence": "high", "notes": "Open-source CLI tool. Agent toolkit must wrap shell execution rather than HTTP REST.", "needs_human": False, "human_reason": None
    },
    99: {
        "id": 99, "name": "YouTube Transcript", "category": "AI, Research and Media-native",
        "one_liner": "Developer API service for extracting structured video transcripts and timestamps from YouTube.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier provides free monthly transcript requests; API keys generated upon registration.",
        "api_surface": {"type": "REST", "breadth": "small", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/youtube-transcript"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "TranscriptAPI authenticates using an API key in header or query parameter.", "url": "https://transcriptapi.com/", "quote": "Include your API key as Authorization: Bearer <API_KEY> or as a query parameter ?api_key=<API_KEY>."},
            {"claim": "Free tier available for developers.", "url": "https://transcriptapi.com/pricing", "quote": "Get started with the free plan to extract video captions and transcripts."}
        ],
        "confidence": "high", "notes": "Community MCP server exists.", "needs_human": False, "human_reason": None
    },
    100: {
        "id": 100, "name": "Grain", "category": "AI, Research and Media-native",
        "one_liner": "AI meeting recorder and conversation intelligence platform for sales and customer interviews.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "Free trial includes meeting recording and access to API tokens in Workspace Settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Grain API authenticates via Bearer API tokens.", "url": "https://grain.com/", "quote": "Access meeting recordings and highlights via the Grain REST API using Bearer token authentication."},
            {"claim": "API tokens are managed in workspace developer settings.", "url": "https://grain.com/help", "quote": "Generate API tokens in your Workspace Settings to automate video ingestion."}
        ],
        "confidence": "high", "notes": "Meeting intelligence tool.", "needs_human": False, "human_reason": None
    }
}
