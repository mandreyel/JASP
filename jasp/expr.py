from typing import List

class Expr:
    "Abstract base for all expressions."
    def __init__(self, line: int, col: int):
        self.line = line
        self.col = col

class AtomExpr(Expr):
    """
    An expression that evaluates to itself, such as a string, number or
    bool.
    """
    def __init__(self, value, line: int=None, col: int=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self) -> str:
        return f"Atom({self.value})"

class RefExpr(Expr):
    """An expression that references a variable."""
    def __init__(self, name: str, line: int=None, col: int=None):
        super().__init__(line, col)
        self.name = name

    def __repr__(self) -> str:
        return f"Ref({self.name})"

class IfExpr(Expr):
    def __init__(self, cond: Expr, true_branch: Expr, false_branch: Expr, line:
            int=None, col: int=None):
        super().__init__(line, col)
        self.cond = cond
        self.true_branch = true_branch
        self.false_branch = false_branch

    def __repr__(self) -> str:
        if self.false_branch:
            return f"If(cond: {self.cond} then: {self.true_branch} else: {self.false_branch})"
        else:
            return f"If(cond: {self.cond} then: {self.true_branch})"

class LetExpr(Expr):
    def __init__(self, name: str, value: Expr, line: int=None, col: int=None):
        super().__init__(line, col)
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"Let(name: {self.name} value: {self.value})"

class FnDefExpr(Expr):
    def __init__(self, name: str, params: List[str], body: Expr, line:
            int=None, col: int=None):
        super().__init__(line, col)
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self) -> str:
        return f"FnDef(name: {self.name} params: {self.params} body: {self.body})"

class FnCallExpr(Expr):
    def __init__(self, fn: Expr, args: List[Expr], line: int=None, col: int=None):
        super().__init__(line, col)
        self.fn = fn
        self.args = args

    def __repr__(self) -> str:
        return f"FnCall(fn: {self.fn} args: {self.args})"

class VectorExpr(Expr):
    def __init__(self, exprs: List[Expr], line: int=None, col: int=None):
        super().__init__(line, col)
        self.exprs = exprs

    def __repr__(self) -> str:
        return f"Vector({self.exprs})"

