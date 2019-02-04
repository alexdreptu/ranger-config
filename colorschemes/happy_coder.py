from ranger.gui.colorscheme import ColorScheme
from ranger.gui import color


class HappyCoder(ColorScheme):
    progress_bar_color = 111

    def use(self, context):
        fg, bg, attr = color.default_colors

        if context.reset:
            return color.default_colors

        if context.in_browser:
            if context.selected:
                fg = color.white
                bg = 97

            if context.directory and not context.selected:
                fg = 111

            if context.border:
                fg = color.magenta

            if context.media and not context.selected:
                if context.image:
                    fg = color.red
                else:
                    fg = color.yellow

            if context.executable and not context.selected and not any((
                    context.media,
                    context.container,
                    context.fifo,
                    context.socket,
                    context.directory,
            )):
                fg = 108

        return fg, bg, attr
