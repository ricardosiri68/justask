'''
Domain model package, all his inner modules have direact accesss
'''
from importlib import import_module
import public # type: ignore

module_register = (
    'poll',
    'question',
    'answer_option',
    'answer'
)

for register in module_register:
    mod = import_module(f'core.entities.{register}')
    public.add(mod.__all__) # type: ignore
