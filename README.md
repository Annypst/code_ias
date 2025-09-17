# ⚠️
值得注意的是，ml_yolo中并未在main中引用函数，需自己编写。 

# Drone Pentagon Target Recognition

This project provides code for recognizing pentagon-shaped targets in aerial images captured by drones. The system is designed to process images in real-time, detect pentagon targets, and output their locations for further navigation or analysis.

## Features

- Real-time image processing for aerial footage
- Pentagon shape detection using computer vision algorithms
- Output of target coordinates for drone navigation
- Modular and extensible codebase

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd code_ias
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Connect your drone and ensure it is streaming video to your computer.
2. Run the main recognition script:
   ```bash
   python main.py
   ```
3. The system will process incoming frames and display detected pentagon targets.

## Project Structure

- `main.py`: Entry point for the recognition system.
- `detector/`: Contains modules for image processing and pentagon detection.
- `utils/`: Utility functions for image handling and visualization.

## Requirements

- Python 3.7+
- OpenCV
- NumPy
- (Other dependencies as listed in `requirements.txt`)

## Example

Sample usage for processing a video file:
```bash
python main.py --video sample.mp4
```

## License

This project is licensed under the MIT License.

## Contact

For questions or contributions, please open an issue or submit a pull request.


