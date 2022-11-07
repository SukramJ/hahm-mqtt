""" Config used by hahm-mqtt. """
from __future__ import annotations

from hahomematic.entity import GenericEntity, CustomEntity


@property
def generticEntityTopic(self: GenericEntity):
    """Return the entity topic."""
    return f"hahm/{self.device.device_address}/{self.channel_no}/{self.parameter}"


GenericEntity.topic = generticEntityTopic

