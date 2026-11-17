# ProspectFlo tools by task

The tools you see depend on what the user allowed at sign-in (read, write, send) and on the account. Each tool's own description is the final word.

Marked **ask first**: send `confirm: true` only after the user says yes to that exact action.

## Account and help

- `get_account_overview`: plan status and monthly allowance use.
- `search_help`, `get_help_article`: Envoy help articles with links.

## AI agent setup

- `get_ai_agent_setup`, `save_ai_agent_setup`.

## Lead lists and leads

- `list_lead_lists`, `get_lead_list`, `get_list_leads`, `create_lead_list`.
- `search_instant_leads`, `import_instant_leads` (ask first when the leads go into a sending campaign).
- `build_a_list` (show the preview; start only after a yes), `get_list_run`, `get_list_run_leads`.
- `clear_list_leads`: **ask first**. Permanent delete.
- `export_list_csv`: a one-time download link for the user.

## Review Queue

- `get_review_queue`, `dismiss_leads`.
- `approve_leads`: **ask first** when the campaign is sending.

## First lines

- `get_leads_for_first_lines`, `save_first_lines`.

## Campaigns

- `list_campaigns`, `get_campaign`, `get_campaign_analytics`, `create_campaign`.
- `get_campaign_writing_brief`, `save_campaign_sequence`, `save_campaign_schedule`, `save_campaign_options`.
- `get_campaign_reply_agent`, `save_campaign_reply_agent`.
- `link_list_to_campaign` (ask first when it adds leads to a sending campaign).
- `start_campaign`: **ask first**. Sends real email.
- `pause_campaign`.

## Enbox

- `list_threads`, `get_thread`, `set_thread_label`.
- `get_reply_brief`, then `send_reply`: **ask first**, only for a reply the user asked for.
- `list_followups`, `stop_followup`.
- `approve_followup`: **ask first**.

## Inboxes

- `get_inbox_status`, `get_inbox_buying_advice`. Buying happens only in the Envoy web app.
