# managers/ownership_manager.py

from ownership.business import Business
from ownership.staff import Staff

from simulation.event_definitions import Events


class OwnershipManager:

    def __init__(self):

        self.businesses = {}

        self.propagation = None

    # =====================================
    # CREATE BUSINESS
    # =====================================

    def create_business(
        self,
        owner_name,
        business_name
    ):

        business = Business(
            business_name
        )

        self.businesses[
            business_name
        ] = business

        # Notify world systems

        if self.propagation:

            self.propagation.propagate(
                Events.BUSINESS_CREATED,
                source="OwnershipManager",
                data={
                    "owner": owner_name,
                    "business": business_name
                }
            )

        return business

    # =====================================
    # HIRE STAFF
    # =====================================

    def hire_staff(
        self,
        business_name,
        staff_name,
        role
    ):

        business = self.businesses.get(
            business_name
        )

        if not business:

            return None

        staff = Staff(
            staff_name,
            role
        )

        business.staff.append(
            staff
        )

        return staff

    # =====================================
    # BUSINESS TICK
    # =====================================

    def process_business_turn(self):

        for business in self.businesses.values():

            if hasattr(
                business,
                "update"
            ):

                business.update()

        print(
            "Businesses Updated"
        )