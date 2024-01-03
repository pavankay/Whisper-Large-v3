
# Whisper-Large-v3
In this projcet we use the Whisper v3 model to record using speech recognition and use the whisper v3 model to transcribe it. Whisper v3 can also transcribe in diffrent languges though it is not the best.
## About
OpenAI's Whisper is an advanced automatic speech recognition (ASR) system designed for transcribing audio files. This repository runs the Whisper v3 model

## Installation

### Prerequisites
- Python 3.11.5 or newer. [Download here](https://www.python.org/downloads/release/python-3120/) and make sure it's added to PATH.
- If you have a GPU:
  - NVIDIA GPU: Install [CUDA 12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive?).

### Python Dependencies
Run the following commands to install necessary Python packages:
```bash
pip install --upgrade pip
pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio]
pip install SpeechRecognition
```
### FFmpeg Installation
FFmpeg is essential for processing audio files. Begin by installing it:

- Visit the [FFmpeg official website](https://ffmpeg.org/download.html) and download the appropriate binaries for your operating system.

#### Windows
1. Extract the downloaded files and place the folder in the "C:/" directory.
2. Rename the folder to "FFmpeg". Your directory should now look like this: "C:/FFmpeg".
3. Add FFmpeg to your system path:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Click on 'Advanced system settings' and then 'Environment Variables'.
   - Under 'System Variables', find and select 'Path', then click 'Edit'.
   - Click 'New' and add the path to the FFmpeg bin folder, e.g., "C:/FFmpeg/bin"
   - Click 'OK' to close all dialog boxes.

#### Mac
1. After installing FFmpeg, open Terminal.
2. Add FFmpeg to your system path using the command:
   ```bash
   export PATH="/path/to/FFmpeg/bin:$PATH"
   ```
   Replace "/path/to/FFmpeg/bin" with the actual path to the FFmpeg bin directory.

#### Linux
1. Install FFmpeg using your distribution's package manager (e.g., `apt`, `yum`, or `pacman`).
2. Most Linux distributions will automatically add FFmpeg to your system path. If not, you can add it manually using:
   ```bash
   export PATH="/path/to/FFmpeg/bin:$PATH"
   ```
   Replace "/path/to/FFmpeg/bin" with the actual path to the FFmpeg bin directory.
### PyTorch Installation
- **Windows**:
  - Without GPU:
    ```bash
    pip install torch
    ```
  - With NVIDIA GPU:
    ```bash
    pip install torch --index-url https://download.pytorch.org/whl/cu121
    ```

- **Mac**:
  - All Mac installations:
    ```bash
    pip install torch
    ```

- **Linux**:
  - With CUDA:
    ```bash
    pip install torch
    ```
  - Without GPU:
    ```bash
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    ```

For installation issues, refer to the [PyTorch official installation guide](https://pytorch.org/get-started/locally/).
