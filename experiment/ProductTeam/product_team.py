import re

import fire

from metagpt.logs import logger
from metagpt.team import Team

from persons.product_manager import SimplePM
from persons.technical_lead import  SimpleTL



async def main(
    idea: str = "Напиши модуль для поддержки работы контакт-центра",
    investment: float = 3.0,
    n_round: int = 5,
    add_human: bool = False,
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            SimplePM(),
            SimpleTL()
        ]
    )
    team.run_project(idea)
    await team.run(n_round=n_round)


if __name__ == "__main__":
    fire.Fire(main)