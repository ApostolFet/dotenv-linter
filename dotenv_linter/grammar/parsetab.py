
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT EQUAL NAME VALUE WHITESPACE\n        body :\n             | body line\n        \n        line : assign\n             | name\n             | comment\n        \n        assign : NAME EQUAL\n               | NAME EQUAL VALUE\n        name : NAMEcomment : COMMENTwhitespace : WHITESPACE'
    
_lr_action_items = {'NAME':([0,1,2,3,4,5,6,7,8,9,],[-1,6,-2,-3,-4,-5,-8,-9,-6,-7,]),'COMMENT':([0,1,2,3,4,5,6,7,8,9,],[-1,7,-2,-3,-4,-5,-8,-9,-6,-7,]),'$end':([0,1,2,3,4,5,6,7,8,9,],[-1,0,-2,-3,-4,-5,-8,-9,-6,-7,]),'EQUAL':([6,],[8,]),'VALUE':([8,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'line':([1,],[2,]),'assign':([1,],[3,]),'name':([1,],[4,]),'comment':([1,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> <empty>','body',0,'p_body','parser.py',69),
  ('body -> body line','body',2,'p_body','parser.py',70),
  ('line -> assign','line',1,'p_line','parser.py',78),
  ('line -> name','line',1,'p_line','parser.py',79),
  ('line -> comment','line',1,'p_line','parser.py',80),
  ('assign -> NAME EQUAL','assign',2,'p_assign','parser.py',86),
  ('assign -> NAME EQUAL VALUE','assign',3,'p_assign','parser.py',87),
  ('name -> NAME','name',1,'p_name','parser.py',97),
  ('comment -> COMMENT','comment',1,'p_comment','parser.py',101),
  ('whitespace -> WHITESPACE','whitespace',1,'p_whitespace','parser.py',105),
]
