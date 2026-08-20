import shutil
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

SRC = Path("src")
OUTPUT = Path("public")

env = Environment(loader=FileSystemLoader(SRC / "pages"))

def clear_output():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)

    OUTPUT.mkdir()

def copy_static():
    shutil.copytree(SRC / "static", OUTPUT / "static")

def generate_page(template, output, current_path="/", **context):
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        env.get_template(template).render(
            current_path=current_path,
            **context,
        )
    )

def generate_data_page(name):
    data = yaml.safe_load(
        (SRC / "data" / f"{name}.yaml").read_text()
    )

    generate_page(
        "entries.html",
        OUTPUT / "pages" / f"{name}.html",
        current_path=f"/pages/{name}.html",
        title=name.title(),
        items=data,
    )

def main():
    clear_output()

    (OUTPUT / ".nojekyll").touch()

    copy_static()

    generate_page(
        "index.html",
        OUTPUT / "index.html",
        current_path="/",
    )

    generate_page(
        "404.html",
        OUTPUT / "404.html",
    )

    for name in ("projects", "experiments", "friends"):
        generate_data_page(name)

if __name__ == "__main__":
    main()
