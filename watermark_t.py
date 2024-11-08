from blind_watermark import WaterMark

bwm1 = WaterMark(password_img=1, password_wm=1)
bwm1.read_img('2.png')
wm = '@defdot'
bwm1.read_wm(wm, mode='str')
bwm1.embed('3.png')
len_wm = len(bwm1.wm_bit)
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))