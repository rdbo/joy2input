# Xbox 360 Joy2Input
# by rdbo

from pynput import mouse, keyboard
import pygame
import math

pygame.init()
pygame.joystick.init()

mouse_ctrl = mouse.Controller()
keyboard_ctrl = keyboard.Controller()
clock = pygame.time.Clock()
deadzone = 0.15
speed_x = 8
speed_y = 8
joystick = pygame.joystick.Joystick(0)

try:
	while True:
		pygame.event.get() # Update joystick data
		analogs = [(joystick.get_axis(0), joystick.get_axis(1)), (joystick.get_axis(3), joystick.get_axis(4))] # [(L_X, L_Y), (R_X, R_Y)]
		triggers = [joystick.get_axis(2), joystick.get_axis(5)] # [LT, RT]
		buttons = [joystick.get_button(0), joystick.get_button(1), joystick.get_button(2), joystick.get_button(3)] # [A, B, X, Y]
		bumper_buttons = [joystick.get_button(4), joystick.get_button(5)] # [LB, RB]
		middle_buttons = [joystick.get_button(6), joystick.get_button(7)] # [BACK, START]
		stick_buttons = [joystick.get_button(9), joystick.get_button(10)] # [L, R]
		dpad = joystick.get_hat(0)

		# Analogs - Mouse X/Y movement, AWSD
		if analogs[1][0] < -deadzone or analogs[1][0] > deadzone:
			mouse_ctrl.move(speed_x * analogs[1][0], 0)
		
		if analogs[1][1] < -deadzone or analogs[1][1] > deadzone:
			mouse_ctrl.move(0, speed_y * analogs[1][1])
		
		if analogs[0][0] < -deadzone:
			keyboard_ctrl.press("A")
		else:
			keyboard_ctrl.release("A")
		
		if analogs[0][0] > deadzone:
			keyboard_ctrl.press("D")
		else:
			keyboard_ctrl.release("D")
		
		if analogs[0][1] < -deadzone:
			keyboard_ctrl.press("W")
		else:
			keyboard_ctrl.release("W")
		
		if analogs[0][1] > deadzone:
			keyboard_ctrl.press("S")
		else:
			keyboard_ctrl.release("S")

		
		# Triggers - Right/Left Click (Press/Release)
		if triggers[0] > -deadzone:
			mouse_ctrl.press(mouse.Button.right)
		else:
			mouse_ctrl.release(mouse.Button.right)
		
		if triggers[1] > -deadzone:
			mouse_ctrl.press(mouse.Button.left)
		else:
			mouse_ctrl.release(mouse.Button.left)
		
		# Buttons
		if buttons[0]:
			keyboard_ctrl.press(keyboard.Key.space)
		else:
			keyboard_ctrl.release(keyboard.Key.space)
		
		if buttons[1]:
			keyboard_ctrl.press("Q")
		else:
			keyboard_ctrl.release("Q")
		
		if buttons[2]:
			keyboard_ctrl.press("E")
		else:
			keyboard_ctrl.release("E")
		
		if buttons[3]:
			keyboard_ctrl.press("T")
		else:
			keyboard_ctrl.release("T")

		# Bumber Buttons
		if bumper_buttons[0]:
			mouse_ctrl.scroll(0, 1)
		
		if bumper_buttons[1]:
			mouse_ctrl.scroll(0, -1)

		# Stick Buttons
		if stick_buttons[0]:
			keyboard_ctrl.press(keyboard.Key.shift)
		else:
			keyboard_ctrl.release(keyboard.Key.shift)
		
		if stick_buttons[1]:
			keyboard_ctrl.press(keyboard.Key.ctrl)
		else:
			keyboard_ctrl.press(keyboard.Key.ctrl)
		
		# Middle Buttons
		if middle_buttons[1]:
			keyboard_ctrl.press(keyboard.Key.esc)
		else:
			keyboard_ctrl.release(keyboard.Key.esc)

		
		'''
		print(f"[X360]")
		print(f"Analogs: {analogs}")
		print(f"Triggets: {triggers}")
		print(f"Buttons: {buttons}")
		print(f"Bumper Buttons: {bumper_buttons}")
		print(f"Middle Buttons: {middle_buttons}")
		print(f"Stick Buttons: {stick_buttons}")
		print(f"DPAD: {dpad}")
		'''

		clock.tick(60) # 60 FPS Cap
except BaseException as e:
	print(f"[!] Exception: {e}")

pygame.joystick.quit()
pygame.quit()
