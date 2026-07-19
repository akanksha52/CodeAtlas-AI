from pathlib import Path

from app.core.dependencies import index_manager
from app.llm.ollama_client import OllamaClient


class ExplainService:

    def __init__(self):
        self.client = OllamaClient()

    def explain(self, path: str):

        if not index_manager.ready():
            raise RuntimeError(
                "Repository not indexed."
            )

        root = Path(index_manager.repository_path)

        file_path = root / path

        if not file_path.exists():
            raise FileNotFoundError(path)

        code = file_path.read_text(
            encoding="utf-8"
        )

        prompt = f"""
        You are an expert Software Architect.

        Analyze the following source code and explain it in a structured way.

        Return the explanation using these headings:

        ## Overview
        Briefly describe what this file is responsible for.

        ## Classes
        List every class and explain its responsibility.

        ## Functions
        List every function and explain what it does.

        ## Flow
        Explain how execution flows through the file.

        ## Dependencies
        Mention any important imports or external services used.

        ## Improvements
        Suggest improvements if appropriate.

        Here is the file:

        Path:
        {path}

        Code:
        {code}
        """

        return self.client.generate(prompt)