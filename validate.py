#!/usr/bin/env python3
"""
Checks the ProspectFlo agent plugin before it is shared.

Run from anywhere:   python3 validate.py
Or with pytest:      pytest validate.py

Standard library only, so it runs in the public repository as it is.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# The plugin sits at the repository root: Antigravity and Grok Build install a GitHub
# repository as one plugin, and the Claude Code and Codex marketplaces point at "./".
ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT

NAME = "prospectflo"
# The public repository. The README's install commands and every manifest must name it.
REPO = "prospectflo/envoy-agent"
REPO_URL = f"https://github.com/{REPO}"
MCP_URL = "https://prospectflo.com/mcp"
TERMS_URL = "https://prospectflo.com/terms#ai-agents"

# Customer-facing text must never name how Envoy works inside.
BANNED_WORDS = ("prompt", "model", "scoring", "ranking")
EM_DASH = "—"

MANIFESTS = {
    "claude": PLUGIN / ".claude-plugin" / "plugin.json",
    "codex": PLUGIN / "plugin.json",
    "antigravity": PLUGIN / ".antigravity-plugin" / "plugin.json",
    "grok": PLUGIN / ".grok-plugin" / "plugin.json",
}
# Plugin only: the exact install command for each supported agent, as the README shows it.
INSTALL_COMMANDS = {
    "Claude Code": f"claude plugin install {NAME} --marketplace {REPO}",
    "Codex": f"codex plugin marketplace add {REPO}\ncodex plugin add {NAME}@{NAME}",
    "Antigravity": f"agy plugin install {REPO_URL}",
    "Grok Build": f"grok plugin install {REPO}",
}
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    assert isinstance(data, dict), f"{path}: top level must be an object"
    return data


def customer_text_files() -> list[Path]:
    files = [ROOT / "README.md", ROOT / "LICENSE"]
    files += sorted((PLUGIN / "skills").rglob("*.md"))
    return files


def without_frontmatter_keys(text: str) -> str:
    """A SKILL.md with its frontmatter keys (format words, not customer text) left out."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return text
    values = "\n".join(line.split(": ", 1)[-1] for line in match.group(1).splitlines())
    return values + "\n" + text[match.end() :]


