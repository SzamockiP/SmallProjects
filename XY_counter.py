from pynput.keyboard import Listener

z_iter = x_iter = 0

def on_press(key):
    global z_iter, x_iter
    if hasattr(key, 'char'):
        if key.char == 'z':
            z_iter += 1
            proc_z = round(z_iter/(x_iter+z_iter)*100)
            print(f'Z:{z_iter} X:{x_iter}  {proc_z}/{100 - proc_z}')
        elif key.char == 'x':
            x_iter += 1
            proc_z = round(z_iter/(x_iter+z_iter)*100)
            print(f'Z:{z_iter} X:{x_iter}  {proc_z}/{100 - proc_z}')

with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread







