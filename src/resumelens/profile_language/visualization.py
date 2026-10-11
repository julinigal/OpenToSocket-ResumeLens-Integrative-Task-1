HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{name} - Candidate Profile</title>
</head>
<body>
  <h1>{name}</h1>
  <p>Experience: {years} years</p>
  {contact_html}
  <h2>Skills</h2>
  <ul>
    {skills_html}
  </ul>
  <h2>Profile Classification</h2>
  <ul>
    {results_html}
  </ul>
</body>
</html>
"""


def render_html(model):
    contact_parts = []
    if model.email:
        contact_parts.append(f"<p>Email: {model.email}</p>")
    if model.phone:
        contact_parts.append(f"<p>Phone: {model.phone}</p>")
    contact_html = "\n  ".join(contact_parts)

    skills_html = "\n    ".join(f"<li>{skill}</li>" for skill in model.skills)
    results_html = "\n    ".join(
        f"<li>{result.profile}: {result.status}</li>" for result in model.results
    )

    return HTML_TEMPLATE.format(
        name=model.name,
        years=model.years,
        contact_html=contact_html,
        skills_html=skills_html,
        results_html=results_html,
    )
