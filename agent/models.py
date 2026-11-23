"""Data models and schema definitions for the Composio App Research Agent."""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class EvidenceItem(BaseModel):
    claim: str = Field(description="The specific fact or claim being supported")
    url: str = Field(description="Exact URL of the official documentation or article")
    quote: str = Field(description="Verbatim text quote from the page proving the claim")


class ApiSurface(BaseModel):
    type: str = Field(
        description="Type of API surface (e.g., REST, GraphQL, REST / GraphQL, SDK, CLI-only, none)"
    )
    breadth: Literal["small", "medium", "large", "none", "unclear"] = Field(
        description="Rough scale of API breadth"
    )
    public_docs: bool = Field(description="Whether official public documentation is accessible")
    existing_mcp: Literal["none", "official", "community"] = Field(
        description="Whether an MCP server exists"
    )
    mcp_link: Optional[str] = Field(default=None, description="Link or reference to existing MCP repository/server")


class AppResearchRecord(BaseModel):
    id: int
    name: str
    category: str
    one_liner: str
    auth_methods: List[str] = Field(
        description="Auth methods supported: OAuth2, API key, Basic, Bearer/token, JWT, other, none"
    )
    self_serve: str = Field(
        description="One of: self_serve_free, self_serve_trial, paid_plan_required, admin_approval, partner_or_contact_sales, no_public_api, unclear"
    )
    self_serve_reason: str = Field(description="Short reason explaining self-serve status")
    api_surface: ApiSurface
    buildable_today: Literal["yes", "partial", "no"] = Field(
        description="Could this be an agent toolkit today"
    )
    main_blocker: str = Field(
        description="Main blocker if not (e.g., none, partner gate, paid-only, approval review, CLI-only, no API, unclear docs)"
    )
    evidence: List[EvidenceItem] = Field(
        default_factory=list,
        description="List of evidence backing each claim with exact URL and verbatim quote"
    )
    confidence: Literal["high", "medium", "low"]
    notes: str = ""
    needs_human: bool = False
    human_reason: Optional[str] = None
