from __future__ import annotations
from dataclasses import dataclass
from io import TextIOWrapper
import re


@dataclass
class Config:
    width: int
    height: int
    x: int
    y: int

    def __iter__(self):
        yield self.width
        yield self.height
        yield self.x
        yield self.y

    @staticmethod
    def parse(file: TextIOWrapper) -> Config:
        lines = "".join(file.readlines())
        get_arg = (
            lambda arg: re.search(f"{arg}(\s)*=(\s)*(\d+)", lines)
            .group()
            .replace(" ", "")
            .replace(f"{arg}=", "")
        )

        try:
            return Config(
                width=int(get_arg("N")),
                height=int(get_arg("M")),
                x=int(get_arg("X")),
                y=int(get_arg("Y")),
            )
        except ValueError:
            raise ValueError(
                "Invalid input format. Expected numbers for M, N, X, and Y."
            )
