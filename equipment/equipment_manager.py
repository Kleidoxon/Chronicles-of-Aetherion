# equipment/equipment_manager.py

from equipment.equipment_slot import EquipmentSlot


class EquipmentManager:

    def __init__(self):

        self.equipment = {

            EquipmentSlot.WEAPON: None,

            EquipmentSlot.HELMET: None,

            EquipmentSlot.CHEST: None,

            EquipmentSlot.GLOVES: None,

            EquipmentSlot.BOOTS: None,

            EquipmentSlot.RING: None,

            EquipmentSlot.RING2: None,

            EquipmentSlot.RING3: None,

            EquipmentSlot.RING4: None,

            EquipmentSlot.RING5: None,

            EquipmentSlot.AMULET: None,

            EquipmentSlot.BELT: None
        }

    def equip(self, item):

        self.equipment[item.slot] = item

        print(
            f"Equipped: {item.name}"
        )

    def unequip(self, slot):

        item = self.equipment[slot]

        self.equipment[slot] = None

        return item

    def get_equipped(self, slot):

        return self.equipment.get(slot)

    def get_total_attack_bonus(self):

        total = 0

        for item in self.equipment.values():

            if (
                item and
                hasattr(item, "attack_bonus")
            ):

                total += item.attack_bonus

        return total

    def get_total_defense_bonus(self):

        total = 0

        for item in self.equipment.values():

            if (
                item and
                hasattr(item, "defense_bonus")
            ):

                total += item.defense_bonus

        return total

    def show_equipment(self):

        print("\n=== EQUIPMENT ===")

        for slot, item in self.equipment.items():

            if item:

                print(
                    f"{slot.value}: {item.name}"
                )

            else:

                print(
                    f"{slot.value}: Empty"
                )