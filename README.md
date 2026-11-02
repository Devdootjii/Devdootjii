<div align="center">

# Divyansh Kumar

`TPM` · `AI SYSTEM ARCHITECT` · `TEAM DEVD00TS`

I take a technology nobody has pointed at a real problem yet, and point it there — then ship it, with the team that has to keep it alive.

<a href="https://github.com/Devdootjii?tab=repositories"><img src="https://img.shields.io/badge/repositories-14-181717?style=flat-square&logo=github&logoColor=white" alt="Repositories"></a>
<a href="https://devdoots-vyom-acre-nine.vercel.app"><img src="https://img.shields.io/badge/VyomAcre-live-00E585?style=flat-square&logo=vercel&logoColor=white" alt="VyomAcre"></a>
<a href="https://auto-reel-maker.streamlit.app"><img src="https://img.shields.io/badge/Auto%20Reels-live-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Auto Reels"></a>
<a href="https://x.com/Devdootji"><img src="https://img.shields.io/badge/@Devdootji-000000?style=flat-square&logo=x&logoColor=white" alt="X"></a>

</div>

```
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│  ROLE      Technical Product Manager · AI System Architect   │
│  TEAM      Devdoots — 6 engineers, 1 protected main          │
│  DOMAIN    Geospatial · vision · agentic workflows           │
│  SHIPPED   600+ commits · 8 languages · 3 live apps          │
│  RULE      runs on a laptop. no GPU. no paid tier.           │
│  STATUS    building                                          │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

---

## 01 — The one rule

If a student in Lucknow cannot clone it and run it tonight, it is not finished.

Every project below runs on a laptop. Every README has a *Known limitations* section that says what does not work — that section is the reason I trust the rest of the document, so I do not let it go empty. And every PR I merge, I can defend line by line, because I review before I merge rather than after.

---

## 02 — Shipped

| Project | What it actually does | Stack | Status |
| :--- | :--- | :--- | :--- |
| **[VyomAcre](https://github.com/Devdootjii/Devdoots_VyomAcre)** | Rooftop leasing marketplace where **Google Earth Engine measures the roof from satellite imagery** instead of a broker visiting it | React 19 · FastAPI · PostgreSQL · Earth Engine · Gemini | 🟢 live |
| **[NETRA](https://github.com/Devdootjii/Devdoots_Netra)** | Turns a passive CCTV feed into an emergency engine — detects a **3-second SOS gesture**, writes a Gemini forensic report, files evidence to Drive | YOLOv8-pose · Gemini Vision · FastAPI · React 19 | 🟢 working system |
| **[Auto Reels Studio](https://github.com/Devdootjii/auto-reel-maker)** | Long video in, caption-burned 9:16 reels out — Whisper transcript, topic cuts, Hindi captions | Whisper · FFmpeg/libass · Streamlit · yt-dlp | 🟢 live |
| **[Devdoots Python Sprint](https://github.com/Devdootjii/Devdoots_Python)** | Not a tutorial repo — a working engineering org: isolated workspaces, branch standards, PR checklists, peer review | Python · Git workflow | 🟢 275 commits |
| **[vyomacre-leads](https://github.com/Devdootjii/vyomacre-leads)** | Lead capture where priority is **scored at submit time**, so nobody sorts a spreadsheet later | Serverless · Postgres | 🟢 live |
| **[VyomAcre Android](https://github.com/Devdootjii/Devdoots_VyomAcre_Android)** | Native client — every screen real Compose, no WebView wrapper | Kotlin · Jetpack Compose · Material 3 | 🟡 v4.0 |

---

## 03 — Three I would defend in an interview

<table>
<tr>
<td width="50%" valign="top">

### 🛰️ VyomAcre

India has idle rooftops. Solar, telecom and logistics need land. Between them sits a broker and a two-week site visit. VyomAcre deletes both.

An owner lists a roof in about two minutes. Earth Engine pre-screens the usable area from satellite imagery. An admin signs off. Businesses send lease requests, and the owner's phone number unlocks **only on acceptance**.

The full loop is in production: signup → list → verify → request → accept → contact unlock.

![React 19](https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Earth Engine](https://img.shields.io/badge/Earth%20Engine-4285F4?style=flat-square&logo=googleearth&logoColor=white)

**[Live app →](https://devdoots-vyom-acre-nine.vercel.app)** · **[Swagger →](https://devdoots-vyomacre-y0gr.onrender.com/docs)** · **[Repo →](https://github.com/Devdootjii/Devdoots_VyomAcre)**

<img src="https://img.shields.io/github/last-commit/Devdootjii/Devdoots_VyomAcre?style=flat-square&label=last%20commit&color=00E585" alt="last commit">

</td>
<td width="50%" valign="top">

### 👁️ NETRA

A camera records. It does not understand. NETRA makes it act.

It counts people, watches for a **sustained SOS — wrist above the shoulder, held three seconds** — and on confirmation sends a snapshot to Gemini Vision, which writes a structured forensic report: threat level, hazards, recommended action. Snapshot and report go to Drive as an evidence pack while the dashboard raises the alarm.

Runs on a webcam, a phone IP camera or an RTSP stream. No GPU. Gemini and Drive are optional — without keys it keeps detecting, it just stops filing paperwork.

![YOLOv8](https://img.shields.io/badge/YOLOv8--pose-00B4D8?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini%20Vision-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React 19](https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black)

**[Repo →](https://github.com/Devdootjii/Devdoots_Netra)**

<img src="https://img.shields.io/github/last-commit/Devdootjii/Devdoots_Netra?style=flat-square&label=last%20commit&color=00B4D8" alt="last commit">

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎬 Auto Reels Studio

A two-hour lecture becomes ten postable reels, with the captions already burned in — including Hindi.

Whisper transcribes, the topic boundaries are found, each segment is reframed to 9:16, captions are rendered with FFmpeg/libass, and the whole set leaves as a ZIP. Source can be a file, a YouTube/Instagram/X/Vimeo link, or Drive. Output can be pushed straight to YouTube or Drive.

No watermark, no clip limit, no subscription.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg%2Flibass-007808?style=flat-square&logo=ffmpeg&logoColor=white)

**[Live app →](https://auto-reel-maker.streamlit.app)** · **[Repo →](https://github.com/Devdootjii/auto-reel-maker)**

<img src="https://img.shields.io/github/last-commit/Devdootjii/auto-reel-maker?style=flat-square&label=last%20commit&color=FF4B4B" alt="last commit">

</td>
<td width="50%" valign="top">

### 🐍 Devdoots Python Sprint

The repo I am quietly proudest of, because it is about people.

Six members, one protected `main`, and rules that are written down instead of assumed. Isolated member workspaces so nobody touches a shared file. Branch naming standard. Structured commit messages — `done` and `update` are banned. A PR merges only after a checklist review. Proof-of-work logs for every task.

275 commits of daily sprint work behind it.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Workflow-F1002B?style=flat-square&logo=git&logoColor=white)

**[Repo →](https://github.com/Devdootjii/Devdoots_Python)** · **[Sprint hub →](https://github.com/Devdootjii/Devdoots_Sprint)**

<img src="https://img.shields.io/github/last-commit/Devdootjii/Devdoots_Python?style=flat-square&label=last%20commit&color=3776AB" alt="last commit">

</td>
</tr>
</table>

---

## 04 — Stack

|  |  |
| :--- | :--- |
| **AI & vision** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![YOLOv8](https://img.shields.io/badge/YOLOv8-00B4D8?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) ![Whisper](https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white) ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white) ![Neon](https://img.shields.io/badge/Neon-00E599?style=flat-square&logo=neon&logoColor=black) ![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white) |
| **Frontend** | ![React 19](https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white) ![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white) ![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin%20%2B%20Compose-7F52FF?style=flat-square&logo=kotlin&logoColor=white) |
| **Platform** | ![Earth Engine](https://img.shields.io/badge/Earth%20Engine-4285F4?style=flat-square&logo=googleearth&logoColor=white) ![Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=flat-square&logo=googledrive&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white) ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Git](https://img.shields.io/badge/Git-F1002B?style=flat-square&logo=git&logoColor=white) |

---

## 05 — How I run a team

Six people, one protected `main`, and rules that are written down rather than assumed.

Every task is scoped to a **45–60 minute focus block**, so "not done" is a fact about the task, not about the person. Every PR gets reviewed against a checklist before it merges — does it run, are the names right, is the proof-of-work log filled in. Every evening there is a five-minute technical standup where each member explains their own work out loud, because a commit nobody can explain is a commit you cannot debug. Three missed submissions earns a review, not a lecture.

The result is a team whose repos read like a company's, not a classroom's.

---

<div align="center">

**Building for the next user, not the next demo.**

<br>

<a href="https://github.com/Devdootjii?tab=repositories"><img src="https://img.shields.io/badge/Explore%20the%20repos-00E585?style=for-the-badge&logo=github&logoColor=black" alt="Explore repositories"></a>

<br><br>

<sub>Profile maintained by hand — no auto-generated stat cards, because a broken image is worse than no image.</sub>

</div>
