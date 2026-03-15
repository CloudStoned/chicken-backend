from ultralytics import YOLO
from PIL import Image
import io
import logging

model = YOLO("./best.pt")

# Configure logger for this module
logger = logging.getLogger(__name__)

def read_photo(img_bytes: bytes, mime_type: str):
    try:
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img)
        logger.info(f"YOLO results count: {len(results) if results else 0}")

        if results and len(results) > 0:
            result = results[0]

            if result.probs is not None:
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
                logger.info(f"Top 3 results: {top_results}")
                return {"top_results": top_results}

        logger.info("No breed detected")
        return {"breed": "Unknown", "confidence": 0.0}

    except Exception as e:
        logger.exception(f"Error processing image: {e}")
        return {"error": str(e), "breed": "Error", "confidence": 0.0}