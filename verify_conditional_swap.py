from app import app
from models import RelicEffect

with app.app_context():
    print("Self-explanatory examples (should NOT be swapped):")
    for e in RelicEffect.query.filter(RelicEffect.description.like('Vigor%')).limit(2).all():
        print(f'  {e.description}')
        print(f'    Effect: {e.effect}')
        print(f'    Notes: {e.notes}')
        print()
    
    print("Non-self-explanatory examples (SHOULD be swapped):")
    for e in RelicEffect.query.filter(RelicEffect.description.like('Poise%')).all():
        print(f'  {e.description}')
        print(f'    Effect: {e.effect}')
        print(f'    Notes: {e.notes}')
        print()
