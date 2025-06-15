from faker import Faker
from app import app, db
from models import Hero, Power, HeroPower
import random

fake = Faker()

with app.app_context():

    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Creating Powers
    power_names = [
        "Super Strength", "Flight", "Telekinesis", "Invisibility",
        "Elasticity", "Super Speed", "Fire Manipulation", "Ice Control"
    ]

    powers = []
    for name in power_names:
        power = Power(
            name=name,
            description=fake.text(max_nb_chars=80)
        )
        db.session.add(power)
        powers.append(power)

    db.session.commit()

    # Creating Heroes
    heroes = []
    for _ in range(10):
        hero = Hero(
            name=fake.name(),
            super_name=fake.unique.first_name() + "-" + fake.word().capitalize()
        )
        db.session.add(hero)
        heroes.append(hero)

    db.session.commit()

    # Creating HeroPowers 
    strengths = ["Strong", "Weak", "Average"]

    for _ in range(20):
        hero_power = HeroPower(
            strength=random.choice(strengths),
            hero=random.choice(heroes),
            power=random.choice(powers)
        )
        db.session.add(hero_power)

    db.session.commit()

    print("Done seeding!")
