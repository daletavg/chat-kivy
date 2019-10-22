from views.chat.chat import ChatWindow,RV
from kivy.app import App
from kivy.lang import Builder

from kivymd.uix.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast


main_kv = """

 ChatWindow
# <ContentNavigationDrawer@MDNavigationDrawer>:
#     drawer_logo: 'demos/kitchen_sink/assets/drawer_logo.png'
# 
#     NavigationDrawerSubheader:
#         text: "Menu:"
# 
# 
# NavigationLayout:
#     id: nav_layout
# 
#     ContentNavigationDrawer:
#         id: nav_drawer
# 
#     BoxLayout:
#         orientation: 'vertical'
#        
#         MDToolbar:
#             id: toolbar
#             title: 'KivyMD Kitchen Sink'
#             md_bg_color: app.theme_cls.primary_color
#             background_palette: 'Primary'
#             background_hue: '500'
#             elevation: 10
#             left_action_items:
#                 [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
# 
#         Widget:
         
        
"""

class ChatApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):

        return ChatWindow()


    # def callback(self, instance, value):
    #     toast("Pressed item menu %d" % value)
    #
    # def on_start(self):
    #     for i in range(15):
    #         self.main_widget.ids.nav_drawer.add_widget(
    #             NavigationDrawerIconButton(
    #                 icon='checkbox-blank-circle', text="Item menu %d" % i,
    #                 on_release=lambda x, y=i: self.callback(x, y)))


if __name__ == '__main__':
    ChatApp().run()



# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
#
# from kivymd.icon_definitions import md_icons
# from kivymd.uix.tab import MDTabsBase
# from kivymd.theming import ThemeManager
#
# demo = """
# <Example@BoxLayout>
#     orientation: 'vertical'
#
#     MDToolbar:
#         title: app.title
#         md_bg_color: app.theme_cls.primary_color
#         background_palette: 'Primary'
#         left_action_items: [['menu', lambda x: x]]
#
#     MDTabs:
#         id: android_tabs
#
#
# <MyTab>
#
#     FloatLayout:
#
#         MDLabel:
#             text: 'Content'
#             halign: 'center'
#             theme_text_color: 'Primary'
#             font_style: 'H6'
#
#
# """
#
# if __name__ == '__main__':
#     from kivy.factory import Factory
#     from kivymd.uix.button import MDIconButton
#
#
#     class MyTab(BoxLayout, MDTabsBase):
#         pass
#
#
#     class Example(App):
#         title = 'Example Tabs'
#         theme_cls = ThemeManager()
#         list_name_icons = list(md_icons.keys())[0:15]
#
#         def build(self):
#             Builder.load_string(demo)
#             screen = Factory.Example()
#
#             for name_tab in self.list_name_icons:
#                 tab = MyTab(text=name_tab)
#                 screen.ids.android_tabs.add_widget(tab)
#             return screen
#
#
# Example().run()