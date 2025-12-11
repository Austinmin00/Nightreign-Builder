from app import app
from db import db
from models import Character, Chalice, ChaliceSlot, Relic, RelicEffect, GuaranteedRelic
import csv
import os

def seed():
    db.drop_all()
    db.create_all()

    # ------------------------------
    # 1. CHARACTERS
    # ------------------------------
    characters = [
        Character(
            key="wylder",
            name="Wylder", 
            role="Damage Dealer",
            description="A swift and agile fighter who excels in close combat.",
            image="wylder_model.png",
            main_weapon="Greatsword",
            secondary_weapon="Small Shield",
            passive="Sixth Sense",
            skill="Clawshot",
            ultimate="Onslaught Stake",
            vigor="240",
            fp="65",
            endurance="54",
            STR="A",
            DEX="B",
            INT="C",
            FAI="C",
            ARC="C"),
        Character(
            key="guardian",
            name="Guardian", 
            role="Tank",
            description="A sturdy protector who can absorb massive amounts of damage.",
            image="guardian_model.png",
            main_weapon="Halberd",
            secondary_weapon="Greatshield",
            passive="Steel Guard",
            skill="Whirlwind",
            ultimate="Wings of Salvation",
            vigor="280",
            fp="55",
            endurance="60",
            STR="B",
            DEX="C",
            INT="D",
            FAI="C",
            ARC="C"),
        Character(
            key="ironeye",
            name="Ironeye", 
            role="Support",
            description="A tactical support character who aids allies with buffs and healing.",
            image="ironeye_model.png",
            main_weapon="Bow",
            secondary_weapon="None",
            passive="Eagle Eye",
            skill="Marking",
            ultimate="Single Shot",
            vigor="200",
            fp="55",
            endurance="56",
            STR="C",
            DEX="A",
            INT="D",
            FAI="D",
            ARC="B"),
        Character(
            key="raider",
            name="Raider", 
            role="Berserker",
            description="A fierce warrior who thrives in the chaos of battle, dealing massive damage.",
            image="raider_model.png",
            main_weapon="Greataxe",
            secondary_weapon="None",
            passive="Fighter's Resolve",
            skill="Retaliate",
            ultimate="Totem Stela",
            vigor="260",
            fp="55",
            endurance="60",
            STR="S",
            DEX="C",
            INT="D",
            FAI="D",
            ARC="C"),
        Character(
            key="revenant",
            name="Revenant", 
            role="Necromancer",
            description="A dark sorcerer who commands the undead to do their bidding.",
            image="revenant_model.png",
            main_weapon="Claws",
            secondary_weapon="Finger Seal",
            passive="Necromancy",
            skill="Summon Spirit",
            ultimate="Immortal March",
            vigor="200",
            fp="80",
            endurance="54",
            STR="C",
            DEX="C",
            INT="B",
            FAI="S",
            ARC="B"),
        Character(
            key="recluse",
            name="Recluse", 
            role="Stealth Assassin",
            description="A master of shadows, striking from the darkness with deadly precision.",
            image="recluse_model.png",
            main_weapon="Staff",
            secondary_weapon="None",
            passive="Elemental Defense",
            skill="Magic Cocktail",
            ultimate="Soulblood Song",
            vigor="200",
            fp="80",
            endurance="54",
            STR="D",
            DEX="C",
            INT="S",
            FAI="S",
            ARC="C"),
        Character(
            key="duchess",
            name="Duchess", 
            role="Mage",
            description="A powerful spellcaster who wields elemental magic to control the battlefield.",
            image="duchess_model.png",
            main_weapon="Dagger",
            secondary_weapon="None",
            passive="Magnificent Poise",
            skill="Restage",
            ultimate="Finale",
            vigor="220",
            fp="75",
            endurance="54",
            STR="D",
            DEX="B",
            INT="A",
            FAI="B",
            ARC="C"),
        Character(
            key="executor",
            name="Executor", 
            role="Defender",
            description="A stalwart protector who shields allies and controls the flow of battle.",
            image="executor_model.png",
            main_weapon="Katana",
            secondary_weapon="None",
            passive="Tenacity",
            skill="Suncatcher",
            ultimate="Aspect of the Crucible: Beast",
            vigor="220",
            fp="55",
            endurance="54",
            STR="C",
            DEX="S",
            INT="D",
            FAI="D",
            ARC="S"),
        Character(
            key="scholar",
            name="Scholar", 
            role="Tactician",
            description="An academic who walks the Lands Between. Boasting impressive arcane levels, he gains incredible advantages through battlefield observation.",
            image="scholar_model.png",
            main_weapon="Thrusting Sword",
            secondary_weapon="None",
            passive="Bagcraft",
            skill="Analyze",
            ultimate="Communion",
            vigor="220",
            fp="65",
            endurance="54",
            STR="D",
            DEX="C",
            INT="C",
            FAI="C",
            ARC="S"),
        Character(
            key="undertaker",
            name="Undertaker", 
            role="Berserker",
            description="An abbess who was mandated to slay the Nightlord. Boasting impressive strength and faith, she sends enemies to the afterlife with ruthless efficiency.",
            image="undertaker_model.png",
            main_weapon="Hammer",
            secondary_weapon="None",
            passive="Confluence",
            skill="Trance",
            ultimate="Loathsome Hex",
            vigor="220",
            fp="65",
            endurance="54",
            STR="A",
            DEX="D",
            INT="D",
            FAI="A",
            ARC="C"),
    ]
    
    db.session.add_all(characters)
    db.session.commit()

    # Character-specific chalices
    wylder_chalice = [
        Chalice(name="wylder_main", img_base="static/images/chalices/wylder_chalices/wylder_main.png", character_id=characters[0].id),
        Chalice(name="wylder_goblet", img_base="static/images/chalices/wylder_chalices/wylder_goblet.png", character_id=characters[0].id),
        Chalice(name="wylder_urn", img_base="static/images/chalices/wylder_chalices/wylder_urn.png", character_id=characters[0].id),
        Chalice(name="soot_covered_wylder_urn", img_base="static/images/chalices/wylder_chalices/soot_covered_wylder_urn.png", character_id=characters[0].id),
        Chalice(name="sealed_wylder_urn", img_base="static/images/chalices/wylder_chalices/sealed_wylder_urn.png", character_id=characters[0].id),
        Chalice(name="decrepit_wylder_goblet", img_base="static/images/chalices/wylder_chalices/decrepit_wylder_goblet.png", character_id=characters[0].id),
        Chalice(name="forgotten_ wylder_goblet", img_base="static/images/chalices/wylder_chalices/forgotten_wylder_goblet.png", character_id=characters[0].id)
    ]

    guardian_chalice = [
        Chalice(name="guardian_main", img_base="static/images/chalices/guardian_chalices/guardian_main.png", character_id=characters[1].id),
        Chalice(name="guardian_goblet", img_base="static/images/chalices/guardian_chalices/guardian_goblet.png", character_id=characters[1].id),
        Chalice(name="guardian_urn", img_base="static/images/chalices/guardian_chalices/guardian_urn.png", character_id=characters[1].id),
        Chalice(name="soot_covered_guardian_urn", img_base="static/images/chalices/guardian_chalices/soot_covered_guardian_urn.png", character_id=characters[1].id),
        Chalice(name="sealed_guardian_urn", img_base="static/images/chalices/guardian_chalices/sealed_guardian_urn.png", character_id=characters[1].id),
        Chalice(name="decrepit_guardian_goblet", img_base="static/images/chalices/guardian_chalices/decrepit_guardian_goblet.png", character_id=characters[1].id),
        Chalice(name="forgotten_guardian_goblet", img_base="static/images/chalices/guardian_chalices/forgotten_guardian_goblet.png", character_id=characters[1].id)
    ]

    ironeye_chalice = [
        Chalice(name="ironeye_main", img_base="static/images/chalices/ironeye_chalices/ironeye_main.png", character_id=characters[2].id),
        Chalice(name="ironeye_goblet", img_base="static/images/chalices/ironeye_chalices/ironeye_goblet.png", character_id=characters[2].id),
        Chalice(name="ironeye_urn", img_base="static/images/chalices/ironeye_chalices/ironeye_urn.png", character_id=characters[2].id),
        Chalice(name="soot_covered_ironeye_urn", img_base="static/images/chalices/ironeye_chalices/soot_covered_ironeye_urn.png", character_id=characters[2].id),
        Chalice(name="sealed_ironeye_urn", img_base="static/images/chalices/ironeye_chalices/sealed_ironeye_urn.png", character_id=characters[2].id),
        Chalice(name="decrepit_ironeye_goblet", img_base="static/images/chalices/ironeye_chalices/decrepit_ironeye_goblet.png", character_id=characters[2].id),
        Chalice(name="forgotten_ironeye_goblet", img_base="static/images/chalices/ironeye_chalices/forgotten_ironeye_goblet.png", character_id=characters[2].id)
    ]

    raider_chalice = [
        Chalice(name="raider_main", img_base="static/images/chalices/raider_chalices/raider_main.png", character_id=characters[3].id),
        Chalice(name="raider_goblet", img_base="static/images/chalices/raider_chalices/raider_goblet.png", character_id=characters[3].id),
        Chalice(name="raider_urn", img_base="static/images/chalices/raider_chalices/raider_urn.png", character_id=characters[3].id),
        Chalice(name="soot_covered_raider_urn", img_base="static/images/chalices/raider_chalices/soot_covered_raider_urn.png", character_id=characters[3].id),
        Chalice(name="sealed_raider_urn", img_base="static/images/chalices/raider_chalices/sealed_raider_urn.png", character_id=characters[3].id),
        Chalice(name="decrepit_raider_goblet", img_base="static/images/chalices/raider_chalices/decrepit_raider_goblet.png", character_id=characters[3].id),
        Chalice(name="forgotten_raider_goblet", img_base="static/images/chalices/raider_chalices/forgotten_raider_goblet.png", character_id=characters[3].id)
    ]

    revenant_chalice = [
        Chalice(name="revenant_main", img_base="static/images/chalices/revenant_chalices/revenant_main.png", character_id=characters[4].id),
        Chalice(name="revenant_goblet", img_base="static/images/chalices/revenant_chalices/revenant_goblet.png", character_id=characters[4].id),
        Chalice(name="revenant_urn", img_base="static/images/chalices/revenant_chalices/revenant_urn.png", character_id=characters[4].id),
        Chalice(name="soot_covered_revenant_urn", img_base="static/images/chalices/revenant_chalices/soot_covered_revenant_urn.png", character_id=characters[4].id),
        Chalice(name="sealed_revenant_urn", img_base="static/images/chalices/revenant_chalices/sealed_revenant_urn.png", character_id=characters[4].id),
        Chalice(name="decrepit_revenant_goblet", img_base="static/images/chalices/revenant_chalices/decrepit_revenant_goblet.png", character_id=characters[4].id),
        Chalice(name="forgotten_revenant_goblet", img_base="static/images/chalices/revenant_chalices/forgotten_revenant_goblet.png", character_id=characters[4].id)
    ]

    recluse_chalice = [
        Chalice(name="recluse_main", img_base="static/images/chalices/recluse_chalices/recluse_main.png", character_id=characters[5].id),
        Chalice(name="recluse_goblet", img_base="static/images/chalices/recluse_chalices/recluse_goblet.png", character_id=characters[5].id),
        Chalice(name="recluse_urn", img_base="static/images/chalices/recluse_chalices/recluse_urn.png", character_id=characters[5].id),
        Chalice(name="soot_covered_recluse_urn", img_base="static/images/chalices/recluse_chalices/soot_covered_recluse_urn.png", character_id=characters[5].id),
        Chalice(name="sealed_recluse_urn", img_base="static/images/chalices/recluse_chalices/sealed_recluse_urn.png", character_id=characters[5].id),
        Chalice(name="decrepit_recluse_goblet", img_base="static/images/chalices/recluse_chalices/decrepit_recluse_goblet.png", character_id=characters[5].id),
        Chalice(name="forgotten_recluse_goblet", img_base="static/images/chalices/recluse_chalices/forgotten_recluse_goblet.png", character_id=characters[5].id)
    ]

    duchess_chalice = [
        Chalice(name="duchess_main", img_base="static/images/chalices/duchess_chalices/duchess_main.png", character_id=characters[6].id),
        Chalice(name="duchess_goblet", img_base="static/images/chalices/duchess_chalices/duchess_goblet.png", character_id=characters[6].id),
        Chalice(name="duchess_urn", img_base="static/images/chalices/duchess_chalices/duchess_urn.png", character_id=characters[6].id),
        Chalice(name="soot_covered_duchess_urn", img_base="static/images/chalices/duchess_chalices/soot_covered_duchess_urn.png", character_id=characters[6].id),
        Chalice(name="sealed_duchess_urn", img_base="static/images/chalices/duchess_chalices/sealed_duchess_urn.png", character_id=characters[6].id),
        Chalice(name="decrepit_duchess_goblet", img_base="static/images/chalices/duchess_chalices/decrepit_duchess_goblet.png", character_id=characters[6].id),
        Chalice(name="forgotten_duchess_goblet", img_base="static/images/chalices/duchess_chalices/forgotten_duchess_goblet.png", character_id=characters[6].id)
    ]

    executor_chalice = [
        Chalice(name="executor_main", img_base="static/images/chalices/executor_chalices/executor_main.png", character_id=characters[7].id),
        Chalice(name="executor_goblet", img_base="static/images/chalices/executor_chalices/executor_goblet.png", character_id=characters[7].id),
        Chalice(name="executor_urn", img_base="static/images/chalices/executor_chalices/executor_urn.png", character_id=characters[7].id),
        Chalice(name="soot_covered_executor_urn", img_base="static/images/chalices/executor_chalices/soot_covered_executor_urn.png", character_id=characters[7].id),
        Chalice(name="sealed_executor_urn", img_base="static/images/chalices/executor_chalices/sealed_executor_urn.png", character_id=characters[7].id),
        Chalice(name="decrepit_executor_goblet", img_base="static/images/chalices/executor_chalices/decrepit_executor_goblet.png", character_id=characters[7].id),
        Chalice(name="forgotten_executor_goblet", img_base="static/images/chalices/executor_chalices/forgotten_executor_goblet.png", character_id=characters[7].id)
    ]

    scholar_chalice = [
        Chalice(name="scholar_main", img_base="static/images/chalices/scholar_chalices/scholar_main.png", character_id=characters[8].id),
        Chalice(name="scholar_goblet", img_base="static/images/chalices/scholar_chalices/scholar_goblet.png", character_id=characters[8].id),
        Chalice(name="scholar_urn", img_base="static/images/chalices/scholar_chalices/scholar_urn.png", character_id=characters[8].id),
        Chalice(name="soot_covered_scholar_urn", img_base="static/images/chalices/scholar_chalices/soot_covered_scholar_urn.png", character_id=characters[8].id),
        Chalice(name="sealed_scholar_urn", img_base="static/images/chalices/scholar_chalices/sealed_scholar_urn.png", character_id=characters[8].id),
        Chalice(name="decrepit_scholar_goblet", img_base="static/images/chalices/scholar_chalices/decrepit_scholar_goblet.png", character_id=characters[8].id),
        Chalice(name="forgotten_scholar_goblet", img_base="static/images/chalices/scholar_chalices/forgotten_scholar_goblet.png", character_id=characters[8].id)
    ]

    undertaker_chalice = [
        Chalice(name="undertaker_main", img_base="static/images/chalices/undertaker_chalices/undertaker_main.png", character_id=characters[9].id),
        Chalice(name="undertaker_goblet", img_base="static/images/chalices/undertaker_chalices/undertaker_goblet.png", character_id=characters[9].id),
        Chalice(name="undertaker_urn", img_base="static/images/chalices/undertaker_chalices/undertaker_urn.png", character_id=characters[9].id),
        Chalice(name="soot_covered_undertaker_urn", img_base="static/images/chalices/undertaker_chalices/soot_covered_undertaker_urn.png", character_id=characters[9].id),
        Chalice(name="sealed_undertaker_urn", img_base="static/images/chalices/undertaker_chalices/sealed_undertaker_urn.png", character_id=characters[9].id),
        Chalice(name="decrepit_undertaker_goblet", img_base="static/images/chalices/undertaker_chalices/decrepit_undertaker_goblet.png", character_id=characters[9].id),
        Chalice(name="forgotten_undertaker_goblet", img_base="static/images/chalices/undertaker_chalices/forgotten_undertaker_goblet.png", character_id=characters[9].id)
    ]
    # Global chalices (shared across all characters)
    global_chalices = [
        Chalice(name="giants_cradle", img_base="static/images/chalices/all_nightfarers/giants_cradle.png", character_id=None),
        Chalice(name="sacred_erdtree", img_base="static/images/chalices/all_nightfarers/sacred_erdtree.png", character_id=None),
        Chalice(name="spirit_shelter", img_base="static/images/chalices/all_nightfarers/spirit_shelter.png", character_id=None),
        Chalice(name="scadutree_grail", img_base="static/images/chalices/all_nightfarers/scadutree_grail.png", character_id=None)
    ]

    db.session.add_all(wylder_chalice + guardian_chalice + ironeye_chalice +
                       raider_chalice + revenant_chalice + recluse_chalice + duchess_chalice + 
                       executor_chalice + scholar_chalice + undertaker_chalice + global_chalices)
    db.session.commit()  # IDs needed for slots

    # ------------------------------

    # Example: assign colors to slots for each chalice

    # Wylder Chalice Slots

    wylder_main = [
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[0].id, slot_index=5, color="blue")
    ]

    wylder_goblet = [
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[1].id, slot_index=5, color="green")
    ]

    wylder_urn = [
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[2].id, slot_index=5, color="blue")
    ]

    soot_covered_wylder_urn = [
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[3].id, slot_index=5, color="yellow")
    ]

    sealed_wylder_urn = [
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[4].id, slot_index=5, color="yellow")
    ]

    decrepit_wylder_goblet = [
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[5].id, slot_index=5, color="yellow")
    ]

    forgotten_wylder_goblet = [
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=wylder_chalice[6].id, slot_index=5, color="white")
    ]

    # Guardian Chalice Slots

    guardian_main = [
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[0].id, slot_index=5, color="green")
    ]

    guardian_goblet = [
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[1].id, slot_index=5, color="green")
    ]

    guardian_urn = [
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[2].id, slot_index=5, color="yellow")
    ]

    soot_covered_guardian_urn = [
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[3].id, slot_index=5, color="green")
    ]

    sealed_guardian_urn = [
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[4].id, slot_index=5, color="blue")
    ]

    decrepit_guardian_goblet = [
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[5].id, slot_index=5, color="green")
    ]

    forgotten_guardian_goblet = [
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=guardian_chalice[6].id, slot_index=5, color="white")
    ]

    # Ironeye Chalice Slots

    ironeye_main = [
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[0].id, slot_index=5, color="green")
    ]

    ironeye_goblet = [
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[1].id, slot_index=5, color="yellow")
    ]

    ironeye_urn = [
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[2].id, slot_index=5, color="green")
    ]

    soot_covered_ironeye_urn = [
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[3].id, slot_index=5, color="yellow")
    ]

    sealed_ironeye_urn = [
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[4].id, slot_index=5, color="red")
    ]

    decrepit_ironeye_goblet = [
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=3, color=" blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[5].id, slot_index=5, color="green")
    ]

    forgotten_ironeye_goblet = [
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=ironeye_chalice[6].id, slot_index=5, color="white")
    ]

    # Raider Chalice Slots

    raider_main = [
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[0].id, slot_index=5, color="yellow")
    ]

    raider_goblet = [
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[1].id, slot_index=5, color="yellow")
    ]

    raider_urn = [
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[2].id, slot_index=5, color="green")
    ]  

    soot_covered_raider_urn = [
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[3].id, slot_index=5, color="green")
    ]

    sealed_raider_urn = [
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[4].id, slot_index=5, color="blue")
    ]

    decrepit_raider_goblet = [
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[5].id, slot_index=5, color="green")
    ]

    forgotten_raider_goblet = [
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=raider_chalice[6].id, slot_index=5, color="white")
    ]

    # Revenant Chalice Slots

    revenant_main = [
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[0].id, slot_index=5, color="green")
    ]  

    revenant_goblet = [
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[1].id, slot_index=5, color="green")
    ]

    revenant_urn = [
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[2].id, slot_index=5, color="yellow")
    ]

    soot_covered_revenant_urn = [
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[3].id, slot_index=5, color="yellow")
    ]

    sealed_revenant_urn = [
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[4].id, slot_index=5, color="red")
    ]

    decrepit_revenant_goblet = [
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[5].id, slot_index=5, color="yellow")
    ]

    forgotten_revenant_goblet = [
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=revenant_chalice[6].id, slot_index=5, color="white")
    ]

    # Recluse Chalice Slots

    recluse_main = [
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=recluse_chalice[0].id, slot_index=5, color="green")
    ]

    recluse_goblet = [
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[1].id, slot_index=5, color="yellow")
    ]

    recluse_urn = [
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[2].id, slot_index=5, color="green")
    ]

    soot_covered_recluse_urn = [
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[3].id, slot_index=5, color="yellow")
    ]

    sealed_recluse_urn = [
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[4].id, slot_index=5, color="red")
    ]

    decrepit_recluse_goblet = [
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[5].id, slot_index=5, color="blue")
    ]

    forgotten_recluse_goblet = [
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=recluse_chalice[6].id, slot_index=5, color="white")
    ]

    # Duchess Chalice Slots

    duchess_main = [
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[0].id, slot_index=5, color="yellow")
    ]

    duchess_goblet = [
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[1].id, slot_index=5, color="green")
    ]

    duchess_urn = [
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[2].id, slot_index=5, color="blue")
    ]

    soot_covered_duchess_urn = [
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[3].id, slot_index=5, color="green")
    ]

    sealed_duchess_urn = [
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[4].id, slot_index=5, color="yellow")
    ]

    decrepit_duchess_goblet = [
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[5].id, slot_index=5, color="green")
    ]

    forgotten_duchess_goblet = [
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=duchess_chalice[6].id, slot_index=5, color="white")
    ]

    # Executor Chalice Slots

    executor_main = [
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[0].id, slot_index=5, color="green")
    ]  

    executor_goblet = [
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=executor_chalice[1].id, slot_index=5, color="green")
    ]

    executor_urn = [
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[2].id, slot_index=5, color="yellow")
    ]

    soot_covered_executor_urn = [
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[3].id, slot_index=5, color="blue")
    ]   

    sealed_executor_urn = [
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=executor_chalice[4].id, slot_index=5, color="blue")
    ]

    decrepit_executor_goblet = [
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[5].id, slot_index=5, color="yellow")
    ]

    forgotten_executor_goblet = [
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=executor_chalice[6].id, slot_index=5, color="white")
    ]

    # Scholar Chalice Slots

    scholar_main = [
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=scholar_chalice[0].id, slot_index=5, color="yellow")
    ]

    scholar_goblet = [
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[1].id, slot_index=5, color="yellow")
    ]

    scholar_urn = [
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[2].id, slot_index=5, color="yellow")
    ]

    soot_covered_scholar_urn = [
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[3].id, slot_index=5, color="green")
    ]

    sealed_scholar_urn = [
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=3, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[4].id, slot_index=5, color="blue")
    ]

    decrepit_scholar_goblet = [
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[5].id, slot_index=5, color="green")
    ]

    forgotten_scholar_goblet = [
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=scholar_chalice[6].id, slot_index=5, color="white")
    ]

    # Undertaker Chalice Slots

    undertaker_main = [
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=2, color="white"),
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[0].id, slot_index=5, color="yellow")
    ]

    undertaker_goblet = [
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=2, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[1].id, slot_index=5, color="yellow")
    ]

    undertaker_urn = [
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=0, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=2, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=4, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[2].id, slot_index=5, color="green")
    ]

    soot_covered_undertaker_urn = [
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=1, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[3].id, slot_index=5, color="blue")
    ]

    sealed_undertaker_urn = [
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=0, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=1, color="green"),
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=3, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=4, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[4].id, slot_index=5, color="red")
    ]

    decrepit_undertaker_goblet = [
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=0, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=1, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=2, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=3, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=4, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[5].id, slot_index=5, color="blue")
    ]

    forgotten_undertaker_goblet = [
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=0, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=1, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=2, color="red"),
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=3, color="blue"),
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=4, color="yellow"),
        ChaliceSlot(chalice_id=undertaker_chalice[6].id, slot_index=5, color="green")
    ]

    def make_global_chalice_slots(chalice, color):
            return [ChaliceSlot(chalice_id=chalice.id, slot_index=i, color=color) for i in range(6)]

    giants_cradle = make_global_chalice_slots(global_chalices[0], "blue")
    sacred_erdtree = make_global_chalice_slots(global_chalices[1], "yellow")
    spirit_shelter = make_global_chalice_slots(global_chalices[2], "green")
    scadutree_grail = make_global_chalice_slots(global_chalices[3], "red")


    db.session.add_all(wylder_main + wylder_goblet + wylder_urn + soot_covered_wylder_urn + sealed_wylder_urn + decrepit_wylder_goblet + forgotten_wylder_goblet + guardian_main + guardian_goblet + guardian_urn + soot_covered_guardian_urn + sealed_guardian_urn + decrepit_guardian_goblet + forgotten_guardian_goblet + ironeye_main + ironeye_goblet + ironeye_urn + soot_covered_ironeye_urn + sealed_ironeye_urn + decrepit_ironeye_goblet + forgotten_ironeye_goblet + raider_main + raider_goblet + raider_urn + soot_covered_raider_urn + sealed_raider_urn + decrepit_raider_goblet + forgotten_raider_goblet + revenant_main + revenant_goblet + revenant_urn + soot_covered_revenant_urn + sealed_revenant_urn + decrepit_revenant_goblet + forgotten_revenant_goblet + recluse_main + recluse_goblet + recluse_urn + soot_covered_recluse_urn + sealed_recluse_urn + decrepit_recluse_goblet + forgotten_recluse_goblet + duchess_main + duchess_goblet + duchess_urn + soot_covered_duchess_urn + sealed_duchess_urn + decrepit_duchess_goblet + forgotten_duchess_goblet + executor_main + executor_goblet + executor_urn + soot_covered_executor_urn + sealed_executor_urn + decrepit_executor_goblet + forgotten_executor_goblet + scholar_main + scholar_goblet + scholar_urn + soot_covered_scholar_urn + sealed_scholar_urn + decrepit_scholar_goblet + forgotten_scholar_goblet + undertaker_main + undertaker_urn + undertaker_goblet + soot_covered_undertaker_urn + sealed_undertaker_urn + decrepit_undertaker_goblet + forgotten_undertaker_goblet + giants_cradle + sacred_erdtree + spirit_shelter + scadutree_grail)
    db.session.commit()

    # ------------------------------
    # 4. RELIC EFFECTS (from CSVs)
    # ------------------------------
    
    # Load regular relic effects
    regular_csv_path = os.path.join("postgres-docker", "data", "Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Expanded.csv")
    with open(regular_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        regular_effects = []
        for row in reader:
            effect = RelicEffect(
                type=row['Category'],
                description=row['Relic Description'],
                effect=row['Effect'],
                stackable=row['Stackable with self?'] or 'Unknown',
                notes=row['Notes'] if row['Notes'] else None,  # NULL if empty
                is_deep=False
            )
            regular_effects.append(effect)
        db.session.add_all(regular_effects)
    
    print(f"Loaded {len(regular_effects)} regular relic effects")
    
    # Load deep relic effects
    deep_csv_path = os.path.join("postgres-docker", "data", "Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded.csv")
    with open(deep_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        deep_effects = []
        for row in reader:
            effect = RelicEffect(
                type=row['Category'],
                description=row['Relic Description'],
                effect=row['Effect'],
                stackable=row['Stackable with self?'] or 'Unknown',
                notes=row['Notes'] if row['Notes'] else None,  # NULL if empty
                is_deep=True
            )
            deep_effects.append(effect)
        db.session.add_all(deep_effects)
    
    print(f"Loaded {len(deep_effects)} deep relic effects")

    # ------------------------------
    # 5. GUARANTEED RELICS (from CSV)
    # ------------------------------

    guaranteed_csv_path = os.path.join("postgres-docker", "data", "Guaranteed Relics.csv")
    with open(guaranteed_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        guaranteed_relics = []
        for row in reader:
            guaranteed = GuaranteedRelic(
                name=row['name'],
                color=row['color'],
                effect_1=row['effect 1'] if row['effect 1'] else None,
                effect_2=row['effect 2'] if row['effect 2'] else None,
                effect_3=row['effect 3'] if row['effect 3'] else None,
                amount_of_effects=int(row['amount of effects']) if row['amount of effects'] else None
            )
            guaranteed_relics.append(guaranteed)
        db.session.add_all(guaranteed_relics)

    db.session.commit()
    print("Seed completed successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed()