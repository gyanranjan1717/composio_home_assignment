"""Builder script to populate curated documentation facts for apps 11-100."""

import os
import json

part2_data = {
    # 2. Support and Helpdesk
    11: {
        "name": "Zendesk",
        "category": "Support and Helpdesk",
        "one_liner": "Enterprise customer service and ticketing support platform.",
        "auth_methods": ["OAuth2", "API key", "Basic"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "14-day free trial or free Sandbox on Enterprise plan allows instant API token generation.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/zendesk"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Zendesk API supports OAuth 2.0 and API token authentication.", "url": "https://developer.zendesk.com/api-reference/ticketing/introduction/#security-and-authentication", "quote": "The Zendesk API supports basic authentication with username and password, API token authentication, and OAuth 2.0."},
            {"claim": "API tokens can be created in Admin Center.", "url": "https://support.zendesk.com/hc/en-us/articles/4408889114522-Generating-a-new-API-token", "quote": "In Admin Center, click Apps and integrations in the sidebar, then select Zendesk API to create an API token."}
        ],
        "confidence": "high",
        "notes": "Basic auth with `{email}/token` and API token is standard for scripting."
    },
    12: {
        "name": "Intercom",
        "category": "Support and Helpdesk",
        "one_liner": "Customer communications platform providing conversational support, chatbots, and ticketing.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Developer Workspace can be created in the Intercom Developer Hub with full API access.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/intercom/mcp-server"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Intercom API uses Bearer Access Tokens or OAuth 2.0.", "url": "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication", "quote": "All API requests require authentication using an Access Token passed as a Bearer token in the Authorization header."},
            {"claim": "Free Developer Workspaces provide API access without paid subscription.", "url": "https://developers.intercom.com/docs/build-an-integration/getting-started/create-a-developer-workspace", "quote": "A developer workspace is a free, isolated workspace dedicated to building and testing your app."}
        ],
        "confidence": "high",
        "notes": "Developer workspaces provide 100% free sandbox environment."
    },
    13: {
        "name": "Freshdesk",
        "category": "Support and Helpdesk",
        "one_liner": "Cloud-based customer support software and ticketing system by Freshworks.",
        "auth_methods": ["Basic", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan (up to 2 agents) provides instant API key in Profile Settings.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Freshdesk API uses HTTP Basic Authentication with API key as username.", "url": "https://developers.freshdesk.com/api/#authentication", "quote": "The Freshdesk API uses HTTP Basic Authentication. Use your API key as the username and a dummy password like 'X'."},
            {"claim": "API keys are accessible under agent profile settings.", "url": "https://support.freshdesk.com/en/support/solutions/articles/21554-how-to-find-your-api-key", "quote": "Log in to your Freshdesk account, click on your profile picture, and view your API key."}
        ],
        "confidence": "high",
        "notes": "Free tier makes testing instantaneous."
    },
    14: {
        "name": "Front",
        "category": "Support and Helpdesk",
        "one_liner": "Customer operations platform combining shared inboxes with ticketing and automation.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "7-day free trial or Developer Portal app creation provides API token access.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Front Core API authenticates with Bearer API tokens and OAuth 2.0.", "url": "https://dev.frontapp.com/docs/getting-started-1", "quote": "Front supports two authentication methods: API tokens for internal integrations and OAuth 2.0 for public integrations."},
            {"claim": "API tokens can be created in Front company settings.", "url": "https://dev.frontapp.com/docs/api-tokens", "quote": "Company admins can create API tokens under Settings > Developers > API tokens."}
        ],
        "confidence": "high",
        "notes": "Clean REST API with rich webhook support."
    },
    15: {
        "name": "Pylon",
        "category": "Support and Helpdesk",
        "one_liner": "B2B support platform embedded into Slack, Microsoft Teams, and email.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "No free public tier; requires an active Pylon workspace/demo to access dashboard API settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Pylon REST API uses Bearer authentication token.", "url": "https://docs.usepylon.com/docs/api-reference/authentication", "quote": "Authenticate requests to the Pylon API by including your API key in the Authorization header as a Bearer token."},
            {"claim": "API keys are generated inside Pylon dashboard settings.", "url": "https://docs.usepylon.com/docs/api-reference/getting-started", "quote": "Generate an API key from the Pylon dashboard under Settings > Developer Settings."}
        ],
        "confidence": "high",
        "notes": "Targeted specifically at B2B Slack/Teams support sync."
    },
    16: {
        "name": "LiveAgent",
        "category": "Support and Helpdesk",
        "one_liner": "Help desk software with live chat, ticket management, and call center capabilities.",
        "auth_methods": ["API key", "Bearer/token"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "14-day free trial allows self-serve API key creation in Configuration > System > API.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "LiveAgent REST API v3 supports API key authentication.", "url": "https://support.liveagent.com/849508-LiveAgent-REST-API-v3", "quote": "LiveAgent REST API v3 requires an API key passed in the apikey header or as a query parameter."},
            {"claim": "API keys are managed in LiveAgent configuration panel.", "url": "https://support.liveagent.com/045812-How-to-get-an-API-key", "quote": "Go to Configuration -> System -> API to generate and manage API keys."}
        ],
        "confidence": "high",
        "notes": "Full OpenAPI/Swagger spec available."
    },
    17: {
        "name": "Plain",
        "category": "Support and Helpdesk",
        "one_liner": "API-first customer service platform built for engineering and modern support teams.",
        "auth_methods": ["Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier available; machine tokens / API keys generated directly in Workspace Settings.",
        "api_surface": {"type": "REST / GraphQL", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Plain uses Bearer Machine User tokens to authenticate its GraphQL and REST APIs.", "url": "https://www.plain.com/docs/graphql/authentication", "quote": "To authenticate with the Plain API, provide your machine user token as a Bearer token in the Authorization header."},
            {"claim": "Machine user tokens can be generated directly in Plain workspace settings.", "url": "https://www.plain.com/docs", "quote": "Create machine users and generate secret keys directly from Settings > Machine Users."}
        ],
        "confidence": "high",
        "notes": "Primary API is GraphQL with full schema types."
    },
    18: {
        "name": "Help Scout",
        "category": "Support and Helpdesk",
        "one_liner": "Help desk and knowledge base platform designed for growing businesses.",
        "auth_methods": ["OAuth2"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "15-day free trial allows self-serve creation of OAuth2 app credentials under My App.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Help Scout Mailbox API 2.0 authenticates exclusively via OAuth 2.0.", "url": "https://developer.helpscout.com/mailbox-api/overview/authentication/", "quote": "Help Scout Mailbox API 2.0 uses OAuth 2.0 for authentication. Client Credentials or Authorization Code flow can be used."},
            {"claim": "API credentials can be generated in the user profile.", "url": "https://developer.helpscout.com/mailbox-api/overview/create-an-app/", "quote": "Create an API app in your Help Scout profile under Your Profile > My Apps."}
        ],
        "confidence": "high",
        "notes": "Client Credentials flow makes server-to-server toolkit very straightforward."
    },
    19: {
        "name": "Gorgias",
        "category": "Support and Helpdesk",
        "one_liner": "Ecommerce-focused customer service and ticketing helpdesk for Shopify and BigCommerce.",
        "auth_methods": ["Basic", "API key", "OAuth2"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "7-day free trial; API credentials accessible under Settings > You > REST API.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Gorgias REST API supports HTTP Basic Auth with user email and API key.", "url": "https://developers.gorgias.com/reference/authentication", "quote": "Authenticate with Gorgias using HTTP Basic Authentication: username is your account email and password is the API key."},
            {"claim": "API keys are generated under account profile settings.", "url": "https://developers.gorgias.com/docs/getting-started", "quote": "API credentials can be retrieved from Settings > You > REST API."}
        ],
        "confidence": "high",
        "notes": "Tightly bound to ecommerce stores."
    },
    20: {
        "name": "Gladly",
        "category": "Support and Helpdesk",
        "one_liner": "Enterprise customer service platform centered around individual customer history and conversations.",
        "auth_methods": ["Basic", "Bearer/token"],
        "self_serve": "paid_plan_required",
        "self_serve_reason": "Enterprise-only platform without public trial or self-serve signup; requires enterprise contract and administrator token generation.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "partial",
        "main_blocker": "paid-only",
        "evidence": [
            {"claim": "Gladly API uses HTTP Basic Authentication with user email and API token.", "url": "https://developer.gladly.com/rest/#section/Authentication", "quote": "Gladly API requires HTTP Basic authentication. Provide your email as the username and an API token as the password."},
            {"claim": "API tokens must be created by an administrator in the Gladly dashboard.", "url": "https://developer.gladly.com/rest/", "quote": "Generate an API token in the Gladly user interface by navigating to Settings > API Tokens."}
        ],
        "confidence": "high",
        "notes": "Enterprise customer service tool; requires tenant base URL and admin token."
    },

    # 3. Communications and Messaging
    21: {
        "name": "Slack",
        "category": "Communications and Messaging",
        "one_liner": "Channel-based enterprise team messaging and collaboration platform.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free Slack workspace creation allows instant app creation at api.slack.com with Bot User OAuth tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "official", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/slack"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Slack Web API authenticates using Bearer tokens (OAuth 2.0).", "url": "https://api.slack.com/authentication/token-types", "quote": "Tokens should be passed in the HTTP Authorization header using the Bearer scheme: Authorization: Bearer xoxb-..."},
            {"claim": "Anyone can create a free workspace and build a Slack App.", "url": "https://api.slack.com/apps", "quote": "Build apps for your workspace or distribute to others using the Slack App Directory."}
        ],
        "confidence": "high",
        "notes": "Official reference MCP server exists in the Model Context Protocol repository."
    },
    22: {
        "name": "Twilio",
        "category": "Communications and Messaging",
        "one_liner": "Cloud communications platform for programmable SMS, voice calls, and video.",
        "auth_methods": ["Basic", "API key", "JWT"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free trial account provides Account SID, Auth Token, and trial phone credits.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/twilio"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Twilio REST API uses HTTP Basic Authentication with Account SID and Auth Token.", "url": "https://www.twilio.com/docs/usage/api#http-basic-authentication", "quote": "Twilio authenticates API requests using HTTP Basic Authentication with your Account SID as the username and your Auth Token as the password."},
            {"claim": "Free trial sign up gives immediate developer credentials.", "url": "https://www.twilio.com/try-twilio", "quote": "Sign up for a free Twilio trial to get instant access to APIs and test credentials."}
        ],
        "confidence": "high",
        "notes": "Industry standard programmable communications API."
    },
    23: {
        "name": "Zoho Cliq",
        "category": "Communications and Messaging",
        "one_liner": "Enterprise team chat and collaboration software by Zoho.",
        "auth_methods": ["OAuth2", "Bearer/token"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free plan (up to 100 users) provides access to Developer Console for bot and webhook creation.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Zoho Cliq REST API authenticates using OAuth 2.0 Bearer tokens.", "url": "https://www.zoho.com/cliq/help/restapi/v2/", "quote": "The Cliq REST API uses OAuth 2.0 protocol for authentication and authorization."},
            {"claim": "Developer console allows creating bots and tokens.", "url": "https://www.zoho.com/cliq/help/platform/", "quote": "Create bots, commands, and widgets using Zoho Cliq developer tools."}
        ],
        "confidence": "high",
        "notes": "Part of the Zoho suite."
    },
    24: {
        "name": "Lark (Larksuite)",
        "category": "Communications and Messaging",
        "one_liner": "Enterprise collaboration platform (chat, docs, meetings, calendar) by ByteDance.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free edition available; Lark Open Platform enables self-serve custom app creation and App Access Tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/larksuite/lark-mcp"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Lark Open Platform uses App Access Tokens (tenant_access_token) in Authorization header.", "url": "https://open.larksuite.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM", "quote": "Calls to Lark Open APIs require an access token passed as Authorization: Bearer <tenant_access_token>."},
            {"claim": "Self-serve custom app creation is available on open platform.", "url": "https://open.larksuite.com/", "quote": "Develop custom enterprise applications and bots on Lark Open Platform."}
        ],
        "confidence": "high",
        "notes": "Fast growing platform across APAC and international enterprise."
    },
    25: {
        "name": "Pumble",
        "category": "Communications and Messaging",
        "one_liner": "Team messaging and business chat application by Cake.com.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free tier available; bot tokens and API keys can be generated in workspace settings.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Pumble API uses Bearer bot tokens in the Authorization header.", "url": "https://pumble.com/help/integrations/api/", "quote": "Authenticate requests with the Pumble API using Bearer <bot_token> in the Authorization header."},
            {"claim": "Bots can be created inside the Pumble workspace.", "url": "https://pumble.com/help/integrations/bots/", "quote": "Create custom bots and configure permissions within your Pumble workspace."}
        ],
        "confidence": "high",
        "notes": "Cost-effective alternative to Slack."
    },
    26: {
        "name": "Discord",
        "category": "Communications and Messaging",
        "one_liner": "Community voice, video, and text communication service for servers and bots.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Discord Developer Portal provides instant self-serve bot token and OAuth2 application creation.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/discord"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Discord API authenticates bots via Bot tokens in Authorization header.", "url": "https://discord.com/developers/docs/reference#authentication", "quote": "API requests require an Authorization header with either Bot <token> or Bearer <token>."},
            {"claim": "Developer portal allows instant bot creation.", "url": "https://discord.com/developers/applications", "quote": "Create applications and configure bot users on the Discord Developer Portal."}
        ],
        "confidence": "high",
        "notes": "Bot token authentication is instant and frictionless."
    },
    27: {
        "name": "Telegram",
        "category": "Communications and Messaging",
        "one_liner": "Cloud-based mobile and desktop messaging app with extensive Bot API.",
        "auth_methods": ["Bearer/token", "API key"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Instant bot creation via @BotFather chat inside Telegram without signup forms or credit cards.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/telegram"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Telegram Bot API uses token directly in HTTP URL endpoint.", "url": "https://core.telegram.org/bots/api#authorizing-your-bot", "quote": "All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME."},
            {"claim": "BotFather provides instant self-serve bot tokens.", "url": "https://core.telegram.org/bots/tutorial#obtain-your-bot-token", "quote": "Talk to @BotFather and follow a few simple steps to get your authorization token."}
        ],
        "confidence": "high",
        "notes": "One of the most accessible bot platforms in the world."
    },
    28: {
        "name": "WhatsApp Business",
        "category": "Communications and Messaging",
        "one_liner": "Cloud API for sending and receiving WhatsApp messages for enterprise customer communication.",
        "auth_methods": ["Bearer/token", "OAuth2"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Meta for Developers provides free sandbox testing environment with temporary access tokens.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "community", "mcp_link": "https://github.com/modelcontextprotocol/servers/tree/main/src/whatsapp"},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "WhatsApp Business Cloud API authenticates via Bearer system or user tokens.", "url": "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started", "quote": "Include your access token in the Authorization header as Authorization: Bearer <ACCESS_TOKEN>."},
            {"claim": "Meta Developer portal provides free test phone number and sandbox.", "url": "https://developers.facebook.com/docs/whatsapp/cloud-api/overview", "quote": "Get started quickly with a Meta-provided test phone number and temporary access token."}
        ],
        "confidence": "high",
        "notes": "Production scale requires Meta Business verification, but developer sandbox is free and self-serve."
    },
    29: {
        "name": "Aircall",
        "category": "Communications and Messaging",
        "one_liner": "Cloud-based business phone system and call center software.",
        "auth_methods": ["Basic", "OAuth2", "API key"],
        "self_serve": "self_serve_trial",
        "self_serve_reason": "7-day free trial; API ID and API Token available under Company Settings > Integrations > API Keys.",
        "api_surface": {"type": "REST", "breadth": "medium", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Aircall Public API supports HTTP Basic Auth using api_id:api_token.", "url": "https://developer.aircall.io/api-references/#authentication", "quote": "The API uses HTTP Basic Authentication. Use your API ID as the username and API Token as the password."},
            {"claim": "API credentials can be generated in the Dashboard.", "url": "https://developer.aircall.io/tutorials/how-to-create-an-api-key/", "quote": "Create API keys in the Aircall Dashboard under Company Settings > Integrations."}
        ],
        "confidence": "high",
        "notes": "Well documented telephony events and webhooks."
    },
    30: {
        "name": "Vonage",
        "category": "Communications and Messaging",
        "one_liner": "Communications platform as a service (CPaaS) for SMS, voice, video, and verify APIs.",
        "auth_methods": ["Basic", "API key", "JWT"],
        "self_serve": "self_serve_free",
        "self_serve_reason": "Free account sign-up includes free trial credits, API Key, and API Secret on the dashboard.",
        "api_surface": {"type": "REST", "breadth": "large", "public_docs": True, "existing_mcp": "none", "mcp_link": None},
        "buildable_today": "yes",
        "main_blocker": "none",
        "evidence": [
            {"claim": "Vonage APIs authenticate using API key/secret or JSON Web Tokens (JWT).", "url": "https://developer.vonage.com/en/getting-started/concepts/authentication", "quote": "Vonage supports two main authentication methods: API key and secret for basic APIs, and JWTs for application-based APIs."},
            {"claim": "Developer account creation is free with initial credit.", "url": "https://dashboard.nexmo.com/sign-up", "quote": "Create a free Vonage API account and get free credit to start testing."}
        ],
        "confidence": "high",
        "notes": "Formerly Nexmo."
    }
}

print(f"Loaded {len(part2_data)} apps for part 2.")