def json_strings(value) -> list[str]:
    """Every string value (not key) in a JSON document."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for item in value.values() for s in json_strings(item)]
    if isinstance(value, list):
        return [s for item in value for s in json_strings(item)]
    return []


def test_every_json_file_parses():
    found = sorted(p for p in ROOT.rglob("*.json") if p.is_file())
    assert len(found) >= 8, f"expected the manifests, found {found}"
    for path in found:
        load(path)


def test_names_and_versions_agree():
    manifests = {kind: load(path) for kind, path in MANIFESTS.items()}
    for kind, data in manifests.items():
        assert data.get("name") == NAME, f"{kind} manifest name"
        assert data.get("repository") == REPO_URL, f"{kind} manifest repository"
    versions = {kind: data.get("version") for kind, data in manifests.items()}
    assert len(set(versions.values())) == 1, f"versions differ: {versions}"
    assert re.fullmatch(r"\d+\.\d+\.\d+", versions["claude"]), "version must be semver"

    claude_market = load(CLAUDE_MARKETPLACE)
    assert claude_market["name"] == NAME
    assert claude_market["owner"]["name"] == "ProspectFlo"
    codex_market = load(CODEX_MARKETPLACE)
    assert codex_market["name"] == NAME
    for market in (claude_market, codex_market):
        entries = market["plugins"]
        assert [entry["name"] for entry in entries] == [NAME]
        # A version on the entry would fight plugin.json (Claude Code: plugin.json wins).
        assert "version" not in entries[0]
    assert claude_market["plugins"][0]["source"] == "./"
    assert codex_market["plugins"][0]["source"] == {"source": "local", "path": "./"}
    assert not (ROOT / "plugins").exists(), "the plugin lives at the repository root"

    claude = manifests["claude"]
    assert claude["author"]["name"] == "ProspectFlo"
    assert claude["homepage"] == "https://prospectflo.com"
    assert claude.get("license")
    assert (
        manifests["codex"]["extensions"]["com.openai"]["interface"]["termsOfServiceURL"]
        == TERMS_URL
    )


def test_mcp_servers_point_at_envoy_only():
    claude = load(PLUGIN / ".mcp.json")["mcpServers"]
    assert list(claude) == [NAME]
    # A plain address: Grok Build reads this file too, and may not expand ${VAR} forms.
    assert claude[NAME] == {"type": "http", "url": MCP_URL}

    codex = load(PLUGIN / "mcp.json")["mcpServers"]
    assert list(codex) == [NAME]
    server = codex[NAME]
    assert server["type"] == "streamable-http"
    assert server["url"] == MCP_URL
    auth = server["extensions"]["com.openai"]["auth"]
    assert auth == {"type": "oauth", "client": {"mode": "dcr"}}
    assert "headers" not in server

    antigravity = load(PLUGIN / "mcp_config.json")["mcpServers"]
    assert antigravity == {NAME: {"serverUrl": MCP_URL}}

    # No client ids, secrets or tokens anywhere in the package.
    for path in ROOT.rglob("*.json"):
        raw = path.read_text(encoding="utf-8").lower()
        for word in ("clientid", "client_id", "clientsecret", "client_secret", "bearer", "token"):
            assert word not in raw, f"{path}: {word}"


def test_readme_installs_the_plugin_only():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^### ([^\n]+)\n\n```bash\n(.*?)\n```", readme, re.M | re.S)
    assert dict(blocks) == INSTALL_COMMANDS, blocks
    # No bare server installs: an agent without the plugin is not offered.
    for banned in ("mcp add", "mcp.json", "cursor://", "Cursor", "Gemini", "Muse"):
        assert banned not in readme, f"README: {banned}"
    assert "### Any other agent\n\nNot supported." in readme
    assert "You need a ProspectFlo plan (the 7-day trial works)." in readme
    assert TERMS_URL in readme
    for repo in re.findall(r"prospectflo/[\w.-]+", readme):
        assert repo == REPO, repo
    for url in re.findall(r"https://[^\s)`\"]+/mcp\b", readme):
        assert url == MCP_URL, url


def test_skills_have_valid_frontmatter():
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    assert [p.parent.name for p in skills] == ["prospectflo", "setup"]
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"---\n(.*?)\n---\n", text, re.S)
        assert match, f"{path}: frontmatter"
        fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
        # Antigravity requires the name to equal the folder name.
        assert fields.get("name") == path.parent.name, f"{path}: name"
        assert len(fields.get("description", "")) > 40, f"{path}: description"
    onboarding = load(MANIFESTS["codex"])["extensions"]["com.openai"]["onboardingSkill"]
    assert (PLUGIN / onboarding).is_file()


def test_customer_text_names_no_internals():
    problems = []
    texts = [
        (p, without_frontmatter_keys(p.read_text(encoding="utf-8"))) for p in customer_text_files()
    ]
    for path in ROOT.rglob("*.json"):
        texts.append((path, "\n".join(json_strings(load(path)))))
    for path, text in texts:
        if EM_DASH in text:
            problems.append(f"{path.relative_to(ROOT)}: em dash")
        lowered = text.lower()
        for word in BANNED_WORDS:
            if word in lowered:
                problems.append(f"{path.relative_to(ROOT)}: '{word}'")
    assert not problems, "\n".join(problems)


def main() -> int:
    failed = 0
    for name, check in sorted(globals().items()):
        if name.startswith("test_") and callable(check):
            try:
                check()
                print(f"ok    {name}")
            except AssertionError as error:
                failed += 1
                print(f"FAIL  {name}: {error}")
    print("passed" if not failed else f"{failed} check(s) failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
