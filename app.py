from pyresearch.heatmap_and_track import process_video
import argparse

# Define the arguments as a dictionary
args = {
    "source_weights_path": "yolov8s.pt", #model
    "source_video_path":  "demo.mp4", #put your video
    "target_video_path": "output.mp4",
    "confidence_threshold": 0.35,
    "iou_threshold": 0.5,
    "heatmap_alpha": 0.5,
    "radius": 25,
    "track_threshold": 0.35,
    "track_seconds": 5,
    "match_threshold": 0.99,
    "display": True,
}

# Convert the dictionary to an argparse Namespace object
args_namespace = argparse.Namespace(**args)

# Call the process_video function with the Namespace object
process_video(args_namespace)
