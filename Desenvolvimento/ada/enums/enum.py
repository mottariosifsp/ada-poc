from enum import Enum
# gource
class Period(Enum):
    morning = 'MORNING'
    afternoon = 'AFTERNOON'
    night = 'NIGHT'

class Day(Enum):
    monday = 'MONDAY'
    tuesday = 'TUESDAY'
    wednesday = 'WEDNESDAY'
    thursday = 'THURSDAY'
    friday = 'FRIDAY'
    saturday = 'SATURDAY'

class Priority(Enum):
    primary = 'PRIMARY'
    secondary = 'SECONDARY'

class Job(Enum):
    TWENTY_HOURS = 'TWENTY_HOURS'
    FORTY_HOURS = 'FORTY_HOURS'
    RDE = 'RDE'
    TEMPORARY = 'TEMPORARY'
    SUBSTITUTE = 'SUBSTITUTE'
