## md -> pdf

```bash
# https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master
pandoc readme.md --pdf-engine=xelatex --standalone --toc --number-sections --template=templates/eisvogel.tex -V "CJKmainfont=Microsoft YaHei UI" -o a.pdf
```
