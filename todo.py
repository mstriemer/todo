#! /usr/bin/python

try:
    import simplejson as json
except ImportError:
    import json
import argparse
import sys

class Task(object):
    def __init__(self, title=None, description=None):
        if title is None:
            raise ValueError, 'A title is required'
        self.title = title
        self.description = description

    def save(self):
        with open('tasks.json', 'w') as f:
            f.write(self.as_json())

    def as_json(self):
        return json.dumps({
            'title': self.title,
            'description': self.description
        })

    def as_text(self):
        return "{0}: {1}".format(self.title, self.description)

    @classmethod
    def from_file(cls):
        with open('tasks.json', 'r') as f:
            attrs_str = f.read()
        attrs = json.loads(attrs_str)
        return cls(**attrs)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Process tasks.")
        parser.add_argument('title', type=str, help='The title of the task')
        parser.add_argument('--desc', type=str, help='The description of the task')
        args = parser.parse_args()

        t = Task(title=args.title, description=args.desc)
        t.save()

    print Task.from_file().as_text()
