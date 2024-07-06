import io
import pymupdf
from PIL import Image
import google.generativeai as genai


def pdf_to_images(pdf_path, dpi=200):
    images = []
    doc = pymupdf.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72))
        image_data = pixmap.tobytes()
        img = Image.open(io.BytesIO(image_data))
        images.append(img)

    return images


model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = ["give a summary about the images"]
prompt.extend(pdf_to_images("static\Damara_Resume.pdf"))
result = model.generate_content(prompt)
print(result.text)
