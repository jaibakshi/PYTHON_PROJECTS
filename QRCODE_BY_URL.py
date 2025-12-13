import qrcode
from PIL import Image

new = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=40,border=6)
new.add_data("https://github.com/jaibakshi/PYTHON_PRJECTS")
new.make(fit=True)
image=new.make_image(fill_color="purple",back_color="white")
image.save("MYGITHUB_DASHBOARD.png")