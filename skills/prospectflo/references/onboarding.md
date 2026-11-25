# Setting up ProspectFlo Envoy, step by step

Start every onboarding run with an automatic account audit (`get_account_overview`, `get_ai_agent_setup`, `get_inbox_status`, `get_scout_status`, `list_lead_lists`, `list_campaigns`, `get_enbox_settings`). Present a short Done vs Next checklist, skip everything already complete, and work one step at a time. Show what you plan to save before saving it. "Set everything up" still means one step at a time, each with a preview and a yes.

## 1. AI agent setup

- Read it with `get_ai_agent_setup`. It lists which basic items are still missing and gives the revision number a save needs.
- Ask the user for each missing item: website, a short company description, the cold offer, client results, links, sender background, the price answer, common objections with their answers, and claims never to make.
- Client results and offers must be the user's real facts. If the user has none yet, leave the field empty and say so.
- Save with `save_ai_agent_setup`. Send only the fields that change. A list field sent replaces the whole list, so send every offer, not only the new one.
- If the save returns `conflict`, read the setup again and redo the change on the new revision.

## 2. Inboxes

- Always check `get_inbox_status` first. Show connected count, warmup readiness (`Ready`, `Warming`, `Paused`, `Needs attention`) and daily capacity.
- **Connect existing inboxes:** call `get_inbox_connect_guide` and share the steps and direct web app links (Gmail App Password, Microsoft OAuth link, or custom SMTP). Never accept passwords in chat. Re-check `get_inbox_status` after the user connects.
- **Buy new inboxes:** explain options with `get_inbox_buying_advice`, then either check custom domains (`check_inbox_domains`) or list Instant prewarmed domains (`list_instant_inboxes`), call `quote_inbox_order`, and call `prepare_inbox_checkout` for a preview + confirmation token. Only after a yes in the next turn, call `prepare_inbox_checkout` with the token and give the user the Stripe Checkout link so they complete payment themselves.

## 3. Envoy Scout

- Required for live `build_a_list` runs and `enrich_leads`. Not required for `search_instant_leads` / `import_instant_leads` or `upload_and_enrich_list` (verification only).
- Check `get_scout_status`. When Scout is not connected and the user needs it, offer to download Envoy Scout for this computer (`"Shall I download Envoy Scout for this computer?"`), then follow the `scout` skill on a yes.

## 4. A lead list

Three ways, and the user picks:

- **Instant leads** (ready now): `search_instant_leads` with a plain description of who to find, plus job titles, keywords, example websites or a place. Rows show masked email and phone. Always tell the user the `place_note` it returns. Import the rows the user wants with `import_instant_leads`, into an existing list (`list_id`), a new one (`new_list_name`), or directly to a campaign (`campaign_id`). Imports count toward the daily import allowance.
- **Build a List** (new leads found live by Envoy Scout): first call `build_a_list` with name, who, where, targeting fields (lookalikes, competitors, exclusions, company size, volume, match, uses/not_uses, lead_kind, auto_clean) and lead_count. Scout never runs Envoy signals, auto-approve, or Envoy AI first lines; leads land in Review Queue so you decide fit (`get_review_queue` -> `approve_leads` / `dismiss_leads`) and write first lines yourself (`save_first_lines`). Show the preview. Ask "Start finding leads now?" as its own question. Only after a yes, call it again with `list_build_id` and `confirmed: true` (and `confirmation_token` if returned). Check progress with `get_list_run`, pause/resume/cancel with `pause_list_run` / `resume_list_run` / `cancel_list_run`, and see leads with `get_list_run_leads`.
- **Upload CSV or public Google Sheet + verify + enrich**: call `fetch_public_google_sheet` for a shared Google Sheet link or take the user's CSV rows, call `upload_and_enrich_list` (supports verify and optional Scout enrichment), track email verification with `verify_list_emails` / `get_list_verification`, and track enrichment with `enrich_leads` / `get_enrichment_status`.

## 5. Review Queue and list management

- `get_review_queue` shows leads waiting for a decision, one page at a time (optionally filtered by `list_id`).
- `approve_leads` sends approved leads into the named campaign, or the campaign their list is linked to. If that campaign is sending, the leads will be emailed: show the preview, ask, and call again with its `confirmation_token` only after a yes.
- `dismiss_leads` removes leads from the queue. A short reason helps Envoy find better leads next time.
- Manage lists with `update_lead_list`, `merge_lead_lists`, `copy_approved_leads`, `move_approved_leads`, `remove_lead_from_list`, `archive_lead_list` and `clear_list_leads` (ask first for previews on merges, moves, archives and deletes).

## 6. A campaign

1. `create_campaign` with a name, and the sending inboxes and daily limit the user picked. Ask and wait for the answer; never pick inboxes or a daily limit yourself, not even the default. Check inboxes first with `get_inbox_status`.
2. `get_campaign_writing_brief` returns the saved facts, the list's audience and signal, the limits, the variables and the writing guide.
3. Write the sequence yourself (see `writing.md`). Show the full draft to the user and ask before the first save with `save_campaign_sequence`.
4. `save_campaign_schedule`: time zone, daily window, days of the week, optional start and end dates.
5. `save_campaign_options`: inboxes, daily limit, gap between sends, tracking, plain text, stop on reply, `group_send`, `unsubscribe_footer` / `unsubscribe_footer_text`, and per-campaign `auto_reply` (turning `auto_reply` on or editing a sending campaign requires confirmation).
6. `get_campaign_reply_agent` and `save_campaign_reply_agent` for the campaign's own reply settings, if the user wants them.
7. `preview_list_link` then `link_list_to_campaign` (supports `replace_list_link` and `port_leads`). A list links to one campaign only, while a campaign can link multiple lists.

## 7. First lines

- Write personal first lines yourself in batches (`get_leads_for_first_lines` + `save_first_lines`); never queue Envoy's server-side AI writer.
- Get the email the lines lead into (`email_copy` or `campaign_id`, else linked campaign), write up to 100 per call, show a short sample first, leave a lead out when nothing true can be said, and report progress after each batch.

## 8. Start and reply mode

- `get_campaign` with the readiness section shows anything still missing (`get_campaign_send_status` shows runtime send blockers for active campaigns).
- Note on `no_compliance_address`: tell the user they can add their business mailing address in Settings, Profile, OR save custom unsubscribe footer text (or turn the footer off) in campaign options.
- `start_campaign` only when the user asks: show its preview, say it will email its remaining leads, end your turn, and call again with the `confirmation_token` after a yes. Resuming is the same. `pause_campaign` stops sending until started again.
- Offer optional reply handling (`autoreply` skill): enable Envoy's guarded Auto-Reply (`set_auto_reply` with preview + yes) or set up a scheduled reply check (`/schedule` or Codex automations) that prepares drafts and waits for a yes before sending.
