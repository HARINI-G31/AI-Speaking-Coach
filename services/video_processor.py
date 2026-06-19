import os
import cv2


def get_video_metadata(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return None

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = frame_count / fps if fps > 0 else 0

    cap.release()

    return {
        "duration": round(duration, 2),
        "frame_count": frame_count,
        "fps": round(fps, 2),
        "resolution": f"{width} x {height}"
    }


def extract_frames(video_path, output_dir, frame_interval=30):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_paths = []
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break

        if frame_count % frame_interval == 0:
            frame_name = f"frame_{frame_count}.jpg"
            frame_path = os.path.join(output_dir, frame_name)

            cv2.imwrite(frame_path, frame)

            frame_paths.append(frame_path)

        frame_count += 1

    cap.release()

    return frame_paths