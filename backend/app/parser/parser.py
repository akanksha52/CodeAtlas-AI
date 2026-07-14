class CodeParser:
    def parse(self, code: bytes):
        tree = self.parser.parse(code)
        root = tree.root_node
        symbols = []