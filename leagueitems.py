'''
This program takes a file in its directory named 'item.json' and
converts its data into a CSV file, which is named 'itemdbase.csv' and
then written into the same folder.
'''

import dataclasses
from dataclasses import dataclass, asdict
import json
import pandas as pd
import csv

ID: str
Name: str
Stacks: int
Consumed: bool
CombineCost: int
TotalCost: int
Sell: int
Rift: bool
Abyss: bool

@dataclass
class Stat:
    MaxHP: int
    HPPerLv: int
    MaxMP: int
    MPPerLv: int
    PcHP: float
    PcMP: float
    HPRegen: int
    HPRegenPerLv: int
    PcHPRegen: float
    MPRegen: int
    MPRegenPerLv: int
    PcMPRegen: float
    Armor: int
    ArmorPerLv: int
    PcArmor: float
    ArmorPen: int
    ArmorPenPerLv: int
    PcArmorPen: float
    PcArmorPenPerLv: float
    AtkDmg: int
    AtkDmgPLv: int
    PcAtkDmg: float
    AbilityPw: int
    AbilityPwPLv: int
    PcAbilityPow: float
    MoveSpd: int
    MoveSpdPerLv: int
    PcMveSpd: float
    PcMveSpdPerLv: float
    AttackSpd: int
    PcAtkSpd: float
    PcAtkSpdPerLv: float
    Dodge: int
    DodgePerLv: int
    PcDodge: float
    CritChance: int
    CritChancePerLv: int
    PcCritChance: float
    CritDamage: int
    CritDamagePerLv: int
    PcCritDamage: float
    Block: int
    PcBlock: float
    MagicRes: int
    MagicResPerLv: int
    PcMagicRes: float
    EXPBonus: int
    PcEXPBonus: float
    PcCooldown: float
    PcCooldownPerLv: float
    TimeDead: int
    TimeDeadPerLv: int
    PcTimeDead: float
    PcTimeDeadPerLv: float
    GoldPer10: int
    MagicPen: int
    MagicPenPerLv: int
    PcMagicPen: float
    PcMagicPenPerLv: float
    EnergyRegen: int
    EnergyRegenPerLv: int
    EnergyPool: int
    EnergyPerLv: int
    PcLifeSteal: float
    PcSpellVamp: float

header = ['ID #','Item Name','Max #','Consumable',
          'Combine','Total','Sell','Rift','Abyss']
for stat in dataclasses.fields(Stat):
        header.append(stat.name)

