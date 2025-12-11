from app import app
from db import db
from models import RelicEffect

with app.app_context():
    total = RelicEffect.query.count()
    regular = RelicEffect.query.filter_by(is_deep=False).count()
    deep = RelicEffect.query.filter_by(is_deep=True).count()
    
    print(f'Total relic effects: {total}')
    print(f'Regular effects: {regular}')
    print(f'Deep effects: {deep}')
    
    print('\nSample regular effects:')
    for e in RelicEffect.query.filter_by(is_deep=False).limit(5):
        print(f'  - {e.description}: {e.effect}')
    
    print('\nSample deep effects:')
    for e in RelicEffect.query.filter_by(is_deep=True).limit(5):
        print(f'  - {e.description}: {e.effect}')
