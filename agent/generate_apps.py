import json
import os

apps = [
    # 1. CRM and Sales
    {"id": 1, "name": "Salesforce", "category": "CRM and Sales", "website_hint": "https://developer.salesforce.com/"},
    {"id": 2, "name": "HubSpot", "category": "CRM and Sales", "website_hint": "https://developers.hubspot.com/"},
    {"id": 3, "name": "Pipedrive", "category": "CRM and Sales", "website_hint": "https://developers.pipedrive.com/"},
    {"id": 4, "name": "Attio", "category": "CRM and Sales", "website_hint": "https://developers.attio.com/"},
    {"id": 5, "name": "Twenty", "category": "CRM and Sales", "website_hint": "https://twenty.com/"},
    {"id": 6, "name": "Podio", "category": "CRM and Sales", "website_hint": "https://developers.podio.com/"},
    {"id": 7, "name": "Zoho CRM", "category": "CRM and Sales", "website_hint": "https://www.zoho.com/crm/developer/"},
    {"id": 8, "name": "Close", "category": "CRM and Sales", "website_hint": "https://developer.close.com/"},
    {"id": 9, "name": "Copper", "category": "CRM and Sales", "website_hint": "https://developer.copper.com/"},
    {"id": 10, "name": "DealCloud", "category": "CRM and Sales", "website_hint": "https://api.docs.dealcloud.com/"},

    # 2. Support and Helpdesk
    {"id": 11, "name": "Zendesk", "category": "Support and Helpdesk", "website_hint": "https://developer.zendesk.com/"},
    {"id": 12, "name": "Intercom", "category": "Support and Helpdesk", "website_hint": "https://developers.intercom.com/"},
    {"id": 13, "name": "Freshdesk", "category": "Support and Helpdesk", "website_hint": "https://developers.freshdesk.com/"},
    {"id": 14, "name": "Front", "category": "Support and Helpdesk", "website_hint": "https://dev.frontapp.com/"},
    {"id": 15, "name": "Pylon", "category": "Support and Helpdesk", "website_hint": "https://docs.usepylon.com/"},
    {"id": 16, "name": "LiveAgent", "category": "Support and Helpdesk", "website_hint": "https://support.liveagent.com/849508-LiveAgent-REST-API-v3"},
    {"id": 17, "name": "Plain", "category": "Support and Helpdesk", "website_hint": "https://www.plain.com/docs"},
    {"id": 18, "name": "Help Scout", "category": "Support and Helpdesk", "website_hint": "https://developer.helpscout.com/"},
    {"id": 19, "name": "Gorgias", "category": "Support and Helpdesk", "website_hint": "https://developers.gorgias.com/"},
    {"id": 20, "name": "Gladly", "category": "Support and Helpdesk", "website_hint": "https://developer.gladly.com/"},

    # 3. Communications and Messaging
    {"id": 21, "name": "Slack", "category": "Communications and Messaging", "website_hint": "https://api.slack.com/"},
    {"id": 22, "name": "Twilio", "category": "Communications and Messaging", "website_hint": "https://www.twilio.com/docs"},
    {"id": 23, "name": "Zoho Cliq", "category": "Communications and Messaging", "website_hint": "https://www.zoho.com/cliq/help/restapi/"},
    {"id": 24, "name": "Lark (Larksuite)", "category": "Communications and Messaging", "website_hint": "https://open.larksuite.com/"},
    {"id": 25, "name": "Pumble", "category": "Communications and Messaging", "website_hint": "https://pumble.com/help/integrations/api/"},
    {"id": 26, "name": "Discord", "category": "Communications and Messaging", "website_hint": "https://discord.com/developers/docs"},
    {"id": 27, "name": "Telegram", "category": "Communications and Messaging", "website_hint": "https://core.telegram.org/bots/api"},
    {"id": 28, "name": "WhatsApp Business", "category": "Communications and Messaging", "website_hint": "https://developers.facebook.com/docs/whatsapp"},
    {"id": 29, "name": "Aircall", "category": "Communications and Messaging", "website_hint": "https://developer.aircall.io/"},
    {"id": 30, "name": "Vonage", "category": "Communications and Messaging", "website_hint": "https://developer.vonage.com/"},

    # 4. Marketing, Ads, Email and Social
    {"id": 31, "name": "Google Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "https://developers.google.com/google-ads"},
    {"id": 32, "name": "Meta Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "https://developers.facebook.com/docs/marketing-apis"},
    {"id": 33, "name": "LinkedIn Ads", "category": "Marketing, Ads, Email and Social", "website_hint": "https://learn.microsoft.com/linkedin/marketing"},
    {"id": 34, "name": "GoHighLevel", "category": "Marketing, Ads, Email and Social", "website_hint": "https://highlevel.stoplight.io/"},
    {"id": 35, "name": "Mailchimp", "category": "Marketing, Ads, Email and Social", "website_hint": "https://mailchimp.com/developer/"},
    {"id": 36, "name": "Klaviyo", "category": "Marketing, Ads, Email and Social", "website_hint": "https://developers.klaviyo.com/"},
    {"id": 37, "name": "systeme.io", "category": "Marketing, Ads, Email and Social", "website_hint": "https://systeme.io/"},
    {"id": 38, "name": "Pinterest", "category": "Marketing, Ads, Email and Social", "website_hint": "https://developers.pinterest.com/"},
    {"id": 39, "name": "Threads (Meta)", "category": "Marketing, Ads, Email and Social", "website_hint": "https://developers.facebook.com/docs/threads"},
    {"id": 40, "name": "SendGrid", "category": "Marketing, Ads, Email and Social", "website_hint": "https://docs.sendgrid.com/api-reference"},

    # 5. Ecommerce
    {"id": 41, "name": "Shopify", "category": "Ecommerce", "website_hint": "https://shopify.dev/"},
    {"id": 42, "name": "WooCommerce", "category": "Ecommerce", "website_hint": "https://woocommerce.com/document/woocommerce-rest-api"},
    {"id": 43, "name": "BigCommerce", "category": "Ecommerce", "website_hint": "https://developer.bigcommerce.com/"},
    {"id": 44, "name": "Salesforce Commerce Cloud", "category": "Ecommerce", "website_hint": "https://developer.salesforce.com/docs/commerce"},
    {"id": 45, "name": "Magento (Adobe Commerce)", "category": "Ecommerce", "website_hint": "https://developer.adobe.com/commerce"},
    {"id": 46, "name": "Squarespace", "category": "Ecommerce", "website_hint": "https://developers.squarespace.com/"},
    {"id": 47, "name": "Ecwid", "category": "Ecommerce", "website_hint": "https://api-docs.ecwid.com/"},
    {"id": 48, "name": "Gumroad", "category": "Ecommerce", "website_hint": "https://gumroad.com/api"},
    {"id": 49, "name": "Amazon Selling Partner", "category": "Ecommerce", "website_hint": "https://developer-docs.amazon.com/sp-api"},
    {"id": 50, "name": "fanbasis", "category": "Ecommerce", "website_hint": "https://fanbasis.com/"},

    # 6. Data, SEO and Scraping
    {"id": 51, "name": "DataForSEO", "category": "Data, SEO and Scraping", "website_hint": "https://docs.dataforseo.com/"},
    {"id": 52, "name": "SE Ranking", "category": "Data, SEO and Scraping", "website_hint": "https://seranking.com/api"},
    {"id": 53, "name": "Ahrefs", "category": "Data, SEO and Scraping", "website_hint": "https://ahrefs.com/api"},
    {"id": 54, "name": "MrScraper", "category": "Data, SEO and Scraping", "website_hint": "https://docs.mrscraper.com/"},
    {"id": 55, "name": "Apify", "category": "Data, SEO and Scraping", "website_hint": "https://docs.apify.com/"},
    {"id": 56, "name": "Firecrawl", "category": "Data, SEO and Scraping", "website_hint": "https://docs.firecrawl.dev/"},
    {"id": 57, "name": "Bright Data", "category": "Data, SEO and Scraping", "website_hint": "https://brightdata.com/"},
    {"id": 58, "name": "Sherlock", "category": "Data, SEO and Scraping", "website_hint": "https://github.com/sherlock-project/sherlock"},
    {"id": 59, "name": "Waterfall.io", "category": "Data, SEO and Scraping", "website_hint": "https://waterfall.io/"},
    {"id": 60, "name": "Clay", "category": "Data, SEO and Scraping", "website_hint": "https://clay.com/"},

    # 7. Developer, Infra and Data platforms
    {"id": 61, "name": "GitHub", "category": "Developer, Infra and Data platforms", "website_hint": "https://docs.github.com/rest"},
    {"id": 62, "name": "Vercel", "category": "Developer, Infra and Data platforms", "website_hint": "https://vercel.com/docs/rest-api"},
    {"id": 63, "name": "Netlify", "category": "Developer, Infra and Data platforms", "website_hint": "https://docs.netlify.com/api"},
    {"id": 64, "name": "Cloudflare", "category": "Developer, Infra and Data platforms", "website_hint": "https://developers.cloudflare.com/api"},
    {"id": 65, "name": "Supabase", "category": "Developer, Infra and Data platforms", "website_hint": "https://supabase.com/docs"},
    {"id": 66, "name": "Neo4j", "category": "Developer, Infra and Data platforms", "website_hint": "https://neo4j.com/docs/api"},
    {"id": 67, "name": "Snowflake", "category": "Developer, Infra and Data platforms", "website_hint": "https://docs.snowflake.com/"},
    {"id": 68, "name": "MongoDB Atlas", "category": "Developer, Infra and Data platforms", "website_hint": "https://mongodb.com/docs/atlas/api"},
    {"id": 69, "name": "Datadog", "category": "Developer, Infra and Data platforms", "website_hint": "https://docs.datadoghq.com/api"},
    {"id": 70, "name": "Sentry", "category": "Developer, Infra and Data platforms", "website_hint": "https://docs.sentry.io/api"},

    # 8. Productivity and Project Management
    {"id": 71, "name": "Notion", "category": "Productivity and Project Management", "website_hint": "https://developers.notion.com/"},
    {"id": 72, "name": "Airtable", "category": "Productivity and Project Management", "website_hint": "https://airtable.com/developers"},
    {"id": 73, "name": "Linear", "category": "Productivity and Project Management", "website_hint": "https://developers.linear.app/"},
    {"id": 74, "name": "Jira", "category": "Productivity and Project Management", "website_hint": "https://developer.atlassian.com/"},
    {"id": 75, "name": "Asana", "category": "Productivity and Project Management", "website_hint": "https://developers.asana.com/"},
    {"id": 76, "name": "Monday.com", "category": "Productivity and Project Management", "website_hint": "https://developer.monday.com/"},
    {"id": 77, "name": "ClickUp", "category": "Productivity and Project Management", "website_hint": "https://clickup.com/api"},
    {"id": 78, "name": "Coda", "category": "Productivity and Project Management", "website_hint": "https://coda.io/developers"},
    {"id": 79, "name": "Smartsheet", "category": "Productivity and Project Management", "website_hint": "https://smartsheet.com/developers"},
    {"id": 80, "name": "Harvest", "category": "Productivity and Project Management", "website_hint": "https://help.getharvest.com/api-v2"},

    # 9. Finance and Fintech
    {"id": 81, "name": "Stripe", "category": "Finance and Fintech", "website_hint": "https://stripe.com/docs/api"},
    {"id": 82, "name": "Plaid", "category": "Finance and Fintech", "website_hint": "https://plaid.com/docs"},
    {"id": 83, "name": "Binance", "category": "Finance and Fintech", "website_hint": "https://binance-docs.github.io/apidocs/spot/en/"},
    {"id": 84, "name": "Paygent Connect", "category": "Finance and Fintech", "website_hint": "https://www.nmi.com/solutions/payment-gateway/"},
    {"id": 85, "name": "iPayX", "category": "Finance and Fintech", "website_hint": "https://ipayx.ai/docs"},
    {"id": 86, "name": "QuickBooks", "category": "Finance and Fintech", "website_hint": "https://developer.intuit.com/"},
    {"id": 87, "name": "Xero", "category": "Finance and Fintech", "website_hint": "https://developer.xero.com/"},
    {"id": 88, "name": "Brex", "category": "Finance and Fintech", "website_hint": "https://developer.brex.com/"},
    {"id": 89, "name": "Ramp", "category": "Finance and Fintech", "website_hint": "https://docs.ramp.com/"},
    {"id": 90, "name": "PitchBook", "category": "Finance and Fintech", "website_hint": "https://pitchbook.com/products/data/api"},

    # 10. AI, Research and Media-native
    {"id": 91, "name": "NotebookLM", "category": "AI, Research and Media-native", "website_hint": "https://cloud.google.com/gemini"},
    {"id": 92, "name": "Otter AI", "category": "AI, Research and Media-native", "website_hint": "https://help.otter.ai/"},
    {"id": 93, "name": "Fathom", "category": "AI, Research and Media-native", "website_hint": "https://fathom.video/"},
    {"id": 94, "name": "Consensus", "category": "AI, Research and Media-native", "website_hint": "https://consensus.app/"},
    {"id": 95, "name": "Reducto", "category": "AI, Research and Media-native", "website_hint": "https://reducto.ai/"},
    {"id": 96, "name": "Devin", "category": "AI, Research and Media-native", "website_hint": "https://docs.devin.ai/"},
    {"id": 97, "name": "higgsfield", "category": "AI, Research and Media-native", "website_hint": "https://higgsfield.ai/cli"},
    {"id": 98, "name": "Mermaid CLI", "category": "AI, Research and Media-native", "website_hint": "https://github.com/mermaid-js/mermaid-cli"},
    {"id": 99, "name": "YouTube Transcript", "category": "AI, Research and Media-native", "website_hint": "https://transcriptapi.com/"},
    {"id": 100, "name": "Grain", "category": "AI, Research and Media-native", "website_hint": "https://grain.com/"}
]

out_dir = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "apps.json")

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(apps, f, indent=2)

print(f"Successfully generated {len(apps)} apps in {out_file}")
