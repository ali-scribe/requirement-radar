# Requirement Radar 🎯

Requirement Radar uses AI to turn rough software feature descriptions into structured requirements, acceptance criteria, missing details, and clarifying questions.

## Features

- AI-powered requirement analysis
- Structured JSON output
- Python-based checks for vague wording and missing outcomes
- Downloadable JSON report
- Simple Streamlit interface

## Tech Stack

- Python
- Streamlit
- Groq API
- ALLaM-2-7B model

## Setup

Requires Python 3.10+ and a Groq API key with access to the configured model.

Install dependencies:

```bash
python -m pip install streamlit groq
```

Set your API key.

**Windows PowerShell:**
```powershell
$env:GROQ_API_KEY="your_api_key"
```

**macOS/Linux:**
```bash
export GROQ_API_KEY="your_api_key"
```

Run the app:

```bash
python -m streamlit run app.py
```

## How It Works

1. The user enters a software feature requirement.
2. The hosted AI model generates a summary, acceptance criteria, missing details, and clarifying questions.
3. Python runs separate heuristic checks.
4. The results can be reviewed and downloaded as JSON.

## AI Disclosure

- Model ID: `allam-2-7b`
- Provider: Groq hosted API
- Input: plain-text software requirement
- Output: structured JSON
- Rule-based checks: implemented in Python

Confirm the model's current availability, pricing, license, and parameter count before relying on it for a submission.

## Limitations

AI output may be inaccurate or incomplete. Rule-based checks are simple heuristics and do not guarantee requirement completeness. API access and quotas may change.

## License

MIT. See [LICENSE](LICENSE).
