"""Functionality that should be available from all engines."""

import pytest
import asyncio
from ltldoorstep.engines import engines

@pytest.mark.parametrize('engine', engines.values())
def test_can_instantiate(engine):
    """Check whether engine can be created with a run method."""

    eng = engine()

    assert asyncio.iscoroutinefunction(eng.run)
