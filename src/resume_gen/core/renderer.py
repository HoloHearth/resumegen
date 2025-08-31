from jinja2 import Environment, FileSystemLoader
from pathlib import Path
class Render:
    
    def __init__(self, template_dir: Path | str ="templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render(self, template_name:str, context: dict, **kwargs) -> str:
        template = self.env.get_template(template_name)
        merged_data = {**context, **kwargs}
        return template.render(merged_data)