---
name: setup
description: Walk the user through setting up ProspectFlo Envoy from the start, one step at a time. Use when the user runs setup or asks how to get started with ProspectFlo or Envoy.
disable-model-invocation: true
---

# ProspectFlo setup

Follow the prospectflo skill and its `references/onboarding.md`.

1. Check the connection by calling `get_account_overview`. If the tools are missing or ask for sign-in, tell the user to finish signing in to ProspectFlo in the browser window their agent opened, then try again. If it returns `plan_inactive` or `plan_required`, stop and tell the user to open Settings, then Plan and billing, in the Envoy web app to choose a plan. A new account can start the 7-day trial there.
2. Tell the user in two or three plain sentences what is already set up and what is next.
3. Go through the setup order: AI agent setup, a lead list, the Review Queue, a campaign (writing brief, the emails you write with the user, schedule, options, link the list), first lines if the list uses them.
4. Stop after each step and ask before the next one.
5. Do not start the campaign. When everything is ready, tell the user it is ready and ask whether to start it.
