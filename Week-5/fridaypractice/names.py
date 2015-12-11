names = [{ 'id': 1, 'name': 'John'},
         { 'id': 2, 'name': 'Molly'},
         { 'id': 3, 'name': 'Jane'}]


class MyMagic:
    def __init__(self, names):
        self.names = names

    def names_as_list(self):
        return [x['name'] for x in self.names]

    def names_with_J(self):
        return list(filter(lambda name: name.startswith('J'), self.names_as_list()))
