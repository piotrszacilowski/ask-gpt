import traceback
from typing import Optional

import openai

from loguru import logger as LOG

from credentials import OPENAI_API_KEY


class GPT:
    def __init__(self):
        self.openai = openai
        openai.api_key = OPENAI_API_KEY

    def ask_gpt(self, prompt: Optional[str] = None) -> str:
        LOG.info(f"Prompt: {prompt}")
        result: str = ""
        if not prompt:
            prompt: str = "Why should DevOps engineer learn kubernetes?"
        try:
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            for choice in response.choices:
                result += choice.message.content
        except Exception:
            LOG.exception("Error occurred while requesting the ChatGPT API.")
            LOG.exception(f"Traceback: {traceback.format_exc()}")

        return result
