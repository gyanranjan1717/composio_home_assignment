"""Curated documentation facts and evidence for Apps 31-60."""

apps_31_60 = {
    # 4. Marketing, Ads, Email and Social (31-40)
    31: {
        "id": 31, "name": "Google Ads", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Online advertising platform for running search, display, video, and shopping campaigns.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "admin_approval",
        "self_serve_reason": "Requires a Manager Account (MCC) and approved Developer Token; test accounts allow testing but production access requires developer token approval.",
        "api_surface": {"type": "REST / gRPC", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "approval review",
        "evidence": [
            {"claim": "Google Ads API requires OAuth 2.0 and a developer token header.", "url": "https://developers.google.com/google-ads/api/docs/first-call/overview", "quote": "Each request must include an OAuth 2.0 access token and a developer-token header to identify the developer."},
            {"claim": "Production developer token requires compliance review and approval.", "url": "https://developers.google.com/google-ads/api/docs/get-started/dev-token", "quote": "Test accounts can use unapproved developer tokens, but production access requires Google review and approval."}
        ],
        "confidence": "high", "notes": "Developer token approval can take days to weeks.", "needs_human": True, "human_reason": "Developer token approval review required for production."
    },
    32: {
        "id": 32, "name": "Meta Ads", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Advertising platform across Facebook, Instagram, Messenger, and Audience Network.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Meta developer account gives instant access to Development Mode and test ad accounts.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Meta Marketing API uses OAuth 2.0 User and System User access tokens.", "url": "https://developers.facebook.com/docs/marketing-apis/overview/authentication", "quote": "All Marketing API requests require an access token passed as Authorization: Bearer <TOKEN> or via the access_token parameter."},
            {"claim": "Developers can create test ad accounts in Development mode.", "url": "https://developers.facebook.com/docs/marketing-apis/overview", "quote": "In development mode, your app can make calls to test ad accounts and manage campaigns immediately."}
        ],
        "confidence": "high", "notes": "Standard Access is self-serve for dev; Advanced Access requires App Review.", "needs_human": False, "human_reason": None
    },
    33: {
        "id": 33, "name": "LinkedIn Ads", "category": "Marketing, Ads, Email and Social",
        "one_liner": "B2B social advertising platform for sponsored content, messaging, and lead gen.",
        "auth_methods": ["OAuth2"],
        "self_serve": "admin_approval",
        "self_serve_reason": "Requires applying to the LinkedIn Marketing Developer Platform and manual partner approval for advertising APIs.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "approval review",
        "evidence": [
            {"claim": "LinkedIn Marketing APIs authenticate via 3-legged OAuth 2.0.", "url": "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication", "quote": "LinkedIn APIs use OAuth 2.0 for user authorization. Requests must pass a Bearer access token in the Authorization header."},
            {"claim": "Access to LinkedIn Marketing APIs requires approved developer application.", "url": "https://learn.microsoft.com/en-us/linkedin/marketing/overview", "quote": "To access Marketing Developer Platform endpoints, you must request access and be approved by the LinkedIn team."}
        ],
        "confidence": "high", "notes": "Strict approval gate for ad campaign management.", "needs_human": True, "human_reason": "Requires LinkedIn Marketing Developer Platform application approval."
    },
    34: {
        "id": 34, "name": "GoHighLevel", "category": "Marketing, Ads, Email and Social",
        "one_liner": "All-in-one CRM and marketing automation platform for marketing agencies.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "Requires active agency account or Marketplace developer account to access API v2 keys/OAuth.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "HighLevel API v2 uses OAuth 2.0 Bearer tokens and Private App tokens.", "url": "https://highlevel.stoplight.io/docs/integrations/00d33e5ffb6c7-authentication", "quote": "HighLevel API v2 authenticates via OAuth 2.0 access tokens passed in the Authorization header as Bearer <access_token>."},
            {"claim": "API access requires an active HighLevel account or Marketplace App.", "url": "https://marketplace.gohighlevel.com/", "quote": "Developers can create private or marketplace integrations through the HighLevel Marketplace Developer Portal."}
        ],
        "confidence": "high", "notes": "API v2 replaced legacy v1 location API keys.", "needs_human": False, "human_reason": None
    },
    35: {
        "name": "Mailchimp", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Marketing automation and email marketing platform for newsletters and campaigns.",
        "auth_methods": ["OAuth2", "API key", "Basic"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account sign-up includes instant API key generation in Account Settings > Extras > API keys.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/mailchimp"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Mailchimp Marketing API supports API keys via Basic auth and OAuth 2.0.", "url": "https://mailchimp.com/developer/marketing/guides/access-the-api/", "quote": "You can authenticate with the Marketing API using an API key (using HTTP Basic Authentication) or OAuth 2.0."},
            {"claim": "API keys can be generated instantly for free on any account.", "url": "https://mailchimp.com/developer/marketing/guides/quick-start/", "quote": "Log in to your Mailchimp account, navigate to Account & billing > Extras > API keys, and click Create A Key."}
        ],
        "confidence": "high", "notes": "API key suffix specifies data center prefix (e.g. us19).", "needs_human": False, "human_reason": None
    },
    36: {
        "id": 36, "name": "Klaviyo", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Marketing automation platform specializing in email, SMS, and ecommerce customer tracking.",
        "auth_methods": ["API key", "Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan allows generating public and private API keys directly in Settings > API Keys.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Klaviyo APIs authenticate via Klaviyo-API-Key header or Bearer OAuth tokens.", "url": "https://developers.klaviyo.com/en/docs/authenticate_with_the_klaviyo_api", "quote": "Authenticate private API requests by providing your private key in the Authorization header: Authorization: Klaviyo-API-Key your-key."},
            {"claim": "API keys are generated in Klaviyo account settings.", "url": "https://developers.klaviyo.com/en/docs/retrieve_api_credentials", "quote": "Access your API keys under Settings > Account > API Keys in your Klaviyo account."}
        ],
        "confidence": "high", "notes": "New 2024/2025 REST endpoints follow JSON:API standard.", "needs_human": False, "human_reason": None
    },
    37: {
        "id": 37, "name": "systeme.io", "category": "Marketing, Ads, Email and Social",
        "one_liner": "All-in-one marketing platform for sales funnels, email marketing, and online courses.",
        "auth_methods": ["API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes access to Public API keys generated in Profile > Settings > Public API keys.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Systeme.io Public API authenticates via X-API-KEY header.", "url": "https://systeme.io/api", "quote": "All requests must include your API key in the X-API-KEY header."},
            {"claim": "Public API keys can be generated in account settings.", "url": "https://systeme.io/help/how-to-use-public-api-keys", "quote": "Go to Settings > Public API Keys to generate an API key for your account."}
        ],
        "confidence": "high", "notes": "Very simple and clean key-based REST endpoints.", "needs_human": False, "human_reason": None
    },
    38: {
        "id": 38, "name": "Pinterest", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Visual discovery, shopping, and social pin bookmarking platform.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Developer portal allows instant app creation and sandbox access tokens; production access requires app review.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Pinterest API v5 authenticates using OAuth 2.0 Bearer tokens.", "url": "https://developers.pinterest.com/docs/api/v5/#tag/Authentication", "quote": "All requests to the Pinterest API must be authenticated with an OAuth 2.0 access token in the Authorization header."},
            {"claim": "Sandbox trials and app creation are available on Pinterest Developer portal.", "url": "https://developers.pinterest.com/docs/getting-started/set-up-app/", "quote": "Create an app on the developer portal to obtain trial credentials and access the sandbox environment."}
        ],
        "confidence": "high", "notes": "Sandbox tier is self-serve; live pin posting needs app review.", "needs_human": False, "human_reason": None
    },
    39: {
        "id": 39, "name": "Threads (Meta)", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Text-based social network by Instagram (Meta) for real-time conversation.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Meta Developer platform allows self-serve app creation and token generation for own user profile.",
        "api_surface": {"type": "REST", "breadth": "small", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/threads"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Threads API uses OAuth 2.0 user tokens for publishing and reading posts.", "url": "https://developers.facebook.com/docs/threads/overview", "quote": "The Threads API enables creators to publish posts, retrieve insights, and manage replies using OAuth 2.0 authorization."},
            {"claim": "Developers can register a Threads app on Meta for Developers.", "url": "https://developers.facebook.com/docs/threads/get-started", "quote": "Create an app in Meta for Developers and configure Threads API use cases."}
        ],
        "confidence": "high", "notes": "Launched in 2024; clean endpoint structure for posting and replies.", "needs_human": False, "human_reason": None
    },
    40: {
        "id": 40, "name": "SendGrid", "category": "Marketing, Ads, Email and Social",
        "one_liner": "Cloud-based customer communication platform for transactional and marketing email delivery.",
        "auth_methods": ["Bearer/token", "API key", "Basic"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier (100 emails/day forever) allows instant API key generation in dashboard.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "SendGrid v3 API uses API keys passed as Bearer tokens in Authorization header.", "url": "https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication", "quote": "SendGrid uses API keys for authentication. Pass your key in the header: Authorization: Bearer <<YOUR_API_KEY>>."},
            {"claim": "API keys can be created directly in the Twilio SendGrid app.", "url": "https://app.sendgrid.com/settings/api_keys", "quote": "Create full access or restricted API keys directly in Settings > API Keys."}
        ],
        "confidence": "high", "notes": "Gold standard for email delivery API.", "needs_human": False, "human_reason": None
    },

    # 5. Ecommerce (41-50)
    41: {
        "id": 41, "name": "Shopify", "category": "Ecommerce",
        "one_liner": "Global ecommerce platform enabling merchants to build and manage online stores.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Shopify Partner account lets developers spin up unlimited development stores and custom apps.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/shopify/shopify-mcp"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Shopify Admin API authenticates using OAuth 2.0 or custom app access tokens.", "url": "https://shopify.dev/docs/apps/auth/admin-app-access-tokens", "quote": "Authenticate requests with the X-Shopify-Access-Token header containing your access token."},
            {"claim": "Shopify Partners can create free development stores.", "url": "https://shopify.dev/docs/apps/tools/development-stores", "quote": "Development stores are free Shopify stores that let you build and test apps without paying a subscription."}
        ],
        "confidence": "high", "notes": "GraphQL Admin API is primary; REST is maintained for legacy endpoints.", "needs_human": False, "human_reason": None
    },
    42: {
        "id": 42, "name": "WooCommerce", "category": "Ecommerce",
        "one_liner": "Open-source, customizable ecommerce platform built on WordPress.",
        "auth_methods": ["Basic", "OAuth2", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Open-source and self-hostable; REST API keys (Consumer Key & Consumer Secret) are generated directly in WordPress admin.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/woocommerce/mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "WooCommerce REST API uses HTTP Basic Auth with Consumer Key and Secret over HTTPS.", "url": "https://woocommerce.com/document/woocommerce-rest-api/", "quote": "The WooCommerce REST API uses HTTP Basic Authentication over HTTPS. Pass your Consumer Key as username and Consumer Secret as password."},
            {"claim": "API keys are generated under WooCommerce Settings.", "url": "https://woocommerce.com/document/woocommerce-rest-api/#section-3", "quote": "Generate API keys in WooCommerce > Settings > Advanced > REST API."}
        ],
        "confidence": "high", "notes": "Frictionless setup on any WordPress instance.", "needs_human": False, "human_reason": None
    },
    43: {
        "id": 43, "name": "BigCommerce", "category": "Ecommerce",
        "one_liner": "Open SaaS ecommerce platform providing headless and enterprise online store management.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "15-day free trial or free Developer Portal sandbox allows generating Store API credentials.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "BigCommerce REST Management APIs authenticate using X-Auth-Token header.", "url": "https://developer.bigcommerce.com/docs/start/authentication/api-accounts", "quote": "Requests to the BigCommerce API require an X-Auth-Token header containing your access token."},
            {"claim": "API accounts can be created in store control panel.", "url": "https://developer.bigcommerce.com/docs/start/authentication/api-accounts#creating-an-api-account", "quote": "Create API accounts under Advanced Settings > API Accounts in the BigCommerce control panel."}
        ],
        "confidence": "high", "notes": "Rich REST and Storefront GraphQL APIs.", "needs_human": False, "human_reason": None
    },
    44: {
        "id": 44, "name": "Salesforce Commerce Cloud", "category": "Ecommerce",
        "one_liner": "Enterprise B2B and B2C ecommerce platform for high-volume enterprise retailers.",
        "auth_methods": ["OAuth2", "JWT"],
        "self_serve": "partner_or_contact_sales",
        "self_serve_reason": "Enterprise sales contract required; Commerce API (SCAPI) requires an Account Manager client ID tied to an active realm.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "partner gate",
        "evidence": [
            {"claim": "Salesforce Commerce API (SCAPI) uses OAuth 2.0 via Salesforce Account Manager.", "url": "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html", "quote": "SCAPI uses OAuth 2.0 access tokens obtained through Account Manager or Shopper Login (SLAS)."},
            {"claim": "Account Manager access requires an enterprise realm and contract.", "url": "https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/account-manager.html", "quote": "Access to Account Manager is restricted to licensed B2C Commerce customers and certified partners."}
        ],
        "confidence": "high", "notes": "Requires institutional realm credentials.", "needs_human": True, "human_reason": "Enterprise partner contract required for Account Manager and sandbox realms."
    },
    45: {
        "id": 45, "name": "Magento (Adobe Commerce)", "category": "Ecommerce",
        "one_liner": "Flexible ecommerce platform offering open-source self-hosted and cloud enterprise editions.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Magento Open Source is free to download and self-host; integration access tokens created in Admin Panel.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Adobe Commerce / Magento REST API supports Bearer token authentication.", "url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/", "quote": "All REST requests require authentication. Pass the token as Authorization: Bearer <token>."},
            {"claim": "Integrations and tokens can be created in Magento admin panel.", "url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token/", "quote": "Create an integration in System > Extensions > Integrations to generate access tokens."}
        ],
        "confidence": "high", "notes": "Open-source edition enables zero-cost testing.", "needs_human": False, "human_reason": None
    },
    46: {
        "id": 46, "name": "Squarespace", "category": "Ecommerce",
        "one_liner": "Website building and ecommerce platform offering hosted online store templates.",
        "auth_methods": ["Bearer/token", "OAuth2", "API key"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "API Keys require a paid Commerce Advanced subscription plan.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Squarespace API uses Bearer API Keys or OAuth 2.0.", "url": "https://developers.squarespace.com/commerce-apis/authentication", "quote": "Authenticate requests with the Authorization header: Authorization: Bearer <API_KEY_OR_OAUTH_TOKEN>."},
            {"claim": "API Keys are available on Commerce Advanced plans.", "url": "https://support.squarespace.com/hc/en-us/articles/360000845648-Squarespace-Commerce-APIs", "quote": "Generating API keys is exclusive to sites on the Commerce Advanced plan."}
        ],
        "confidence": "high", "notes": "Gated by subscription tier.", "needs_human": False, "human_reason": None
    },
    47: {
        "id": 47, "name": "Ecwid", "category": "Ecommerce",
        "one_liner": "Embeddable ecommerce widget and storefront for websites, social media, and marketplaces.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes free developer account on Ecwid App Market with secret tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Ecwid REST API authenticates using Bearer secret tokens or OAuth 2.0.", "url": "https://api-docs.ecwid.com/reference/authentication", "quote": "To authenticate, provide your access token in the Authorization header: Bearer <secret_token>."},
            {"claim": "Developers can register for a free developer account.", "url": "https://api-docs.ecwid.com/docs/getting-started", "quote": "Sign up for a free developer account to get your client credentials and test store."}
        ],
        "confidence": "high", "notes": "Embeddable shopping cart architecture.", "needs_human": False, "human_reason": None
    },
    48: {
        "id": 48, "name": "Gumroad", "category": "Ecommerce",
        "one_liner": "Direct-to-consumer digital commerce and creator monetization storefront.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account sign up; personal access tokens and OAuth applications can be created in Advanced Settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/gumroad"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Gumroad API supports OAuth 2.0 access tokens and personal access tokens.", "url": "https://gumroad.com/api", "quote": "Authenticate with Gumroad using an access_token query parameter or Authorization: Bearer <access_token> header."},
            {"claim": "Access tokens are created in Gumroad settings.", "url": "https://gumroad.com/settings/advanced", "quote": "Create applications and generate personal access tokens in Advanced Settings."}
        ],
        "confidence": "high", "notes": "Simple digital product API.", "needs_human": False, "human_reason": None
    },
    49: {
        "id": 49, "name": "Amazon Selling Partner", "category": "Ecommerce",
        "one_liner": "Comprehensive API suite for Amazon sellers and vendors to manage orders, inventory, and pricing.",
        "auth_methods": ["OAuth2", "other"],
        "self_serve": "admin_approval",
        "self_serve_reason": "Requires active Professional Selling account ($39.99/mo), AWS account for IAM Signature V4, and developer application approval.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "approval review",
        "evidence": [
            {"claim": "SP-API uses Login with Amazon (LWA) OAuth 2.0 and AWS Signature Version 4.", "url": "https://developer-docs.amazon.com/sp-api/docs/authorization-and-authentication", "quote": "Calls to the Selling Partner API require LWA access tokens and AWS Signature Version 4 signing."},
            {"claim": "Developer profile registration requires Amazon vetting.", "url": "https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer", "quote": "To call SP-API endpoints, you must submit a developer profile application and receive approval."}
        ],
        "confidence": "high", "notes": "Complex dual auth: AWS SigV4 + LWA OAuth.", "needs_human": True, "human_reason": "Developer registration vetting and paid professional selling plan required."
    },
    50: {
        "id": 50, "name": "fanbasis", "category": "Ecommerce",
        "one_liner": "Creator economy platform for athlete and influencer bookings, experiences, and subscriptions.",
        "auth_methods": ["none"],
        "self_serve": "no_public_api",
        "self_serve_reason": "Fanbasis is a closed consumer/creator platform with no public developer portal or documented 3rd party API.",
        "api_surface": {"type": "none", "breadth": "none", "public_docs": False, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "no", "main_blocker": "no API",
        "evidence": [
            {"claim": "Fanbasis has no public developer documentation or open API portal.", "url": "https://fanbasis.com/", "quote": "Fanbasis connects fans with creators and athletes; no public developer documentation or API portal is published."},
            {"claim": "No self-serve API access exists for external developers.", "url": "https://fanbasis.com/terms", "quote": "Platform access is provided through user web and mobile interfaces."}
        ],
        "confidence": "high", "notes": "No public API exists.", "needs_human": True, "human_reason": "No public 3rd party API exists on the platform."
    },

    # 6. Data, SEO and Scraping (51-60)
    51: {
        "id": 51, "name": "DataForSEO", "category": "Data, SEO and Scraping",
        "one_liner": "Data-for-SEO APIs providing search engine results, keyword research, and backlink data.",
        "auth_methods": ["Basic", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free trial with $1 free balance upon registration; API credentials generated on dashboard.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "DataForSEO API uses HTTP Basic Authentication with login and password/API key.", "url": "https://docs.dataforseo.com/v3/overview/", "quote": "DataForSEO uses standard HTTP Basic Authentication. Use your account email as login and API password as password."},
            {"claim": "Free sandbox credits provided upon registration.", "url": "https://app.dataforseo.com/register", "quote": "Sign up to receive free credits and access API credentials immediately."}
        ],
        "confidence": "high", "notes": "Pay-as-you-go developer friendly model.", "needs_human": False, "human_reason": None
    },
    52: {
        "id": 52, "name": "SE Ranking", "category": "Data, SEO and Scraping",
        "one_liner": "SEO analysis platform providing rank tracking, site audits, and competitive research.",
        "auth_methods": ["API key", "Bearer/token"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "API access requires an active paid subscription (Pro or Business tier) with API addon enabled.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "paid-only",
        "evidence": [
            {"claim": "SE Ranking API uses API key passed in Authorization header.", "url": "https://seranking.com/api.html", "quote": "Requests require an API token passed in the Authorization header: Authorization: Token <YOUR_API_TOKEN>."},
            {"claim": "API access is available on paid plans.", "url": "https://seranking.com/pricing.html", "quote": "API access is included in the Pro and Business plans."}
        ],
        "confidence": "high", "notes": "Requires subscription tier.", "needs_human": False, "human_reason": None
    },
    53: {
        "id": 53, "name": "Ahrefs", "category": "Data, SEO and Scraping",
        "one_liner": "SEO software suite for backlink analysis, keyword explorer, and site auditing.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "API v3 requires an active Enterprise subscription or API Units subscription.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "paid-only",
        "evidence": [
            {"claim": "Ahrefs API v3 uses OAuth 2.0 and API keys with Bearer token authentication.", "url": "https://ahrefs.com/api/documentation", "quote": "API requests require an Authorization header: Authorization: Bearer <token>."},
            {"claim": "Ahrefs API v3 requires paid API Units or Enterprise plan.", "url": "https://ahrefs.com/api/pricing", "quote": "Access to API v3 is available for Enterprise plans or through purchased API units."}
        ],
        "confidence": "high", "notes": "High financial barrier for full production data.", "needs_human": False, "human_reason": None
    },
    54: {
        "id": 54, "name": "MrScraper", "category": "Data, SEO and Scraping",
        "one_liner": "Visual web scraper and automation platform with API endpoints for data extraction.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes monthly scraping credits and instant API key generation.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "MrScraper API uses Bearer token authentication.", "url": "https://docs.mrscraper.com/api-reference", "quote": "All API requests require an Authorization header formatted as Bearer <API_KEY>."},
            {"claim": "API keys can be generated in the user profile.", "url": "https://docs.mrscraper.com/", "quote": "Find your API key in your account settings under API Keys."}
        ],
        "confidence": "high", "notes": "Accessible scraper.", "needs_human": False, "human_reason": None
    },
    55: {
        "id": 55, "name": "Apify", "category": "Data, SEO and Scraping",
        "one_liner": "Cloud platform for web scraping, data extraction, and serverless Actor automation.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier provides $5 monthly credit and instant API token in Settings > Integrations.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/apify/mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Apify API authenticates using personal API tokens via Bearer header or token query param.", "url": "https://docs.apify.com/api/v2#/introduction/authentication", "quote": "Authenticate via Authorization: Bearer <token> or by adding token=<token> to query string."},
            {"claim": "Free tier includes recurring $5 monthly platform credits.", "url": "https://apify.com/pricing", "quote": "Get started on the Free plan with $5 prepaid platform usage every month."}
        ],
        "confidence": "high", "notes": "Rich actor ecosystem and community MCP server.", "needs_human": False, "human_reason": None
    },
    56: {
        "id": 56, "name": "Firecrawl", "category": "Data, SEO and Scraping",
        "one_liner": "API service that converts websites into clean Markdown and structured data for LLM applications.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan includes 500 free credits with instant API key creation on firecrawl.dev.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://github.com/mendableai/firecrawl-mcp-server"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Firecrawl API authenticates using Bearer token API keys.", "url": "https://docs.firecrawl.dev/api-reference/introduction", "quote": "Pass your API key in the Authorization header as Authorization: Bearer <fc-...>."},
            {"claim": "Official Firecrawl MCP server is provided by the team.", "url": "https://docs.firecrawl.dev/mcp", "quote": "Connect Firecrawl to your AI agents using our official Model Context Protocol (MCP) server."}
        ],
        "confidence": "high", "notes": "Highly optimized for LLMs with official MCP server.", "needs_human": False, "human_reason": None
    },
    57: {
        "id": 57, "name": "Bright Data", "category": "Data, SEO and Scraping",
        "one_liner": "Web data platform offering proxy networks, Web Unlocker, and Scraping Browser APIs.",
        "auth_methods": ["Bearer/token", "API key", "Basic"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "Free trial available with credit card verification; API tokens generated in Control Panel.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/brightdata"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Bright Data API authenticates via Bearer API tokens.", "url": "https://docs.brightdata.com/api-reference/authentication", "quote": "Authenticate requests with Authorization: Bearer <API_TOKEN>."},
            {"claim": "API tokens can be created in the User Settings.", "url": "https://brightdata.com/cp/setting/tokens", "quote": "Generate API tokens to interact with proxy zones and dataset APIs."}
        ],
        "confidence": "high", "notes": "Comprehensive proxy and browser infrastructure.", "needs_human": False, "human_reason": None
    },
    58: {
        "id": 58, "name": "Sherlock", "category": "Data, SEO and Scraping",
        "one_liner": "Open-source Python CLI tool to find social media accounts by username across 400+ platforms.",
        "auth_methods": ["none"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "100% open source on GitHub (MIT License); run directly via Python CLI or Docker without accounts.",
        "api_surface": {"type": "CLI-only", "breadth": "small", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "CLI-only",
        "evidence": [
            {"claim": "Sherlock is a command-line tool with no hosted REST API.", "url": "https://github.com/sherlock-project/sherlock", "quote": "Hunt down social media accounts by username across social networks using the Sherlock CLI command."},
            {"claim": "No API key or authentication is required to run the tool.", "url": "https://github.com/sherlock-project/sherlock#installation", "quote": "Clone the repo and run python3 -m sherlock username."}
        ],
        "confidence": "high", "notes": "CLI tool, not a hosted SaaS API. Toolkit must wrap shell execution.", "needs_human": False, "human_reason": None
    },
    59: {
        "id": 59, "name": "Waterfall.io", "category": "Data, SEO and Scraping",
        "one_liner": "B2B data enrichment and contact intelligence waterfall API for sales teams.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "No self-serve free tier; requires contacting sales or purchasing a paid data package.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial", "main_blocker": "paid-only",
        "evidence": [
            {"claim": "Waterfall API uses Bearer token authentication.", "url": "https://waterfall.io/", "quote": "API requests require authentication with your Waterfall API key in the Authorization header."},
            {"claim": "Access is provided through paid sales subscriptions.", "url": "https://waterfall.io/pricing", "quote": "Contact sales or book a demo to get access to custom enrichment waterfalls and API keys."}
        ],
        "confidence": "medium", "notes": "Niche B2B data vendor.", "needs_human": True, "human_reason": "Commercial data vendor requiring sales consultation for API access."
    },
    60: {
        "id": 60, "name": "Clay", "category": "Data, SEO and Scraping",
        "one_liner": "Data enrichment and AI prospecting platform combining 50+ data providers into a spreadsheet UI.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "14-day free trial includes free credits; Webhook integrations and API keys accessible in Settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/clay"},
        "buildable_today": "yes", "main_blocker": "none",
        "evidence": [
            {"claim": "Clay supports inbound webhook APIs and REST enrichment actions.", "url": "https://clay.com/docs", "quote": "Trigger Clay tables and enrich data via webhooks or API keys in the Authorization header."},
            {"claim": "Free trial provides 100 credits for testing.", "url": "https://clay.com/pricing", "quote": "Try Clay with a 14-day free trial and 100 credits included."}
        ],
        "confidence": "high", "notes": "Very popular B2B enrichment aggregator.", "needs_human": False, "human_reason": None
    }
}
