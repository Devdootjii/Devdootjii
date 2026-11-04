#!/usr/bin/env python3
"""
Regenerates assets/activity.svg and assets/langs.svg from real GitHub data.

Run locally:   GITHUB_TOKEN=$(gh auth token) python scripts/generate_stats.py
In Actions:    runs weekly, GITHUB_TOKEN is provided automatically.

No third-party dependencies - standard library only.
"""
import json
import os
import sys
import time
import datetime
import urllib.request
import urllib.error

USER = os.environ.get("GH_USER", "Devdootjii")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
API = "https://api.github.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def api(path, retries=4):
    url = API + path
    for attempt in range(retries):
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("User-Agent", "profile-stats-generator")
        if TOKEN:
            req.add_header("Authorization", "Bearer " + TOKEN)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            # 202 = stats still being computed, retry after a pause
            if e.code == 202 and attempt < retries - 1:
                time.sleep(5)
                continue
            if e.code in (403, 429) and attempt < retries - 1:
                time.sleep(10)
                continue
            return None
        except Exception:
            if attempt < retries - 1:
                time.sleep(5)
                continue
            return None
    return None


def public_repos():
    repos = api(f"/users/{USER}/repos?per_page=100&type=owner")
    if not isinstance(repos, list):
        return []
    return [
        r["name"] for r in repos
        if not r.get("fork") and not r.get("private") and r["name"] != USER
    ]


def weekly_activity(repos):
    weekly = [0] * 52
    for name in repos:
        d = api(f"/repos/{USER}/{name}/stats/participation")
        if isinstance(d, dict) and isinstance(d.get("all"), list):
            for i, v in enumerate(d["all"][:52]):
                weekly[i] += v
    return weekly


def language_bytes(repos):
    total = {}
    for name in repos:
        d = api(f"/repos/{USER}/{name}/languages")
        if isinstance(d, dict):
            for k, v in d.items():
                total[k] = total.get(k, 0) + v
    return total


