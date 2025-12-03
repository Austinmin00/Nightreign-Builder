from db import db
    
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)  # Unique key for character identification
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)  # Path to character image
    
    main_weapon = db.Column(db.String(50), nullable=False)
    secondary_weapon = db.Column(db.String(50), nullable=False)
    passive = db.Column(db.String(100), nullable=False)
    skill = db.Column(db.String(100), nullable=False)
    ultimate = db.Column(db.String(100), nullable=False)

    vigor = db.Column(db.String(10), nullable=False)
    fp = db.Column(db.String(10), nullable=False)
    endurance = db.Column(db.String(10), nullable=False)

    STR = db.Column(db.String(2), nullable=False)
    DEX = db.Column(db.String(2), nullable=False)
    INT = db.Column(db.String(2), nullable=False)
    FAI = db.Column(db.String(2), nullable=False)
    ARC = db.Column(db.String(2), nullable=False)

    chalices = db.relationship('Chalice', backref='character', lazy=True)

from db import db

class Chalice(db.Model):
    __tablename__ = "chalices"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    img_base = db.Column(db.String(200), nullable=False)  # Path to the chalice image
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=True)  # Null for global chalices

    # Optional backref to slots if needed
    slots = db.relationship("ChaliceSlot", backref="chalice", lazy=True)

class ChaliceFile(db.Model):
    __tablename__ = "chalice_files"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(120), nullable=False)  # Path to the chalice file
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)

class ChaliceSlot(db.Model):
    __tablename__ = "chalice_slots"

    id = db.Column(db.Integer, primary_key=True)
    chalice_id = db.Column(db.Integer, db.ForeignKey("chalices.id"), nullable=False)
    slot_index = db.Column(db.Integer, nullable=False)  # 0–5
    color = db.Column(db.String(20), nullable=False)  # e.g., "red", "blue", "yellow", "white"
    relic_id = db.Column(db.Integer, db.ForeignKey("relics.id"), nullable=True)  # null until assigned



class Relic(db.Model):
    __tablename__ = "relics"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    color = db.Column(db.String(20), nullable=False)  # red, blue, yellow, or any
    max_effects = db.Column(db.Integer, default=3)
    img_base = db.Column(db.String(200), nullable=False)  # base image path

    # Optional backref to effects
    effects = db.relationship("RelicEffect", backref="relic", lazy=True)


class RelicEffect(db.Model):
    __tablename__ = "relic_effects"

    id = db.Column(db.Integer, primary_key=True)
    relic_id = db.Column(db.Integer, db.ForeignKey("relics.id"), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., AP_flat, STR, INT, etc.
    value = db.Column(db.Float, nullable=False)  # numeric value
    effect_index = db.Column(db.Integer, nullable=False)  # 1, 2, 3 for ordering/level


class WorkshopSession(db.Model):
    __tablename__ = "workshop_sessions"

    id = db.Column(db.Integer, primary_key=True)

    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)
    chalice_id = db.Column(db.Integer, db.ForeignKey("chalices.id"), nullable=True)

    # e.g. [4, None, 10, None, None]
    slot_relics = db.Column(db.JSON, nullable=False, default=list)
