# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class DarkStarDBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'dspdb':
            return 'dspdb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'dspdb':
            return 'dspdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'dspdb' or \
            obj2._meta.app_label == 'dspdb':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'dspdb':
            return db == 'dspdb'
        return None

        
class Abilities(models.Model):
    abilityid = models.PositiveSmallIntegerField(db_column='abilityId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    job = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    validtarget = models.PositiveSmallIntegerField(db_column='validTarget')  # Field name made lowercase.
    recasttime = models.PositiveSmallIntegerField(db_column='recastTime')  # Field name made lowercase.
    recastid = models.PositiveSmallIntegerField(db_column='recastId')  # Field name made lowercase.
    message1 = models.PositiveSmallIntegerField()
    message2 = models.PositiveSmallIntegerField()
    animation = models.PositiveSmallIntegerField()
    animationtime = models.PositiveSmallIntegerField(db_column='animationTime')  # Field name made lowercase.
    casttime = models.PositiveSmallIntegerField(db_column='castTime')  # Field name made lowercase.
    actiontype = models.PositiveIntegerField(db_column='actionType')  # Field name made lowercase.
    range = models.FloatField()
    isaoe = models.PositiveIntegerField(db_column='isAOE')  # Field name made lowercase.
    ce = models.SmallIntegerField(db_column='CE')  # Field name made lowercase.
    ve = models.SmallIntegerField(db_column='VE')  # Field name made lowercase.
    meritmodid = models.SmallIntegerField(db_column='meritModID')  # Field name made lowercase.
    addtype = models.SmallIntegerField(db_column='addType')  # Field name made lowercase.
    content_tag = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abilities'


class AbilitiesCharges(models.Model):
    recastid = models.PositiveSmallIntegerField(db_column='recastId', primary_key=True)  # Field name made lowercase.
    job = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    maxcharges = models.PositiveIntegerField(db_column='maxCharges')  # Field name made lowercase.
    chargetime = models.PositiveSmallIntegerField(db_column='chargeTime')  # Field name made lowercase.
    meritmodid = models.PositiveSmallIntegerField(db_column='meritModID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abilities_charges'
        unique_together = (('recastid', 'job', 'level'),)


class AccountIpRecord(models.Model):
    login_time = models.DateTimeField(primary_key=True)
    accid = models.IntegerField()
    charid = models.IntegerField()
    client_ip = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_ip_record'
        unique_together = (('login_time', 'accid'),)


class Accounts(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email2 = models.CharField(max_length=64)
    timecreate = models.DateTimeField()
    timelastmodify = models.DateTimeField()
    content_ids = models.PositiveIntegerField()
    expansions = models.PositiveSmallIntegerField()
    features = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    priv = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'


class AccountsBanned(models.Model):
    accid = models.PositiveIntegerField(primary_key=True)
    timebann = models.DateTimeField()
    timeunbann = models.DateTimeField()
    banncomment = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_banned'


class AccountsParties(models.Model):
    charid = models.ForeignKey('AccountsSessions', models.DO_NOTHING, db_column='charid', primary_key=True)
    partyid = models.PositiveIntegerField()
    partyflag = models.PositiveSmallIntegerField()
    allianceid = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_parties'


class AccountsSessions(models.Model):
    accid = models.PositiveIntegerField(unique=True)
    charid = models.PositiveIntegerField(primary_key=True)
    targid = models.PositiveSmallIntegerField()
    linkshellid1 = models.PositiveIntegerField()
    linkshellrank1 = models.PositiveSmallIntegerField()
    linkshellid2 = models.PositiveIntegerField()
    linkshellrank2 = models.PositiveSmallIntegerField()
    session_key = models.CharField(max_length=20)
    server_addr = models.IntegerField()
    server_port = models.PositiveSmallIntegerField()
    client_addr = models.IntegerField()
    client_port = models.PositiveSmallIntegerField()
    version_mismatch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_sessions'


class AuctionHouse(models.Model):
    itemid = models.PositiveSmallIntegerField()
    stack = models.PositiveIntegerField()
    seller = models.PositiveIntegerField()
    seller_name = models.CharField(max_length=15, blank=True, null=True)
    date = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=15, blank=True, null=True)
    sale = models.PositiveIntegerField()
    sell_date = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'auction_house'


class AuditChat(models.Model):
    lineid = models.AutoField(db_column='lineID', primary_key=True)  # Field name made lowercase.
    speaker = models.TextField()
    type = models.TextField()
    lsname = models.TextField(db_column='lsName', blank=True, null=True)  # Field name made lowercase.
    recipient = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_chat'


class AuditGm(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    gm_name = models.CharField(max_length=16)
    command = models.CharField(max_length=40)
    full_string = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'audit_gm'
        unique_together = (('date_time', 'gm_name'),)


class Augments(models.Model):
    augmentid = models.PositiveSmallIntegerField(db_column='augmentId', primary_key=True)  # Field name made lowercase.
    multiplier = models.SmallIntegerField()
    modid = models.PositiveSmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()
    ispet = models.IntegerField(db_column='isPet')  # Field name made lowercase.
    pettype = models.PositiveIntegerField(db_column='petType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'augments'
        unique_together = (('augmentid', 'multiplier', 'modid', 'ispet', 'pettype'),)


class AutomatonSpells(models.Model):
    spellid = models.PositiveSmallIntegerField(primary_key=True)
    skilllevel = models.PositiveSmallIntegerField()
    heads = models.PositiveIntegerField()
    enfeeble = models.PositiveSmallIntegerField()
    immunity = models.PositiveSmallIntegerField()
    removes = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'automaton_spells'


class BcnmBattlefield(models.Model):
    bcnmid = models.PositiveSmallIntegerField(db_column='bcnmId')  # Field name made lowercase.
    battlefieldnumber = models.IntegerField(db_column='battlefieldNumber', blank=True, null=True)  # Field name made lowercase.
    monsterid = models.IntegerField(db_column='monsterId')  # Field name made lowercase.
    conditions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bcnm_battlefield'


class BcnmInfo(models.Model):
    bcnmid = models.PositiveSmallIntegerField(db_column='bcnmId', primary_key=True)  # Field name made lowercase.
    zoneid = models.PositiveIntegerField(db_column='zoneId')  # Field name made lowercase.
    name = models.CharField(max_length=30)
    fastestname = models.CharField(db_column='fastestName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fastestpartysize = models.PositiveIntegerField(db_column='fastestPartySize')  # Field name made lowercase.
    fastesttime = models.PositiveIntegerField(db_column='fastestTime', blank=True, null=True)  # Field name made lowercase.
    timelimit = models.PositiveSmallIntegerField(db_column='timeLimit')  # Field name made lowercase.
    levelcap = models.PositiveSmallIntegerField(db_column='levelCap')  # Field name made lowercase.
    partysize = models.PositiveSmallIntegerField(db_column='partySize')  # Field name made lowercase.
    lootdropid = models.PositiveSmallIntegerField(db_column='lootDropId')  # Field name made lowercase.
    rules = models.PositiveSmallIntegerField()
    ismission = models.PositiveIntegerField(db_column='isMission')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcnm_info'


class BcnmLoot(models.Model):
    lootdropid = models.PositiveSmallIntegerField(db_column='LootDropId')  # Field name made lowercase.
    itemid = models.PositiveSmallIntegerField(db_column='itemId')  # Field name made lowercase.
    rolls = models.PositiveSmallIntegerField()
    lootgroupid = models.PositiveIntegerField(db_column='lootGroupId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcnm_loot'


class BcnmTreasureChests(models.Model):
    bcnmid = models.PositiveSmallIntegerField(db_column='bcnmId')  # Field name made lowercase.
    battlefieldnumber = models.IntegerField(db_column='battlefieldNumber', blank=True, null=True)  # Field name made lowercase.
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcnm_treasure_chests'


class BlueSpellList(models.Model):
    spellid = models.SmallIntegerField(primary_key=True)
    mob_skill_id = models.PositiveSmallIntegerField()
    set_points = models.SmallIntegerField()
    trait_category = models.SmallIntegerField()
    trait_category_weight = models.SmallIntegerField()
    primary_sc = models.SmallIntegerField()
    secondary_sc = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_spell_list'
        unique_together = (('spellid', 'mob_skill_id'),)


class BlueSpellMods(models.Model):
    spellid = models.PositiveSmallIntegerField(db_column='spellId', primary_key=True)  # Field name made lowercase.
    modid = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_spell_mods'
        unique_together = (('spellid', 'modid'),)


class BlueTraits(models.Model):
    trait_category = models.PositiveSmallIntegerField(primary_key=True)
    trait_points_needed = models.PositiveSmallIntegerField()
    traitid = models.PositiveIntegerField()
    modifier = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'blue_traits'
        unique_together = (('trait_category', 'trait_points_needed', 'modifier'),)


class CharBlacklist(models.Model):
    charid_owner = models.PositiveIntegerField()
    charid_target = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'char_blacklist'
        unique_together = (('charid_target', 'charid_owner'),)


class CharEffects(models.Model):
    charid = models.PositiveIntegerField()
    effectid = models.PositiveSmallIntegerField()
    icon = models.PositiveSmallIntegerField()
    power = models.PositiveSmallIntegerField()
    tick = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    subid = models.PositiveSmallIntegerField()
    subpower = models.SmallIntegerField()
    tier = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_effects'


class CharEquip(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    slotid = models.PositiveIntegerField()
    equipslotid = models.PositiveIntegerField()
    containerid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_equip'
        unique_together = (('charid', 'equipslotid'),)


class CharExp(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    mode = models.PositiveIntegerField()
    war = models.PositiveSmallIntegerField()
    mnk = models.PositiveSmallIntegerField()
    whm = models.PositiveSmallIntegerField()
    blm = models.PositiveSmallIntegerField()
    rdm = models.PositiveSmallIntegerField()
    thf = models.PositiveSmallIntegerField()
    pld = models.PositiveSmallIntegerField()
    drk = models.PositiveSmallIntegerField()
    bst = models.PositiveSmallIntegerField()
    brd = models.PositiveSmallIntegerField()
    rng = models.PositiveSmallIntegerField()
    sam = models.PositiveSmallIntegerField()
    nin = models.PositiveSmallIntegerField()
    drg = models.PositiveSmallIntegerField()
    smn = models.PositiveSmallIntegerField()
    blu = models.PositiveSmallIntegerField()
    cor = models.PositiveSmallIntegerField()
    pup = models.PositiveSmallIntegerField()
    dnc = models.PositiveSmallIntegerField()
    sch = models.PositiveSmallIntegerField()
    geo = models.PositiveSmallIntegerField()
    run = models.PositiveSmallIntegerField()
    merits = models.PositiveIntegerField()
    limits = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_exp'


class CharInventory(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    location = models.PositiveIntegerField()
    slot = models.PositiveIntegerField()
    itemid = models.PositiveSmallIntegerField(db_column='itemId')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    bazaar = models.PositiveIntegerField()
    signature = models.CharField(max_length=20)
    extra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'char_inventory'
        unique_together = (('charid', 'location', 'slot'),)


class CharJobs(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    unlocked = models.PositiveIntegerField()
    genkai = models.PositiveIntegerField()
    war = models.PositiveIntegerField()
    mnk = models.PositiveIntegerField()
    whm = models.PositiveIntegerField()
    blm = models.PositiveIntegerField()
    rdm = models.PositiveIntegerField()
    thf = models.PositiveIntegerField()
    pld = models.PositiveIntegerField()
    drk = models.PositiveIntegerField()
    bst = models.PositiveIntegerField()
    brd = models.PositiveIntegerField()
    rng = models.PositiveIntegerField()
    sam = models.PositiveIntegerField()
    nin = models.PositiveIntegerField()
    drg = models.PositiveIntegerField()
    smn = models.PositiveIntegerField()
    blu = models.PositiveIntegerField()
    cor = models.PositiveIntegerField()
    pup = models.PositiveIntegerField()
    dnc = models.PositiveIntegerField()
    sch = models.PositiveIntegerField()
    geo = models.PositiveIntegerField()
    run = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_jobs'


class CharLook(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    face = models.PositiveIntegerField()
    race = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    head = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    hands = models.PositiveSmallIntegerField()
    legs = models.PositiveSmallIntegerField()
    feet = models.PositiveSmallIntegerField()
    main = models.PositiveSmallIntegerField()
    sub = models.PositiveSmallIntegerField()
    ranged = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_look'


class CharMerit(models.Model):
    charid = models.PositiveIntegerField()
    meritid = models.PositiveSmallIntegerField()
    upgrades = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_merit'
        unique_together = (('meritid', 'charid'),)


class CharPet(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    wyvernid = models.PositiveSmallIntegerField()
    automatonid = models.PositiveSmallIntegerField()
    unlocked_attachments = models.TextField(blank=True, null=True)
    equipped_attachments = models.TextField(blank=True, null=True)
    adventuringfellowid = models.PositiveSmallIntegerField()
    chocoboid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_pet'


class CharPoints(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    sandoria_cp = models.PositiveIntegerField()
    bastok_cp = models.PositiveIntegerField()
    windurst_cp = models.PositiveIntegerField()
    beastman_seal = models.PositiveIntegerField()
    kindred_seal = models.PositiveSmallIntegerField()
    kindred_crest = models.PositiveSmallIntegerField()
    high_kindred_crest = models.PositiveSmallIntegerField()
    sacred_kindred_crest = models.PositiveSmallIntegerField()
    ancient_beastcoin = models.PositiveSmallIntegerField()
    valor_point = models.PositiveSmallIntegerField()
    scyld = models.PositiveSmallIntegerField()
    guild_fishing = models.PositiveIntegerField()
    guild_woodworking = models.PositiveIntegerField()
    guild_smithing = models.PositiveIntegerField()
    guild_goldsmithing = models.PositiveIntegerField()
    guild_weaving = models.PositiveIntegerField()
    guild_leathercraft = models.PositiveIntegerField()
    guild_bonecraft = models.PositiveIntegerField()
    guild_alchemy = models.PositiveIntegerField()
    guild_cooking = models.PositiveIntegerField()
    cinder = models.PositiveIntegerField()
    fire_fewell = models.PositiveIntegerField()
    ice_fewell = models.PositiveIntegerField()
    wind_fewell = models.PositiveIntegerField()
    earth_fewell = models.PositiveIntegerField()
    lightning_fewell = models.PositiveIntegerField()
    water_fewell = models.PositiveIntegerField()
    light_fewell = models.PositiveIntegerField()
    dark_fewell = models.PositiveIntegerField()
    ballista_point = models.PositiveIntegerField()
    fellow_point = models.PositiveIntegerField()
    chocobuck_sandoria = models.PositiveSmallIntegerField()
    chocobuck_bastok = models.PositiveSmallIntegerField()
    chocobuck_windurst = models.PositiveSmallIntegerField()
    research_mark = models.PositiveIntegerField()
    tunnel_worm = models.PositiveIntegerField()
    morion_worm = models.PositiveIntegerField()
    phantom_worm = models.PositiveIntegerField()
    moblin_marble = models.PositiveIntegerField()
    infamy = models.PositiveSmallIntegerField()
    prestige = models.PositiveSmallIntegerField()
    legion_point = models.PositiveIntegerField()
    spark_of_eminence = models.PositiveIntegerField()
    shining_star = models.PositiveIntegerField()
    imperial_standing = models.PositiveIntegerField()
    runic_portal = models.PositiveIntegerField()
    leujaoam_assault_point = models.PositiveIntegerField()
    mamool_assault_point = models.PositiveIntegerField()
    lebros_assault_point = models.PositiveIntegerField()
    periqia_assault_point = models.PositiveIntegerField()
    ilrusi_assault_point = models.PositiveIntegerField()
    nyzul_isle_assault_point = models.PositiveIntegerField()
    zeni_point = models.PositiveIntegerField()
    jetton = models.PositiveIntegerField()
    therion_ichor = models.PositiveIntegerField()
    maw = models.PositiveIntegerField()
    allied_notes = models.PositiveIntegerField()
    bayld = models.PositiveIntegerField()
    kinetic_unit = models.PositiveSmallIntegerField()
    obsidian_fragment = models.PositiveIntegerField()
    lebondopt_wing = models.PositiveSmallIntegerField()
    pulchridopt_wing = models.PositiveSmallIntegerField()
    mweya_plasm = models.PositiveIntegerField()
    cruor = models.PositiveIntegerField()
    resistance_credit = models.PositiveIntegerField()
    dominion_note = models.PositiveIntegerField()
    fifth_echelon_trophy = models.PositiveIntegerField()
    fourth_echelon_trophy = models.PositiveIntegerField()
    third_echelon_trophy = models.PositiveIntegerField()
    second_echelon_trophy = models.PositiveIntegerField()
    first_echelon_trophy = models.PositiveIntegerField()
    cave_points = models.PositiveIntegerField()
    id_tags = models.PositiveIntegerField()
    op_credits = models.PositiveIntegerField()
    traverser_stones = models.PositiveIntegerField()
    voidstones = models.PositiveIntegerField()
    kupofried_corundums = models.PositiveIntegerField()
    imprimaturs = models.PositiveIntegerField()
    pheromone_sacks = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_points'


class CharProfile(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    rank_points = models.PositiveIntegerField()
    rank_sandoria = models.PositiveIntegerField()
    rank_bastok = models.PositiveIntegerField()
    rank_windurst = models.PositiveIntegerField()
    fame_sandoria = models.PositiveSmallIntegerField()
    fame_bastok = models.PositiveSmallIntegerField()
    fame_windurst = models.PositiveSmallIntegerField()
    fame_norg = models.PositiveSmallIntegerField()
    fame_jeuno = models.PositiveSmallIntegerField()
    fame_aby_konschtat = models.PositiveSmallIntegerField()
    fame_aby_tahrongi = models.PositiveSmallIntegerField()
    fame_aby_latheine = models.PositiveSmallIntegerField()
    fame_aby_misareaux = models.PositiveSmallIntegerField()
    fame_aby_vunkerl = models.PositiveSmallIntegerField()
    fame_aby_attohwa = models.PositiveSmallIntegerField()
    fame_aby_altepa = models.PositiveSmallIntegerField()
    fame_aby_grauberg = models.PositiveSmallIntegerField()
    fame_aby_uleguerand = models.PositiveSmallIntegerField()
    fame_adoulin = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_profile'


class CharRecast(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    id = models.SmallIntegerField()
    time = models.IntegerField()
    recast = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_recast'
        unique_together = (('charid', 'id'),)


class CharSkills(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    skillid = models.PositiveIntegerField()
    value = models.PositiveSmallIntegerField()
    rank = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_skills'
        unique_together = (('charid', 'skillid'),)


class CharSpells(models.Model):
    charid = models.PositiveIntegerField()
    spellid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_spells'
        unique_together = (('spellid', 'charid'),)


class CharStats(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    hp = models.PositiveSmallIntegerField()
    mp = models.PositiveSmallIntegerField()
    nameflags = models.PositiveIntegerField()
    mhflag = models.PositiveIntegerField()
    mjob = models.PositiveIntegerField()
    sjob = models.PositiveIntegerField()
    death = models.PositiveIntegerField()
    number_2h = models.PositiveIntegerField(db_column='2h')  # Field renamed because it wasn't a valid Python identifier.
    title = models.PositiveSmallIntegerField()
    bazaar_message = models.TextField(blank=True, null=True)
    zoning = models.PositiveIntegerField()
    mlvl = models.PositiveIntegerField()
    slvl = models.PositiveIntegerField()
    pet_id = models.PositiveSmallIntegerField()
    pet_type = models.PositiveSmallIntegerField()
    pet_hp = models.PositiveSmallIntegerField()
    pet_mp = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_stats'


class CharStorage(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    inventory = models.PositiveIntegerField()
    safe = models.PositiveIntegerField()
    locker = models.PositiveIntegerField()
    satchel = models.PositiveIntegerField()
    sack = models.PositiveIntegerField()
    case = models.PositiveIntegerField()
    wardrobe = models.PositiveIntegerField()
    wardrobe2 = models.PositiveIntegerField()
    wardrobe3 = models.PositiveIntegerField()
    wardrobe4 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char_storage'


class CharStyle(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    head = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    hands = models.PositiveSmallIntegerField()
    legs = models.PositiveSmallIntegerField()
    feet = models.PositiveSmallIntegerField()
    main = models.PositiveSmallIntegerField()
    sub = models.PositiveSmallIntegerField()
    ranged = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'char_style'


class CharUnlocks(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    sandoria_supply = models.PositiveIntegerField()
    bastok_supply = models.PositiveIntegerField()
    windurst_supply = models.PositiveIntegerField()
    mog_locker = models.PositiveIntegerField()
    runic_portal = models.PositiveIntegerField()
    maw = models.PositiveIntegerField()
    past_sandoria_tp = models.PositiveIntegerField()
    past_bastok_tp = models.PositiveIntegerField()
    past_windurst_tp = models.PositiveIntegerField()
    homepoints = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'char_unlocks'


class CharVars(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    varname = models.CharField(max_length=30)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_vars'
        unique_together = (('charid', 'varname'),)


class Chars(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    accid = models.PositiveIntegerField()
    charname = models.CharField(max_length=15)
    nation = models.PositiveIntegerField()
    pos_zone = models.PositiveSmallIntegerField()
    pos_prevzone = models.PositiveSmallIntegerField()
    pos_rot = models.PositiveIntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    moghouse = models.PositiveIntegerField()
    boundary = models.PositiveSmallIntegerField()
    home_zone = models.PositiveIntegerField()
    home_rot = models.PositiveIntegerField()
    home_x = models.FloatField()
    home_y = models.FloatField()
    home_z = models.FloatField()
    missions = models.TextField(blank=True, null=True)
    assault = models.TextField(blank=True, null=True)
    campaign = models.TextField(blank=True, null=True)
    quests = models.TextField(blank=True, null=True)
    keyitems = models.TextField(blank=True, null=True)
    set_blue_spells = models.TextField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    weaponskills = models.TextField(blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    zones = models.TextField(blank=True, null=True)
    playtime = models.PositiveIntegerField()
    unlocked_weapons = models.TextField(blank=True, null=True)
    gmlevel = models.PositiveSmallIntegerField()
    mentor = models.SmallIntegerField()
    campaign_allegiance = models.PositiveIntegerField()
    isstylelocked = models.IntegerField()
    nnameflags = models.PositiveIntegerField()
    moghancement = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'chars'


class ConquestSystem(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_control = models.IntegerField()
    region_control_prev = models.IntegerField()
    sandoria_influence = models.IntegerField()
    bastok_influence = models.IntegerField()
    windurst_influence = models.IntegerField()
    beastmen_influence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_system'


class DeliveryBox(models.Model):
    charid = models.PositiveIntegerField(primary_key=True)
    charname = models.CharField(max_length=15, blank=True, null=True)
    box = models.PositiveIntegerField()
    slot = models.PositiveSmallIntegerField()
    itemid = models.PositiveSmallIntegerField()
    itemsubid = models.PositiveSmallIntegerField()
    quantity = models.PositiveIntegerField()
    extra = models.TextField(blank=True, null=True)
    senderid = models.PositiveIntegerField()
    sender = models.CharField(max_length=15, blank=True, null=True)
    received = models.IntegerField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'delivery_box'
        unique_together = (('charid', 'box', 'slot'),)


class DespoilEffects(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    effectid = models.PositiveSmallIntegerField(db_column='effectId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'despoil_effects'


class ExpBase(models.Model):
    level = models.PositiveIntegerField(primary_key=True)
    exp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'exp_base'


class ExpTable(models.Model):
    level = models.IntegerField(primary_key=True)
    r1 = models.PositiveSmallIntegerField()
    r2 = models.PositiveSmallIntegerField()
    r3 = models.PositiveSmallIntegerField()
    r4 = models.PositiveSmallIntegerField()
    r5 = models.PositiveSmallIntegerField()
    r6 = models.PositiveSmallIntegerField()
    r7 = models.PositiveSmallIntegerField()
    r8 = models.PositiveSmallIntegerField()
    r9 = models.PositiveSmallIntegerField()
    r10 = models.PositiveSmallIntegerField()
    r11 = models.PositiveSmallIntegerField()
    r12 = models.PositiveSmallIntegerField()
    r13 = models.PositiveSmallIntegerField()
    r14 = models.PositiveSmallIntegerField()
    r15 = models.PositiveSmallIntegerField()
    r16 = models.PositiveSmallIntegerField()
    r17 = models.PositiveSmallIntegerField()
    r18 = models.PositiveSmallIntegerField()
    r19 = models.PositiveSmallIntegerField()
    r20 = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'exp_table'


class FishingFish(models.Model):
    fishid = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    min = models.PositiveIntegerField()
    max = models.PositiveIntegerField()
    watertype = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    stamina = models.PositiveIntegerField()
    log = models.PositiveIntegerField()
    quest = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_fish'


class FishingLure(models.Model):
    lureid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    fishid = models.PositiveSmallIntegerField()
    luck = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_lure'
        unique_together = (('lureid', 'fishid'),)


class FishingRod(models.Model):
    rodid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    fishid = models.PositiveSmallIntegerField()
    flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_rod'
        unique_together = (('rodid', 'fishid'),)


class FishingZone(models.Model):
    zoneid = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    fishid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fishing_zone'
        unique_together = (('zoneid', 'fishid'),)


class GuildItemPoints(models.Model):
    guildid = models.PositiveIntegerField(primary_key=True)
    itemid = models.PositiveSmallIntegerField()
    rank = models.PositiveSmallIntegerField()
    points = models.PositiveSmallIntegerField()
    max_points = models.PositiveSmallIntegerField()
    pattern = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_item_points'
        unique_together = (('guildid', 'itemid', 'pattern'),)


class GuildShops(models.Model):
    guildid = models.PositiveSmallIntegerField(primary_key=True)
    itemid = models.PositiveSmallIntegerField()
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    max_quantity = models.PositiveSmallIntegerField()
    daily_increase = models.PositiveSmallIntegerField()
    initial_quantity = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_shops'
        unique_together = (('guildid', 'itemid'),)


class Guilds(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    points_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'guilds'


class InstanceEntities(models.Model):
    instanceid = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'instance_entities'
        unique_together = (('instanceid', 'id'),)


class InstanceList(models.Model):
    instanceid = models.PositiveIntegerField(primary_key=True)
    instance_name = models.CharField(max_length=35)
    entrance_zone = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    start_rot = models.PositiveIntegerField()
    music_day = models.SmallIntegerField()
    music_night = models.SmallIntegerField()
    battlesolo = models.SmallIntegerField()
    battlemulti = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'instance_list'


class ItemArmor(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    level = models.PositiveIntegerField()
    ilevel = models.IntegerField()
    jobs = models.PositiveIntegerField()
    mid = models.PositiveSmallIntegerField(db_column='MId')  # Field name made lowercase.
    shieldsize = models.PositiveIntegerField(db_column='shieldSize')  # Field name made lowercase.
    scripttype = models.PositiveSmallIntegerField(db_column='scriptType')  # Field name made lowercase.
    slot = models.PositiveSmallIntegerField()
    rslot = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_armor'


class ItemBasic(models.Model):
    itemid = models.PositiveSmallIntegerField(primary_key=True)
    subid = models.PositiveSmallIntegerField()
    name = models.TextField()
    sortname = models.TextField()
    stacksize = models.PositiveIntegerField(db_column='stackSize')  # Field name made lowercase.
    flags = models.PositiveSmallIntegerField()
    ah = models.PositiveIntegerField(db_column='aH')  # Field name made lowercase.
    nosale = models.PositiveIntegerField(db_column='NoSale')  # Field name made lowercase.
    basesell = models.PositiveIntegerField(db_column='BaseSell')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_basic'


class ItemEquipment(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    level = models.PositiveIntegerField()
    ilevel = models.IntegerField()
    jobs = models.PositiveIntegerField()
    mid = models.PositiveSmallIntegerField(db_column='MId')  # Field name made lowercase.
    shieldsize = models.PositiveIntegerField(db_column='shieldSize')  # Field name made lowercase.
    scripttype = models.PositiveSmallIntegerField(db_column='scriptType')  # Field name made lowercase.
    slot = models.PositiveSmallIntegerField()
    rslot = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_equipment'


class ItemFurnishing(models.Model):
    itemid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    storage = models.PositiveIntegerField()
    moghancement = models.PositiveSmallIntegerField()
    element = models.PositiveIntegerField()
    aura = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'item_furnishing'


class ItemLatents(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    modid = models.PositiveSmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()
    latentid = models.SmallIntegerField(db_column='latentId')  # Field name made lowercase.
    latentparam = models.SmallIntegerField(db_column='latentParam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_latents'
        unique_together = (('itemid', 'modid', 'value', 'latentid', 'latentparam'),)


class ItemMods(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    modid = models.PositiveSmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_mods'
        unique_together = (('itemid', 'modid'),)


class ItemModsPet(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    modid = models.PositiveSmallIntegerField(db_column='modId')  # Field name made lowercase.
    value = models.SmallIntegerField()
    pettype = models.PositiveIntegerField(db_column='petType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_mods_pet'
        unique_together = (('itemid', 'modid', 'pettype'),)


class ItemPuppet(models.Model):
    itemid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    slot = models.PositiveIntegerField()
    element = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'item_puppet'


class ItemUsable(models.Model):
    itemid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    validtargets = models.PositiveIntegerField(db_column='validTargets')  # Field name made lowercase.
    activation = models.PositiveIntegerField()
    animation = models.PositiveSmallIntegerField()
    animationtime = models.PositiveIntegerField(db_column='animationTime')  # Field name made lowercase.
    maxcharges = models.PositiveIntegerField(db_column='maxCharges')  # Field name made lowercase.
    usedelay = models.PositiveIntegerField(db_column='useDelay')  # Field name made lowercase.
    reusedelay = models.PositiveIntegerField(db_column='reuseDelay')  # Field name made lowercase.
    aoe = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'item_usable'


class ItemWeapon(models.Model):
    itemid = models.PositiveSmallIntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    skill = models.PositiveIntegerField()
    subskill = models.IntegerField()
    ilvl_skill = models.SmallIntegerField()
    ilvl_parry = models.SmallIntegerField()
    ilvl_macc = models.SmallIntegerField()
    dmgtype = models.PositiveIntegerField(db_column='dmgType')  # Field name made lowercase.
    hit = models.PositiveIntegerField()
    delay = models.IntegerField()
    dmg = models.PositiveIntegerField()
    unlock_points = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item_weapon'


class JobPoints(models.Model):
    job_pointid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    upgrade = models.PositiveIntegerField()
    jobs = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'job_points'


class Linkshells(models.Model):
    linkshellid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    color = models.PositiveSmallIntegerField()
    poster = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    messagetime = models.PositiveIntegerField()
    postrights = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'linkshells'


class Merits(models.Model):
    meritid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    upgrade = models.PositiveIntegerField()
    value = models.SmallIntegerField()
    jobs = models.PositiveIntegerField()
    upgradeid = models.PositiveIntegerField()
    catagoryid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'merits'


class MobDroplist(models.Model):
    dropid = models.PositiveSmallIntegerField(db_column='dropId')  # Field name made lowercase.
    droptype = models.PositiveIntegerField(db_column='dropType')  # Field name made lowercase.
    groupid = models.PositiveIntegerField(db_column='groupId')  # Field name made lowercase.
    grouprate = models.PositiveSmallIntegerField(db_column='groupRate')  # Field name made lowercase.
    itemid = models.PositiveSmallIntegerField(db_column='itemId')  # Field name made lowercase.
    itemrate = models.PositiveSmallIntegerField(db_column='itemRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_droplist'


class MobFamilyMods(models.Model):
    familyid = models.PositiveSmallIntegerField(primary_key=True)
    modid = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()
    is_mob_mod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_family_mods'
        unique_together = (('familyid', 'modid'),)


class MobFamilySystem(models.Model):
    familyid = models.PositiveSmallIntegerField(primary_key=True)
    family = models.TextField(blank=True, null=True)
    systemid = models.PositiveIntegerField()
    system = models.TextField(blank=True, null=True)
    mobsize = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    hp = models.PositiveIntegerField(db_column='HP')  # Field name made lowercase.
    mp = models.PositiveIntegerField(db_column='MP')  # Field name made lowercase.
    str = models.PositiveSmallIntegerField(db_column='STR')  # Field name made lowercase.
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Field name made lowercase.
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Field name made lowercase.
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Field name made lowercase.
    int = models.PositiveSmallIntegerField(db_column='INT')  # Field name made lowercase.
    mnd = models.PositiveSmallIntegerField(db_column='MND')  # Field name made lowercase.
    chr = models.PositiveSmallIntegerField(db_column='CHR')  # Field name made lowercase.
    att = models.PositiveSmallIntegerField(db_column='ATT')  # Field name made lowercase.
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    acc = models.PositiveSmallIntegerField(db_column='ACC')  # Field name made lowercase.
    eva = models.PositiveSmallIntegerField(db_column='EVA')  # Field name made lowercase.
    slash = models.FloatField(db_column='Slash')  # Field name made lowercase.
    pierce = models.FloatField(db_column='Pierce')  # Field name made lowercase.
    h2h = models.FloatField(db_column='H2H')  # Field name made lowercase.
    impact = models.FloatField(db_column='Impact')  # Field name made lowercase.
    fire = models.FloatField(db_column='Fire')  # Field name made lowercase.
    ice = models.FloatField(db_column='Ice')  # Field name made lowercase.
    wind = models.FloatField(db_column='Wind')  # Field name made lowercase.
    earth = models.FloatField(db_column='Earth')  # Field name made lowercase.
    lightning = models.FloatField(db_column='Lightning')  # Field name made lowercase.
    water = models.FloatField(db_column='Water')  # Field name made lowercase.
    light = models.FloatField(db_column='Light')  # Field name made lowercase.
    dark = models.FloatField(db_column='Dark')  # Field name made lowercase.
    element = models.FloatField(db_column='Element')  # Field name made lowercase.
    detects = models.SmallIntegerField()
    charmable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_family_system'


class MobGroups(models.Model):
    groupid = models.PositiveIntegerField(primary_key=True)
    poolid = models.PositiveIntegerField()
    zoneid = models.PositiveSmallIntegerField()
    respawntime = models.PositiveIntegerField()
    spawntype = models.PositiveIntegerField()
    dropid = models.PositiveIntegerField()
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    mp = models.IntegerField(db_column='MP')  # Field name made lowercase.
    minlevel = models.PositiveIntegerField(db_column='minLevel')  # Field name made lowercase.
    maxlevel = models.PositiveIntegerField(db_column='maxLevel')  # Field name made lowercase.
    allegiance = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_groups'


class MobPets(models.Model):
    mob_mobid = models.PositiveIntegerField(primary_key=True)
    pet_offset = models.PositiveIntegerField()
    job = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_pets'


class MobPoolMods(models.Model):
    poolid = models.PositiveSmallIntegerField(primary_key=True)
    modid = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()
    is_mob_mod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_pool_mods'
        unique_together = (('poolid', 'modid'),)


class MobPools(models.Model):
    poolid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=24, blank=True, null=True)
    packet_name = models.CharField(max_length=24, blank=True, null=True)
    familyid = models.PositiveSmallIntegerField()
    modelid = models.CharField(max_length=20)
    mjob = models.PositiveIntegerField(db_column='mJob')  # Field name made lowercase.
    sjob = models.PositiveIntegerField(db_column='sJob')  # Field name made lowercase.
    cmbskill = models.PositiveIntegerField(db_column='cmbSkill')  # Field name made lowercase.
    cmbdelay = models.PositiveSmallIntegerField(db_column='cmbDelay')  # Field name made lowercase.
    cmbdmgmult = models.PositiveSmallIntegerField(db_column='cmbDmgMult')  # Field name made lowercase.
    behavior = models.PositiveSmallIntegerField()
    aggro = models.PositiveIntegerField()
    true_detection = models.PositiveIntegerField()
    links = models.PositiveIntegerField()
    mobtype = models.PositiveSmallIntegerField(db_column='mobType')  # Field name made lowercase.
    immunity = models.IntegerField()
    name_prefix = models.PositiveIntegerField()
    flag = models.PositiveIntegerField()
    entityflags = models.PositiveIntegerField(db_column='entityFlags')  # Field name made lowercase.
    animationsub = models.IntegerField()
    hasspellscript = models.PositiveIntegerField(db_column='hasSpellScript')  # Field name made lowercase.
    spelllist = models.SmallIntegerField(db_column='spellList')  # Field name made lowercase.
    namevis = models.IntegerField()
    roamflag = models.PositiveSmallIntegerField()
    skill_list_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_pools'


class MobSkillLists(models.Model):
    skill_list_name = models.CharField(max_length=40, blank=True, null=True)
    skill_list_id = models.PositiveSmallIntegerField(primary_key=True)
    mob_skill_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_skill_lists'
        unique_together = (('skill_list_id', 'mob_skill_id'),)


class MobSkills(models.Model):
    mob_skill_id = models.PositiveSmallIntegerField(primary_key=True)
    mob_anim_id = models.PositiveSmallIntegerField()
    mob_skill_name = models.CharField(max_length=40)
    mob_skill_aoe = models.PositiveIntegerField()
    mob_skill_distance = models.FloatField()
    mob_anim_time = models.PositiveSmallIntegerField()
    mob_prepare_time = models.PositiveSmallIntegerField()
    mob_valid_targets = models.PositiveSmallIntegerField()
    mob_skill_flag = models.PositiveIntegerField()
    mob_skill_param = models.SmallIntegerField()
    knockback = models.IntegerField()
    primary_sc = models.IntegerField()
    secondary_sc = models.IntegerField()
    tertiary_sc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_skills'


class MobSpawnMods(models.Model):
    mobid = models.PositiveIntegerField(primary_key=True)
    modid = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()
    is_mob_mod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spawn_mods'
        unique_together = (('mobid', 'modid'),)


class MobSpawnPoints(models.Model):
    mobid = models.IntegerField(primary_key=True)
    mobname = models.CharField(max_length=24, blank=True, null=True)
    polutils_name = models.CharField(max_length=50, blank=True, null=True)
    groupid = models.PositiveIntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    pos_rot = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spawn_points'


class MobSpellLists(models.Model):
    spell_list_name = models.CharField(max_length=30, blank=True, null=True)
    spell_list_id = models.PositiveSmallIntegerField(primary_key=True)
    spell_id = models.PositiveSmallIntegerField()
    min_level = models.PositiveIntegerField()
    max_level = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mob_spell_lists'
        unique_together = (('spell_list_id', 'spell_id'),)


class NmSpawnPoints(models.Model):
    mobid = models.IntegerField(primary_key=True)
    pos = models.PositiveIntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()

    class Meta:
        managed = False
        db_table = 'nm_spawn_points'
        unique_together = (('mobid', 'pos'),)


class NpcList(models.Model):
    npcid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=24, blank=True, null=True)
    polutils_name = models.CharField(max_length=50, blank=True, null=True)
    pos_rot = models.PositiveIntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    flag = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    speedsub = models.PositiveIntegerField()
    animation = models.PositiveIntegerField()
    animationsub = models.PositiveIntegerField()
    namevis = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    entityflags = models.PositiveIntegerField(db_column='entityFlags')  # Field name made lowercase.
    look = models.CharField(max_length=20)
    name_prefix = models.PositiveIntegerField()
    content_tag = models.CharField(max_length=14, blank=True, null=True)
    widescan = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'npc_list'


class PetList(models.Model):
    petid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    poolid = models.PositiveIntegerField()
    minlevel = models.PositiveIntegerField(db_column='minLevel')  # Field name made lowercase.
    maxlevel = models.PositiveIntegerField(db_column='maxLevel')  # Field name made lowercase.
    time = models.PositiveIntegerField()
    element = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pet_list'


class PetName(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pet_name'


class ServerVariables(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_variables'


class SkillCaps(models.Model):
    level = models.PositiveIntegerField(primary_key=True)
    r0 = models.PositiveSmallIntegerField()
    r1 = models.PositiveSmallIntegerField()
    r2 = models.PositiveSmallIntegerField()
    r3 = models.PositiveSmallIntegerField()
    r4 = models.PositiveSmallIntegerField()
    r5 = models.PositiveSmallIntegerField()
    r6 = models.PositiveSmallIntegerField()
    r7 = models.PositiveSmallIntegerField()
    r8 = models.PositiveSmallIntegerField()
    r9 = models.PositiveSmallIntegerField()
    r10 = models.PositiveSmallIntegerField()
    r11 = models.PositiveSmallIntegerField()
    r12 = models.PositiveSmallIntegerField()
    r13 = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_caps'


class SkillRanks(models.Model):
    skillid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=12, blank=True, null=True)
    war = models.PositiveIntegerField()
    mnk = models.PositiveIntegerField()
    whm = models.PositiveIntegerField()
    blm = models.PositiveIntegerField()
    rdm = models.PositiveIntegerField()
    thf = models.PositiveIntegerField()
    pld = models.PositiveIntegerField()
    drk = models.PositiveIntegerField()
    bst = models.PositiveIntegerField()
    brd = models.PositiveIntegerField()
    rng = models.PositiveIntegerField()
    sam = models.PositiveIntegerField()
    nin = models.PositiveIntegerField()
    drg = models.PositiveIntegerField()
    smn = models.PositiveIntegerField()
    blu = models.PositiveIntegerField()
    cor = models.PositiveIntegerField()
    pup = models.PositiveIntegerField()
    dnc = models.PositiveIntegerField()
    sch = models.PositiveIntegerField()
    geo = models.PositiveIntegerField()
    run = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_ranks'


class SkillchainDamageModifiers(models.Model):
    chain_level = models.CharField(primary_key=True, max_length=1)
    chain_count = models.CharField(max_length=1)
    initial_modifier = models.IntegerField()
    magic_burst_modifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skillchain_damage_modifiers'
        unique_together = (('chain_level', 'chain_count'),)


class SpellList(models.Model):
    spellid = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    jobs = models.CharField(max_length=22)
    group = models.PositiveIntegerField()
    element = models.PositiveIntegerField()
    zonemisc = models.PositiveSmallIntegerField()
    validtargets = models.PositiveIntegerField(db_column='validTargets')  # Field name made lowercase.
    skill = models.PositiveIntegerField()
    mpcost = models.PositiveSmallIntegerField(db_column='mpCost')  # Field name made lowercase.
    casttime = models.PositiveSmallIntegerField(db_column='castTime')  # Field name made lowercase.
    recasttime = models.PositiveIntegerField(db_column='recastTime')  # Field name made lowercase.
    message = models.PositiveSmallIntegerField()
    magicburstmessage = models.SmallIntegerField(db_column='magicBurstMessage')  # Field name made lowercase.
    animation = models.PositiveSmallIntegerField()
    animationtime = models.PositiveSmallIntegerField(db_column='animationTime')  # Field name made lowercase.
    aoe = models.PositiveIntegerField(db_column='AOE')  # Field name made lowercase.
    base = models.PositiveSmallIntegerField()
    multiplier = models.FloatField()
    ce = models.PositiveIntegerField(db_column='CE')  # Field name made lowercase.
    ve = models.PositiveIntegerField(db_column='VE')  # Field name made lowercase.
    requirements = models.IntegerField()
    spell_range = models.PositiveSmallIntegerField()
    content_tag = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spell_list'


class StatusEffects(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    flags = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField()
    negative_id = models.PositiveSmallIntegerField(blank=True, null=True)
    overwrite = models.PositiveSmallIntegerField()
    block_id = models.PositiveSmallIntegerField(blank=True, null=True)
    remove_id = models.PositiveSmallIntegerField()
    element = models.PositiveSmallIntegerField()
    min_duration = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'status_effects'


class SynthRecipes(models.Model):
    id = models.PositiveSmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.PositiveIntegerField(db_column='Type')  # Field name made lowercase.
    keyitem = models.PositiveIntegerField(db_column='KeyItem')  # Field name made lowercase.
    alchemy = models.PositiveIntegerField(db_column='Alchemy')  # Field name made lowercase.
    bone = models.PositiveIntegerField(db_column='Bone')  # Field name made lowercase.
    cloth = models.PositiveIntegerField(db_column='Cloth')  # Field name made lowercase.
    cook = models.PositiveIntegerField(db_column='Cook')  # Field name made lowercase.
    gold = models.PositiveIntegerField(db_column='Gold')  # Field name made lowercase.
    leather = models.PositiveIntegerField(db_column='Leather')  # Field name made lowercase.
    smith = models.PositiveIntegerField(db_column='Smith')  # Field name made lowercase.
    wood = models.PositiveIntegerField(db_column='Wood')  # Field name made lowercase.
    crystal = models.PositiveSmallIntegerField(db_column='Crystal')  # Field name made lowercase.
    hqcrystal = models.PositiveSmallIntegerField(db_column='HQCrystal')  # Field name made lowercase.
    ingredient1 = models.PositiveSmallIntegerField(db_column='Ingredient1')  # Field name made lowercase.
    ingredient2 = models.PositiveSmallIntegerField(db_column='Ingredient2')  # Field name made lowercase.
    ingredient3 = models.PositiveSmallIntegerField(db_column='Ingredient3')  # Field name made lowercase.
    ingredient4 = models.PositiveSmallIntegerField(db_column='Ingredient4')  # Field name made lowercase.
    ingredient5 = models.PositiveSmallIntegerField(db_column='Ingredient5')  # Field name made lowercase.
    ingredient6 = models.PositiveSmallIntegerField(db_column='Ingredient6')  # Field name made lowercase.
    ingredient7 = models.PositiveSmallIntegerField(db_column='Ingredient7')  # Field name made lowercase.
    ingredient8 = models.PositiveSmallIntegerField(db_column='Ingredient8')  # Field name made lowercase.
    result = models.PositiveSmallIntegerField(db_column='Result')  # Field name made lowercase.
    resulthq1 = models.PositiveSmallIntegerField(db_column='ResultHQ1')  # Field name made lowercase.
    resulthq2 = models.PositiveSmallIntegerField(db_column='ResultHQ2')  # Field name made lowercase.
    resulthq3 = models.PositiveSmallIntegerField(db_column='ResultHQ3')  # Field name made lowercase.
    resultqty = models.PositiveIntegerField(db_column='ResultQty')  # Field name made lowercase.
    resulthq1qty = models.PositiveIntegerField(db_column='ResultHQ1Qty')  # Field name made lowercase.
    resulthq2qty = models.PositiveIntegerField(db_column='ResultHQ2Qty')  # Field name made lowercase.
    resulthq3qty = models.PositiveIntegerField(db_column='ResultHQ3Qty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'synth_recipes'


class Traits(models.Model):
    traitid = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    job = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    modifier = models.PositiveSmallIntegerField()
    value = models.SmallIntegerField()
    content_tag = models.CharField(max_length=7, blank=True, null=True)
    meritid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'traits'
        unique_together = (('traitid', 'job', 'level', 'rank', 'modifier'),)


class Transport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    transport = models.PositiveIntegerField()
    door = models.PositiveIntegerField()
    dock_x = models.FloatField()
    dock_y = models.FloatField()
    dock_z = models.FloatField()
    dock_rot = models.PositiveIntegerField()
    boundary = models.PositiveSmallIntegerField()
    anim_arrive = models.PositiveIntegerField()
    anim_depart = models.PositiveIntegerField()
    time_offset = models.PositiveSmallIntegerField()
    time_interval = models.PositiveSmallIntegerField()
    time_anim_arrive = models.PositiveIntegerField()
    time_waiting = models.PositiveSmallIntegerField()
    time_anim_depart = models.PositiveIntegerField()
    zone = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'transport'


class WaterPoints(models.Model):
    waterid = models.AutoField(primary_key=True)
    zoneid = models.PositiveSmallIntegerField()
    type = models.PositiveIntegerField()
    pointid = models.PositiveIntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()

    class Meta:
        managed = False
        db_table = 'water_points'


class WeaponSkills(models.Model):
    weaponskillid = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    jobs = models.CharField(max_length=22)
    type = models.PositiveIntegerField()
    skilllevel = models.PositiveSmallIntegerField()
    element = models.PositiveIntegerField()
    animation = models.PositiveIntegerField()
    animationtime = models.PositiveSmallIntegerField(db_column='animationTime')  # Field name made lowercase.
    range = models.PositiveIntegerField()
    aoe = models.PositiveIntegerField()
    primary_sc = models.IntegerField()
    secondary_sc = models.IntegerField()
    tertiary_sc = models.IntegerField()
    main_only = models.IntegerField()
    unlock_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon_skills'


class ZoneSettings(models.Model):
    zoneid = models.PositiveSmallIntegerField(primary_key=True)
    zonetype = models.PositiveSmallIntegerField()
    zoneip = models.TextField()
    zoneport = models.PositiveSmallIntegerField()
    name = models.TextField()
    music_day = models.PositiveIntegerField()
    music_night = models.PositiveIntegerField()
    battlesolo = models.PositiveIntegerField()
    battlemulti = models.PositiveIntegerField()
    restriction = models.PositiveIntegerField()
    tax = models.FloatField()
    misc = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'zone_settings'


class ZoneWeather(models.Model):
    zoneid = models.PositiveSmallIntegerField(primary_key=True)
    weather_day = models.PositiveSmallIntegerField()
    common = models.PositiveIntegerField()
    normal = models.PositiveIntegerField()
    rare = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'zone_weather'
        unique_together = (('zoneid', 'weather_day'),)


class Zonelines(models.Model):
    zoneline = models.PositiveIntegerField(primary_key=True)
    fromzone = models.PositiveSmallIntegerField()
    tozone = models.PositiveSmallIntegerField()
    tox = models.FloatField()
    toy = models.FloatField()
    toz = models.FloatField()
    rotation = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'zonelines'
