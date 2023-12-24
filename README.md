
# Whisper-v3
In this projcet we use the Whisper v3 model to record using speech recognition and use the whisper v3 model to transcribe it. Whisper v3 can also transcribe in diffrent languges though it is not the best.
## About
OpenAI's Whisper is an advanced automatic speech recognition (ASR) system designed for transcribing audio files. This repository runs the Whisper v3 model

## Installation

### Prerequisites
- Python 3.11.5 or newer. [Download here](https://www.python.org/downloads/release/python-3120/) and make sure it's added to PATH.
- If you have a GPU:
  - NVIDIA GPU: Install [CUDA 12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows).
  - AMD GPU (Linux): Install [ROCm for Linux](https://rocm.docs.amd.com/en/docs-5.6.0/deploy/linux/install_overview.html).
  - AMD GPU (Windows): Install [ROCm for Windows](https://rocm.docs.amd.com/en/docs-5.6.0/deploy/windows/index.html).

### Python Dependencies
Run the following commands to install necessary Python packages:
```bash
pip install --upgrade pip
pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio]
pip install SpeechRecognition
```
### FFmpeg Installation
FFmpeg is required for processing audio files. Follow these steps to install it:
- **Windows/Mac/Linux**: 
  - Visit the [FFmpeg official website](https://ffmpeg.org/download.html) and follow the instructions for your operating system.
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
  - With ROCm:
    ```bash
    pip install torch --index-url https://download.pytorch.org/whl/rocm5.6
    ```
  - With CUDA:
    ```bash
    pip install torch
    ```
  - Without GPU:
    ```bash
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    ```

For installation issues, refer to the [PyTorch official installation guide](https://pytorch.org/get-started/locally/).
