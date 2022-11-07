""" Helper used by hahm-mqtt. """
from __future__ import annotations

from typing import TypeVar, Union

from hahomematic.entity import CustomEntity, GenericEntity, GenericHubEntity
from hahomematic.hub import HmHub


# Union for entity types used as base class for entities
HmBaseEntity = Union[CustomEntity, GenericEntity]
# Union for entity types used as base class for sysvar entities
HmBaseHubEntity = Union[HmHub, GenericHubEntity]
# Entities that support callbacks from backend
HmCallbackEntity = (CustomEntity, GenericEntity)
# Generic base type used for entities in Homematic(IP) Local
HmGenericEntity = TypeVar("HmGenericEntity", bound=HmBaseEntity)
# Generic base type used for sysvar entities in Homematic(IP) Local
HmGenericSysvarEntity = TypeVar("HmGenericSysvarEntity", bound=HmBaseHubEntity)