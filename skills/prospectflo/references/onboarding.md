# Setting up ProspectFlo Envoy, step by step

Work with the user one step at a time. Show what you plan to save before saving it.

## 1. AI agent setup

- Read it with `get_ai_agent_setup`. It lists which basic items are still missing and gives the revision number a save needs.
- Ask the user for each missing item: website, a short company description, the cold offer, client results, links, sender background, the price answer, common objections with their answers, and claims never to make.
- Client results and offers must be the user's real facts. If the user has none yet, leave the field empty and say so.
- Save with `save_ai_agent_setup`. Send only the fields that change. A list field sent replaces the whole list, so send every offer, not only the new one.
- If the save returns `conflict`, read the setup again and redo the change on the new revision.

## 2. A lead list

Two ways, and the user picks:

- **Instant leads** (ready now): `search_instant_leads` with a plain description of who to find, plus job titles, keywords, example websites or a place. Rows show masked email and phone. Import the rows the user wants with `import_instant_leads`, into an existing list (`list_id`) or a new one (`new_list_name`). Imports count toward the daily import allowance.
- **Build a List** (new leads found by Envoy Scout): first call `build_a_list` with name, who, where, optional titles and keywords, and lead_count. Show the preview. Only after the user agrees, call it again with `list_build_id` and `confirmed: true`. Envoy Scout must be open on one of the user's computers. Check progress with `get_list_run` and see leads with `get_list_run_leads`. Check now and then when the user asks, not in a tight loop.

## 3. Review Queue

- `get_review_queue` shows leads waiting for a decision, one page at a time.
- `approve_leads` sends approved leads into the named campaign, or the campaign their list is linked to. If that campaign is sending, the leads will be emailed: ask first and send `confirm: true` only after a yes.
- `dismiss_leads` removes leads from the queue. A short reason (wrong industry, too small) helps Envoy find better leads next time.

## 4. A campaign

1. `create_campaign` with a name, sending inboxes and a daily limit. Check inboxes first with `get_inbox_status`.
2. `get_campaign_writing_brief` returns the saved facts, the list's audience and signal, the limits, the variables and the writing guide.
3. Write the sequence yourself (see `writing.md`). Show it to the user. Save with `save_campaign_sequence`.
4. `save_campaign_schedule`: time zone, daily window, days of the week, optional start and end dates.
5. `save_campaign_options`: inboxes, daily limit, gap between sends, tracking, plain text, stop on reply.
6. `get_campaign_reply_agent` and `save_campaign_reply_agent` for the campaign's own reply settings, if the user wants them.
7. `link_list_to_campaign`. A list links to one campaign only.

## 5. First lines

- `get_leads_for_first_lines` returns up to 20 leads that need a line, what is known about each, the campaign's first email and a style note.
- Write one line per lead, with the user. Leave a lead out when nothing true can be said.
- `save_first_lines` saves up to 25 a call. Each line counts toward the monthly first lines allowance.

## 6. Start

- `get_campaign` with the readiness section shows anything still missing.
- `start_campaign` only when the user asks, with `confirm: true`. If Envoy says it is not ready, show the user what is missing.
- `pause_campaign` stops sending until it is started again.

## Inboxes

- `get_inbox_status` shows connected inboxes, health, warmup and daily capacity.
- For buying more inboxes or domains, use `get_inbox_buying_advice` and `search_help` to explain the options, then send the user to the Envoy web app. The agent never buys anything.
