# ProspectFlo Envoy for coding agents

Run your ProspectFlo Envoy cold email account from the coding agent you already use. Ask your agent to set up your account, guide inbox connections or prepare an inbox checkout link, upload and verify leads, build a lead list, write and run a campaign, manage Auto-Reply, or answer a reply in the Enbox. The agent works as you, with your plan's limits, after you sign in once.

You need a ProspectFlo plan (the 7-day trial works). Using an agent with Envoy is covered by the terms at https://prospectflo.com/terms#ai-agents.

## Quick start (about 60 seconds, no terminal needed)

1. Copy the message for your agent below and paste it straight into your agent chat (or run the terminal command if you prefer). Your agent downloads and installs the ProspectFlo plugin for you.
2. When a ProspectFlo sign-in page opens in your browser, sign in, confirm with your password or two-step code, accept the agent terms, and choose what the agent may do: read, write, and send.
3. Go back to your agent and follow the guided setup.

### Claude Code

```bash
claude plugin install prospectflo --marketplace prospectflo/envoy-agent
```

No terminal needed: paste this straight into Claude:

> Install the ProspectFlo plugin from prospectflo/envoy-agent (run `/plugin install prospectflo --marketplace prospectflo/envoy-agent` or `claude plugin install prospectflo --marketplace prospectflo/envoy-agent`), connect my ProspectFlo account, and run `/prospectflo:setup`.

Using Claude Desktop, Cowork, or claude.ai without Claude Code? Open **Customize -> Connectors -> Add custom connector** and paste `https://prospectflo.com/mcp`. To sign in again later in Claude Code, run `/mcp` and choose `prospectflo`. Commands start with `/prospectflo:`, for example `/prospectflo:inbox`.

### Codex

```bash
codex plugin marketplace add prospectflo/envoy-agent
codex plugin add prospectflo@prospectflo
codex mcp add prospectflo --url https://prospectflo.com/mcp
```

No terminal needed: paste this straight into Codex:

> Install the ProspectFlo plugin from prospectflo/envoy-agent (`codex plugin marketplace add prospectflo/envoy-agent` and `codex plugin add prospectflo@prospectflo`), connect my ProspectFlo account at `https://prospectflo.com/mcp`, and run `$prospectflo:setup`.

The last line signs you in: a ProspectFlo page opens in your browser; press Allow. In the Codex app you can also open `/plugins`, install ProspectFlo Envoy and sign in when it asks. To run a command, type `$` and pick one, for example `$prospectflo:inbox`.

### Antigravity

```bash
agy plugin install https://github.com/prospectflo/envoy-agent
```

No terminal needed: paste this straight into Antigravity:

> Install the ProspectFlo plugin from https://github.com/prospectflo/envoy-agent (`agy plugin install https://github.com/prospectflo/envoy-agent`), connect my ProspectFlo account, and run `/setup`.

Commands are plain slash commands, for example `/inbox`.

### Grok Build

```bash
grok plugin install prospectflo/envoy-agent
```

No terminal needed: paste this straight into Grok Build:

> Install the ProspectFlo plugin from prospectflo/envoy-agent (`grok plugin install prospectflo/envoy-agent` or `/plugins install https://github.com/prospectflo/envoy-agent`), connect my ProspectFlo account, and set up my ProspectFlo account.

Ask in plain words; the agent picks the right ProspectFlo skill.

### Cursor

No terminal needed: paste this straight into Cursor:

> Add the ProspectFlo server at `https://prospectflo.com/mcp` to your Cursor config file in my home folder, tell me when to restart and turn on `prospectflo` under Customize, and then set up my ProspectFlo account.

Or add it to `.cursor/mcp.json` in your home folder (create the file if it is missing; if it already lists other servers, add only the `prospectflo` entry):

```json
{
  "mcpServers": {
    "prospectflo": {
      "url": "https://prospectflo.com/mcp"
    }
  }
}
```

Restart Cursor, then turn on `prospectflo` under Customize. A ProspectFlo page opens in your browser: sign in and press Allow. Ask in plain words; Cursor has no ProspectFlo commands.

### Any other agent

Not supported. ProspectFlo works only with the agents above.

### Try asking

