# Raspberry Pi Prize Selector

This application is designed to run on a Raspberry Pi 5. It uses a state machine to select a random prize from a list when a button is pressed, and plays a corresponding video using OpenCV. After the prize video is played, an idle video loops while waiting for the next button press.

## Features

- Randomly selects a prize on button press.
- Plays prize videos using OpenCV.
- Loops an idle video while waiting for button press.

## Requirements

### Hardware

- Raspberry Pi 5
- Button connected to a GPIO pin
- Display connected to the Raspberry Pi
- Optional: Speakers for audio playback

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/cthadeufaria/raspberry-pi-animation-button.git
    cd raspberry-pi-animation-button
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Connect the hardware:**

    - Connect a button to a GPIO pin on the Raspberry Pi.
    - Connect a display to the Raspberry Pi.
    - Optionally, connect speakers for audio playback.

4. **Configure GPIO pin:**

    Edit the GPIO pin number in the code to match your setup.

## Usage

1. **Prepare videos:**

    - Place your prize videos in the videos directory.
    - Ensure there is an idle video available.

2. **Run the application:**

    ```bash
    python main.py
    ```

3. **Operation:**

    - Press the button to select a random prize.
    - Watch the prize video play on the display.
    - After the prize video, the idle video will play while waiting for the next button press.

## Customization

- **Prize Videos:** Add or remove prize videos as needed.
- **Idle Video:** Replace the idle video with your desired idle video.

## License

See the `LICENSE` file for details.

## Contact

For questions or suggestions, please open an issue or contact [crls.thadeu@gmail.com](mailto:crls.thadeu@gmail.com).

## Contribution

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
