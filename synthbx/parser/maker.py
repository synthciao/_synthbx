from synthbx.xast.schema import Schema
from synthbx.xast.program import Program
from synthbx.xast.unit import Unit
from synthbx.xast.type import Type, SubType, EquiType, SymbolType, NumberType
from synthbx.xast.relation import Relation
from synthbx.xast.directive import Directive, DirectiveType
from synthbx.xast.rule import Rule
from synthbx.xast.atom import Atom
from synthbx.xast.negation import Negation
from synthbx.xast.constraint import Constraint
from synthbx.xast.conjunction import Conjunction
from synthbx.xast.variable import Variable
from synthbx.xast.constant import NumberConstant, SymbolConstant
from synthbx.xast.cmp import Cmp
from synthbx.xast.fact import Fact
from synthbx.util.list import flatten


def make_schema(relation_list):
    return Schema(relations=relation_list)


def make_program(unit_list):
    unit_list = list(flatten(unit_list))
    type_decl_list = [u for u in unit_list if isinstance(u, Type)]
    relation_decl_list = [u for u in unit_list if type(u) is Relation]
    directive_list = [u for u in unit_list if type(u) is Directive]
    rule_list = [u for u in unit_list if type(u) is Rule]
    fact_list = [u for u in unit_list if type(u) is Fact]

    return Program(
        type_decls=type_decl_list,
        relation_decls=relation_decl_list,
        directives=directive_list,
        rules=rule_list,
        facts=fact_list
    )


def make_type(type_name):
    if type_name == 'symbol':
        return SymbolType()
    elif type_name == 'number':
        return NumberType()
    else:
        return make_subtype(type_name, 'symbol')


def make_subtype(ident, type_name):
    return SubType(name=ident, base=Type(type_name))


def make_equitype(ident, type_name):
    return EquiType(name=ident, alias=Type(type_name))


def make_relation(ident, attribute_decl_list):
    return Relation(name=ident, schema=attribute_decl_list)


def make_directive(io, ident_list):
    return [Directive(type=DirectiveType(io), name=ident) for ident in ident_list]


def make_conjunction(items):
    return Conjunction(items=items)


def make_rule(head, body):
    return Rule(head=head, body=body)


def make_fact(atom):
    return Fact(atom=atom)


def make_atom(ident, argument_list):
    return Atom(name=ident, args=argument_list)


def make_negation(atom):
    return Negation(atom=atom)


def make_constraint(variable, cmp, constant):
    return Constraint(cmp=cmp, var=variable, const=constant)


def make_variable(variable):
    return Variable(name=variable)


def make_constant(constant):
    if type(constant) is int:
        return NumberConstant(value=constant)
    elif type(constant) is str:
        return SymbolConstant(value=constant)
    else:
        raise NotImplementedError('Only number and symbol are implemented')
