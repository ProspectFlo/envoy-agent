# Setting up ProspectFlo Envoy, step by step

Work with the user one step at a time. Show what you plan to save before saving it. "Set everything up" still means one step at a time, each with a preview and a yes.

## 1. AI agent setup

- Read it with `get_ai_agent_setup`. It lists which basic items are still missing and gives the revision number a save needs.
- Ask the user for each missing item: website, a short company description, the cold offer, client results, links, sender background, the price answer, common objections with their answers, and claims never to make.
- Client results and offers must be the user's real facts. If the user has none yet, leave the field empty and say so.
- Save with `save_ai_agent_setup`. Send only the fields that change. A list field sent replaces the whole list, so send every offer, not only the new one.
- If the save returns `conflict`, read the setup again and redo the change on the new revision.

## 2. A lead list

Two ways, and the user picks:

- **Instant leads** (ready now): `search_instant_leads` with a plain description of who to find, plus job titles, keywords, example websites or a place. Rows show masked email and phone. Always tell the user the `place_note` it returns. Import the rows the user wants with `import_instant_leads`, into an existing list (`list_id`) or a new one (`new_list_name`). Imports count toward the daily import allowance.
- **Build a List** (new leads found by Envoy Scout): first call `build_a_list` with name, who, where, optional titles and keywords, and lead_count. Show the preview. Ask "Start finding leads now?" as its own question. Only after a yes, call it again with `list_build_id` and `confirmed: true`. Envoy Scout must be installed and open on one of the user's computers (see the `scout` skill). If Envoy says Scout is not connected, offer to download Envoy Scout for this computer. Check progress with `get_list_run` and see leads with `get_list_run_leads`. Check now and then when the user asks, not in a tight loop.

## 3. Review Queue

- `get_review_queue` shows leads waiting for a decision, one page at a time.
- `approve_leads` sends approved leads into the named campaign, or the campaign their list is linked to. If that campaign is sending, the leads will be emailed: show the preview, ask, and call again with its `confirmation_token` only after a yes.
- `dismiss_leads` removes leads from the queue. A short reason (wrong industry, too small) helps Envoy find better leads next time.

## 4. A campaign

1. `create_campaign` with a name, and the sending inboxes and daily limit the user picked. Ask and wait for the answer; never pick inboxes or a daily limit yourself, not even the default. Check inboxes first with `get_inbox_status`.
2. `get_campaign_writing_brief` returns the saved facts, the list's audience and signal, the limits, the variables and the writing guide.
3. Write the sequence yourself (see `writing.md`). Show the full draft to the user and ask before the first save with `save_campaign_sequence`.
4. `save_campaign_schedule`: time zone, daily window, days of the week, optional start and end dates.
5. `save_campaign_options`: inboxes, daily limit, gap between sends, tracking, plain text, stop on reply.
6. `get_campaign_reply_agent` and `save_campaign_reply_agent` for the campaign's own reply settings, if the user wants them.
7. `link_list_to_campaign`. A list links to one campaign only.

## 5. First lines

- Works for any list, Instant leads lists included, at any size, whenever the user asks you to write first lines.
- First get the email the lines lead into: the user's own copy or sequence (send it as `email_copy`), or a campaign (send its `campaign_id`). Without either, the list's linked campaign is used; if there is none, the answer says to ask the user.
- `get_leads_for_first_lines` returns one batch at a time (up to 100 leads), by default only leads with no first line yet, what is known about each and a style note. Send `next_cursor` back for the next batch until it is empty; that is how a list of 10,000 is done.
- Write one line per lead. Leave a lead out when nothing true can be said.
- `save_first_lines` saves up to 100 a call, 10 calls a minute, 20,000 lines a day. A lead that already has a line keeps it unless the user asked to replace lines (`replace: true`). When a limit is reached, wait `retry_after_seconds`, then go on with the leads not saved.
- Give a progress line after each batch, for example: 200 of 640 leads have a first line now.

## 6. Start

- `get_campaign` with the readiness section shows anything still missing.
- `start_campaign` only when the user asks: show its preview, say it will email its remaining leads, and call again with the `confirmation_token` after a yes. Resuming is the same. If Envoy says it is not ready, show the user what is missing.
- `pause_campaign` stops sending until it is started again.

## Inboxes

- `get_inbox_status` shows connected inboxes, health, warmup and daily capacity.
- For buying more inboxes or domains, use `get_inbox_buying_advice` and `search_help` to explain the options, then send the user to the Envoy web app. The agent never buys anything.
