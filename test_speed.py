import time, subprocess, os, concurrent.futures

# Test processing 10 pages of PDF 04 with 6 threads
t0 = time.time()
tmp_dir = "/tmp/test_ocr_speed"
os.makedirs(tmp_dir, exist_ok=True)

# Render 10 pages to ppm
subprocess.run(["pdftoppm", "-r", "130", "-f", "65", "-l", "74", "/home/justin/Desktop/review/review/04 UnderStanding Information Security_removed.pdf", f"{tmp_dir}/pg"], check=True)

ppm_files = sorted([os.path.join(tmp_dir, f) for f in os.listdir(tmp_dir) if f.endswith(".ppm")])

def ocr_img(img):
    txt_prefix = img[:-4]
    subprocess.run(["tesseract", img, txt_prefix, "--oem", "1", "--psm", "3", "-l", "eng"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    txt_file = txt_prefix + ".txt"
    if os.path.exists(txt_file):
        with open(txt_file) as f:
            return f.read()
    return ""

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(ocr_img, ppm_files))

# Clean up
for f in os.listdir(tmp_dir):
    os.remove(os.path.join(tmp_dir, f))
os.rmdir(tmp_dir)

elapsed = time.time() - t0
words = sum(len(r.split()) for r in results)
print(f"Processed {len(ppm_files)} pages in {elapsed:.2f}s ({elapsed/len(ppm_files):.2f}s/page). Extracted {words} words.")
