from pprint import pprint
from panos.panorama import Panorama, DeviceGroup
from panos.policies import PostRulebase
from panos import policies

profiles_group = "STRICT"
# Create a config tree for the rule
panorama = Panorama("192.168.1.xx", "admin", "xxxxx")

# build a configuration  tree

# under panorama, we have the device group object  in the tree

DG = DeviceGroup("NGFW-HOME-CLUSTER")
panorama.add(DG)

# under device group we have Post Rules and Pre Rules

post_rule_base = PostRulebase()
DG.add(post_rule_base)

rules = policies.SecurityRule.refreshall(post_rule_base)
for rule in rules:
    rule.group = profiles_group
    rule.apply()

print("Starting commit")
panorama.commit(sync=True, exception=True)
print("Commit finished successfully")
