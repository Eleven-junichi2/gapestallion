import gapestallion.entity


def test_entity_init():
    entity_a = gapestallion.entity.Entity()
    entity_b = gapestallion.entity.Entity()
    assert entity_a.id == 0
    assert entity_b.id == 1
