import codecs

text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"
rot13 = codecs.encode(text, 'rot_13')
print(rot13)

text = codecs.decode(rot13, 'rot_13')
print(text)