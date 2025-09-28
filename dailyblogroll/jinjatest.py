from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("jinjatest"),
    autoescape=select_autoescape()
)

def main():
    template = env.get_template("dailyblogtemplate.html")

    jinja_vars = {}
    jinja_item_list = []
    jinja_vars['title'] = "My Blogroll"
    jinja_vars['previous'] = "page1.html"

    item = {}
    item['name'] = "Example Blog"
    item['url'] = "https://chasingdings.com"
    item['image'] = "images/303118891c325ea66b90a1409e3c9a44a16f48d4458d738ed0cb05a1e09852bc.png"
    item['one_liner'] = "This is an example blog."
    jinja_item_list.append(item)
    jinja_vars['blogs'] = jinja_item_list

    output = template.render(vars=jinja_vars)

    print(output)

if __name__ == "__main__":
    main()
