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

    item = {}
    item['name'] = "Example Blog"
    item['url'] = "http://example.com"
    item['image'] = "http://example.com/image.jpg"
    item['one_liner'] = "This is an example blog."
    jinja_item_list.append(item)
    jinja_vars['blogs'] = jinja_item_list

    output = template.render(vars=jinja_vars)

    print(output)

if __name__ == "__main__":
    main()
