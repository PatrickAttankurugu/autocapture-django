# Ghana Card Auto-Detection System

A browser-based system for real-time detection, auto-capture, and verification of Ghana national ID cards.

## Overview

This project implements a web-based Ghana Card detection and auto-capture system that works entirely client-side without server dependencies. The system uses a custom-trained YOLOv8 object detection model converted to ONNX format to detect Ghana cards in real-time through device cameras, provides visual feedback on card positioning, and automatically captures well-aligned cards.


## Features

- **Real-time detection** with bounding box visualization
- **Auto-capture** of properly aligned Ghana cards
- **Visual feedback** with color-coded alignment indicators
- **Responsive design** for both desktop and mobile devices
- **Fully client-side** processing with no server dependencies
- **Low latency** detection (100-150ms per frame)
- **Backend API integration** for optional verification services

## Technical Details

- **Model**: Custom-trained YOLOv8-nano (3M parameters)
- **Input**: 640×640 RGB images from camera feed
- **Output**: Bounding boxes, confidence scores, and alignment metrics
- **Web Technologies**: HTML5, CSS3, JavaScript (vanilla)
- **ML Framework**: ONNX.js / TensorFlow.js for inference
- **Performance**: ~10 FPS on mid-range mobile devices, ~20 FPS on desktop

## Project Structure

```
ghana_card_detector/
├── css/               # Styling
│   └── styles.css     # Main stylesheet
├── docs/              # Documentation
│   └── ...            # Detailed project documentation
├── js/                # JavaScript
│   └── detector.js    # Core detection engine
├── models/            # ML models
│   └── best.onnx      # ONNX model file
├── training/          # Training code and notebooks
│   └── ...            # Training scripts and resources
├── index.html         # Main application page
└── README.md          # This file
```

## Setup and Usage

### Prerequisites

- Modern web browser (Chrome, Firefox, Edge, Safari)
- Camera access
- At least 2GB of RAM

### Installation

1. Clone the repository:
   
2. Navigate to the project directory:
   ```
   cd ghana-card-detector
   ```

3. Serve the files using any HTTP server:
   ```
   # Using Python's built-in server
   python -m http.server 8000
   
   # Or using Node.js
   npx serve
   ```

4. Open your browser to `http://localhost:8000`

### Usage Instructions

1. Allow camera access when prompted
2. Position a Ghana card within the guide frame
3. Wait for the bounding box to turn green
4. The system will automatically capture the card when properly aligned
5. Use "Manual Capture" button if needed
6. Send to backend for verification if required

## Training Your Own Model

The model was trained on a dataset of 600 images (200 positive Ghana card examples and 400 negative examples). Detailed information about the training process can be found in the `training/` directory.

A brief summary of the training process:

1. Data collection and annotation (positive and negative examples)
2. Dataset organization and preprocessing
3. Model configuration (YOLOv8-nano)
4. Transfer learning from pre-trained weights
5. Performance evaluation
6. ONNX conversion and optimization

## Performance Metrics

- **Precision**: 96.8%
- **Recall**: 97.5%
- **mAP50**: 98.4%
- **mAP50-95**: 95.2%
- **Auto-capture success rate**: 92%

## Key Thresholds and Parameters

- **Confidence Threshold**: 0.2
- **Consecutive Detections Required**: 3
- **Alignment Score Threshold**: 0.5
- **Aspect Ratio Tolerance**: 0.3
- **Ideal Area Range**: 8-70% of frame

## Limitations

- Requires good lighting conditions for optimal performance
- May struggle with cards at extreme angles (>45°)
- Limited to Ghana national ID cards only
- Performance varies based on device capabilities

## Future Improvements

- Model quantization for smaller size and faster inference
- Enhanced user guidance with on-screen positioning hints
- OCR integration for data extraction
- Additional ID card types recognition
- Background blur detection for quality assessment

