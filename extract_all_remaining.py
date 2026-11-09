import os, subprocess, concurrent.futures, time

pdfs = [
    {
        "name": "02 UnderStanding and Using Data_removed.pdf",
        "out": "/home/justin/Desktop/review/review/extracted/02_data.txt",
        "start": 81,
        "end": 164
    },
    {
        "name": "03 Overview of System Architecture_removed.pdf",
        "out": "/home/justin/Desktop/review/review/extracted/03_system_architecture.txt",
        "start": 77,
        "end": 223
    },
    {
        "name": "04 UnderStanding Information Security_removed.pdf",
        "out": "/home/justin/Desktop/review/review/extracted/04_information_security.txt",
        "start": 67,
        "end": 131
    },
    {
        "name": "05 Understanding the IT Business and Ethics_removed.pdf",
        "out": "/home/justin/Desktop/review/review/extracted/05_it_business_ethics.txt",
        "start": 68,
        "end": 230
    },
    {
        "name": "06 Project Management & Technical Communication_removed.pdf",
        "out": "/home/justin/Desktop/review/review/extracted/06_project_management.txt",
        "start": 66,
        "end": 142
    }
]

def ocr_single_image(img_path):
    txt_prefix = img_path[:-4]
    subprocess.run(["tesseract", img_path, txt_prefix, "--oem", "1", "--psm", "3", "-l", "eng"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    txt_file = txt_prefix + ".txt"
    content = ""
    if os.path.exists(txt_file):
        with open(txt_file, "r", errors="ignore") as f:
            lines = f.readlines()
            # Clean repetitive headers/URLs
            cleaned = [l for l in lines if not "topcit.or.kr" in l and not l.startswith("https://") and not l.strip().isdigit()]
            content = "".join(cleaned)
    return content

for item in pdfs:
    pdf_path = os.path.join("/home/justin/Desktop/review/review", item["name"])
    print(f"=== Starting remaining OCR for {item['name']} (Pages {item['start']} to {item['end']}) ===")
    
    batch_size = 15
    for batch_start in range(item["start"], item["end"] + 1, batch_size):
        batch_end = min(batch_start + batch_size - 1, item["end"])
        tmp_dir = f"/tmp/ocr_batch_{os.getpid()}"
        os.makedirs(tmp_dir, exist_ok=True)
        
        # Render pages
        subprocess.run(["pdftoppm", "-r", "130", "-f", str(batch_start), "-l", str(batch_end), pdf_path, f"{tmp_dir}/pg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        ppm_files = sorted([os.path.join(tmp_dir, f) for f in os.listdir(tmp_dir) if f.endswith(".ppm")])
        if ppm_files:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                results = list(executor.map(ocr_single_image, ppm_files))
            
            with open(item["out"], "a", encoding="utf-8") as out_fp:
                for res in results:
                    out_fp.write(res + "\n\n")
            
            print(f"  Processed pages {batch_start}-{batch_end} of {item['end']}")
            
        # Clean temp directory
        for f in os.listdir(tmp_dir):
            try: os.remove(os.path.join(tmp_dir, f))
            except: pass
        try: os.rmdir(tmp_dir)
        except: pass

print("=== ALL REMAINING PAGES FULLY OCR-EXTRACTED! ===")