with open('itemdbase.csv', 'w',newline='') as f:
    output = csv.writer(f)
    output.writerow(header)
    with open('item.json', 'r') as jfile:
        jsondata = json.load(jfile)
        for i in jsondata['data'].items():
            ID = i[0]
            item = jsondata['data'][ID]
            Name = item.get('name','')
            Stacks = item.get('stacks',1)
            Consumed = item.get('consumed',False)
            CombineCost = item['gold'].get('base',0)
            TotalCost = item['gold'].get('total',0)
            Sell = item['gold'].get('sell',0)
            Rift = item['maps'].get('11',True)
            Abyss = item['maps'].get('12',True)
            statblock = item.get('stats','')
            stat = Stat(statblock.get('FlatHPPoolMod',None),
                          statblock.get('rFlatHPModPerLevel',None),
                          statblock.get('FlatMPPoolMod',None),
                          statblock.get('rFlatMPModPerLevel',None),
                          statblock.get('PercentHPPoolMod',None),
                          statblock.get('PercentMPPoolMod',None),
                          statblock.get('FlatHPRegenMod',None),
                          statblock.get('rFlatHPRegenModPerLevel',None),
                          statblock.get('PercentHPRegenMod',None),
                          statblock.get('FlatMPRegenMod',None),
                          statblock.get('rFlatMPRegenModPerLevel',None),
                          statblock.get('PercentMPRegenMod',None),
                          statblock.get('FlatArmorMod',None),
                          statblock.get('rFlatArmorModPerLevel',None),
                          statblock.get('PercentArmorMod',None),
                          statblock.get('rFlatArmorPenetrationMod',None),
                          statblock.get('rFlatArmorPenetrationModPerLevel',None),
                          statblock.get('rPercentArmorPenetrationMod',None),
                          statblock.get('rPercentArmorPenetrationModPerLevel',None),
                          statblock.get('FlatPhysicalDamageMod',None),
                          statblock.get('rFlatPhysicalDamageModPerLevel',None),
                          statblock.get('PercentPhysicalDamageMod',None),
                          statblock.get('FlatMagicDamageMod',None),
                          statblock.get('rFlatMagicDamageModPerLevel',None),
                          statblock.get('PercentMagicDamageMod',None),
                          statblock.get('FlatMovementSpeedMod',None),
                          statblock.get('rFlatMovementSpeedModPerLevel',None),
                          statblock.get('PercentMovementSpeedMod',None),
                          statblock.get('rPercentMovementSpeedModPerLevel',None),
                          statblock.get('FlatAttackSpeedMod',None),
                          statblock.get('PercentAttackSpeedMod',None),
                          statblock.get('rPercentAttackSpeedModPerLevel',None),
                          statblock.get('rFlatDodgeMod',None),
                          statblock.get('rFlatDodgeModPerLevel',None),
                          statblock.get('PercentDodgeMod',None),
                          statblock.get('FlatCritChanceMod',None),
                          statblock.get('rFlatCritChanceModPerLevel',None),
                          statblock.get('PercentCritChanceMod',None),
                          statblock.get('FlatCritDamageMod',None),
                          statblock.get('rFlatCritDamageModPerLevel',None),
                          statblock.get('PercentCritDamageMod',None),
                          statblock.get('FlatBlockMod',None),
                          statblock.get('PercentBlockMod',None),
                          statblock.get('FlatSpellBlockMod',None),
                          statblock.get('rFlatSpellBlockModPerLevel',None),
                          statblock.get('PercentSpellBlockMod',None),
                          statblock.get('FlatEXPBonus',None),
                          statblock.get('PercentEXPBonus',None),
                          statblock.get('rPercentCooldownMod',None),
                          statblock.get('rPercentCooldownModPerLevel',None),
                          statblock.get('rFlatTimeDeadMod',None),
                          statblock.get('rFlatTimeDeadModPerLevel',None),
                          statblock.get('rPercentTimeDeadMod',None),
                          statblock.get('rPercentTimeDeadModPerLevel',None),
                          statblock.get('rFlatGoldPer10Mod',None),
                          statblock.get('rFlatMagicPenetrationMod',None),
                          statblock.get('rFlatMagicPenetrationModPerLevel',None),
                          statblock.get('rPercentMagicPenetrationMod',None),
                          statblock.get('rPercentMagicPenetrationModPerLevel',None),
                          statblock.get('FlatEnergyRegenMod',None),
                          statblock.get('rFlatEnergyRegenModPerLevel',None),
                          statblock.get('FlatEnergyPoolMod',None),
                          statblock.get('rFlatEnergyModPerLevel',None),
                          statblock.get('PercentLifeStealMod',None),
                          statblock.get('PercentSpellVampMod',None))
            info = [ID,Name,Stacks,Consumed,CombineCost,
                    TotalCost,Sell,Rift,Abyss]
            for i in vars(stat):
                info.append(asdict(stat)[i])
            output.writerow(info)

ifile = r'itemdbase.csv'
itemstats = pd.read_csv(ifile,index_col = 0)
itemstats = itemstats.dropna(axis=1,how='all')
itemstats.loc[:,itemstats.columns.str.contains('Regen')] *= 5
itemstats.loc[:,itemstats.columns.str.startswith('Pc')] *= 100
itemstats.loc[:,itemstats.columns.str.contains('Chance')] *= 100
itemstats.to_csv('itemdbase.csv')
