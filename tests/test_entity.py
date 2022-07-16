import gapes


def test_entity_init():
    entity_a = gapes.Entity()
    entity_b = gapes.Entity()
    assert entity_a.id == 0
    assert entity_b.id == 1
