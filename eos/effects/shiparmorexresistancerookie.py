# shipArmorEXResistanceRookie
#
# Used by:
# Ship: Devoter
# Ship: Impairor
# Ship: Phobos
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", ship.getModifiedItemAttr("rookieArmorResistanceBonus"))
