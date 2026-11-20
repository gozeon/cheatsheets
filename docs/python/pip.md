
## 离线缓存和安装

```
mkdir offline_wheels

# 缓存
pip download --only-binary=:all: --platform win_amd64 --python-version 3.12 -d ./offline_wheels "markitdown[all]" pypdf pdfplumber reportlab pypdfium2 pytesseract pdf2image Pillow pandas defusedxml lxml openpyxl

# 安装
pip install --no-index --find-links=./offline_wheels "markitdown[all]" pypdf pdfplumber reportlab pypdfium2 pytesseract pdf2image Pillow pandas defusedxml lxml openpyxl
```
