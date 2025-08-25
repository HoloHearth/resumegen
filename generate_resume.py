import json
from pathlib import Path

# ===== Helpers =====
def render_list(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"

def render_experience(entries):
    html = ""
    for entry in entries:
        html += f"""
        <section>
            <div class="experience-header">
                <span class="job-title">{entry['title']}</span>
                <span class="job-period">{entry['period']}</span>
            </div>
            <div><em>{entry['company']}</em></div>
            {render_list(entry['items'])}
        </section>
        """
    return html

def render_education(entries):
    html = ""
    for entry in entries:
        html += f"<p><strong>{entry['institution']}</strong></p>{render_list(entry['items'])}"
    return html


# ===== Load JSON Resume Data =====
with open("resume.json", "r", encoding="utf-8") as f:
    data = json.load(f)

name = data["name"]
email = data["email"]
phone = data["phone"]
github = data["github"]
summary_points = data["summary_points"]
skills = data["skills"]
experience_entries = data["experience_entries"]
education_entries = data["education_entries"]

# ===== HTML Resume Template =====
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} - Resume</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0.3in 0.5in 0.5in 0.5in;
            line-height: 1.4;
            color: #000;
            background-color: #fff;
            font-size: 12px;
        }}
        h1 {{
            font-size: 20px;
            margin-top: 0;
            margin-bottom: 4px;
            color: #2c3e50;
        }}
        .contact {{
            display: flex;
            justify-content: space-between;
            font-size: 10.5px;
            margin-top: 0;
            margin-bottom: 10px;
        }}
        h2 {{
            font-size: 14px;
            margin: 12px 0 6px 0;
            border-bottom: 1px solid #ccc;
            padding-bottom: 2px;
            color: #2c3e50;
        }}
        .job-title {{ font-weight: bold; }}
        .job-period {{ float: right; font-style: italic; font-size: 10.5px; }}
        ul {{ margin: 2px 0 6px 16px; padding-left: 0; }}
        li {{ margin-bottom: 3px; }}
        .education, .skills {{ font-size: 11px; }}
        a {{ color: #2c3e50; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>

    <h1>{name}</h1>
    <div class="contact">
        <div class="contact-left">
            <a href="mailto:{email}">{email}</a> | {phone}
        </div>
        <div class="contact-right">
            <a href="{github}" target="_blank">GitHub</a>
        </div>
    </div>

    <h2>Summary</h2>
    {render_list(summary_points)}

    <h2>Skills & Technologies</h2>
    <div class="skills">
        {", ".join(skills)}
    </div>

    <h2>Experience</h2>
    {render_experience(experience_entries)}

    <h2>Education</h2>
    <div class="education">
        {render_education(education_entries)}
    </div>

</body>
</html>
"""

# ===== Save File =====
with open("resume.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("resume.html has been generated.")
