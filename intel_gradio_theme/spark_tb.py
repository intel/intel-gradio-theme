from __future__ import annotations
import gradio as gr
from collections.abc import Iterable
from gradio.themes.base import Base
from gradio.themes.utils import fonts, sizes
import datetime
import os

class Color:
    all = []

    def __init__(
        self,
        c50: str,
        c100: str,
        c200: str,
        c300: str,
        c400: str,
        c500: str,
        c600: str,
        c700: str,
        c800: str,
        c900: str,
        c950: str = None,
        name: str | None = None,
    ):
        self.c50 = c50
        self.c100 = c100
        self.c200 = c200
        self.c300 = c300
        self.c400 = c400
        self.c500 = c500
        self.c600 = c600
        self.c700 = c700
        self.c800 = c800
        self.c900 = c900
        self.c950 = c950
        self.name = name
        Color.all.append(self)

    def expand(self) -> list[str]:
        return [
            self.c50, self.c100, self.c200, self.c300, self.c400,
            self.c500, self.c600, self.c700, self.c800, self.c900, self.c950
        ]

neutral = Color(
    name="neutral",
    c50="#ffffff",
    c100="#f7f7f8",
    c200="#f1f1f3",
    c300="#e7e7eb",
    c400="#dcdce3",
    c500="#bec0cb",
    c600="#acaebc",
    c700="#82879b",
    c800="#676d84",
    c900="#383e56",
    c950="#1c223b",
)


darkNeutral = Color(
    name="dark-neutral",
    c50="#020316",
    c100="#070c21",
    c200="#0d132b",
    c300="#1c223b",
    c400="#383e56",
    c500="#555b72",
    c600="#676d84",
    c700="#82879b",
    c800="#acaebc",
    c900="#e7e7eb",
    c950="#fff",
)

aqua = Color(
    name="aqua",
    c50="#D1FBF4",
    c100="#a2f6e8",
    c200="#5be3cd",
    c300="#16cfb1",
    c400="#0f9b8f",
    c500="#09857c",
    c600="#08746e",
    c700="#065955",
    c800="#044845",
    c900="#022b2a",
    c950="#022b2a"
)

cosmos = Color(
    name="cosmos",
    c50="#e1d9ff",
    c100="#c9bbff",
    c200="#af98ff",
    c300="#9974ff",
    c400="#8b50ff",
    c500="#7000ff",
    c600="#5400c0",
    c700="#4600a0",
    c800="#38007f",
    c900="#1f0047",
    c950="#1f0047"
)

class SparkThemeTb(Base):
    def __init__(
        self,
        *,
        primary_hue: Color | str = aqua,
        secondary_hue: Color | str = cosmos,
        neutral_hue: Color | str = neutral,
        spacing_size: sizes.Size | str = sizes.spacing_lg,
        radius_size: sizes.Size | str = sizes.radius_none,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.LocalFont("IntelOne Text"),
            fonts.GoogleFont("Poppins"),
            "ui-sans-serif",
            "system-ui",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.LocalFont("IntelOne Mono"),
            fonts.GoogleFont("Source Code Pro"),
            "ui-monospace",
            "Consolas",
            "monospace",
        ),
        # add core color for color_accent_dark
        color_accent_dark: str = "*primary_200",
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        # add core color for color_accent_dark
        self.color_accent_dark = color_accent_dark

        self.name = "spark-island"
        
        super().set(
            # slider_color="*neutral_900",
            slider_color_dark="*primary_200",
            # accordion_text_color="*body_text_color",
            # accordion_text_color_dark="*body_text_color",
            # table_text_color="*body_text_color",
            # table_text_color_dark="*body_text_color",
            body_text_color="*neutral_950", #updated
            block_label_text_color="*body_text_color",
            block_title_text_color="*body_text_color",
            body_text_color_subdued="*neutral_800", #updated
            # background_fill_primary_dark="*neutral_900",
            # background_fill_secondary_dark="*neutral_800",
            # block_background_fill_dark="*neutral_800",
            # input_background_fill_dark="*neutral_700",
            button_border_width="2px",
            # button_primary_border_color="*neutral_900",
            button_primary_background_fill="*primary_500",
            button_primary_background_fill_hover="*primary_700",
            # button_primary_text_color="white",
            button_primary_background_fill_dark="*primary_400",
            button_primary_border_color_dark="*primary_400",
            button_primary_background_fill_hover_dark="*primary_600",
            button_primary_text_color_dark="*neutral_50",

            #button secondary
            
            button_secondary_text_color="*primary_500",
            button_secondary_text_color_hover="*primary_700",
            button_secondary_border_color="*primary_500",
            button_secondary_background_fill="*neutral_50",
            button_secondary_background_fill_hover="*neutral_100",
            button_secondary_border_color_hover="*primary_700",

            button_secondary_text_color_dark="*primary_300",
            button_secondary_text_color_hover_dark="*primary_200",button_secondary_border_color_dark="*primary_300",
            button_secondary_background_fill_dark="*neutral_950",
            button_secondary_background_fill_hover_dark="*neutral_900",
            button_secondary_border_color_hover_dark="*primary_300",

            

            # button_cancel_border_color="*neutral_900",
            # button_cancel_background_fill="*button_secondary_background_fill",
            button_cancel_background_fill_hover="*neutral_200",
            button_cancel_background_fill_hover_dark="*neutral_800",
            # button_cancel_text_color="*button_secondary_text_color",
            # checkbox_label_border_color="*checkbox_background_color",
            # checkbox_label_border_color_hover="*button_secondary_border_color_hover",
            # checkbox_label_border_color_selected="*button_primary_border_color",
            # checkbox_label_border_width="*button_border_width",
            # checkbox_background_color="*input_background_fill",
            # checkbox_label_background_fill_selected="*button_primary_background_fill",
            # checkbox_label_text_color_selected="*button_primary_text_color",
            # checkbox_label_padding="*spacing_sm",
            # button_large_padding="*spacing_lg",
            # button_small_padding="*spacing_sm",
            # shadow_drop_lg="0 1px 4px 0 rgb(0 0 0 / 0.1)",
            # block_shadow="none",
            # block_shadow_dark="*shadow_drop_lg",
            # block_title_text_weight="500",
            # block_label_text_weight="400",
            # block_label_text_size="*text_md",
            prose_header_text_weight = "200",
            button_large_text_weight = "500",
            button_medium_text_weight = "500",
            button_small_text_weight = "500",
            stat_background_fill_dark="*primary_400",
            )
    
    @staticmethod
    def header(title: str = "Demo App"):
        return gr.HTML(f"<header class=\"spark-header\"><img src=\"https://www.intel.com/content/dam/logos/intel-header-logo.svg\" class=\"spark-logo\"></img><div class=\"spark-title\">{title}</div></header>", padding=False)

    @staticmethod
    def footer(content: str = f"©{datetime.datetime.now().year} Intel Corporation. All rights reserved."):
        return gr.HTML(f"<footer class=\"spark-footer\"><div class=\"spark-footer-info\">{content}</div></footer>", padding=False)

    def load_css(self):
        current_dir = os.path.dirname(__file__)
        css_path = os.path.join(current_dir, "spark.css")
        with open(css_path, "r") as file:
            css = file.read()
        css = css.replace("[primary-500]", self.primary_500)
        return css
