from core.command import BaseCommand
from abc import ABC, abstractmethod


class Assistant:
    def __init__(self):
        self.commands: dict[str, type[BaseCommand]] = {}
        self.history: list[str] = []
