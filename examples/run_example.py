import json
from pathlib import Path

from resumelens.pipeline import run_pipeline

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "resumes"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

RESUMES = (
    ("juan_jaramillo.txt", "FULL_STACK_DEVELOPER"),
    ("juliana_galvis.txt", "MACHINE_LEARNING_ENGINEER"),
    ("tony_stark.txt", "DATA_SCIENTIST"),
    ("andres_aristizabal.txt", "SOFTWARE_ARCHITECT"),
)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    for resume_file, target_profile in RESUMES:
        text = (DATA_DIR / resume_file).read_text()
        results, html = run_pipeline(text, target_profile)

        html_path = OUTPUT_DIR / resume_file.replace(".txt", ".html")
        html_path.write_text(html)

        print(f"--- {resume_file} ({target_profile}) ---")
        print(json.dumps(results, indent=2))
        print(html_path)
        print()


if __name__ == "__main__":
    main()