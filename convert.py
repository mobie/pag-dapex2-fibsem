from mobie.migration.migrate_v2 import migrate_project
from mobie.validation import validate_project

# this could also be done via CLI!
migrate_project("./data")
validate_project("./data")
