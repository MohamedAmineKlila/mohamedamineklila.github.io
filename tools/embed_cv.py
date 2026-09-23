import base64
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
html_path = root / "index.html"
pdf_path = root / "resume.pdf"

content = html_path.read_text(encoding="utf-8")
data = base64.b64encode(pdf_path.read_bytes()).decode()
uri = "data:application/pdf;base64," + data

if 'href="data:application/pdf;base64,' in content:
    content = re.sub(r'href="data:application/pdf;base64,[^"]+"', 'href="' + uri + '"', content, count=1)
else:
    content = content.replace(
        'href="resume.pdf"',
        'href="' + uri + '"',
        1,
    )

html_path.write_text(content, encoding="utf-8", newline="")
print("re-embedded resume.pdf into index.html")