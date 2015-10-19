import numpy, os, random
from PIL import Image

# where to save the config file
folder = raw_input('Enter The Path to your Demonsaw Folder: ')
# make sure the save folder exists or create it
if not os.path.exists(folder):
    os.makedirs(folder)

# where to download file to.
down = raw_input('Enter The Path to your Downloads Folder: ')
# make sure the save folder exists or create it
if not os.path.exists(down):
    os.makedirs(down)

# Path to Shared folder
up = raw_input('Enter The Path to a Folder you would like to share with your private groups: ')
# make sure the save folder exists or create it
if not os.path.exists(up):
    os.makedirs(up)

user = raw_input('Enter Your UserName: ')
router = raw_input('Enter Router IP of Domain Name: ')
port = raw_input('Enter The Routers Port#: ')

# register the .ico extension with PIL so we can save to .ico
Image.register_extension("PNG", '.ico')

# set range size for the number of files to generate
for n in xrange(5):
    a = numpy.random.rand(16, 16, 3) * 255  # 16x16 image 3 bit depth
    im_out = Image.fromarray(a.astype('uint8')).convert('RGBA')
    icon = os.path.join(folder, 'GroupImage%000d.ico' % n)  # change the filename here if you want
    im_out.save(icon)

# create and open new demonsaw.xml file
f = open(os.path.join(folder, "demonsaw.xml"), "w")

# write configuration to demonsaw.xml
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<demonsaw version="2">\n')
f.write('<view>\n')
f.write('<option>true</option>\n')
f.write('<toolbar>true</toolbar>\n')
f.write('<menubar>true</menubar>\n')
f.write('<detail>true</detail>\n')
f.write('</view>\n')
f.write('<clients>\n')
f.write('<client enabled="true">\n')
f.write('<name>' + user + '</name>\n')
f.write('<router>\n')
f.write('<address>' + router + '</address>\n')
f.write('<port>' + port + '</port>\n')
f.write('</router>\n')
f.write('<security>\n')
f.write('<key_size>128</key_size>\n')
f.write('<prime_size>128</prime_size>\n')
f.write('<hash>0</hash>\n')
f.write('<salt/>\n')
f.write('</security>\n')
f.write('<timeout>\n')
f.write('<socket>4000</socket>\n')
f.write('<download>51000</download>\n')
f.write('<upload>60000</upload>\n')
f.write('</timeout>\n')
f.write('<transfer>\n')
f.write('<path>' + down + '</path>\n')
f.write('<searches>128</searches>\n')
f.write('<downloads>3</downloads>\n')
f.write('<uploads>5</uploads>\n')
f.write('</transfer>\n')
f.write('<chat>\n')
f.write('<audio>true</audio>\n')
f.write('<visual>true</visual>\n')
f.write('<volume>40</volume>\n')
f.write('</chat>\n')
f.write('<groups>\n')
e0 = 1
e1 = 1
e2 = 1
e3 = 1
e4 = 1
e5 = 1

while e5 != 100:
    e0 = random.randint(1, 100)
    e1 = random.randint(1, 100)
    e2 = random.randint(1, 100)
    e3 = random.randint(1, 100)
    e4 = 100 - (e0 + e1 + e2 + e3)
    if e4 < 1:
            e4 = 1
    e5 = e0 + e1 + e2 + e3 + e4
    print 'one moment please: currently randomizing entropy source weightings    ' + str(e5)
print 'you will now be asked to faceroll the keyboard 5 times, this provides a true random seed, this input becomes the salt for the entropy source.\n'

