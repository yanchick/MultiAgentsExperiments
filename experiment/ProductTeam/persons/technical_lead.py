from metagpt.actions import Action
from metagpt.logs import logger
from metagpt.roles import Role

class SimpleTLWriter(Action):
    PROMPT_TEMPLATE: str = """
    Context: {context}
    You are a technical lead. Write a technical specification for the product. Split process, scope, and requirements into sections. Write tasks for development.
    """

    name: str = "SimpleTLWriter"

    async def run(self, context: str, k: int = 1):
        prompt = self.PROMPT_TEMPLATE.format(context=context, k=k)

        rsp = await self._aask(prompt)

        code_text = parse_code(rsp)

        return code_text


class SimpleTL(Role):
    name: str = "Bob"
    profile: str = "SimpleTL"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleTLWriter])
        # self._watch([SimpleWriteCode])
        self._watch([SimplePMWrite])  # feel free to try this too

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo

        # context = self.get_memories(k=1)[0].content # use the most recent memory as context
        context = self.get_memories()  # use all memories as context

        code_text = await todo.run(context, k=5)  # specify arguments
        msg = Message(content=code_text, role=self.profile, cause_by=type(todo))

        return msg

