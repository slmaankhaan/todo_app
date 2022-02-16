from pyramid.config import Configurator
from pyramid_sqlalchemy import metadata

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_chameleon')
    config.add_static_view(name='deform_static', path='deform:static')
    config.add_static_view(name='static', path='todo:static')
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')
    config.scan()
    metadata.create_all()
    return config.make_wsgi_app()
