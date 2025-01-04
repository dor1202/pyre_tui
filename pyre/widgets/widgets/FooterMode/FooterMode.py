from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.reactive import reactive


class FooterMode(Widget):
    DEFAULT_CSS = """
    FooterMode {
        align: right middle;
    }
    
    .modeValue {
        background: green;
        margin: 0 1;
    }
    """

    mode = reactive("match", recompose=True)

    def compose(self) -> ComposeResult:
        yield Label(self.mode, classes="modeValue")