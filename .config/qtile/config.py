from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [
    #~~~~~~~~~~~~~~~~~Changing Windows~~~~~~~~~~~~~~~~~
    Key([mod], "h", lazy.layout.left(),                     desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(),                    desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),                     desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),                       desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),                 desc="Move window focus to other window"),
    #~~~~~~~~~~~~~~~~~~Moving Windows~~~~~~~~~~~~~~~~~~
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),    desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),   desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),    desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),      desc="Move window up"),
    #~~~~~~~~~~~~~~~~~~Resize Windows~~~~~~~~~~~~~~~~~~
    Key([mod, "control"], "h", lazy.layout.grow_left(),     desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),    desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),     desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),       desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),                desc="Reset all window sizes"),
    #~~~~~~~~~~~~~~~~~~Technical Tasks~~~~~~~~~~~~~~~~~
    Key([mod], "r", lazy.spawncmd(),                        desc="Spawn a command using a prompt widget"),
    Key([mod], "w", lazy.window.kill(),                     desc="Kill focused window"),
    Key([mod], "Return", lazy.spawn(terminal),              desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(),                   desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.restart(),              desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),             desc="Shutdown Qtile"),
    #~~~~~~~~~~~~~~~General Applications~~~~~~~~~~~~~~~
    Key([mod, "shift"], "d", lazy.spawn('discord-ptb')),
    Key([mod, "shift"], "s", lazy.spawn('spotify')),
    Key([mod, "shift"], "f", lazy.spawn('firefox')),
    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    #Key([mod, "shift"], "Return", lazy.spawn('alacritty -e ranger')),
    Key([mod, "shift"], "p", lazy.spawn('alacritty -e htop')),
    Key([mod, "shift"], "g", lazy.spawn('steam-runtime')),
    Key([mod, "shift"], "v", lazy.spawn('lutris')),
    Key([mod, "shift"], "KP_End", lazy.spawn('element-desktop --profile=snowphie')),
    Key([mod, "shift"], "KP_Down", lazy.spawn('element-desktop --profile=snowphii')),
    Key([mod, "control"], "s", lazy.spawn('flameshot gui')),
]

groups = []
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "minus",]
group_labels = ["  ", "  ", "  ", "  ", "  ", "  ",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])
layouts = [
    layout.Columns(
        margin=0, 
        border_width=1,
        border_focus="#63659e",    
        border_normal="#41425d"
        ),
    layout.Max(
        margin=0,
        border_width=0,
        border_focus="#63659e",
        border_normal="#41425d"
        ),
    layout.MonadTall(
        margin=8, 
        border_width=2, 
        border_focus="#63659E", 
        border_normal="#41425d"
        ),
    layout.RatioTile(
        margin=8, 
        border_width=2, 
        border_focus="#63659E", 
        border_normal="#41425d"
        ),
]
# COLORS FOR THE BAR

def init_colors():
    return [["#63659E", "#41425d"] # 0 ~ Purples
            ]


colors = init_colors()

def init_widgets_defaults():
    return dict(font="helvetica",
                fontsize = 14,
                padding_x=8,
                padding_y=0,
                rounded=False,
                background='#090c10',
                border="#63659E",
                unfocused_border="#41425d"
                )

widget_defaults = init_widgets_defaults()
extension_defaults = widget_defaults.copy()

powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
    ]
}
screens = [
    #~~~~~~~~~~~~~~~~~~~Main Monitor~~~~~~~~~~~~~~~~~~~
    Screen(
        top=bar.Bar(
            [
            widget.GroupBox(),
            widget.Prompt(),
            widget.TaskList(
                icon_size=0,
                max_title_width=120,
                **powerline
                ),
            widget.KeyboardLayout(
                fmt=' Keyboard: {} ',
                display_map={'us': 'Frens','fr': 'Sophie'},
                configured_keyboards=['fr','us'],
                background="#9C27B0",
                **powerline
                ),
            widget.PulseVolume(
                fmt=' Vol: {} ',
                background="#673AB7",
                limit_max_volume=True,
                **powerline
                ),
            widget.OpenWeather(
                format=' {location_city}: {main_temp}°{units_temperature} | {humidity}% ',
                location='Brisbane',
                background="#3F51B5",
                **powerline
                ),
            widget.Clock(
                format=' %d %B %Y | %a %I:%M %p ',
                background="#3280bd"
                )
            ],
            20,
        ),
    ),
    #~~~~~~~~~~~~~~~~~~Second Monitor~~~~~~~~~~~~~~~~~~
    Screen(
        top=bar.Bar(
            [
            widget.GroupBox(),
            widget.Prompt(),
            widget.Sep(
                linewidth = 0,
                padding = 12
                ),
            widget.TaskList(
                icon_size=12,
                max_title_width=180,
                padding_x=8,
                padding_y=0
                ),
            widget.Systray(
                fmt='Vol: {} ',
                padding=7
                #background="#E91E63"
                ),
            widget.Sep(
                       linewidth = 0,
                       padding = 12,
                       **powerline
                       ),

            widget.NvidiaSensors(
                format=' GPU:{temp}°C ',
                background="#9C27B0",
                **powerline
                ),
            widget.ThermalSensor(
                format=' CPU: {temp:.0f}{unit}',
                background="#673AB7"
                ),
            widget.CPU(
                format='| {load_percent}%',
                background="#673AB7",
                **powerline
                ),
            widget.Memory(
                format=' MEM {MemPercent}% ',
                background="#3F51B5",
                **powerline
                ),
            widget.Clock(
                format=' %d %B %Y | %a %I:%M %p ',
                background="#3280bd"),
        ],
        20,
    ),
),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=1,
    border_focus="#63659E",
    border_normal="#41425d",
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart" # smart, focus, never, urgent
reconfigure_screens = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
wmname = "Qtile"