- "Set up my ProspectFlo account."
- "Check my sending inboxes, or quote 3 new Google Workspace inboxes."
- "Any new replies? Show me who wrote back."
- "Answer Dana at Acme and suggest a quick call on Thursday."
- "Turn on Auto-Reply, or schedule a weekday reply check that asks before sending."
- "Write a 4 email campaign for dentists in Austin and add some word swaps."
- "Upload and verify leads from my Google Sheet, or find 200 Instant leads for roofing companies in Texas."
- "How is my Dentists Q1 campaign doing?"

You never need the commands. Plain requests work. The agent shows you what it wrote before it saves anything. Before anything sends, deletes, prepares an inbox checkout order or turns on Auto-Reply, it shows you a preview of exactly what will happen and asks for your yes to that one action.

## Commands

| What it does | Claude Code | Codex | Antigravity |
|---|---|---|---|
| Full account audit and step-by-step setup, from business facts to first campaign | `/prospectflo:setup` | `$prospectflo:setup` | `/setup` |
| Check inbox health, get connection guides, or quote and prepare inbox checkout | `/prospectflo:inboxes` | `$prospectflo:inboxes` | `/inboxes` |
| Turn on guarded Auto-Reply or schedule an approval-first reply check | `/prospectflo:autoreply` | `$prospectflo:autoreply` | `/autoreply` |
| Your new replies as a short list; open, compose or manage threads | `/prospectflo:inbox` | `$prospectflo:inbox` | `/inbox` |
| Draft a reply with you, send only on your yes | `/prospectflo:reply` | `$prospectflo:reply` | `/reply` |
| Write or rewrite a campaign, add word swaps, configure options, start on your yes | `/prospectflo:campaign` | `$prospectflo:campaign` | `/campaign` |
| Instant leads, Google Sheet or CSV upload, verify, enrich, Review Queue and first lines | `/prospectflo:leads` | `$prospectflo:leads` | `/leads` |
| Install, connect or update Envoy Scout; run Build a List | `/prospectflo:scout` | `$prospectflo:scout` | `/scout` |
| Campaign results in plain words | `/prospectflo:report` | `$prospectflo:report` | `/report` |

In Grok Build and Cursor, ask in plain words.

## What the agent will ask you first

Keep your agent's approval prompts on for ProspectFlo: it asks you before anything sends or deletes.

The agent asks for your yes before it starts a campaign, adds leads to a campaign that is sending, updates a campaign that is sending, prepares an inbox checkout order or discards an unpaid one, turns on Auto-Reply, deletes or archives a list or campaign, approves a follow-up, composes a new email or sends a reply. It shows you what it wrote before it saves or sends it. When it sends a reply for you, that conversation becomes yours: Envoy's automatic replies and AI follow-ups stop on it until you hand it back.

In Claude Code, the plugin also makes Claude Code itself ask you before each of those actions.

## FAQ

**Do I need a plan?** Yes. If your agent says your plan is not active, open Envoy, go to Settings, then Plan and billing, and choose a plan. A new account starts the 7-day trial at https://prospectflo.com/pricing.

**How do I disconnect?** Open Envoy, go to Settings, then Security, then Connected AI apps, and choose Disconnect next to the app. Access ends at once. You can also uninstall the plugin from your agent.

**What can it not do?** It never accepts your email passwords or signs in to your email accounts for you, and it never charges a card, changes your plan, cancels subscriptions, issues refunds or changes team members. When you ask for new inboxes, it can check domains, quote an order and prepare a Stripe Checkout link so you only complete payment yourself. For inbox connections, it gives step-by-step instructions and direct links to the Envoy web app at https://prospectflo.com. With your yes, it downloads the Envoy Scout installer for your computer from downloads.prospectflo.com, checks it is signed by PHM Group LLC, and opens it; you finish the install and connect Scout from its own screen. Scout updates itself; the plugin never replaces it. It will not look inside, copy or change ProspectFlo or Envoy Scout code or files, or this plugin, and it will not explain how Envoy works inside.

**Where do I see what it did?** In the Envoy web app. After every save the agent tells you which screen to open: Leads, Build a List, Enbox, Campaigns, AI agent or Inboxes & Infrastructure.

## Help

- Help articles: ask your agent, or visit https://prospectflo.com.
- Terms for agent use: https://prospectflo.com/terms#ai-agents.
- Privacy: https://prospectflo.com/privacy.

All rights reserved, ProspectFlo. See `LICENSE`.