# icon0
f.write('<group enabled="true">\n')
f.write('<path>' + folder + '/GroupImage0.ico</path>\n')
f.write('<entropy>' + str(e0) + '</entropy>\n')
c0 = random.randint(0, 4)
f.write('<cipher>' + str(c0) + '</cipher>\n')
k0 = random.sample([128, 192, 256], 1)
f.write('<key_size>' + str(k0) + '</key_size>\n')
h0 = random.randint(0, 9)
f.write('<hash>' + str(h0) + '</hash>\n')
s0 = raw_input('FaceRoll the keyboard and hit Enter: ')
f.write('<salt>' + str(s0) + '<salt/>\n')
i0 = random.randint(0, 99)
f.write('<iterations>' + str(i0) + '</iterations>\n')
f.write('</group>\n')

# icon1
f.write('<group enabled="true">\n')
f.write('<path>' + folder + '/GroupImage1.ico</path>\n')
f.write('<entropy>' + str(e1) + '</entropy>\n')
c1 = random.randint(0, 4)
f.write('<cipher>' + str(c1) + '</cipher>\n')
k1 = random.sample([128, 192, 256], 1)
f.write('<key_size>' + str(k1) + '</key_size>\n')
h1 = random.randint(0, 9)
f.write('<hash>' + str(h1) + '</hash>\n')
s1 = raw_input('FaceRoll the keyboard and hit Enter: ')
f.write('<salt>' + str(s1) + '<salt/>\n')
i1 = random.randint(0, 99)
f.write('<iterations>' + str(i1) + '</iterations>\n')
f.write('</group>\n')

# icon2
f.write('<group enabled="true">\n')
f.write('<path>' + folder + '/GroupImage1.ico</path>\n')
f.write('<entropy>' + str(e2) + '</entropy>\n')
c2 = random.randint(0, 4)
f.write('<cipher>' + str(c2) + "</cipher>\n")
k2 = random.sample([128, 192, 256], 1)
f.write("<key_size>" + str(k2) + "</key_size>\n")
h2 = random.randint(0, 9)
f.write('<hash>' + str(h2) + "</hash>\n")
s2 = raw_input('FaceRoll the keyboard and hit Enter: ')
f.write('<salt>' + str(s2) + '<salt/>\n')
i2 = random.randint(0, 99)
f.write('<iterations>' + str(i2) + '</iterations>\n')
f.write('</group>\n')

# icon3
f.write('<group enabled="true">\n')
f.write('<path>' + folder + '/GroupImage1.ico</path>\n')
f.write('<entropy>' + str(e3) + '</entropy>\n')
c3 = random.randint(0, 4)
f.write('<cipher>' + str(c3) + '</cipher>\n')
k3 = random.sample([128, 192, 256], 1)
f.write('<key_size>' + str(k3) + '</key_size>\n')
h3 = random.randint(0, 9)
f.write('<hash>' + str(h3) + '</hash>\n')
s3 = raw_input('FaceRoll the keyboard and hit Enter: ')
f.write('<salt>' + str(s3) + '<salt/>\n')
i3 = random.randint(0, 99)
f.write('<iterations>' + str(i3) + '</iterations>\n')
f.write('</group>\n')

# icon4
f.write('<group enabled="true">\n')
f.write('<path>' + folder + '/GroupImage1.ico</path>\n')
f.write('<entropy>' + str(e4) + '</entropy>\n')
c4 = random.randint(0, 4)
f.write('<cipher>' + str(c4) + '</cipher>\n')
k4 = random.sample([128, 192, 256], 1)
f.write('<key_size>' + str(k4) + '</key_size>\n')
h4 = random.randint(0, 9)
f.write('<hash>' + str(h4) + "</hash>\n")
s4 = raw_input('FaceRoll the keyboard and hit Enter: ')
f.write('<salt>' + str(s4) + '<salt/>\n')
i4 = random.randint(0, 99)
f.write('<iterations>' + str(i4) + '</iterations>\n')
f.write('</group>\n')

f.write('</groups>\n')
f.write('<folders>\n')
f.write('<folder>' + up + '</folder>\n')
f.write('</folders>\n')
f.write('<files/>\n')
f.write('</client>\n')
f.write('</clients>\n')
f.write('<routers/>\n')
f.write('</demonsaw>\n')
f.close()
