import os
from flask import Flask, render_template, flash, request, redirect, url_for
from PIL import Image
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		image_file = request.files['url']
		file_name = image_file.filename
		image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		img_path = f"uploads/{file_name}"

		with Image.open(img_path) as rgb_image:
			img_width = rgb_image.width
			img_height = rgb_image.height

			colors = []
			for x in range(img_width):
				for y in range(img_height):
					colors.append(rgb_image.getpixel(xy=(x, y)))
		most_common_color = Counter(colors).most_common()[0][0]
		print(most_common_color)
		return render_template('index.html', color=most_common_color)
	return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
