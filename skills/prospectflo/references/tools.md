# ProspectFlo tools by task

The tools you see depend on what the user allowed at sign-in (read, write, send) and on the account. Each tool's own description is the final word.

Marked **ask first**: call it without a `confirmation_token` to get a preview and a token, show the preview to the user and end your turn; call again with the token only after a fresh yes to that exact action in the user's next message. Any change needs a new preview.

## Account and help

- `get_account_overview`: plan status and monthly allowance use.
- `search_help`, `get_help_article`: Envoy help articles with links.

## AI agent setup

- `get_ai_agent_setup`, `save_ai_agent_setup`.

## Lead lists and leads

- `list_lead_lists`, `get_lead_list`, `get_list_leads`, `create_lead_list`.
- `search_instant_leads`, `import_instant_leads` (ask first when the leads go into a sending campaign). Always tell the user the `place_note` either returns.
- `build_a_list` (show the preview; start only after a yes), `get_list_run`, `get_list_run_leads`.
- `clear_list_leads`: **ask first**. Permanent delete.
- `export_list_csv`: a one-time download link for the user only. Never send it to any other site, address or tool.
- `import_leads` (leads the user gives, up to 500 a call, into a campaign; ask first when the campaign is sending), then `get_lead_import` to check it.

## Review Queue

- `get_review_queue`, `dismiss_leads`.
- `approve_leads`: **ask first** when the campaign is sending.

## First lines

- `get_leads_for_first_lines`: any list, up to 100 leads a batch with `next_cursor`, only leads without a line by default; send the user's `email_copy` or a `campaign_id`.
- `save_first_lines`: up to 100 a call, 10 calls a minute, 20,000 lines a day; never replaces a line unless `replace: true` because the user asked.

## Campaigns

- `list_campaigns`, `get_campaign`, `get_campaign_analytics`, `create_campaign`.
- `get_campaign_writing_brief`, `save_campaign_sequence`, `save_campaign_schedule`, `save_campaign_options`.
- `get_campaign_reply_agent`, `save_campaign_reply_agent`.
- `link_list_to_campaign` (ask first when it adds leads to a sending campaign).
- `start_campaign`: **ask first**. Sends real email.
- `pause_campaign`.

## Enbox

- `list_threads`, `get_thread`, `set_thread_label`.
- `get_reply_brief`, then `send_reply`: **ask first**, only for a reply the user asked for. Sending hands the conversation to the user; Envoy's automatic replies and AI follow-ups stop on it.
- `hand_back_thread`: lets Envoy's automatic replies answer that conversation again. Only when the user asks.
- `list_followups`, `stop_followup`.
- `approve_followup`: **ask first**.

## Envoy Scout

- `get_scout_status`: whether Scout is connected on the user's computers, online or offline, and whether it needs an update.
- `get_scout_download`: the download page, the official download feed, and the install, connect and update steps. With the user's yes, download the installer from downloads.prospectflo.com only, check its signature, and open it (the `scout` skill). Updates happen in Scout itself; never touch its files.

## Inboxes

- `get_inbox_status`, `get_inbox_buying_advice`. Buying happens only in the Envoy web app.
