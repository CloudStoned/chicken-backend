from ultralytics import YOLO
from PIL import Image
import io

model = YOLO("./best.pt")

def read_photo(img_bytes: bytes, mime_type: str):
    try:
        print("Reading photo...")
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img)

        if results and len(results) > 0:
            result = results[0]
            
            if result.probs is not None:
                # Get top 3 results
                top3_indices = result.probs.top5[:3]
                top3_confs = result.probs.top5conf[:3]
                
                top_results = []
                for i, (idx, conf) in enumerate(zip(top3_indices, top3_confs)):
                    class_name = model.names[int(idx)]
                    top_results.append({
                        "breed": class_name,
                        "confidence": round(float(conf), 4),
                        "rank": i + 1
                    })
                
                return {"top_results": top_results}

        return {"breed": "Unknown", "confidence": 0.0}

    except Exception as e:
        print(f"!!! Error: {e}")
        return {"error": str(e), "breed": "Error", "confidence": 0.0}