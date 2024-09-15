
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role


class SimplePMWrite(Action):
    PROMPT_TEMPLATE: str = """
    You are a product manager. Generate a high-level product description for a new product.
    Propose a product name, a brief description, and a few key features.
    Product must solve a specific problem, have a clear target audience, and be user-centric.
    The problem: {instruction}
    """
    name: str = "SimplePM"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)

        rsp = await self._aask(prompt)

        return rsp


class SimplePM(Role):
    name: str = "Alice"
    profile: str = "SimplePM"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([UserRequirement])
        self.set_actions([SimplePMWrite])
