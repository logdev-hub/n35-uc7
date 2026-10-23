from pathlib import Path
import qrcode

url = "https://m365.cloud.microsoft/chat/agent/T_f782183f-8876-44ec-c3ed-1c2729e25265.70693c39-4cbe-4b59-b644-a14ab35c1303.gpt.87677e96-5893-4094-bc56-c471a2304ec3"
output = Path(__file__).resolve().parents[1] / "assets" / "images" / "logi-a-qr.png"
output.parent.mkdir(parents=True, exist_ok=True)
image = qrcode.make(url, box_size=8, border=2)
image.save(output)
print(output)
