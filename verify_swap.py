from app import app
from models import RelicEffect

with app.app_context():
    print("Poise effects:")
    for e in RelicEffect.query.filter(RelicEffect.description.like('Poise%')).all():
        print(f'  {e.description}')
        print(f'    Effect: {e.effect}')
        print(f'    Notes: {e.notes}')
        print()
    
    print("Improved [Status] Resistance:")
    for e in RelicEffect.query.filter(RelicEffect.description.like('Improved [Status]%')).all():
        print(f'  {e.description}')
        print(f'    Effect: {e.effect}')
        print(f'    Notes: {e.notes}')
