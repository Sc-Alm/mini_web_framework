import jinja2


def jinja_page_render():
    bcc = jinja2.FileSystemBytecodeCache('templates/jinja_cache_bucket')
    templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
    templateEnv = jinja2.Environment(loader=templateLoader, bytecode_cache=bcc)
    TEMPLATE_FILE = "index.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render()