# ---------------------------------------------------------------- activity
def build_activity(weekly, repo_count, today=None):
    W, H = 1200, 320
    x0, x1 = 64, 1136
    base_y, top_y = 262, 78
    maxv = max(weekly) or 1
    n = len(weekly)
    slot = (x1 - x0) / n
    bw = slot * 0.62
    scale = (base_y - top_y) / maxv

    today = today or datetime.date.today()
    start = today - datetime.timedelta(weeks=52)
    labels, last = [], -999
    for w in range(n):
        d = start + datetime.timedelta(weeks=w)
        if d.day <= 7:
            cx = x0 + w * slot + bw / 2
            if cx - last >= 74:
                labels.append((cx, d.strftime("%b").upper()))
                last = cx

    bars = []
    for i, v in enumerate(weekly):
        h = v * scale
        x = x0 + i * slot + (slot - bw) / 2
        y = base_y - h
        op = 1.0 if v > 0 else 0.3
        bars.append(
            f'  <rect x="{x:.1f}" y="{y:.2f}" width="{bw:.1f}" height="{h:.2f}" '
            f'rx="1.6" fill="url(#barGrad)" opacity="{op}"/>'
        )

    grid = []
    for gv in [0, 25, 50, 75]:
        gy = base_y - gv * scale
        grid.append(f'  <line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="#1A2434" stroke-width="1"/>')
        grid.append(f'  <text x="{x0-12}" y="{gy+4:.1f}" text-anchor="end" font-family="ui-monospace,Menlo,monospace" font-size="11" fill="#4A5C72">{gv}</text>')

    mtxt = "\n".join(
        f'  <text x="{cx:.0f}" y="{base_y+22}" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" '
        f'font-size="12" fill="#5A6E86">{nm}</text>' for cx, nm in labels
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Commit activity across {repo_count} public repositories over the last 52 weeks, {sum(weekly)} commits">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#00E585" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#00E585" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="acBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0A1019"/><stop offset="100%" stop-color="#0E1626"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00E585" stop-opacity="0"/><stop offset="100%" stop-color="#00E585" stop-opacity="0.85"/>
    </linearGradient>
    <clipPath id="reveal">
      <rect x="{x0}" y="{top_y-14}" width="{x1-x0}" height="{base_y-top_y+28}">
        <animate attributeName="width" from="0" to="{x1-x0}" dur="1.7s" begin="0.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.9 0.3 1" keyTimes="0;1"/>
      </rect>
    </clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#acBg)" stroke="#22304A"/>

  <text x="{x0}" y="40" font-family="ui-monospace,Menlo,monospace" font-size="13" letter-spacing="2.5" fill="#00E585">COMMIT ACTIVITY</text>
  <text x="{x0}" y="62" font-family="'Segoe UI',system-ui,Helvetica,sans-serif" font-size="15" fill="#7E93A8">Last 52 weeks across {repo_count} public repositories</text>
  <text x="{x1}" y="46" text-anchor="end" font-family="'Segoe UI',system-ui,Helvetica,sans-serif" font-size="34" font-weight="800" fill="#E8F5EF">{sum(weekly)}</text>
  <text x="{x1}" y="64" text-anchor="end" font-family="ui-monospace,Menlo,monospace" font-size="11" letter-spacing="1.6" fill="#5A6E86">COMMITS</text>

{chr(10).join(grid)}

  <g clip-path="url(#reveal)">
{chr(10).join(bars)}
  </g>

  <rect x="{x0}" y="{top_y-14}" width="2" height="{base_y-top_y+28}" fill="url(#edge)" opacity="0">
    <animate attributeName="x" from="{x0}" to="{x1}" dur="1.7s" begin="0.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.9 0.3 1" keyTimes="0;1"/>
    <animate attributeName="opacity" values="0;0.9;0" keyTimes="0;0.7;1" dur="1.9s" begin="0.1s" fill="freeze"/>
  </rect>

{mtxt}
  <line x1="{x0}" y1="{base_y}" x2="{x1}" y2="{base_y}" stroke="#2A3A52" stroke-width="1.2"/>
</svg>
'''


# ---------------------------------------------------------------- languages
COLORS = {
    "Python": "#3776AB", "JavaScript": "#F1E05A", "Kotlin": "#A97BFF",
    "Jupyter Notebook": "#DA5B0B", "HTML": "#E34C26", "CSS": "#563D7C",
    "TypeScript": "#3178C6", "C#": "#178600", "Java": "#B07219",
    "Dart": "#00B4AB", "Go": "#00ADD8", "Rust": "#DEA584",
    "Shell": "#89E051", "Dockerfile": "#384D54", "Batchfile": "#C1F12E",
    "Other": "#4A5C72",
}


def build_langs(langs):
    tot = sum(langs.values()) or 1
    ordered = sorted(langs.items(), key=lambda kv: -kv[1])
    top = ordered[:6]
    other = sum(v for _, v in ordered[6:])
    if other:
        top.append(("Other", other))

    W, H = 1200, 250
    bx0, bx1, by, bh = 64, 1136, 96, 30
    span = bx1 - bx0

    segs, cur = [], bx0
    for name, v in top:
        w = span * v / tot
        segs.append(f'    <rect x="{cur:.2f}" y="{by}" width="{w:.2f}" height="{bh}" fill="{COLORS.get(name, "#4A5C72")}"/>')
        cur += w

    legend = []
    for i, (name, v) in enumerate(top):
        col, row = i % 4, i // 4
        lx, ly = bx0 + col * 268, 172 + row * 40
        c = COLORS.get(name, "#4A5C72")
        pct = 100 * v / tot
        ptxt = f"{pct:.1f}%" if pct >= 0.1 else "<0.1%"
        legend.append(
            f'    <circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{c}"/>\n'
            f'    <text x="{lx+16}" y="{ly}" font-family="\'Segoe UI\',system-ui,Helvetica,sans-serif" font-size="13.5" fill="#9FB3C8">{name}</text>\n'
            f'    <text x="{lx+16}" y="{ly+17}" font-family="ui-monospace,Menlo,monospace" font-size="11.5" fill="#5A6E86">{ptxt}</text>'
        )

    top3 = ", ".join(f"{n} {100*v/tot:.0f} percent" for n, v in top[:3])

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Language breakdown: {top3}, and others">
  <defs>
    <linearGradient id="lbBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0A1019"/><stop offset="100%" stop-color="#0E1626"/>
    </linearGradient>
    <clipPath id="reveal"><rect x="{bx0}" y="{by-2}" width="{span}" height="{bh+4}" rx="4">
      <animate attributeName="width" from="0" to="{span}" dur="1.6s" begin="0.15s" fill="freeze" calcMode="spline" keySplines="0.3 0.9 0.25 1" keyTimes="0;1"/>
    </rect></clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#lbBg)" stroke="#22304A"/>
  <text x="{bx0}" y="44" font-family="ui-monospace,Menlo,monospace" font-size="13" letter-spacing="2.5" fill="#00E585">LANGUAGES</text>
  <text x="{bx0}" y="66" font-family="'Segoe UI',system-ui,Helvetica,sans-serif" font-size="15" fill="#7E93A8">By bytes written across all public repositories</text>
  <g clip-path="url(#reveal)">
{chr(10).join(segs)}
  </g>
  <rect x="{bx0}" y="{by}" width="{span}" height="{bh}" rx="4" fill="none" stroke="#0A1019" stroke-width="1.5"/>
{chr(10).join(legend)}
</svg>
'''


def write_if_changed(path, content):
    full = os.path.join(ROOT, path)
    old = open(full, encoding="utf-8").read() if os.path.exists(full) else ""
    if old == content:
        print(f"  {path}: unchanged")
        return False
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)
    print(f"  {path}: updated")
    return True


def main():
    print(f"Collecting data for {USER} ...")
    repos = public_repos()
    if not repos:
        print("No repositories returned - aborting so the charts are not wiped.")
        return 1
    print(f"  {len(repos)} public repositories")

    weekly = weekly_activity(repos)
    langs = language_bytes(repos)
    print(f"  {sum(weekly)} commits in the last 52 weeks")
    print(f"  {len(langs)} languages")

    changed = write_if_changed("assets/activity.svg", build_activity(weekly, len(repos)))
    changed |= write_if_changed("assets/langs.svg", build_langs(langs))
    print("Done." if changed else "Nothing to do.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
