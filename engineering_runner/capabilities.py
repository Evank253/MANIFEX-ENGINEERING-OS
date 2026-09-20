from dataclasses import dataclass
from .models import CapabilityPolicy
@dataclass(frozen=True)
class CapabilityGrant:
    filesystem_read:tuple[str,...]; filesystem_write:tuple[str,...]; network_allowed:tuple[str,...]
    credentials:tuple[str,...]; tools:tuple[str,...]; enforcement_level:str="policy-only"
class CapabilityBroker:
    def grant(self,policy):
        return CapabilityGrant(tuple(policy.filesystem.read),tuple(policy.filesystem.write),tuple(policy.network.allowed),tuple(policy.credentials),tuple(policy.tools))
