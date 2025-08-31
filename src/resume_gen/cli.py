import typer
from typing import List, Optional
from pathlib import Path
app = typer.Typer(help="Resume_Gen CLI")

@app.command()
def render(
    format: str = typer.Option("html", "--format", "-f", help="Output format (html, pdf, latex, md)"),
    output: Path = typer.Option("resume.html", "--output", "-o", help="Output file path"),
    tags: Optional[List[str]] = typer.Option(None, "--tags", "-t", help="Filter entries by tags"),
):
    """
    Render the resume into a specific format.
    """
    print(format, output, tags)
    #data = parser.load_resume("data/resume.json")
    #if tags:
        #data = filter.filter_entries(data, tags)
    #content = renderer.render(data, format=format)
    #output.write_text(content)
    #typer.echo(f"✅ Resume rendered to {output}")

if __name__ == "__main__":
    app()