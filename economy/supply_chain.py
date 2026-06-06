class SupplyChain:
    def __init__(self):
        self.materials = {}

    def transport_goods(self, item, quantity):
        print(f"Transporting {quantity} {item}")

    def add_material(self, material, quantity):
        self.materials[material] = quantity
    