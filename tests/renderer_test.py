import pytest
from pathlib import Path
from src.resume_gen.core.renderer import Render  # <-- replace with the actual filename where your class lives


@pytest.fixture
def template_dir(tmp_path: Path):
    """Create a temporary template directory with sample templates."""
    template = tmp_path / "hello.html"
    template.write_text("Hello, {{ name }}!")

    another = tmp_path / "greet.html"
    another.write_text("{{ greeting }}, {{ person }}!")

    return tmp_path


def test_render_basic(template_dir):
    r = Render(template_dir)
    output = r.render("hello.html", {"name": "World"})
    assert output == "Hello, World!"


def test_render_with_extra_kwargs(template_dir):
    r = Render(template_dir)
    output = r.render("greet.html", {"person": "Alice"}, greeting="Hi")
    assert output == "Hi, Alice!"


def test_render_merges_kwargs_override(template_dir):
    r = Render(template_dir)
    # kwargs should override context
    output = r.render("hello.html", {"name": "Wrong"}, name="Correct")
    assert output == "Hello, Correct!"


def test_render_missing_template_raises(template_dir):
    r = Render(template_dir)
    with pytest.raises(Exception):  # more specifically jinja2.exceptions.TemplateNotFound
        r.render("does_not_exist.html", {})


def test_render_empty_context(template_dir):
    r = Render(template_dir)
    # No variables -> template renders with blanks
    output = r.render("greet.html", {}, greeting="Hello", person="Bob")
    assert output == "Hello, Bob!"
