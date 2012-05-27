#/usr/bin/env python3

import markdown

md=markdown.Markdown(output_format="html5")

ethics=open("hackerethik.mdown","r").read()
template=open("web/template.html","r").read()

html=template.replace("{{CONTENT}}",md.convert(ethics))

open("web/index.html","w").write(html)

