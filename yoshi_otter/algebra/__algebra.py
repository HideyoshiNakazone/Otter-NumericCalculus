# Otter - Program made for educational intent, can be freely distributed
# and can be used for economical intent. I will not take legal actions
# unless my intelectual propperty, the code, is stolen or change without permission.
#
# Copyright (C) 2020  VItor Hideyoshi Nakazone Batista
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from yoshi_otter.algebra.integral.double import Double
from yoshi_otter.algebra.integral.simple import Simple
from yoshi_otter.algebra.roots import Roots
from yoshi_otter.algebra.edo import Edo

from typing import Callable, Union
from inspect import signature

from yoshi_otter.shared import InvalidFunctionSignature


class Algebra:

    def __init__(self, function: Callable[[float], float] | Callable[[float, float], float]) -> None:
        self.f = function

        self.integral = self.__Integral(self.f)
        self.roots = Roots(self.f)
        self.edo = Edo(self.f)

    def d(self, x: float, e: float = 10 ** -4) -> float:
        if len(signature(self.f).parameters) == 1:
            return (self.f(x + e) - self.f(x - e)) / (2 * e)
        else:
            raise InvalidFunctionSignature("This method is only valid for one dimensional functions.")

    class __Integral:

        def __init__(self, function: Union[Callable[[float], float], Callable[[float, float], float]]) -> None:
            self.f = function

            self.simple = Simple(self.f)
            self.double = Double(self.f)
