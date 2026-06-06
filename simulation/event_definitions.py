# simulation/event_definitions.py

class Events:

    # ==================================
    # ECONOMY
    # ==================================

    BUSINESS_CREATED = "business_created"

    BUSINESS_BANKRUPT = "business_bankrupt"

    TAX_COLLECTED = "tax_collected"

    MARKET_PRICE_CHANGED = "market_price_changed"

    RESOURCE_SHORTAGE = "resource_shortage"

    RESOURCE_SURPLUS = "resource_surplus"

    # ==================================
    # WAR
    # ==================================

    WAR_DECLARED = "war_declared"

    WAR_ENDED = "war_ended"

    CITY_CONQUERED = "city_conquered"

    # ==================================
    # GOVERNANCE
    # ==================================

    GOVERNOR_ASSIGNED = "governor_assigned"

    CORRUPTION_INCREASED = "corruption_increased"

    CITY_UPGRADED = "city_upgraded"

    # ==================================
    # ENVIRONMENT
    # ==================================

    MINE_CREATED = "mine_created"

    FOREST_DESTROYED = "forest_destroyed"

    ENVIRONMENT_RESTORED = "environment_restored"

    # ==================================
    # POPULATION
    # ==================================

    POPULATION_GROWTH = "population_growth"

    POPULATION_DECLINE = "population_decline"

    MIGRATION_STARTED = "migration_started"

    # ==================================
    # AI
    # ==================================

    AI_DECISION = "ai_decision"

    AI_WAR_TRIGGER = "ai_war_trigger"

    AI_BUSINESS_EXPANSION = "ai_business_expansion"

    # ==================================
    # DIMENSION
    # ==================================

    DIMENSION_OPENED = "dimension_opened"

    REALITY_CHANGED = "reality_changed"

    # ==================================
    # UNIVERSE
    # ==================================

    COSMIC_EVENT = "cosmic_event"

    CONVERGENCE_EVENT = "convergence_event"