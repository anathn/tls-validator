from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def dump_html(domain_data):
    
    ev = Environment(loader=FileSystemLoader("templates/"))
    template = ev.get_template("index.tpl")
    today_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return template.render(today_date=today_date, domain_data=domain_data)

