from app import app
from db import db
from models import RelicEffect

with app.app_context():
    effects = RelicEffect.query.filter_by(is_deep=False).filter(RelicEffect.notes != None).all()
    non_self_exp = [e for e in effects if e.notes and 'self-explanatory' not in e.notes.lower()]
    
    print(f'Non-self-explanatory notes: {len(non_self_exp)}\n')
    
    for e in non_self_exp[:15]:
        print(f'Description: {e.description}')
        print(f'Effect: {e.effect}')
        print(f'Notes: {e.notes}')
        print('-' * 80)
