# English-Braille Translator
English to Braille language translation machine learning model project. The project leverages advanced libraries like TensorFlow and OpenCV for efficient model training and deployment. 

---

## Tech Stack

Our project is built using the following technologies:

- **Python**: The core programming language for scripting and development.
- **OpenCV**: For image processing and computer vision tasks.
- **TensorFlow**: For building, training, and deploying machine learning models.
- Other libraries: Check `requirements.txt` for additional dependencies.

[![My Skills](https://skillicons.dev/icons?i=py,tensorflow,opencv)](https://www.python.org/)

## Deployment
To set up this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-REPOSITORY-HTTPS-LINK.git
cd your-repository
```

### 2. Install Dependencies

Ensure you have Python installed (version 3.8+ recommended). Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Install TensorFlow

Depending on your setup, install TensorFlow for CPU or GPU.

#### TensorFlow for CPU:

```bash
pip install tensorflow
```

#### TensorFlow for GPU:

1. Ensure you have the **CUDA Toolkit** and **cuDNN** installed. Refer to [TensorFlow GPU setup documentation](https://www.tensorflow.org/install/gpu).
2. Install TensorFlow:
   ```bash
   pip install tensorflow[and-cuda]
   ```

Check TensorFlow's GPU compatibility:

```python
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```

---

## Running the Code

Navigate to the `main.ipynb` file to execute the project code. Follow these steps:

1. Open the `.ipynb` file.
2. Navigate to each step in the notebook interface.
3. Follow the instructions provided in the markdown cells to run the code step by step.

---

## Project Overview


---

## Contributing to the Project

Feel free to contribute to this repository! Fork the repo, make your changes, and submit a pull request.

### Our Current Contributors

🧑‍💻 [(3normousz)](https://github.com/3normousz)<br>
😎 [(KenjiTECHinc)](https://github.com/KenjiTECHinc)<br>
😿 [(Nattapat140)](https://github.com/Nattapat140)<br>
💯 [(kharryhsu)](https://github.com/kharryhsu)<br>
👍 [(Kyou140)](https://github.com/Kyou140)<br>
🐈 [(yurawaru)](https://github.com/yurawaru)<br>

---

## License

This project is licensed under the [MIT License](LICENSE).

