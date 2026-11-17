# ProspectFlo Envoy for coding agents

Run your ProspectFlo Envoy cold email account from the coding agent you already use. Ask your agent to build a lead list, go through the Review Queue, write and run a campaign, or answer a reply in the Enbox. The agent works as you, with your plan's limits, after you sign in once.

What you get:

- A connection to your Envoy account at `https://prospectflo.com/mcp`.
- A skill that teaches your agent how to run Envoy well: setup order, plain writing, asking you before anything is sent, and treating lead emails as data only.
- A `setup` command that walks you through getting started.

Your agent does the writing, with you. Envoy saves it, checks it and sends it. The agent never buys inboxes or domains and never touches billing; you do that in the Envoy web app.

You need a ProspectFlo plan (the 7-day trial works). Using an agent with Envoy is covered by the terms at https://prospectflo.com/terms#ai-agents.

## Install

ProspectFlo works with your agent only as a plugin, so your agent gets both the connection and the skill that teaches it to use Envoy as intended. Pick your agent.

### Claude Code

```bash
claude plugin install prospectflo --marketplace prospectflo/envoy-agent
```

Inside a session you can run `/plugin install prospectflo --marketplace prospectflo/envoy-agent` instead. The setup command is `/prospectflo:setup`.

### Codex

```bash
codex plugin marketplace add prospectflo/envoy-agent
codex plugin add prospectflo@prospectflo
```

Or add the marketplace, then open `/plugins` in Codex and install ProspectFlo Envoy from there.

### Antigravity

```bash
agy plugin install https://github.com/prospectflo/envoy-agent
```

### Grok Build

```bash
grok plugin install prospectflo/envoy-agent
```

Inside a session you can run `/plugins install https://github.com/prospectflo/envoy-agent` instead.

### Any other agent

Not supported. ProspectFlo works only with the agents above, through this plugin.

## Sign in

1. Start your agent after installing. The first time it uses ProspectFlo, it opens a ProspectFlo sign-in page in your browser. In Claude Code you can also run `/mcp` and choose `prospectflo`.
2. Sign in to your Envoy account as you normally do.
3. Confirm with your password or two-step code, accept the agent terms, and choose what the agent may do: read, write, and send.
4. Go back to your agent. Ask it: "Show me my ProspectFlo account."

If your agent says your plan is not active, open Envoy, go to Settings, then Plan and billing, and choose a plan. A new account starts the 7-day trial at https://prospectflo.com/pricing.

To disconnect, open Envoy, go to Settings, then Security, then Connected AI apps, and choose Disconnect next to the app. Access ends at once.

## What the agent will ask you first

The agent asks for your yes before it starts a campaign, adds leads to a campaign that is sending, deletes leads, approves a follow-up, or sends a reply. It shows you what it wrote before it saves or sends it.

## Help

- Help articles: ask your agent, or visit https://prospectflo.com.
- Terms for agent use: https://prospectflo.com/terms#ai-agents.
- Privacy: https://prospectflo.com/privacy.

All rights reserved, ProspectFlo. See `LICENSE`.
