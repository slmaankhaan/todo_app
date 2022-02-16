from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'deform>=2.0a2'
]
setup(name='todo',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = todo:main
      """
      )
