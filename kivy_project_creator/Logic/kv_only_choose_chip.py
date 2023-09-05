from kivymd.uix.screen import MDScreen

KV = '''
<MyScreen>

    [...]

        MDBoxLayout:
            id: chip_box
            adaptive_size: True
            spacing: "8dp"

            MyChip:
                text: "Elevator"
                on_active: if self.active: root.removes_marks_all_chips(self)

            MyChip:
                text: "Washer / Dryer"
                on_active: if self.active: root.removes_marks_all_chips(self)

            MyChip:
                text: "Fireplace"
                on_active: if self.active: root.removes_marks_all_chips(self)


[...]
'''


class MyScreen(MDScreen):
    def removes_marks_all_chips(self, selected_instance_chip):
        for instance_chip in self.ids.chip_box.children:
            if instance_chip != selected_instance_chip:
                instance_chip.active = False