import json
import pandas as pd

json_file = "YUSUFFEBRIANSYAH_V3925058.json"   # pastikan file JSON ada di folder yang sama dengan kode ini

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

output_file = "output_data.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for key, value in data.items():
        df = pd.DataFrame(value)   # ubah setiap bagian JSON ke DataFrame
        df.to_excel(writer, sheet_name=key, index=False)  # simpan ke sheet sesuai nama key

print(f"✅ Konversi selesai! File Excel tersimpan sebagai: {output_file}")
