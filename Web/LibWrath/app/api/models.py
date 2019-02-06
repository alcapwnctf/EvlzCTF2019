from django.db import models

from django.contrib.auth.models import User, Group

from api.helpers import DefaultUUID
class Device(models.Model):
    """
        Extended User Model with to hold information for Agent Nodes
        :param user: User info (username, email, password, etc)
        :param uuid: Compliant UUID supplied by the agent, Generate UUID on the agent based on system parameters to prevent duplicate instances
        :param topics_pub: List of topics the node is publishing to
        :param topic_sub: List of topics the node is subscribed to
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    uuid = models.CharField(max_length=54, unique=True, blank=True, default=DefaultUUID)
    status = models.CharField(max_length=50, default='offline')
    last_tick = models.DateTimeField(null=True)