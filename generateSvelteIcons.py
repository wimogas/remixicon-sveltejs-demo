import os

absolute_path = os.path.dirname(__file__)
relative_svg_path = "src/assets/svg-clean"
relative_icons_path = "src/icons/"
full_svg_path = os.path.join(absolute_path, relative_svg_path)
full_icons_path = os.path.join(absolute_path, relative_icons_path)

res = []

for path in os.listdir(full_svg_path):
  if os.path.isfile(os.path.join(full_svg_path, path)):
    res.append(path)

template_icon = os.path.join(absolute_path, "src/_TemplateIcon.svelte")

def createSvelteIcon(svg):
  with open(template_icon, "r") as f:
    template = f.read()
    svg_name = svg.replace(".svg", "")
    component = template.replace("[icon].svg", svg).replace("./", "../").replace("[icon-name]", svg_name)
    new_file = open(os.path.join(absolute_path, relative_icons_path + svg_name + "Icon.svelte"), "w")
    new_file.write(component)
    new_file.close()

for svg in res:
  createSvelteIcon(svg)

icons = []

for path in os.listdir(full_icons_path):
  if os.path.isfile(os.path.join(full_icons_path, path)):
    icons.append("export { default as " + path.replace(".svelte", "") + " } from './icons/" + path + "';\n")

main_icons = open(os.path.join(absolute_path, "src/icons.js"), "w")
for icon in icons: 
  main_icons.write(icon)
