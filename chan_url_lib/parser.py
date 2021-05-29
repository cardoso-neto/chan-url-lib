from __future__ import annotations

import re
from pathlib import Path


class ChanURI:
    thread_url_regex = r"https?://boards.(4channel|4chan).org/(?P<board>[\w-]+)/thread/(?P<thread>[0-9]+)"
    def __init__(self, chan: str, board: str, thread_id: int) -> None:
        self.chan = chan
        self.board = board
        self.thread_id = thread_id

    @classmethod
    def from_path(cls, path: Path) -> ChanURI:
        return cls(str(path.parent.parent), str(path.parent), int(path.name))

    @classmethod
    def from_url(cls, url: str) -> ChanURI:
        match_ = re.match(cls.thread_url_regex, url)
        chan = "4chan"
        board = match_.group("board")
        thread_id = match_.group("thread")
        return cls(chan, board, int(thread_id))

    def __repr__(self) -> str:
        r = (
            "ChanURI("
            f"chan={self.chan!r}, board={self.board!r}, thread_id={self.thread_id!r})"
        )
        return r

    def __str__(self) -> str:
        return f"{self.chan}/{self.board}/{self.thread_id}"
