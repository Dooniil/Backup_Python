import os
import zipfile
import time

source = []
source.extend(input('Enter directory or file: ').split())


target_dir = input('Enter directory for safe backup: ')
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y_%m_%d')
now = time.strftime('%Hh_%Mm_%Ss')

if not os.path.exists(today):
	os.mkdir(today)

comment = input('If you need to stay the comment for backup: ')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'
print(source)


new_zip = zipfile.ZipFile(target, mode='w')
for source_name in source:
	if os.path.isfile(source_name):
		new_zip.write(source_name)
	else:
		for root, dirs, files in os.walk(source_name):
			new_zip.write(root)
			for file_name in files:
				new_zip.write(os.path.join(root, file_name))
print('Archive has created')
new_zip.close()