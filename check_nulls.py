from app import app
from db import db
from models import RelicEffect

with app.app_context():
    # Check for NULL values in notes and stackable columns
    null_notes = RelicEffect.query.filter(RelicEffect.notes == None).count()
    empty_notes = RelicEffect.query.filter(RelicEffect.notes == '').count()
    null_stackable = RelicEffect.query.filter(RelicEffect.stackable == None).count()
    
    print(f'Notes with NULL: {null_notes}')
    print(f'Notes with empty string: {empty_notes}')
    print(f'Stackable with NULL: {null_stackable}')
    
    # Check relic_id column
    null_relic_id = RelicEffect.query.filter(RelicEffect.relic_id == None).count()
    non_null_relic_id = RelicEffect.query.filter(RelicEffect.relic_id != None).count()
    
    print(f'\nRelic_id with NULL: {null_relic_id}')
    print(f'Relic_id with non-NULL: {non_null_relic_id}')
    
    # Sample records with empty notes
    print('\nSample records with empty notes field:')
    for e in RelicEffect.query.filter(RelicEffect.notes == '').limit(3):
        print(f'  - {e.description}: notes="{e.notes}" (repr: {repr(e.notes)})')
