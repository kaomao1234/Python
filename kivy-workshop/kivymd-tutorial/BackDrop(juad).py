import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
Builder.load_string('''
<MyClass@MDFloatLayout>:
	orientation:'vertical'
	canvas:
		Color:
			rgba:1,1,1,1
		Rectangle:
			id:img
			pos:self.pos
			size:self.size
			source:"C:/Users/borip/Documents/GitHub/PythonWorkShop/WorkKivy/Project/WinterCakeApp/Icon/Rose_Vale_Flowers_Soft_Organic_Fashion_Logo.png"
	MDBoxLayout:
		y:-1000
		size_hint_y:.5
		id:box
		padding:dp(10)
		orientation:'vertical'
		radius:[dp(20),dp(20),dp(0),dp(0)]
		md_bg_color:.5,.5,.5,1
		Label:
			text:'Sign in'
		MDLabel:
			text:'Username'
		TextInput:
		MDLabel:
			text:'Password'
		TextInput:
		MDBoxLayout:
			size_hint_y:None
			height:dp(70)
			padding:dp(10)
			MDBoxLayout:
				radius:[dp(10)]
				md_bg_color:0,0,1,1
				Button:
					text:'Sign in'
					background_color:0,0,0,0
			MDBoxLayout:
				radius:[dp(10)]
				md_bg_color:0,1,0,1
				Button:
					text:'Sign in'
					background_color:0,0,0,0
''')
class MyClass(MDFloatLayout):
    pass
class TestApp(MDApp):
	def build(self):
		print(Window.size)
		return MyClass()
	def on_start(self):
		anim = Animation(y=0,duration=0.5)
		anim.start(self.root.ids.box)

TestApp().run()