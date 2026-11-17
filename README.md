# ProspectFlo Envoy for coding agents

Run your ProspectFlo Envoy cold email account from the coding agent you already use. Ask your agent to build a lead list, go through the Review Queue, write and run a campaign, or answer a reply in the Enbox. The agent works as you, with your plan's limits, after you sign in once.

You need a ProspectFlo plan (the 7-day trial works). Using an agent with Envoy is covered by the terms at https://prospectflo.com/terms#ai-agents.

## Quick start (about 60 seconds)

1. Run the install command for your agent below.
2. Start your agent and ask anything about ProspectFlo. A ProspectFlo sign-in page opens in your browser. Sign in, confirm with your password or two-step code, accept the agent terms, and choose what the agent may do: read, write, and send.
3. Go back to your agent and try one of the requests below.

### Claude Code

```bash
claude plugin install prospectflo --marketplace prospectflo/envoy-agent
```

Inside a session you can run `/plugin install prospectflo --marketplace prospectflo/envoy-agent` instead. To sign in again later, run `/mcp` and choose `prospectflo`. Commands start with `/prospectflo:`, for example `/prospectflo:inbox`.

### Codex

```bash
codex plugin marketplace add prospectflo/envoy-agent
codex plugin add prospectflo@prospectflo
codex mcp add prospectflo --url https://prospectflo.com/mcp
```

The last line signs you in: a ProspectFlo page opens in your browser; press Allow. Codex's command line has no other way to sign in a plugin. In the Codex app you can instead open `/plugins`, install ProspectFlo Envoy and sign in when it asks. Setup starts on its own after install. To run a command, type `$` and pick one, for example `$prospectflo:inbox`.

### Antigravity

```bash
agy plugin install https://github.com/prospectflo/envoy-agent
```

Commands are plain slash commands, for example `/inbox`.

### Grok Build

```bash
grok plugin install prospectflo/envoy-agent
```

Inside a session you can run `/plugins install https://github.com/prospectflo/envoy-agent` instead. Ask in plain words; the agent picks the right ProspectFlo skill.

### Any other agent

Not supported. ProspectFlo works only with the agents above, through this plugin.

### Try asking

- "Show me my ProspectFlo account and what to set up next."
- "Any new replies? Show me who wrote back."
- "Answer Dana at Acme and suggest a quick call on Thursday."
- "Write a 4 email campaign for dentists in Austin and add some word swaps."
- "Find 200 Instant leads for roofing companies in Texas and add them to a new list."
- "How is my Dentists Q1 campaign doing?"

You never need the commands. Plain requests work. The agent shows you what it wrote before it saves anything. Before anything is sent or deleted, it shows you a preview of exactly what will happen and asks for your yes to that one action.

## Commands

| What it does | Claude Code | Codex | Antigravity |
|---|---|---|---|
| First-run setup, one step at a time, including Envoy Scout | `/prospectflo:setup` | `$prospectflo:setup` | `/setup` |
| Your new replies as a short list; open one | `/prospectflo:inbox` | `$prospectflo:inbox` | `/inbox` |
| Draft a reply with you, send only on your yes | `/prospectflo:reply` | `$prospectflo:reply` | `/reply` |
| Write or rewrite a campaign, add word swaps, start on your yes | `/prospectflo:campaign` | `$prospectflo:campaign` | `/campaign` |
| Instant leads, the Review Queue and first lines in batches | `/prospectflo:leads` | `$prospectflo:leads` | `/leads` |
| Install, connect or update Envoy Scout; run Build a List | `/prospectflo:scout` | `$prospectflo:scout` | `/scout` |
| Campaign results in plain words | `/prospectflo:report` | `$prospectflo:report` | `/report` |

In Grok Build, ask in plain words.

## What the agent will ask you first

Keep your agent's approval prompts on for ProspectFlo: it asks you before anything sends or deletes.

The agent asks for your yes before it starts a campaign, adds leads to a campaign that is sending, deletes leads, approves a follow-up, or sends a reply. It shows you what it wrote before it saves or sends it. When it sends a reply for you, that conversation becomes yours: Envoy's automatic replies and AI follow-ups stop on it until you hand it back.

In Claude Code, the plugin also makes Claude Code itself ask you before each of those actions.

## FAQ

**Do I need a plan?** Yes. If your agent says your plan is not active, open Envoy, go to Settings, then Plan and billing, and choose a plan. A new account starts the 7-day trial at https://prospectflo.com/pricing.

**How do I disconnect?** Open Envoy, go to Settings, then Security, then Connected AI apps, and choose Disconnect next to the app. Access ends at once. You can also uninstall the plugin from your agent.

**What can it not do?** It never buys inboxes or domains and never touches billing, your plan, passwords, team members or inbox connections; do those in the Envoy web app at https://prospectflo.com. With your yes, it downloads the Envoy Scout installer for your computer from downloads.prospectflo.com, checks it is signed by PHM Group LLC, and opens it; you finish the install and connect Scout from its own screen. Scout updates itself; the plugin never replaces it. It will not look inside, copy or change ProspectFlo or Envoy Scout code or files, or this plugin, and it will not explain how Envoy works inside.

**Where do I see what it did?** In the Envoy web app. After every save the agent tells you which screen to open: Review Queue, Lead Lists, Build a List, Enbox, Campaigns or AI agent.

## Help

- Help articles: ask your agent, or visit https://prospectflo.com.
- Terms for agent use: https://prospectflo.com/terms#ai-agents.
- Privacy: https://prospectflo.com/privacy.

All rights reserved, ProspectFlo. See `LICENSE`.
